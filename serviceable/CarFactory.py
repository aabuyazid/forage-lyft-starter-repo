from serviceable.Serviceable import Car
from datetime import date
from serviceable.carparts.Battery import *
from serviceable.carparts.Engine import *
from serviceable.carparts.Tires import *



class CarFactory():

    @staticmethod
    def create_calliope(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list) -> Car:
        return Car(
                engine=CapuletEngine(last_service_mileage, current_mileage),
                battery=SpindlerBattery(last_service_date, current_date),
                tires=CarriganTires(tire_wear)
                )

    @staticmethod
    def create_glissade( current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list) -> Car:
        return Car(
                engine=WilloughbyEngine(last_service_mileage, current_mileage),
                battery=SpindlerBattery(last_service_date, current_date),
                tires=OctoprimeTires(tire_wear)
                )

    @staticmethod
    def create_rorschach(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list) -> Car:
        return Car(
                engine=WilloughbyEngine(last_service_mileage, current_mileage),
                battery=NubbinBattery(last_service_date, current_date),
                tires=CarriganTires(tire_wear)
                )

    @staticmethod
    def create_thovex(current_date: date, last_service_date: date, current_mileage: int, last_service_mileage: int, tire_wear: list) -> Car:
        return Car(
                engine=CapuletEngine(last_service_mileage, current_mileage),
                battery=NubbinBattery(last_service_date, current_date),
                tires=OctoprimeTires(tire_wear)
                )

    @staticmethod
    def create_palindrome(current_date: date, last_service_date: date, warning_light_on: bool, tire_wear: list) -> Car:
        return Car(
                engine=SternmanEngine(warning_light_on),
                battery=NubbinBattery(last_service_date, current_date),
                tires=OctoprimeTires(tire_wear)
                )
