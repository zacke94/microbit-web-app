import csv
import os
import json

def highest_lowest():
	try:
		with open('app/data/highest_lowest_log.csv') as f: #Highest a_temp
			z = csv.reader(f, delimiter=',')
			sortedlist = sorted(z, key=lambda colomn: colomn[0], reverse=True)
			sortedlist = list(sortedlist)
			highest_a_temp = sortedlist[0][0]
			a_temp_date = sortedlist[0][1]

		with open('app/data/highest_lowest_log.csv') as f: #lowest a_light
			z = csv.reader(f, delimiter=',')
			sortedlist = sorted(z, key=lambda colomn: colomn[1], reverse=False)
			sortedlist = list(sortedlist)
			lowest_a_light = sortedlist[0][2]
			a_light_date = sortedlist[0][3]

		with open('app/data/highest_lowest_log.csv') as f: #highest b_temp
			z = csv.reader(f, delimiter=',')
			sortedlist = sorted(z, key=lambda colomn: colomn[2], reverse=True)
			sortedlist = list(sortedlist)
			highest_b_temp = sortedlist[0][4]
			b_temp_date = sortedlist[0][5]

		with open('app/data/highest_lowest_log.csv') as f: #lowest b_light
			z = csv.reader(f, delimiter=',')
			sortedlist = sorted(z, key=lambda colomn: colomn[3], reverse=False)
			sortedlist = list(sortedlist)
			lowest_b_light = sortedlist[0][6]
			b_light_date = sortedlist[0][7]

		json_data = json.dumps(
						{'a_temp': highest_a_temp, 'a_temp_date': a_temp_date,
						'a_light': lowest_a_light, 'a_light_date': a_light_date,
						'b_temp': highest_b_temp, 'b_temp_date': b_temp_date,
						'b_light': lowest_b_light, 'b_light_date': b_light_date})
		return json_data

	except FileNotFoundError as e:
		json_data = json.dumps(
						{'a_temp': 0, 'a_temp_date': 0,
						'a_light': 0, 'a_light_date': 0,
						'b_temp': 0, 'b_temp_date': 0,
						'b_light': 0, 'b_light_date': 0})
		return json_data

def delete_saved_log():
	if os.path.exists("app/data/highest_lowest_log.csv"):
		os.remove("app/data/highest_lowest_log.csv")
	else:
		return "File doesn't exist"

def save_mb_coords(mb_A, mb_B): 
	coords_list = []
	coords_list.append(mb_A)
	coords_list.append(mb_B)
	
	try:
		with open('app/data/mb_coords.csv', 'w', newline='') as csvfile:
			writer = csv.writer(csvfile, delimiter=',')
			writer.writerow(coords_list)
	except FileNotFoundError as e:
		return "File was not found"

def show_locations():
	try:
		read_list = []
		with open('app/data/mb_coords.csv') as f:
			z = csv.reader(f, delimiter=',')
			for k in z:
				read_list.append(k)

		json_data = json.dumps({'mb_A': read_list[0][0], 'mb_B': read_list[0][1]})
		return json_data
		
	except FileNotFoundError as e:
		json_data = json.dumps({'mb_A': "?", 'mb_B': "?"})
		return json_data

def show_current_read():
	try:
		read_list = []
		with open('app/data/current_read_log.csv') as f: #Highest a_temp
			z = csv.reader(f, delimiter=',')
			for k in z:
				read_list.append(k)
		
		json_data = json.dumps(
						{'a_temp': read_list[0][0], 'a_light': read_list[0][1],
						'b_temp': read_list[0][2], 'b_light': read_list[0][3]})
		return json_data

	except FileNotFoundError as e:
		json_data = json.dumps(
						{'a_temp': 0, 'a_light': 0,
						'b_temp': 0, 'b_light': 0})
		return json_data
