#while loops keep iterating until a condition is broken (becomes false)
#or a control flow of IF takes you to a break clause

#syntax --> while <condition>:
    #block of code

#While iterator with a counter
# import time
# age = 0 #has to be outside so it doesnt get reset to zero
# while age <= 18:
#     print('Happy Birthday')
#     print('Here is some money')
#     print('You are', age)
#     age += 1
#     time.sleep(1)
#
#while iterator with break condition
age = 0
while True:
    print('Happy Birthday')
    print('Here is some money')
    print('You are', age)
    age += 1
    response = input ('> continue?')('y/n')
    if response == 'n':
        break
    elif response =='egg':
        print('EGGS! Bip')
    elif response == 'y'
        pass
    else: 
        print('cool cool', response)
        time.sleep[2]