from classes import *


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError as error:
            return f'{error}'
        except IndexError as error:
            return f'{error}'
        except KeyError as error:
            return f'{error}'
        except Exception as error:
            return f'{error}'

    return inner


@input_error
def parse_input(user_input):
# Function return a list with arguments or a error code.
    
    if user_input and user_input.count(' ') == 0:
        cmd = user_input
    elif user_input.count(' ') > 0:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
    else:
        raise ValueError('Error: input is empty')
    
    return cmd, *args


@input_error
def add_contact(args: list, book: AddressBook):
# The first parameter by method is list: 'name', 'phone(s)' and may be 'birthday'.
    
    if len(args) > 1: 
        record = Record(args[0])
        args, *args = args
        # This is Python -_:)_-

        for arg in args:
            if arg:
                record.add_phone(arg)
                #raise ValueError("Warning: the argument isn't phone")
        #record.add_birthday(args[-1])
        #raise ValueError("Warning: the argument isn't phone or birthday party.")
    elif len(args) > 0 and args[0]:
        record = Record(args[0])
            
    else:
        raise ValueError('Error: no arguments.')
    
    book.data[record.name.value] = record
    return 'Contact added.'


@input_error
def change_contact(args, book: AddressBook):
# Updates an existing contact or adds a new one.
    
    if args and args[0] in book.data.keys():
        name, *phones = args
        book.data[name].edit_phone(phones[0], phones[1])
        if book.data[name].find_phone(phones[1]):
            return 'Contact updated.'
        else:
            raise "Warning: Contact isn't updated."
    else:
        return add_contact(args, book)


@input_error
def show_phone(name: str, book: AddressBook):
    #if name in book.data.keys():
    return (f'{name}: {[phone.value for phone in book.data[name].phones]}\n')
    #else:
        #raise ValueError (f'Warning: the phone by "{name}" isn\'t found.')


@input_error
def show_all(book: AddressBook):
    return book.data.values()


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    book.date[name].add_birthday(birthday)


@input_error
def show_birthday(args, book: AddressBook):
    name = args
    return book.date[name].birthday.value


@input_error
def show_birthdays(book: AddressBook):
    return  [f'{name}: {birthday}\n' for name, birthday in book.get_upcoming_birthdays()]

def my_main(values):
    book = AddressBook()
    #print("Welcome to the assistant bot!")
    print(f"\n\n{values}")
    while True:
        #user_input = input("Enter a command: ")
        command, *args = parse_input(values)
        #command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, book))

        elif command == "change":
            print(change_contact(args, book))

        elif command == "phone":
            print(show_phone(args, book))

        elif command == "all":
            print(*[*show_all(book), '\n'])

        elif command == "add-birthday":
            add_birthday(args, book)

        elif command == "show-birthday":
            print(show_birthday(args, book))

        elif command == "birthdays":
            print(*show_birthdays(book))

        else:
            print("Invalid command.")
        break

#if __name__ == '__main__':
t_arguments = [
        "",
        " ",
        "  ",
        "   ",
        "    ",
        ".",
        ". . ",
        ". . . ",
        ". . . .",
        "Joy1",
        "Joy2 ",
        "Joy3 0000",
        "Joy4 1111111111",
        "Joy5 55555555555555",
        "Joy6 01.01.1990",
        "Joy7 0000 01.01.1990",
        "Joy8 1111111111 01.01.1990",
        "Joy10 55555555555555 01.01.1990",
        "Joy11 1111111111 1111111111 ",
        "Joy11 1111111111 2222222222 ",
        "Joy12 1111111111 1111111111 01.01.1990",
        "Joy13 1111111111 01.01.1990 1111111111",
        "Joy14 01.01.1990 1111111111 1111111111"]

commands = [
        # "",
        # " ",
        # "  ",
        # "   ",
        # "    ",
        # ".",
        # ". . ",
        # ". . . ",
        # "close ",
        # "exit ",
        # "hello ",
        "add ",
        "change ",
        # "phone ",
        # "all ",
        # "add-birthday ",
        # "show-birthday ",
        # "birthdays "
        ]
my_input = ''

#my_main('add Joy9 1111111111 1111111111 ')

for command in commands:
    my_input = f'{command}'
    my_main(my_input)
    for argument in t_arguments:
        my_input = f'{command}{argument}'
        my_main(my_input)