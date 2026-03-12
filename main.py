
<<<<<<< HEAD

title = []
time = []
status = []
=======
from tracker import add_book, view_reading_list

>>>>>>> 4b7909c (udated file names and added imports from tracker)

def menu():
    print("1. Add Book")
    print("2. View reading list")
    print("3. View summary")
    print("4. Exit")



def summary(): 
        pass





while True:
        
        menu()
        number = input("Enter choice: ")

        if number == "1":
                add_book()

        elif number == "2":
                view_reading_list()

        elif number == "3":
                summary()

        elif number == "4":
                print("Goodbye!")
                break
        else:
                print("Invalid choice. Try again.")
        
