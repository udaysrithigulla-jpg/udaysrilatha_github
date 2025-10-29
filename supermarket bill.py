
from datetime import date , datetime
name=input("enter your name:")
#list of items:
lists='''
salt

40/kg

coffe powder

80/kg

oil

30/liter

soaps

40/each

rice

90/kg'''

print(lists)
#declaration:
price=0
pricelist= []
totalprice=0
finalprice=0
ilist=[]
qlist=[]
plist=[]
#rates for items:
items={"salt":40,
"coffe powder":80,
"oil":30,"soaps":40,"rice":90}
option=int(input("list of items press1:"))
if option == 1:
    print(lists)
for i in range(len(items)):
    inp1=int(input("if u want to buy press1 or 2 for exit"))
    if inp1 == 2:
        break
    if inp1 == 1:
        item=input("enter ur items:")
        quantity=int(input("enter ur quantity:"))
        if item in items.keys():
            price=quantity*(items[item])
            pricelist.append((item,items,quantity,price))
            totalpricet=price
            ilist.append(item)
            qlist.append(quantity)
            plist.append(price)
            gst=(totalprice*5)/100
            finalamount=gst+totalprice
        else:
           print("sry u entered item is not avaiable" )
    else:
      print("u enter wrong number")
    inp=input('are u want to bill the items yes or no:')
if inp == "yes":
    pass
    if finalamount != 0:
       for i in range (len(pricelist)):
            print(i,ilist[i],qlist[i],plist[i])
    if inp == "yes":
      pass
      if finalamount !=0:
         print(25*"=","ammu supermarket", 25*"=")
         print(30*"","thigulla")
         print("Name:",name,30*" ","date:",date.today())
         print(74*"-")
         print("sno",7*" ","items",7*" ","quantity",7*" ","price")
         for i in range(len(pricelist)):
              print(i,7*'',7*'',ilist[i],7*"",qlist[i],plist[i])
              print(74*"-")
              print(50*" ","totalprice", 'rs',totalprice)
              print("gst amount:",50*" ",'rs',gst)
              print(74*"-")
              print(50*" ","final amount",'rs',finalamount)
              print(74*"-")
              print(50*" ","thak you for visiting")
              print(74*"-" )