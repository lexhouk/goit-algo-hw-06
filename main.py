from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    ...


class Phone(Field):
    def valid(self) -> bool:
        return len(str(self)) == 10 and str(self).isdigit()


class Record:
    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str) -> None:
        new = Phone(phone)

        if new.valid():
            self.phones.append(new)

    def remove_phone(self, phone: str) -> None:
        for id, current in enumerate(self.phones):
            if str(current) == phone:
                del self.phones[id]
                break

    def edit_phone(self, current: str, new: str) -> None:
        new: Phone = Phone(new)

        if new.valid():
            for id, phone in enumerate(self.phones):
                if str(phone) == current:
                    self.phones[id] = new
                    break

    def find_phone(self, phone: str) -> Phone:
        for current in self.phones:
            if str(current) == phone:
                return current

        return Phone('')

    def __str__(self) -> str:
        phones = '; '.join(str(phone) for phone in self.phones)
        return f'Contact name: {str(self.name)}, phones: {phones}'


class AddressBook(UserDict):
    def add_record(self, record: Record) -> None:
        self.data[str(record.name)] = record

    def find(self, name: str) -> Record:
        return self.data.get(name, Record(''))

    def delete(self, name: str) -> None:
        for id, record in self.data.items():
            if str(record.name) == name:
                del self.data[id]
                break
