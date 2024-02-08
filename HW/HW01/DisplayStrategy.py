from abc import ABC, abstractmethod


class DisplayStrategy(ABC):
    @abstractmethod
    def display(self, data):
        pass


class ContactDisplay(DisplayStrategy):
    def display(self, contacts):
        for contact in contacts:
            print('New display strategy')
            print(f"Name: {contact['name']}")
            print(f"Phones: {', '.join(contact['phones'])}")
            print(f"Birthday: {contact['birthday']}")
            print(f"Email: {contact['email']}")
            print(f"Status: {contact['status']}")
            print(f"Note: {contact['note']}")
            print("_" * 50)



class NoteDisplay(DisplayStrategy):
    def display(self, notes):
        print("Notes:")
        for note in notes:
            print(f"Note: {note}")
            print("_" * 50)


class CommandDisplay(DisplayStrategy):
    def display(self, commands):
        print("Available commands:")
        for command in commands:
            print(command)
