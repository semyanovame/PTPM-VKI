class UserInterface:
    def __init__(self, validator):
        self.validator = validator

    def get_user_input(self):
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        confirm_password = input("Подтвердите пароль: ")
        return login, password, confirm_password

    def display_message(self, message):
        print(message)