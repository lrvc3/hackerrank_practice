# Creating an acronym generator
'''
Convert Ram Access Memory: RAM
All caps
'''

original_string = input("Enter the string: ")

list1 = original_string.split()
# This method works too
# acron = ""
# for i in range(len(list1)):
#     acron += list1[i][0].upper()

# print(acron)
acron = ""
for i in list1:
    acron += i[0].upper()
print(acron) 
    
