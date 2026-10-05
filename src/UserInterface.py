import abc

class AbstractUserInterface(abc.ABC):
    @abc.abstractmethod
    def get_user_input(self):
        pass
    @abc.abstractmethod
    def display_message(self, message):
        pass
class UserInterface(AbstractUserInterface):
     

    def get_user_input(self):
        login = input("Введите логин: ")
        password = input("Введите пароль: ")
        confirm_password = input("Подтвердите пароль: ")
        return login, password, confirm_password
    def display_message(self, message):
        print(message)