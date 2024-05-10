from collections import UserDict
from dataclasses import dataclass


@dataclass
class Field:
    value: str

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    ...


class Phone(Field):
    def __init__(self, value: str):
        if len(value) != 10 or not value.isdigit():
            raise ValueError('The number is not valid!')
        super().__init__(value)


class Record:
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.phones: list[Phone] = []

    def __find(self,
               phone: str,
               get_instance: bool = False
               ) -> int | Phone | None:
        for id, instance in enumerate(self.phones):
            if instance.value == phone:
                return instance if get_instance else id
        return None

    def add_phone(self, phone: str) -> None:
        self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        if id := self.__find(phone):
            del self.phones[id]

    def edit_phone(self, current: str, new: str) -> None:
        id = self.__find(current)

        if id is None:
            raise ValueError(f'Phone {current} not found!')
        else:
            self.phones[id] = Phone(new)

    def find_phone(self, phone: str) -> Phone | None:
        return self.__find(phone, True)

    def __str__(self) -> str:
        phones = '; '.join(map(lambda phone: phone.value, self.phones))
        return f'Contact name: {self.name.value}, phones: {phones}'


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[record.name.value] = record

    def find(self, name: str) -> Record | None:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        for id, record in self.data.items():
            if record.name.value == name:
                del self.data[id]
                break
