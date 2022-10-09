from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List


class Address:
    def __init__(self, street: str, street2: str, city: str, zipcode: str):
        self.street = street
        self.street = street
        self.city = city
        self.zipcode = zipcode


class IPayRollCalculator(ABC):
    @abstractmethod
    def calculate_payroll() -> int:
        pass


class IRole(ABC):
    @abstractmethod
    def perform_duties(hours: int) -> None:
        pass


class SalesRole(IRole):
    def perform_duties(hours: int) -> None:
        pass


class ManagerRole(IRole):
    def perform_duties(hours: int) -> None:
        pass


class FactoryRole(IRole):
    def perform_duties(hours: int) -> None:
        pass


class Employee:
    def __init__(self, id: int, name: str,
                 street: str, street2: str, city: str, zipcode: str):
        self.id = id
        self.name = name
        self.address = Address(street, street2, city, zipcode)
        self.role = IRole()
        self.payroll = IPayRollCalculator()
        self.coworkers = List[Employee](
            id, name, street, street2, city, zipcode)


class PayrollPolicy:
    def __init__(self, hours_worked: int):
        self.hours_worked = hours_worked

    def track_work(hours: int) -> None:
        pass


class SalaryPolicy(PayrollPolicy, IPayRollCalculator):
    def __init__(self, hours_worked: int, weekly_salary: int):
        super().__init__(hours_worked)
        self.weekly_salary = weekly_salary

    def calculate_payroll() -> int:
        pass


class HourlyPolicy(PayrollPolicy, IPayRollCalculator):
    def __init__(self, hours_worked: int, hours_rate: int):
        super().__init__(hours_worked)
        self.hours_rate = hours_rate

    def calculate_payroll() -> int:
        pass


class CommissionPolicy(SalaryPolicy):
    def __init__(self, hours_worked: int, weekly_salary: int, commission: int):
        super().__init__(hours_worked, weekly_salary)
        self.commission = commission

    def calculate_payroll() -> int:
        pass
