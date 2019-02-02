def main():
    l = 0

    menu()

    l = eval(input("Please type 1-4 from the menu or press 5 to quit. "))
    if l == 1:
        a = int(input("Enter pushed element"))
        s.push(a)
    elif l == 2:
        print(s.pop())
    elif l == 3:
        print(s.recent())
    elif l == 4:
        print(s.display())
    elif l == 5:
        print("Good Bye! ")
    else:
        print("That is not a valid selection, please type the correct number\n")
        main()
    while l == 5:
        break
    else:
        replayMenu()


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def recent(self):
        return self.items[len(self.items) - 1]

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
    print("1. Push")
    print("2. Pop")
    print("3. Recent")
    print("4. Display")
    print("5. Quit\n")


s = Stack()
main()