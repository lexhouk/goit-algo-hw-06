from collections import UserDict


class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return str(self.value)


class Name(Field):
    ...


class Phone(Field):
    @staticmethod
    def valid(phone: str) -> bool:
        return len(phone) == 10 and phone.isdigit()


class Record:
    def __init__(self, name) -> None:
        self.name = Name(name)
        self.phones = []

    def add_phone(self, phone: str) -> None:
        if Phone.valid(phone):
            self.phones.append(Phone(phone))

    def remove_phone(self, phone: str) -> None:
        for id, current in enumerate(self.phones):
            if str(current) == phone:
                del self.phones[id]
                break

    def edit_phone(self, current: str, new: str) -> None:
        if Phone.valid(new):
            for id, phone in enumerate(self.phones):
                if str(phone) == current:
                    self.phones[id] = Phone(new)
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
