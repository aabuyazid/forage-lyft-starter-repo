from abc import ABC, abstractmethod
from serviceable.carparts.Engine import Engine
from serviceable.carparts.Battery import Battery

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class Car(Serviceable):
    def __init__(self, engine : Engine, battery: Battery) -> None:
        super().__init__()
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service()

