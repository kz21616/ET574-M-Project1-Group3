import time

from data import titles, times, statuses

def add_book():

    title = input("Enter book title: ")

    time = int(input("Enter reading time (minutes): "))

    status = input("Enter status (Finished/In Progress): ")

    titles.append(title)
    times.append(time)
    statuses.append(status)

    print("Book added!")


def view_reading_list():
    if len(titles) == 0:
        print("No books in the reading list yet.")
        return
    print("\nYour Reading List:")    
    
    for i in range(len(titles)):
        print(f"{i+1}, {titles[i]} | {time[i]} minutes | {status[i]}")
