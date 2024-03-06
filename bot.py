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
        finally:
            pass
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
        raise ValueError('Error: Input is empty\n')
    
    return cmd, *args


@input_error
def add_contact(args, book: AddressBook):
    message = ""
    if len(args) > 0:
        name, *args = args
        phone = None
        if args and len(args) > 0:
            phone, *_ = args
        record = book.find(name)
        if record is None:
            record = Record(name)
            book.add_record(record)
            message = "Contact added.\n"
        else:
            message = "The contact exists in the book phone.\n"
        if phone:
            record.add_phone(phone)
            message = f"{message}Phone added.\n"
    else:
        raise ValueError('Error: Contact name must not be empty.')
    
    return message


@input_error
def change_contact(args, book: AddressBook):
# Updates an existing contact or adds a new one.
    if len(args) > 0:
        name, *args = args
        phone = None
        new_phone = None
        record = book.find(name)
        if record:
            if len(args) > 1:
                phone, new_phone, *_ = args
                record.edit_phone(phone, new_phone)
                return 'Phone updated.'
            elif len(args) > 0:
                phone, *_ = args
                record.add_phone(phone)
                return 'Phone added.'
            else:
                raise ValueError('Warning: New phone number not specified.')
        else:
            return add_contact([name, *args], book)
    else:
        raise ValueError ('Warning: Contact name is empty.')


@input_error
def show_phone(name: str, book: AddressBook):
    return (f'{name}: {[phone.value for phone in book.data[name].phones]}\n')


@input_error
def show_all(book: AddressBook):
    return ''.join(repr(value) for value in book.data.values())


@input_error
def add_birthday(args, book: AddressBook):
    name, birthday = args
    book.date[name].add_birthday(birthday)


@input_error
def show_birthday(args, book: AddressBook):
    name, *_ = args
    return book.date[name].birthday.value


@input_error
def show_birthdays(book: AddressBook):
    return  [f'{name}: {birthday}\n' for name, birthday in book.get_upcoming_birthdays()]


def main():
    book = AddressBook()
    #print("Welcome to the assistant bot!")
    while True:
        for values in get_command():
            print(f"\nget_command: {values}")

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

            #elif command == "all":
                #print(*show_all(book), '\n')

            elif command == "add-birthday":
                add_birthday(args, book)

            elif command == "show-birthday":
                print(show_birthday(args, book))

            elif command == "birthdays":
                print(*show_birthdays(book))

            else:
                print("Invalid command.")
            print(show_all(book))
        break


def get_command():
    arguments = [
        # "",
        # " ",
        # "  ",
        # "   ",
        # "    ",
        # "~",
        # "~ ~",
        # "~ ~ ~",
        # "~ ~ ~ ~",
        # "Joy1",
        # "Joy1 ",
        # "Joy1 9876",
        # "Joy1 1111111111",
        # "Joy2 2222222222",
        # "Joy3 3333333333",
        # "Joy4 44444444444",
        # "Joy1 1111133333",
        # "Joy4 4444444444",
        # "Joy1 9999999999999999",
        # "Joy1 01.01.1990",
        # "Joy1 0000 01.01.1990",
        # "Joy1 1111111111 01.01.1990",
        # "Joy1 9999999999999999 01.01.1990",
        # "Joy1 1111111111 1111111111 ",
        # "Joy1 1111111111 1111122222 ",
        # "Joy1 1111111111 1111111111 01.01.1990",
        # "Joy1 1111111111 01.01.1990 1111111111",
        # "Joy1 01.01.1990 1111111111 1111111111",

        "add ~",
        "add ~ ~",
        "add ~ ~ ~",
        "add ~ ~ ~ ~",
        "add Joy1",
        "add Joy1 ",
        "add Joy1 9876",
        "add Joy1 1111111111",
        "add Joy2 2222222222",
        "add Joy3 3333333333",
        "add Joy4 44444444444",
        "add Joy1 1111133333",
        "add Joy4 4444444444",
        "add Joy1 9999999999999999",
        "add Joy1 01.01.1990",
        "add Joy1 0000 01.01.1990",
        "add Joy1 1111111111 01.01.1990",
        "add Joy1 9999999999999999 01.01.1990",
        "add Joy1 1111111111 1111111111 ",
        "add Joy1 1111111111 1111122222 ",
        "add Joy1 1111111111 1111111111 01.01.1990",
        "add Joy1 1111111111 01.01.1990 1111111111",
        "add Joy1 01.01.1990 1111111111 1111111111",
        
        "change Joy8 8888888888",
        "change Joy8 8888888888 8880000888",
        "change ~",
        "change ~ ~",
        "change ~ ~ ~",
        "change ~ ~ ~ ~",
        "change Joy1",
        "change Joy1 ",
        "change Joy1 9876",
        "change Joy4 1111111111",
        "change Joy3 2222222222",
        "change Joy2 3333333333",
        "change Joy1 44444444444",
        "change Joy1 1111133333",
        "change Joy4 4444444444",
        "change Joy1 9999999999999999",
        "change Joy1 01.01.1990",
        "change Joy1 0000 01.01.1990",
        "change Joy1 1111111111 01.01.1990",
        "change Joy1 9999999999999999 01.01.1990",
        "change Joy1 1111111111 1111111111 ",
        "change Joy1 1111111111 1111122222 ",
        "change Joy1 1111111111 1111111111 01.01.1990",
        "change Joy1 1111111111 01.01.1990 1111111111",
        "change Joy1 01.01.1990 1111111111 1111111111",
        ]

    commands = [
        "",
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
        # "add ",
        # "change ",
        # "phone ",
        # "all ",
        # "add-birthday ",
        # "show-birthday ",
        # "birthdays "
        ]
    for command in commands:
        my_input = f'{command}'
        #yield my_input
        for argument in arguments:
            my_input = f'{command}{argument}'
            yield my_input

if __name__ == "__main__":
    main()