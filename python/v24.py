# tupple change nh hote
tup=(1,23,3,4,5,"grr")
# tup=(1,)
# agr hum one value dere to , dena padega nhi to int ayega 

print(type(tup),tup)
print(len(tup))
print(tup[0])
print(tup[-1])
print(tup[2])
print(tup[3])
if 2 in tup:
    print("yes")
else:
    print("no")
tup2=tup[1:2]
print(tup2)