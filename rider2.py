import random
import json


user=input("enter your name:")
print('***WElCOME TO UBER***',user)
print("please wear the MASK and sanitize your hands")
print(" ")
lst=['sarjapur','huskur','electonic city','textmart','havalahalli','star market','nandihills','D-Mart','ksr','yashwanthpoor','shivaji market']
lst2=[['mock'],['john','prem','salman'],['kethan','masun'],['krishna'],['vamsi']]
i=0
while i<len(lst):
    print("*",lst[i])
    i+=1
#print(lst)
print("*********************************************")
pick_up=input(" Enter your pick-up location :")
user2=input("please choose your destination above mentioned locations:")
def my_rider():
    index = 1
    total=0
    dict={}
    while True:
        limit = input("enter your choice(go/stop) :")
        if limit=="stop":
            break
        a=random.choice(lst2)
        i=0
        while i<len(a):
            print(a[i], "is avaialble")
            i+=1
        
        if user2 in lst: 
            rider=input("choose the rider :")
            num=int(input("how many kilometers :"))
            b=num*5
            total+=b
            print("**pay your money here**")
            print(rider,"total money = ",total)
            dict[rider]={"kilometers":num,"amount":b}
            print(dict)
        else:
            print("Sorry!! We are not found your location")
        index+=1

    with open("rider.json","w+") as file:
        json.dump(dict,file,indent=4)
        a=json.dumps(dict)
        return dict

def main():
    user3=int(input("Enter 1 for book the cab:"))
    if user3==1:
        print("your destination is confirmed!!")
        user5=int(input("enter (1 for confirm your cab and 2 for cancel the cab)"))
        if user5==1:
            print("your cab is confirmed")
            my_rider()
            rating=input("If you driver is good give rating:")
        else:
            print("your cab is cancelled succesfully")
        
    
main()
print("Thank you to visit uber!!!stay safe")
    


    
