class Book():
    def __init__(self,book_name,book_auther,book_issued_status):
        self.name =  book_name
        self.auther = book_auther
        self.status = book_issued_status


    def __str__(self):
        return (f"Book Name : {self.name.capitalize()}\nAuther Name : {self.auther.title()}\nAvailblity status : {self.status.title()}\n")

class library():
    lib = {
        101 : Book("martian",'andy willer','available'),
        102 : Book("python 101",'john smith','unavailable')
    }

    def __init__(self):
        self.display()

    def display(self):
        print("===========================")
        print("----------LIBRARY----------")
        print("===========================")
        print("\n0 -> Exit")
        print("1 -> List all books")
        print("2 -> Add Books")
        print("3 -> Edit Books")

        self.main()

    def dis_books(self):
        print("--------------------------")
        for i in self.lib:
            print(f"{self.lib[i]}")
            print("--------------------------")

    def add_book(self):
        print("--------------------------")
        self.new_name = input("Enter Book Name : ")
        self.new_auth = input("Enter Book's Auther full Name : ")
        self.new_status = "Available"
        self.new_id = 101 + len(self.lib)
        self.lib[self.new_id] = Book(self.new_name,self.new_auth,self.new_status)
        
        if self.new_id in self.lib : print("Book Added Succesfully") 
        else : print("Please Try Again Later.") 

    def edit_books(self):

        for i in self.lib:
            if self.lib[i].name == self.edit_name:
                print("Book Found. autherd by ",self.lib[i].auther)
                intend_name=input("Enter Name : ").lower()
                intend_auther=input("Enter Auther : ").lower()
                intend_status=input("Enter Status : ").lower()
                self.lib[i] = Book(intend_name,intend_auther,intend_status)
                print("Book Edited Succesfully")
                return

        else : print("Book Not Found")

    def main(self):
        while True:
            user_input = input("\nEnter Your choice: ")
            if user_input.isdigit():
                if user_input == '1':
                    self.dis_books()

                elif user_input == '2':
                    self.add_book()
                
                elif user_input == '3':
                    self.edit_books()

                elif user_input == '0':
                    print("\n\tThanks For Visiting Library.\n")
                    break
                
                else: 
                    print("Please Enter Correct option.")
            else:
                print("Please Enter choice using Numbers Only.")

library()

"""
Functions To Add : 
    1.  Issue a Book 
    2.  Reurn a Book
    3.  Specific Book Info 

Featurs To Add : 
    Members and there ids 
        issueing books to specific customer
        cheking who has Whic issued books 

IMP : Adding an Admin Pannel 
"""





""" Pending Edit_books() 
 print("\nEnter choice from following :- \n1 -> name\n2 -> Auther \n3 -> Availbility Status")
 self.edit_type = input("What you want to edit : ").lower()
 if self.edit_type == '1' or self.edit_type == '2' or self.edit_type == '3' :
     check_name = input("Enter Name :")
     occur = 0
     for i in self.lib:
         if self.lin[i].name == check_name:
             occur+=1
             if occur>2:
                 print("theres Two Book named", check_name)
                 check_auther = input('Please Enter Auhter name')
                 for j in self.lib:
                         if self.
         else : 
             print("please enter correct Book name.\nPlease try again. ")

 else : 
     print("please enter correct option to edit .\nPlease try again. ")

"""