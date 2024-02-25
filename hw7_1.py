import re

from collections import UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):
    def __validation(self, value):
        if len(re.search(r'\d', value).string) == 10:
            return value
        raise ValueError ('The number of digits in the number does not correspond to 10.')
    
    def __init__(self, value):
        super().__init__(self.__validation(value))


class Birthday(Field):
    def __init__(self, value):
        try:
            date_birthday = datetime.strptime(value, '%d.%m.%Y')
            return super().__init__(date_birthday.strftime('%d.%m.%Y'))
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
        self.birthday = None
    
    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone: str):
        self.phones.remove(Phone(phone))
    
    def edit_phone(self, phone: str, new_phone: str):
        self.phones = [Phone(new_phone) if item.value == phone else item for item in self.phones]
   
    def find_phone(self, phone: str):
        for item in self.phones:
            if item.value == phone:
                return item
    
    def add_birthday(self, birthday):
        self.birthday = Birthday(birthday)
    
    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"


class AddressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record
    
    def find(self, name: str):
        if self.data[name]:
            return self.data[name]
        return None
    
    def delete(self, name: str):
        self.data.pop(name)
    
    def get_upcoming_birthdays(self):
        upcoming_birthdays = []

        for name, record in self.data.items():
            buffer_record = Record(name)
            # The 'buffer_record' is needed to keep the original date.
            
            #for phone in record.phones:
                #buffer_record.add_phone(phone.value)

            try:
                now_date = datetime.today().date()
                date_user =  datetime.strptime(record.birthday.value, '%d.%m.%Y').replace(now_date.year).date()
                dates_differences = (date_user - now_date).days

                if dates_differences <= 7 and dates_differences >= 0:
                    if date_user.weekday() == 6:
                        buffer_record.add_birthday((date_user + timedelta(days = 1)).strftime('%d.%m.%Y'))
                    elif date_user.weekday() == 5:
                        buffer_record.add_birthday((date_user + timedelta(days = 2)).strftime('%d.%m.%Y'))
                    else:
                        buffer_record.add_birthday(date_user.strftime('%d.%m.%Y'))

                    upcoming_birthdays.append({name : record.birthday.value})
            except:
                return None
        return upcoming_birthdays