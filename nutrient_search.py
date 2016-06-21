from urllib2 import urlopen
from json import load
from api_keys import *

apiUrl_usda = "http://api.nal.usda.gov/ndb/nutrients/?format=json&max=5&api_key=" + USDA_KEY + "&"

def nutrient_search():
	global nutrient_id
	global high_or_low
	global nutrient_choice
	print "Select one from the following: calcium, carbohydrate, cholesterol, fat, fiber, iron, magnesium, phosphorus, potassium, protein, sodium, vitamin A, vitamin B-6, vitamin B-12, vitamin C, vitamin D, vitamin E, vitamin K, zinc"

	nutrient_choice = raw_input("Which nutrient are you interested in? ").lower()
	
	high_or_low = raw_input("Do you want high content or low content foods? ").lower()

	if nutrient_choice == 'protein':
		nutrient_id = 203
		return nutrient_id
	elif nutrient_choice == 'fat':
		nutrient_id = 204
		return nutrient_id
	elif nutrient_choice == 'carbohydrate':
		nutrient_id = 205
		return nutrient_id
	elif nutrient_choice == 'fiber':
		nutrient_id = 291
		return nutrient_id
	elif nutrient_choice == 'calcium':
		nutrient_id = 301
		return nutrient_id
	elif nutrient_choice == 'iron':
		nutrient_id = 303
		return nutrient_id
	elif nutrient_choice == 'magnesium':
		nutrient_id = 304
		return nutrient_id
	elif nutrient_choice == 'phosphorus':
		nutrient_id = 305
		return nutrient_id
	elif nutrient_choice == 'potassium':
		nutrient_id = 306
		return nutrient_id
	elif nutrient_choice == 'sodium':
		nutrient_id = 307
		return nutrient_id
	elif nutrient_choice == 'zinc':
		nutrient_id = 309
		return nutrient_id
	elif nutrient_choice == 'vitamin c':
		nutrient_id = 401
		return nutrient_id
	elif nutrient_choice == 'vitamin b-6':
		nutrient_id = 415
		return nutrient_id
	elif nutrient_choice == 'vitamin b-12':
		nutrient_id = 418
		return nutrient_id
	elif nutrient_choice == 'vitamin a':
		nutrient_id = 318
		return nutrient_id
	elif nutrient_choice == 'vitamin e':
		nutrient_id = 323
		return nutrient_id
	elif nutrient_choice == 'vitamin d':
		nutrient_id = 324
		return nutrient_id
	elif nutrient_choice == 'vitamin k':
		nutrient_id = 430
		return nutrient_id
	elif nutrient_choice == 'cholesterol':
		nutrient_id = 601
		return nutrient_id
	else:
		print "We don't have information for that nutrient, please select another"
		nutrient_search()

def food_options(nutrient):
	global json_obj_usda
	global food_dictionary

	vegetarian_options = raw_input("Are you vegetarian, vegan, or neither? ").lower()

	if vegetarian_options == 'neither':
		food_list = apiUrl_usda + "nutrients=" + str(nutrient_id) + "&sort=c&fg=0100&fg=0500&fg=0900&fg=1000&fg=1100&fg=1200&fg=1300&fg=1500&fg=1600&fg=2000"
		response_usda = urlopen(food_list)
		json_obj_usda = load(response_usda)
		food_dictionary = json_obj_usda["report"]["foods"]
	elif vegetarian_options == 'vegetarian':
		food_list = apiUrl_usda + "nutrients=" + str(nutrient_id) + "&sort=c&fg=0100&fg=0900&fg=1100&fg=1200&fg=1600&fg=2000"
		response_usda = urlopen(food_list)
		json_obj_usda = load(response_usda)
		food_dictionary = json_obj_usda["report"]["foods"]
	elif vegetarian_options == 'vegan':
		food_list = apiUrl_usda + "nutrients=" + str(nutrient_id) + "&sort=c&fg=0900&fg=1100&fg=1200&fg=1600&fg=2000"
		response_usda = urlopen(food_list)
		json_obj_usda = load(response_usda)
		food_dictionary = json_obj_usda["report"]["foods"]
	else:
		print "We don't have information on that option, please select another"
		food_options(nutrient_id)

def parse_data():
	list_of_foods = []
	for i in food_dictionary:
		if i["name"] not in list_of_foods:
			list_of_foods.append(i["name"])
	if high_or_low == 'high':
		print "Try eating these foods high in " + nutrient_choice + ":"
		return list_of_foods
	elif high_or_low == 'low':
		print "Try to avoid eating these foods high in " + nutrient_choice + ":"
		return list_of_foods
	else:
		print "Sorry, I couldn't provide the information you requested. Please try again"
	
#def main():
nutrient_search()
food_options(nutrient_id)
print parse_data()