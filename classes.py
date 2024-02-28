import re

from collections import UserDict
from datetime import datetime, timedelta


class Field:
    def __init__(self, value: str):
        self.value = value
    
    @property
    def value(self):
        return self.__value
    
    @value.setter
    def value(self, value):
        self.__value = value
    
    @classmethod
    def validation(cls, value: str):
        pass

    def __str__(self):
        return self.value
    
    def __repr__(self) -> str:
        return f"Field(value={self.value})"
    
    def __call__(self):
        return self.value

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Field):
            return NotImplemented
        return self.value == __value

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)

    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, Field):
            return NotImplemented
        return self.value < __value

    def __gt__(self, __value: object) -> bool:
        if not isinstance(__value, Field):
            return NotImplemented
        return self.value > __value

    def __le__(self, __value: object) -> bool:
        if not isinstance(__value, Field):
            return NotImplemented
        return self.value <= __value

    def __ge__(self, __value: object) -> bool:
        if not isinstance(__value, Field):
            return NotImplemented
        return self.value >= __value


class Name(Field):
    def __init__(self, value: str):
        if value:
            super().__init__(value)
        else:
            raise ValueError('Error: the entered contact name is empty.')

    def __str__(self):
        return super().__str__()
    
    def __repr__(self) -> str:
        return f"Name(value={super().value})"
    
    def __call__(self):
        return super().value

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Name):
            return NotImplemented
        return super().value == __value

    def __ne__(self, __value: object) -> bool:
        return not super().__eq__(__value)

    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, Name):
            return NotImplemented
        return super().value < __value

    def __gt__(self, __value: object) -> bool:
        if not isinstance(__value, Name):
            return NotImplemented
        return super().value > __value

    def __le__(self, __value: object) -> bool:
        if not isinstance(__value, Name):
            return NotImplemented
        return super().value <= __value

    def __ge__(self, __value: object) -> bool:
        if not isinstance(__value, Name):
            return NotImplemented
        return super().value >= __value


class Phone(Field):
    def __init__(self, value: str):
        super().__init__(value)
    
    @classmethod
    def validation(cls, value: str):
        if cls.value == value:
            return cls.__validation(value)
    
    def __validation(self, value: str):
        if re.fullmatch(r'\d{10}', value):
            super().__init__(value)
        raise ValueError (f'The number of digits in the number does not correspond to 10.\n{value}\n')

    def __str__(self):
        return super().value
    
    def __repr__(self) -> str:
        return f"Phone(value={super().value})"
    
    def __call__(self):
        return super()

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Phone):
            return NotImplemented
        return super().value == __value

    def __ne__(self, __value: object) -> bool:
        return not super().__eq__(__value)

    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, Phone):
            return NotImplemented
        return super().value < __value

    def __gt__(self, __value: object) -> bool:
        if not isinstance(__value, Phone):
            return NotImplemented
        return super().value > __value

    def __le__(self, __value: object) -> bool:
        if not isinstance(__value, Phone):
            return NotImplemented
        return super().value <= __value

    def __ge__(self, __value: object) -> bool:
        if not isinstance(__value, Phone):
            return NotImplemented
        return super().value >= __value


class Birthday(Field):
    def __init__(self, value: str):
        super().__init__(self.__validation(value))
    
    @classmethod
    def validation(cls, value: str):
        return cls.__validation(value)
    
    def __validation(self, value: str):
        try:
            date_birthday = datetime.strptime(value, '%d.%m.%Y')
            return date_birthday.strftime('%d.%m.%Y')
        except ValueError:
            raise ValueError("Invalid date format. Use DD.MM.YYYY")

    def __str__(self):
        return f"Birthday party: {super().value}"
    
    def __repr__(self) -> str:
        return f"Birthday(value={super().value})"
    
    def __call__(self):
        return super().value

    def __eq__(self, __value: object) -> bool:
        if not isinstance(__value, Birthday):
            return NotImplemented
        return super().value == __value

    def __ne__(self, __value: object) -> bool:
        return not super().__eq__(__value)

    def __lt__(self, __value: object) -> bool:
        if not isinstance(__value, Birthday):
            return NotImplemented
        return super().value < __value

    def __gt__(self, __value: object) -> bool:
        if not isinstance(__value, Birthday):
            return NotImplemented
        return super().value > __value

    def __le__(self, __value: object) -> bool:
        if not isinstance(__value, Birthday):
            return NotImplemented
        return super().value <= __value

    def __ge__(self, __value: object) -> bool:
        if not isinstance(__value, Birthday):
            return NotImplemented
        return super().value >= __value


class Record:
    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []
        self.birthday = None

    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
    
    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))
    
    def remove_phone(self, phone: str):
        self.phones.remove(Phone(phone))
    
    def edit_phone(self, phone: str, new_phone: str):
        self.phones = [Phone(new_phone) if item == phone else item for item in self.phones]
   
    def find_phone(self, phone: str):
        for item in self.phones:
            if item == phone:
                phone = item
                break
        return phone
    
    def add_birthday(self, birthday: str):
        self.birthday = Birthday(birthday)
    
    def __str__(self):
        return f"Record a contact: {self.name}, \
            phones: {'; '.join(p.value for p in self.phones)}, \
            birthday: {self.birthday if self.birthday else ''}"
    
    def __repr__(self) -> str:
        return f"Record(value={self.name}, \
        phones={'; '.join(p for p in self.phones)}, \
        birthday={self.birthday if self.birthday else ''}"
    
    def __call__(self):
        return self.name

    def __eq__(self, other: object) -> bool:
        result = False
        if not isinstance(other, Record):
            return NotImplemented
        result = (self.name == other.__name)
        result = result and (len(self.phone) == len(other.phones))
        result = result and (lambda a: True if self.phones[a]==other.phones[a] else False, range(len(other.phones)))
        result = result (self.birthday == other.birthday)
        return result

    def __ne__(self, __value: object) -> bool:
        return not self.__eq__(__value)

    # def __lt__(self, __value: object) -> bool:
    #     if not isinstance(__value, Record):
    #         return NotImplemented
    #     return self.value < __value

    # def __gt__(self, __value: object) -> bool:
    #     if not isinstance(__value, Record):
    #         return NotImplemented
    #     return self.value > __value

    # def __le__(self, __value: object) -> bool:
    #     if not isinstance(__value, Record):
    #         return NotImplemented
    #     return self.value <= __value

    # def __ge__(self, __value: object) -> bool:
    #     if not isinstance(__value, Record):
    #         return NotImplemented
    #     return self.value >= __value


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