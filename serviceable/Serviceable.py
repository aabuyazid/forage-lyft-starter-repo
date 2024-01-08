from abc import ABC, abstractmethod
from serviceable.carparts.Engine import Engine
from serviceable.carparts.Battery import Battery
from serviceable.carparts.Tires import Tires

class Serviceable(ABC):
    @abstractmethod
    def needs_service(self) -> bool:
        pass

class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tires: Tires) -> None:
        super().__init__()
        self.engine = engine
        self.battery = battery
        self.tires = tires


    def needs_service(self) -> bool:
        return self.engine.needs_service() or self.battery.needs_service() or self.tires.needs_service()

