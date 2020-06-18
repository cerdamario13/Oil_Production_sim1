import string

characters = string.printable

# print(characters)

test = ["Dante", "t"]
for i in characters:
  test[1] = i
  # print(test)

test2 = 'sjhdfjhauihewhfuohsorry'
if 'sorry' in test2:
  print('yay')
