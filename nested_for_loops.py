# Here we iterate of nested lists and/or dictionaires

list_data = [1, 2, 3]#
embedded_list = [[1, 2, 3],[7, 8, 9]]

dict_data = {
    1:{
        'name': 'James',
        'money': '£30000'
    },
    2:{
        'name':'Isabella',
        'money':'£330001'

    }
}
# for data in embedded_list:
#     print(data) #data is a list
#     for embedded_data in data:
#         print(embedded_data)

for data in dict_data:
    print(data)


