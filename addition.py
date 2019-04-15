"""This is a simple program to add the two given numbers"""

first_value = int(input("Enter a number to add: "))

second_value = int(input("Enter another number to add with {0}: ".format(first_value)))

addition = first_value + second_value

print("\nSum of {} and {} is {}".format(first_value,second_value,addition))