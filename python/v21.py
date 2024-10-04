# defalut arrgument 
# def average(a,b,c=1):
#     print("the averge is",(a+b)/2)
    
# # average(4,6)
# # average(5)
# # a ki only value di h isliye output 6 ara h
# # or agr humko b ki value dena h to b=8
# KeyWord arguments:
# average(b=9,a=21)


# def name(fname,mname="jhon" ,lname="whatson"):
#     print("hello,",fname,mname,lname)
    
# name("any","Wathley","Harsha")
# Required argument
# a or b ki value optional h c ki value fixed
# average(5,6)

# def name(fname,mname,lname):
#     print("hello,",fname,mname,lname)
    
# name("peter","quil","Wathley") 



# varible leght arguments:
def averge(*numbers):
    # print(type(numbers))
    sum=0
    for i in numbers:
        sum=sum +i
    # print("averge is:",sum/len(numbers))
    return 7
    return sum/len(numbers)
c=averge(5,6,3,4)
print(c)

# def name(**name):
#     print(type(name))
#     print('hello,',name["fname"],name["mname"],name["lname"])
# name(mname="a",lname="b",fname="c")












  
