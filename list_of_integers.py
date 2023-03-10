
# Write a program that accepts user input to create a list of integers. Then, compute the sum of all the integers in the list.

numbers = input("Enter numbers: ")
list_int = [int(x) for x in numbers.split(',')]
total= sum(list_int)
print ("Total is ", total)
