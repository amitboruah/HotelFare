class hotelfarecal:

    def __init__(self,total='',room=0,p=0,food=0,a=1000,name='',address='',cindate='',coutdate='',rno=''):

        print ("\n\n*****WELCOME TO THE HOTEL*****\n")

        self.total=total
        self.food=food
        self.room=room
        self.a=a
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=rno
    def inputdata(self):
        self.name=input("\nEnter your name:")
        self.address=input("\nEnter your address:")
        self.cindate=input("\nEnter your check in date:")
        self.coutdate=input("\nEnter your checkout date:")
        self.rno=input("\nEnter Room no:")
        
    def roomrent(self):

        print ("We have the following rooms for you:-")

        print ("1.  type A rs 6000 Per Night :-")

        print ("2.  type B rs 5000 Per Night :-")

        print ("3.  type C rs 4000 Per Night :-")

        print ("4.  type D rs 3000 Per Night :-")

        x=int(input("Enter Your Choice Please :-"))

        n=int(input("For How Many Nights Did You Stay:"))

        if(x==1):

            print ("you have opted room type A")

            self.room=6000*n

        elif (x==2):

            print ("you have opted room type B")

            self.room=5000*n

        elif (x==3):

            print ("you have opted room type C")

            self.room=4000*n

        elif (x==4):
            print ("you have opted room type D")

            self.room=3000*n

        else:

            print ("please choose a room")

        print ("your room rent is =",self.room,"\n")

    def restaurentbill(self):

        print("\n*****RESTAURANT MENU*****")

        print("1.water  :-Rs20","\n","2.tea  :-Rs10","\n","3.Fixed breakfast  :-Rs100","\n","4.Fixed lunch  :-Rs140","\n","5.dinner  :-Rs180","\n","6.Exit")


        while (1):

            c=int(input("Enter your choice:"))


            if (c==1):
                d=int(input("Enter the quantity:"))
                self.food=self.food+20*d

            elif (c==2):
                 d=int(input("Enter the quantity:"))
                 self.food=self.food+10*d

            elif (c==3):
                 d=int(input("Enter the quantity:"))
                 self.food=self.food+90*d

            elif (c==4):
                 d=int(input("Enter the quantity:"))
                 self.food=self.food+110*d

            elif (c==5):
                 d=int(input("Enter the quantity:"))
                 self.food=self.food+150*d

            elif (c==6):
                break
            else:
                print("Invalid option")

        print ("Total food Cost=Rs",self.food,"\n")




    def display(self):
        print ("\n\n******HOTEL BILL******")
        print ("Customer details:-\n")
        print ("Customer name:",self.name)
        print ("Customer address:",self.address)
        print ("Check in date:",self.cindate)
        print ("Check out date",self.coutdate)
        print ("Room no.",self.rno)
        print ("Your Room rent is:",self.room)
        print ("Your Food bill is:",self.food,"\n")
   
        

        self.total=self.room+self.food

        print ("Your sub total bill is:",self.total)
        self.a=(18*self.total)/100
        print ("Additional Service Charges is",self.a)
        print ("Your grandtotal bill is:",self.total+self.a,"\n")
        

                   

def main():

    a=hotelfarecal()
    

    while (1):
        print("1.Enter Customer Data")
        
        print("2.Calculate room rent")

        print("3.Calculate restaurant bill")

        print("4.Show total cost")

        print("5.EXIT")

        b=int(input("\nEnter your choice:"))
        if (b==1):
            a.inputdata()

        if (b==2):

            a.roomrent()

        if (b==3):

            a.restaurentbill()

        if (b==4):

            a.display()

        if (b==5):

            quit()
main()

