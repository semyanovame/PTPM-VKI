import abc

class AbstractPushingService(abc.ABC):
    @abc.abstractmethod
    def push_data(self, result):
        pass
class PushingService(AbstractPushingService):
    def push_data(self, result):
        print(f"Отправлено: {result}")