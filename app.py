# has_good_credit = True
# has_crimnal_record = True
#
# if has_good_credit and not has_crimnal_record:
#     print("Eligible for loan")
#
#
# temperature = 30
#
# if temperature != 30:
#     print ("It's a hot day")
# else:
#     print ("It's not a hot day")
#
# name = 'yu'
#
# if len(name) < 3:
#     print("name must be at least 3 characters")
# elif len(name) > 50:
#     print("name can be maximum of 50 characters")
# else:
#     print('name looks good')
# weight = int(input('Weight: '))
# unit= input ('(L)bs or (K)g: ')
# if unit.upper() == "L":
#     converted = weight * 0.45
#     print(f'You are {converted} kilos')
# else:
#     converted = weight / 0.45
#     print(f'You are {converted} pounds')
# i = 1
# while i <=5:
#     print('*' * i)
#     i = i + 1
# print("Done")


name = input('Write your name: ')

if len(name) < 3:
    print("name must be at least 3 characters")
elif len(name) > 50:
    print("name can be maximum of 50 characters")
else:
    print('name looks good')