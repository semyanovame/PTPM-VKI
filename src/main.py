from src.Validator import Validator
from src.Database import Database
from src.user_interface import UserInterface
from src.pushing_service import PushingService
from src.Controller import Controller


if __name__ == "__main__":
    controller = Controller(
        validator=Validator(),
        pushing_service=PushingService(),
        database=Database("users.db"),
        user_interface=UserInterface(),
    )
    ok, msg = controller.process_registration()
    print(f"ok={ok}, msg={msg}")