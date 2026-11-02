def validate_password(password: str) -> bool:
        if not isinstance(password, str):
            raise TypeError("Пароль должен быть строкой") #1этап
        if ' ' in password:
            raise ValueError("Пароль не должен содержать пробелы")

        if not (8 <= len(password) <= 20): #этап2
            return False 

        has_upper = False
        has_lower = False
        has_digit = False
        has_special = False

        special_chars = set('!@#$%^&*')

        for ch in password:
            if ch.isupper():
                has_upper = True
            elif ch.islower():
                has_lower = True
            elif ch.isdigit():
                has_digit = True
            elif ch in special_chars:
                has_special = True

        return has_upper and has_lower and has_digit and has_special