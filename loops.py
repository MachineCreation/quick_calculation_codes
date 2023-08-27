#first_list = [1,2,3,"a","b","c"]

#letter_list = []
#number_list = []

#for item in first_list:
#    if item in [1,2,3,4,5,6,7,8,9,0]:
#        number_list.append(item)
#   else:
#        letter_list.append(item)


#print(number_list)
#print(letter_list)

#first_list_length = len(first_list)

#for i in range(first_list_length):
 #   print(first_list(i))




while True:
    user_input = input('Type your name or type "quit"\n')
    if user_input.lower() == 'quit':
        break
    elif user_input.lower()[0] in 'abcdefg':
        print('Go home')
    elif user_input.lower()[0] in 'hijklmnop':
        print('Stay here')
    else:
        print('Proceed to next phase')
