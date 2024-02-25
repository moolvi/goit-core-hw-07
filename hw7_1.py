import re

from collections import UserDict


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


class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []
    
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