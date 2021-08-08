import random
class Food:
    def __init__(self):
        self.admin={'vikaspaliwal1111':1234567}
        self.food={}
        self.user={}
        
    def add_food(self):                               ## add the food in list
        i=int(input("enter how types of food you want to add: "))
        a={}
        for i in range(i):
           
            name=input("Enter food name: ")
            food_id=random.randint(1,100)
            quantity=input("enter the quantity of food: ")
            initial_price=int(input("enter price of food: "))
            discount=int(input("enter discount on this food in percentage: "))
            final_price=initial_price-((initial_price/100)*discount)
            stock=int(input("how many stocks you want to add : "))
            a[food_id]={"name":name,"quantity":quantity,"initial_price":initial_price,"discount":discount,"final_price":final_price,"stock":stock}
            print()
            print("Added successfully")
        self.food.update(a)
        
        
        
    def food_list(self):                             ## Food lsit which user can see 
        i=[i for i in self.food.keys()]
        for k in range(len(i)):
            print((self.food[i[k]]["name"]).title(),"\t(",self.food[i[k]]["quantity"],")","\t[ INR",self.food[i[k]]["final_price"],"]")
        a=input("Look Tast ,right!!!!!!yyou want to order something ? (enter yes or no)")
        if a=="yes" or "Yes":
            x=map(list(int, input().split()))
            print("Food is Ordered")
            print("Sit relax now and enjoy!!!!!!")
        elif a=="No" or "no":
            print("Thank you")
        else:
            print("invalid choice")
            
    
                                                       
    def edit_food(self):                             ## Edit the food
        i=[i for i in self.food.keys()]
        x=int(input("enter food id: "))
        if x in i:
            ans=True
            while ans:
                choice=int(input("1.enter 1 to edit name \n2.enter 2 to edit quantity \n3.enter 3 to edit initial_price \n4.enter 4 to edit to discount \n5.enter 5 to edit stock \n6.enter 0 to exit "))
                if choice == 1:
                    a=input("enter new name of food: ")
                    self.food[x]["name"]=a
                elif choice == 2:
                    a=int(input("enter new quantity: "))
                    self.food[x]["quantity"]=a
                elif choice == 3:
                    a=int(input("enter new initial_price: "))
                    self.food[x]["initial_price"]=a
                elif choice == 4:
                    a=int(input("enter new discount:"))
                    self.food[x]["discount"]=a
                elif choice == 5:
                    a=int(input("enter new stocks: "))
                    self.food[x]["stock"]=a
                elif choice == 0:
                    ans=False
                else:
                    print("Invalid choice!!!!")
            print("Successfully edited")
        else:
            print("Sorry!!, you entered wrong food_id, please!,try again ")
            
            
            
    def delete_food(self):                      ## delete the food from list
        i=[i for i in self.food.keys()]
        x=int(input("enter food id: "))
        if x in i:
            del self.food[x]
            print("Successfully deleted")
        else:
            print("Sorry!!, you entered wrong food_id, please!,try again")
            
            
            
    def food_full_list(self):                     ## view food full details
        print(self.food)
    
     
    def view_profile(self):                       ## View profile of user
        x=input("please,enter your mail again ")
        print(self.user[x])
    
    
    
    def update_profile(self):                    ## profile_update
        x=input("please,enter your mail again for verification: ")
        
        ans=True
        while ans:
            i=int(input("1.enter 1 to update password \n2.enter 2 to update name \n3.enter 3 to update phone number \n4.enter 4 to update address \n5.enter 0 to exit "))
            if i == 1:
                a=input("enter new password: ")
                self.user[x][0]=a
                print("Successfully updated")
            elif i == 2:
                a=input("enter new name: ")
                self.user[x][1]=a
                print("Successfully updated")
            elif i == 3:
                a=int(input("enter new phone number: "))
                self.user[x][2]=a
                print("Successfully updated")
            elif i == 4:
                a=input("enter new address: ")
                self.user[x][3]=a
                print("Successfully updated")
            elif i == 0:
                ans=False
            else:
                print("Invalid choice!!!!")
            
            
            
            
                
        
        
        
    def login(self):                              ## Login
        i=input("admin or user: ")
        if i == 'admin':
            x=input("please,enter your mail")
            y=input("please,enter your password")
            a=[i for i in self.admin.keys()]
            b=[i for i in self.admin.values()]
            if x  in a and y in b:
                ans=True
                while ans:
                    choice=int(input("1.enter 1 to add food \n2.enter 2 to edit food \n3.enter 3 to delete food \n4.enter 4 to view food list along with details \n5.enter 0 to exit "))
                    if choice == 1:
                        self.add_food()
                    elif choice == 2:
                        self.edit_food()
                    elif choice == 3:
                        self.delete_food()
                    elif choice == 4:
                        self.food_full_list()
                    elif choice == 0:
                        ans= False
                    else:
                        print("Invalid choice!!!")
            else:
                print("Sorry, you are not an admin")
        elif i == 'user':
            x=input("please,enter your mail")
            y=input("please,enter your password")
            a=[i for i in self.user.keys()]
            b=[i for i in self.user.values()]
            if x in a:
                ans=True
                while ans:
                    choice=int(input("1.enter 1 to Place new order \n2.enter 2 to view order history \n3.enter 3 to update profile \n4.enter 4 to view profile \n5.enter 0 to exit "))
                    if choice == 1:
                        print("Here is the Food list : ")
                        self.food_list()
                        
                    elif choice == 2:
                        pass
                        
                        
                    elif choice == 3:
                        self.update_profile()
                        
                        
                    elif choice == 4:
                        self.view_profile()
                        
                    elif choice == 0:
                        ans=False
                    else:
                        print("Invalid choice!!!!")
            else:
                print("Sorry!!, you are not a user,Please,check!!!!!")
            
            
                
                       
                
                
            
        
    def signup(self):                                 ## signup
        a={}
        name=input("enter your full name: ")
        phone=int(input("enter your number: "))
        email=input("please,enter your email: ")
        address=input("please enter your address: ")
        password=input("create a password: ")
        print("signup successfully!!!")
        a[email]=[password,name,phone,address]
        self.user.update(a)
        
    def menu(self):                                  ## or starting interface
        print("You need to signup first")
        ans= True
        while ans:
            
            i=input("login or signup or exit ?")
            if i == 'login':
                self.login()
            elif i == "signup":
                self.signup()
            elif i == exit():
                ans=False
            else:
                print("Invalid input!!!!!")
        
        
            
            
a=Food()
a.menu()
