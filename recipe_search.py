from urllib2 import urlopen
from json import load
from api_keys import *

apiUrl_recipe = "http://food2fork.com/api/search?key=" + RECIPE_KEY + "&q="

def recipe_api_search():
	global select_ingredient
	select_ingredient = raw_input("Which ingredient do you want to search for? [one word] ").lower()

	recipe_url = apiUrl_recipe + str(select_ingredient) + "&count=3"
	response_recipe = urlopen(recipe_url)
	json_obj_recipe = load(response_recipe)
	recipe_list = json_obj_recipe["recipes"]
	
	return_recipe = []
	for i in recipe_list:
		if i["title"] not in return_recipe:
			return_recipe.append(i["title"])
			return_recipe.append(i["source_url"])
	print "Try one of these recipes:"
	return return_recipe