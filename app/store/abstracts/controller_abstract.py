from abc import ABC, abstractmethod


class ControllerAbstract(ABC):
    @abstractmethod
    def get_horoscope(self, data):
        pass


class UserAbstract(ABC):
    @abstractmethod
    def get_user(self, user_id):
        pass

    @abstractmethod
    def get_users(self):
        pass

    @abstractmethod
    def create_user(self, user):
        pass

    @abstractmethod
    def update_user(self, user):
        pass

    @abstractmethod
    def delete_user(self, user_id):
        pass
