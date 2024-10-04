# print a list 
# list = [1,2,4,6,88,125]
# for i in list:
#     print(i)
#    count a number 
 
# a=123456
# a= str(a)
# count=0
# for i in a:
#     count+= 1
# print(count)

#   Python program to check if the given string is a palindrome.  

# given_number="madam"
# reverse_str=""
# for i in given_number:
#     reverse_str=i+reverse_str
# if(given_number==reverse_str):
#    print("The string", given_number,"is a Palindrome.")
 
# # else the given string is not a palindrome   
# else:
#    print("The string",given_number,"is NOT a Palindrome.")



#  Python program that accepts a word from the user and reverses it.
# given_number=input("enter a words:")
# reverse_str=""
# for i in given_number:
#   reverse_str=i+reverse_str
# print(reverse_str)   

# Armstrong number, ya Narcissistic number, 
# ek aisa number hota hai jo apne digits ke sum ke 
# equal hota hai, jab unhe unke digits ke count ke power par 
# raise kiya jata hai.


# the given number
given_number = 153
 
# convert given number to string
# so that we can iterate through it
given_number = str(given_number)
 
# store the lenght of the string for future use
string_length = len(given_number)
 
# initialize a sum variable with
# 0 value to store the sum of the product of
# each digit
sum = 0
 
# iterate through the given string
for i in given_number:
    sum += int(i)**string_length
 
# if the sum matches the given string
# its an amstrong number
if sum == int(given_number):
    print("The given number",given_number,"is an Amstrong number.")
 
# if the sum do not match with the given string
# its an amstrong number
else:
    print("The given number",given_number,"is Not an Amstrong number.")

