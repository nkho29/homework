import json

with open("example.json", "r" ) as example_file:
    read_example = example_file.read()
    print(type(read_example))
    dict_example = json.loads(read_example)
    print(type(dict_example))
    dict_example["Number"] = "1"
    print(dict_example)
    str_example = json.dumps(dict_example)
    print(type(str_example))

with open("new.json", "w+") as new_file:
     new_file.write(str_example)
     new_file.seek(0)
     print(new_file.read())