import time
name=input("Enter Your Name:")
timestamp =time.strftime("%H:%M:%S")
hour=int(time.strftime("%H"))
print(hour)
# hour=int(input("enter hour:"))
# print(hour)

if (hour >= 0 and hour < 12):
    print("Good morning")
elif( hour >=12 and hour <16):
    print("Good Afternoon") 
elif(hour>=17 and hour<24):
    print("Good Night")    

    
    
    
    
    
    
    
    
    
    