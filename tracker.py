from data import titles, times, statuses

def add_book():

    title = input("Enter book title: ")

    time = int(input("Enter reading time (minutes): "))

    status = input("Enter status (Finished/In Progress): ")

    titles.append(title)
    times.append(time)
    statuses.append(status)

    print("Book added!")
