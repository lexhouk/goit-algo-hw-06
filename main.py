from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    ...


class Phone(Field):
    def valid(self, phone: str) -> bool:
        ...


class Record:
    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str) -> None:
        ...

    def remove_phone(self, phone: str) -> None:
        ...

    def edit_phone(self, current: str, new: str) -> None:
        ...

    def find_phone(self, phone: str) -> Phone:
        ...

    def __str__(self) -> str:
        return ('Contact name: ',
                self.name.value,
                ', phones: ',
                '; '.join(p.value for p in self.phones))


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        ...

    def find(self, name: str) -> Record:
        ...

    def delete(self, name: str) -> None:
        ...
