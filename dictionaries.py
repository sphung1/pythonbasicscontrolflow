#dictionaries work with key values pairs
    #they DO NOT use index. they use KEYS
    #You look up keys to get values
    #they are unique
    #dictionaires AKA --> hashs or (confusingly) objects in JS

#defining a dictionary
    #{}
    #key: value
    #where key can be a string or a number with colon(:) at the end
    #where the value can be any object (arrays, dictionaries, stirngs etc...)

crazy_cruella_vil = {
    'name':'Cruella De Vil',
    'occupation': 'Evil with puppies',
    'address': 'Diseny World',
    'door_number': 10,
    'skills': ['fashion', 'laughing', 'design']
}
print(crazy_cruella_vil)
print(type(crazy_cruella_vil['name']))

#how to accesss the didtionary ---> use the keys inside []

print(crazy_cruella_vil['skills'])

#how to EDIT a value
    #use the key and [] and reassign

    #accessing and directly manipulating using methods
    #adding skill to directory

crazy_cruella_vil['skills'].append('Business Skills')
print(crazy_cruella_vil['skills'])

#change door number
crazy_cruella_vil['door_number']=101
print(crazy_cruella_vil['door_number'])

#ADDING a new key:value
    #same as editing = if it doesnt exists, it creates it

crazy_cruella_vil['favourite_colour'] = 'Black & White'
print(crazy_cruella_vil['favourite_colour'])


#USEFUL methods of dictionaires
    #Getting all the keys out

keys = crazy_cruella_vil.keys()
print(keys)

values = crazy_cruella_vil.values()
print(values)