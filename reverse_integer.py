# Code to reverse an integer with no zeros and signs
#  

x = int(input("Enter the integer number: "))
integer_string = str(x)
list_integrs = list(integer_string)
length = len(list_integrs)

list_integrs2 = []
for i in range(length - 1, -1, -1):
    if list_integrs[i] != '0':
        list_integrs2.append(list_integrs[i])
    else:
        continue

String_of_intergs = ''.join(list_integrs2)
print(String_of_intergs)
