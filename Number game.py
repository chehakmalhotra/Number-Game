print("This is a fun little game about counting. It's pretty easy, really. Here's how it works ...")

print("We start off with Zero (0) and take turns counting up by 1, 2, or 3. Whoever counts to 23 looses!")

print("Example: I start off by counting to 1. Because I counted to 1, you can count up to 2, 3, or 4. Let's say you pick 4. I can then pick 5, 6, or 7. The goal of the game is to get the other player to count to 23!")

print("Okay, now that you know how to play ... would you like to pick first?")
re="yes"
while re=="yes" or "y":
    z=0
    choice=input("Do you want to go first or second?")
    if choice=="second":
       a="2"
       print("I choose", a)
       for i in range(3,23,4):
          a=3+i
          if a=="22":
             break
          print("Choose" ,i,i+1, "or" , i+2)
          x=input("")
          print("I choose", a)
       x=input("Choose 23")


    if choice=="first":
        print("Choose",1,2,"or",3)
        k=int(input(""))
        if k==1:
          print("I choose",2)
          for i in range(3,23,4):
             a=3+i
             if a=="22":
                break
             print("Choose",i,i+1,"or",i+2)
             x=input("")
       
             print("I choose",a)
        elif k==3:
            a="6"
            print("I choose",a)
            for i in range(7,23,4):
                a=3+i
                print("Choose",i,i+1,"or",i+2)
                x=input("")
                print("I choose",a)
            if a=="22":
                print("Choose 23")
        elif k==2:
            a=3
            for i in range(3,23,4):
                print("I Choose",a)            
                print("Choose",a+1,a+2,"or",a+3)
                x=int(input(""))
                if (x-2)%4!=0:
                    if x%4==0:
                            a=x+2
                    elif (x-1)%4==0:
                        a=x+1
                    elif (x+1)%4==0:
                        a=x+3
                    else:
                        a+=4
               
    print("I Choose", a)
    if a=="22":
        x=input("Choose 23")
        re=input("It's really very easy, try again?")
    
