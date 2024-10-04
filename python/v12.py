# string slicing
name="harry,wathley"
# print(name[0:5])
# including 0 but not 4
print(name[6:12])
print(len(name))
print(name[1:4])
print(name[:5])
print(name[0:-3])
print(name[-1:len(name)-3])
print(name[-3:-1])
# quick quicz
nm="harry"
print(nm[-4:-2])

#uper case
a="have a good day"
print(a.upper())

# lower case
a="have a good day"
print(a.lower())

# strip method in string modified
a="  i want you to do   warship  "
print(a.strip())
# replace string
b="i  want she to purches leptop"
print(b.replace("i","you"))

# split
a="i am taking example "
print(a.split())

# captialize
a="blogheading"
print(a.capitalize())

# center method
a="its center method"
print(a.center(40))

# count function
a="how mony word are come multiple time  time"
print(a.count("time"))
# endwith 
str1="welcome to the console"
print(str1.endswith("console"))

# find
a="find a function"
print(a.find("a"))
 
# index function
# a="to the"
# print(a.index("is"))

# isalnum
a="welcome  To"
print(a.isalnum())

# isalphase()
a="i"
print(a.isalpha())


# is lower
s="small"
print(s.islower())
# isprintable
a="t is printable "
print(a.isprintable())

# issopace
a="  "
print(a.isspace())

# istittle
a="os is tittle"
print(a.istitle())

# swapcase
a="UPPER CASE TO LOWER CASE"
print(a.swapcase())
# title
a="tittle tittle"
print(a.title())








