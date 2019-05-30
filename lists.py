# lists in python
#keep lists of objects ordered by index
#to delcare a list use the []
#separate objects using commas,
#List AKA --> Arrays


crazy_ex_landlords = ['Jane', 'Mike','Cruela']

print (crazy_ex_landlords)
print (type(crazy_ex_landlords))

#how do we access a list --> with the index

print(crazy_ex_landlords[1])
print(crazy_ex_landlords[-1])

#edit an entry --> use the index and reassign
    #example change mike to mike tyson
crazy_ex_landlords[1] = 'Mike Tyson'

print (crazy_ex_landlords[1])

#adding to the list --> use .append()
    #add Yuri to the list
crazy_ex_landlords.append('Yuri')

print(crazy_ex_landlords)

#removing something from list --> use .pop()
    #remove jane from list
crazy_ex_landlords.pop(0)

print(crazy_ex_landlords)

#lists can contain anything - they can contain:
    #strings, int, objts,lists, dictionaries etc...
combined_list = [1,'10', 'ten', True, crazy_ex_landlords]

print (combined_list)

#List slicing --> is used to manage lists
