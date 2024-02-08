from Bot import Bot
from DisplayStrategy import ContactDisplay, NoteDisplay, CommandDisplay

if __name__ == "__main__":
    print('Hello. I am your contact-assistant. What should I do with your contacts?')
    bot = Bot()
    bot.book.load("auto_save")

    # Створюємо об'єкти конкретних класів реалізацій
    contact_display = ContactDisplay()
    note_display = NoteDisplay()
    command_display = CommandDisplay()

    commands = ['Add', 'Search', 'Edit', 'Load', 'Remove', 'Save', 'Congratulate', 'View', 'Exit']
    while True:
        action = input('Type help for list of commands or enter your command\n').strip().lower()
        if action == 'help':
            format_str = str('{:%s%d}' % ('^', 20))
            for command in commands:
                print(format_str.format(command))
            action = input().strip().lower()
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")
        else:
            bot.handle(action)
            if action in ['add', 'remove', 'edit']:
                bot.book.save("auto_save")

        # Відображення даних за допомогою об'єктів конкретних класів реалізацій
        if action == 'view':
            contact_display.display(bot.book.data)
        elif action == 'congratulate':
            print(bot.book.congratulate())
        elif action == 'help':
            command_display.display(commands)

        if action == 'exit':
            break
