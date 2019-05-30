#Here we will practice ceating a list of dictionaires

list_of_evil_people = []

crazy_cruella_vil = {
    'name':'Cruella De Vil',
    'occupation': 'Evil with puppies',
    'address': 'Diseny World',
    'door_number': 10,
    'skills': ['fashion', 'laughing', 'design']

}

villan_2 = {
     'Name': 'Mickey Mouse',
     'Occupation': 'Entertainer',
     'Address':'DisenyLand',
     'Door Number': 1,
     'Skills': ['Being loud', 'Slapping', 'Autographs']
 }

villan_3 = {
     'Name' : 'V3',
     'Occupation': 'Robber',
     'Address': 'Streets',
     'Door Number': 'None',
     'Skills':['Stealing', 'Running']
 }

list_of_evil_people.append(crazy_cruella_vil)
list_of_evil_people.append(villan_2)
list_of_evil_people.append(villan_3)

# #How do we access mickey mouse' details?
print(list_of_evil_people[1])

for dict in list_of_evil_people:
    print(dict)
    print(type(dict))
    for key in dict:
        print(key)
        print (dict[key])
        print((str)(key) + ':'. dict[key])