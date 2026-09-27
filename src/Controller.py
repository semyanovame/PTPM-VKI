class Controller:
    def __init__(self, validator, pushing_service, database, user_interface):
        self.validator = validator
        self.pushing_service = pushing_service
        self.database = database
        self.user_interface = user_interface

    def process_registration(self):
        login, password, confirm_password = self.user_interface.get_input()
        
        if self.database.does_user_exist(login, password, confirm_password):
            self.database.get_data(login, password, confirm_password)
            result = f"Пользователь {login} уже существует."
        else:
            is_valid, error_message = self.validator.validate_main(login, password, confirm_password)
            if not is_valid:
                return False, error_message
            hashed_password = self.validator.hash_password(password)
            self.database.add_data(login, hashed_password, hashed_password, "Success", None)
            result = f"Регистрация успешна для пользователя: {login}"
            self.pushing_service.push_data(result)
        return True, result