from collections import UserDict
from dataclasses import dataclass


@dataclass
class Field:
    _value: str

    def __str__(self) -> str:
        return str(self._value)


class Name(Field):
    ...


class Phone(Field):
    @staticmethod
    def valid(phone: str) -> bool:
        return len(phone) == 10 and phone.isdigit()


class Record:
    def __init__(self, name: str) -> None:
        self.name = Name(name)
        self.__phones: list[Phone] = []

    def __find(self,
               phone: str,
               get_instance: bool = False
               ) -> int | Phone | None:
        for id, instance in enumerate(self.__phones):
            if str(instance) == phone:
                return instance if get_instance else id
        return None

    def add_phone(self, phone: str) -> None:
        if Phone.valid(phone):
            self.__phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        if id := self.__find(phone):
            del self.__phones[id]

    def edit_phone(self, current: str, new: str) -> None:
        if Phone.valid(new) and (id := self.__find(current)):
            self.__phones[id]._value = new

    def find_phone(self, phone: str) -> Phone | None:
        return self.__find(phone, True)

    def __str__(self) -> str:
        return f'Contact name: {str(self.name)}, ' \
               f"phones: {'; '.join(map(str, self.__phones))}"


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[str(record.name)] = record

    def find(self, name: str) -> Record | None:
        return self.data.get(name)

    def delete(self, name: str) -> None:
        for id, record in self.data.items():
            if str(record.name) == name:
                del self.data[id]
                break
