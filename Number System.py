sp=int(input("enter the starting point value : "))
ep=int(input("enter the end point value : "))
upt=int(input("enter the updatation value : "))
order=int(input("for forward order press 1 and for reverse order press 2 : "))
choice=int(input("for row/horizontal press 1 and for coloum/vertical press 2 : "))
if order==1 and (ep>sp):
    for i in range (sp,ep+1,upt):
        if choice==1:
            print(i,end=' ')
        elif choice==2:
            print(i) 
        else:
            print("invalid choice enter")    
elif order==1 and (sp>ep):
    for i in range (ep,sp+1,upt):
        if choice==1:
            print(i,end=' ')
        elif choice==2:
            print(i)
elif order==2 and (ep>sp):
    for i in range (sp,ep+1,upt):
        if choice==1:
            print(i,end=' ')
        elif choice==2:
            print(i)
        else:
            print("invalid choice enter")
elif order==2 and (sp>ep):
    for i in range (ep,sp+1,upt):
        if choice==1:
            print(i,end=' ')
        elif choice==2:
            print(i)
        else:
            print("invalid choice enter")
else:
    print("invalid order enter")            