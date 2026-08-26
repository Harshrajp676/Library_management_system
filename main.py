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
        print("4 -> Delete Books")

        self.main()

    def main(self):
        """Main input loop for the menu."""
        while True:
            try:
                choice = input("\nEnter your choice: ").strip()
            except (EOFError, KeyboardInterrupt):
                print("\nExiting.")
                break

            if choice == "0":
                print("Goodbye.")
                break
            elif choice == "1":
                self.dis_books()
            elif choice == "2":
                self.add_book()
            elif choice == "3":
                self.edit_books()
            elif choice == "4":
                # minimal delete implementation to match menu
                del_name = input("Enter Name of book to delete: ")
                for i in list(library.lib.keys()):
                    if library.lib[i].name == del_name:
                        del library.lib[i]
                        print("Book Deleted Successfully")
                        break
                else:
                    print("Book Not Found")
            else:
                print("Invalid choice. Please try again.")

    def dis_books(self):
        print("--------------------------")
        for i in library.lib:
            print(f"{library.lib[i]}")
            print("--------------------------")

    def add_book(self):
        print("--------------------------")
        self.new_name = input("Enter Book Name : ")
        self.new_auth = input("Enter Book's Auther full Name : ")
        self.new_status = "Available"
        self.new_id = 101 + len(library.lib)
        library.lib[self.new_id] = Book(self.new_name,self.new_auth,self.new_status)
        
        if self.new_id in library.lib : print("Book Added Succesfully") 
        else : print("Please Try Again Later.") 

    def edit_books(self):
        self.edit_name = input("Enter Name of book : ")
        for i in library.lib:
            if library.lib[i].name == self.edit_name:
                print("Book Found. autherd by ",self.lib[i].auther)
                intend_name=input("Enter Name : ").lower()
                intend_auther=input("Enter Auther : ").lower()
                intend_status=input("Enter Status : ").lower()
                self.lib[i] = Book(intend_name,intend_auther,intend_status)
                print("Book Edited Succesfully")
                return

        else : print("Book Not Found")
   
library()
