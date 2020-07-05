class Library:
    def __init__(self, libraryname, listofbooks):
        self.libraryname = libraryname
        self.listofbooks = listofbooks
        self.lentbooksinfo = {}

    def printlentbooksinfo(self):
        if bool(self.lentbooksinfo) == False:
            print('No book has been lent currently.')

        else:
            for book, user in self.lentbooksinfo.items():
                print(f'{book} has been lent to {user}.')

    def addbook(self, book):
        self.listofbooks.append(book)
        print("Book has been added to the book list.")

    def displaybooks(self):
        print(f"We have following books in our library: {self.libraryname}")
        for book in self.listofbooks:
            print(book)

    def lendbook(self, person, book):
        if book in self.listofbooks:
            self.listofbooks.remove(book)
            self.lentbooksinfo.update({book: person})
            print("Lender-Book database has been updated. You can take the book now.")

        elif book in self.lentbooksinfo.keys():
            print(
                f'{book} is not available right now. It has been lent to {self.lentbooksinfo[book]}')

        else:
            print(f"Sorry, We do not have '{book}'.")
            self.displaybooks()

    def returnbook(self, book):
        if book in self.lentbooksinfo:
            self.addbook(book)
            self.lentbooksinfo.pop(book)
            print("Book has been returned to the library.")
        else:
            print(f"'{book}'' does not belong to the library.")


if __name__ == "__main__":
    fahadliblist = ['Python', 'Rich Daddy Poor Daddy',
                    'Harry Potter', 'C++ Basics', 'Algorithms by CLRS']
    fahadlib = Library('Imperial Library', fahadliblist)

    while True:
        print('\n')
        print(
            f"Welcome to the {fahadlib.libraryname}. Enter your choice to continue")
        print('1. To display all the books.')
        print('2. To add a book.')
        print('3. To lend a book.')
        print('4. To return a book.')
        print('5. Information about lent books.')
        print('6. Quit.')

        inp = int(input('\n'))

        if inp not in [1, 2, 3, 4, 5, 6]:
            print("Please enter a valid option")
            continue

        elif inp == 1:
            fahadlib.displaybooks()

        elif inp == 2:
            print('Enter the name of the book:')
            book = input()
            fahadlib.addbook(book)

        elif inp == 3:
            print('Enter the name of person:')
            person = input()
            print('Enter the name of the book:')
            book = input()
            fahadlib.lendbook(person, book)

        elif inp == 4:
            print('Enter the name of the book:')
            book = input()
            fahadlib.returnbook(book)

        elif inp == 5:
            fahadlib.printlentbooksinfo()

        elif inp == 6:
            exit()

        else:
            print('Unexpexted input!')
