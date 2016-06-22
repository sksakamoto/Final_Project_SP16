from urllib2 import urlopen
from json import load
from api_keys import *

apiUrl_recipe = "http://food2fork.com/api/search?key=" + RECIPE_KEY + "&q="

def recipe_api_search():
	global select_ingredient
	global recipe_list
	select_ingredient = raw_input("Which ingredient do you want to search for? [one word] ").lower()
	#select_ingredient = select_ingredient.split(" ")

	#recipe_url = apiUrl_recipe + str(select_ingredient[0]) + "%20" + str(select_ingredient[1]) + "&count=3"
	recipe_url = apiUrl_recipe + str(select_ingredient) + "&count=3"
	response_recipe = urlopen(recipe_url)
	json_obj_recipe = load(response_recipe)
	recipe_list = json_obj_recipe["recipes"]
	
	
	return_recipe = []
	for i in recipe_list:
		if i["title"] not in return_recipe:
			return_recipe.append(str(i["title"]))
			# return_recipe.append(str(i["source_url"]))
	print "How about one of these recipes?"
	print return_recipe

def url_display():
	selection = raw_input("Which one would you like to try? [1, 2, 3] ")
	if selection == '1':
		print "Here's the URL:"
		return recipe_list[0]["source_url"]
	if selection == '2':
		print "Here's the URL:"
		return recipe_list[1]["source_url"]
	if selection == '3':
		print "Here's the URL:"
		return recipe_list[2]["source_url"]
	else:
		print "Sorry, I didn't get that. Please try again"


