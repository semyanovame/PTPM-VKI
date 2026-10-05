class Controller:
    def __init__(self, validator, pushing_service, database, user_interface):
        self.validator = validator
        self.pushing_service = pushing_service
        self.database = database
        self.user_interface = user_interface

    def process_registration(self):
        login, password, confirm_password = self.user_interface.get_user_input()
        
        if self.database.does_user_exist(login):
            result = f"Пользователь {login} уже существует."
            self.pushing_service.push_data(result)
            self.user_interface.display_message(result)
        else:
            is_valid, error_message = self.validator.validate_main(login, password, confirm_password)
            if not is_valid:
                result = f"Ошибка: {error_message}"
                self.pushing_service.push_data(result)
                self.user_interface.display_message(result)
                return False, result
            hashed_password = self.validator.hash_password(password)
            self.database.add_data(login, hashed_password, hashed_password, "Success", None)
            result = f"Регистрация успешна для пользователя: {login}"
            self.pushing_service.push_data(result)
            self.user_interface.display_message(result)
        return True, result