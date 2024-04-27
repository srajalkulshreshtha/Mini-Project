#inventory management
l={"parle g":10,"oreo":20,"dairy milk":80,"halidram namkeen":80,"cold drink":80,"energy drink":40,"toffie":5,}
totalamount=0
print(l)
name=input("enter customer name:")
cardamount=int(input("enter card balance:"))
while True:
    cart=input("items purchased:")
    quantity=int(input("enter the quantity:"))
    s=l[cart]
    a=quantity*s
    print(a)
    choice=int(input("1 to continue:"))
    totalamount+=a
    if(choice==1):
        continue;
    else:
        break;
#totalamount+=a
if(cardamount<totalamount):
    print("insufficient balance")
    r=int(input("0 to recharge"))
    if(r==0):
        k=int(input("enter recharge amount"))
        cardamount+=k
        amountleft=cardamount-totalamount
        print("card balance",amountleft)
    else:
        print("no rechgarge")
elif(cardamount>totalamount):
    amountleft=cardamount-totalamount
    print("card balance",amountleft)
else:
    print() 
