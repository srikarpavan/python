def main():
    l = 0

    menu()

    l = int(input("Please type 1-4 from the menu or press 5 to quit. "))
    if l == 1:
        a = int(input("Enter pushed element"))
        q.enqueue(a)
    elif l == 2:
        print(q.dequeue())
    elif l == 3:
        print(q.display())
    elif l == 4:
        print(q.size())
    elif l == 5:
        print("Good Bye! ")
    else:
        print("That is not a valid selection, please type the correct number\n")
        main()
    while l == 5:
        break
    else:
        replayMenu()


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

    def display(self):
        return self.items


def replayMenu():
    startover = ""
    startover = input("Would you like to start from the beginning, yes or no? ")
    while startover.lower() != "yes":
        print("Thanks for using our Stacks Program! Bye! ")
        break
    else:
        main()


def menu():
    print("Select a operation'")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Size")
    print("4. Display")
    print("5. Quit\n")


q = Queue()
main()