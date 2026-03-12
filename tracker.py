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

from data import titles, times, statuses

def view_reading_list():
    
    if len(titles) == 0:
        print("\nNo books in the reading list yet.\n")
        return
    
    print("\nYour Reading List:")    
    
    for i in range(len(titles)):
        print(f"{i+1}. Titles: {titles[i]} | Time: {times[i]} minutes | Status: {statuses[i]}")
    
    print()

def summary_report():

    if len(titles) == 0:
        print("\nNo data available.\n")
        return

    total_books = len(titles)
    total_time = sum(times)

    finished = 0
    in_progress = 0

    for status in statuses:
        if status.lower() == "finished":
            finished += 1
        elif status.lower() == "in progress":
            in_progress += 1

    max_time = max(times)
    index = times.index(max_time)
    max_book = titles[index]

    print("\nSummary Report")
    print("-----------------")
    print(f"Total books: {total_books}")
    print(f"Total reading time: {total_time} minutes")
    print(f"Finished: {finished}")
    print(f"In Progress: {in_progress}")
    print(f"Book with most time spent: {max_book} ({max_time} minutes)")
    print()