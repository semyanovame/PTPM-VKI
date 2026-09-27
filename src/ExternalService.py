import abc

class AbstractPushingService(abc.ABC):
    @abc.abstractmethod
    def push_data(self, login, password):
        pass
class PushingService(AbstractPushingService):
    def push_data(self, login, password):
        # Logic to push data to an external service
        print(f"Pushing data: login={login}, password={password}")