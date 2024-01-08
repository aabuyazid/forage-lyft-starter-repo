from abc import ABC, abstractmethod

class Tires(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class CarriganTires(Tires):
    def __init__(self, tire_wear: list) -> None:
        super().__init__()
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        return any([wear >= 0.9 for wear in self.tire_wear])

class OctoprimeTires(Tires):
    def __init__(self, tire_wear: list ) -> None:
        super().__init__()
        self.tire_wear = tire_wear

    def needs_service(self) -> bool:
        return sum(self.tire_wear) >= 3
