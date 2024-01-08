from abc import ABC, abstractmethod
from datetime import date
from dateutil.relativedelta import relativedelta

class Battery(ABC):
    @abstractmethod
    def needs_service(self) -> bool: 
        pass

class SpindlerBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date) -> None:
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return relativedelta(self.current_date, self.last_service_date).years >= 2
        
class NubbinBattery(Battery):
    def __init__(self, last_service_date: date, current_date: date) -> None:
        super().__init__()
        self.last_service_date = last_service_date
        self.current_date = current_date

    def needs_service(self) -> bool:
        return relativedelta(self.current_date, self.last_service_date).years >= 4
        
