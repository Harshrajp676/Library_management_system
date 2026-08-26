class Person () : 
    def __init__(self,user_id,name,issued_books,user_status):
        self.__user_id= user_id
        self.__name = name 
        self.__issued_books = issued_books
        self.__user_status = user_status
    
    def __str__(self):
        return (f"\nAccount info :- \n\tUser ID : {self.__user_id}\n\tName : {self.__name.capitalize()}\n\tIssued Books : {self.__issued_books} \n\tStatus : {self.__user_status.capitalize()}")
    
class Memebers():

    Users_list = {
    1 : Person(1,'harsh',['python 101'],'admin'),
    2 : Person(2,'raj',['martian'],'user'),
    3 : Person(3,'parmar',['project hail marry'],'user'),
    }

    def __init__(self):
        self.main()

    def display_menu(self):
        print("==================================================")
        print("----------------------WELCOME---------------------")
        print("==================================================")
        print("\n\t0 -> Exit")
        print("\t1 -> Display account information")
        print("\t2 -> Return Book")

    def id_check(self):
        while True:
            user_id = input("Enter You ID : ").lower()
            if user_id.isdigit() : 
                if int(user_id) in Memebers.Users_list:
                    return user_id
                else : 
                    print("User Not found,\nPlease Try again")
            else:
                print("Please Enter ID in numbers " if user_id.isdigit()== False else "User Not Found\nPlease Try again")

    def acc_info(self):
        user_id = self.id_check()
        print(Memebers.Users_list[int(user_id)] if user_id != None else "")

    def return_book(self):
        user_id = int(self.id_check())
        temp_issued = Memebers.Users_list[user_id]._Person__issued_books
        print("Your Issued Books : ",temp_issued)
        user_return = input("Enter book to reteurn : ").lower().strip()
        if user_return in  temp_issued:
            for i in range(0,len(temp_issued)):
                if temp_issued[i] == user_return : temp_issued.pop(i)
                
            Memebers.Users_list[user_id]._Person__issued_books = temp_issued
            print(f"You issued Books : {temp_issued if bool(temp_issued == True) else "None"}")

        else :
            print("currently There is no such issued book on you id.\nPlease Try agian")

    def main(self):
        self.display_menu()
        while True :
            choice  = input("\nenter you choice : ").lower()
            if choice.isdigit() and choice == '1':
                self.acc_info()
                
            elif choice.isdigit() and choice == '2':
                self.return_book()

            elif choice.isdigit and choice =='0':
                print("Thank you for using .")
                break

            else :
                print("Please Enter Correct Option\nPlease Try Again")

Memebers()