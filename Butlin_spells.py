file_directory = "dd5th_spells.json"

json_data=open(file_directory).read()

data = json.loads(json_data)
pprint(data)