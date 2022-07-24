import logging
from dataclasses import dataclass, field
import random
from typing import Dict, List
from abc import ABC, abstractmethod

import pandas as pd

from faker import Faker
from faker.providers import (
    internet,
    geo,
    credit_card,
    color,
    company,
    date_time,
    address,
)


@dataclass
class Employee(ABC):
    """Employee"""

    name: str
    email: str
    company: str
    app_endpoint: str
    app_ip: str
    manager: str
    department: str
    geo: str
    area: str = field(init=False)

    def __post_init__(self):
        self.area = self.determine_area()

    @abstractmethod
    def determine_area(self) -> str:
        """determine"""


@dataclass
class LendingEmployee(Employee):
    """Lending Employee"""

    def __post_init__(self):
        self.department = "Lending"
        super().__post_init__()

    def determine_area(self):
        if self.name[0] in "AEIOU":
            return "A"
        else:
            return "B"


@dataclass
class AvaxEmployee(Employee):
    """avax Employee"""

    department: str = "Avax"
    geo: str = None

    def determine_area(self):
        if self.name[1].upper() in "AEIOU":
            return "A"
        else:
            return "B"


class EmployeeFactory:
    """Employee Factory"""

    def create_employee(self, data: Dict) -> Employee:
        """create data

        Args:
            data (Dict): dictionary of data

        Raises:
            Exception: _description_

        Returns:
            Employee: employee class
        """
        if data["department"] == "Lending":
            return LendingEmployee(**data)
        elif data["department"] == "Avax":
            return AvaxEmployee(**data)
        else:
            print(data)
            raise Exception("Department Not Recognized")

    def fake_maker(self, department: str, r: Faker) -> Dict:
        fake = {
            "name": r.name(),
            "email": r.ascii_company_email(),
            "company": r.company(),
            "app_endpoint": r.hostname(),
            "app_ip": r.ipv4_private(),
            "manager": r.name(),
        }
        if department == "Lending":
            return {**{"geo": r.country(), "department": "Lending"}, **fake}
        elif department == "Avax":
            return {**{"department": "Avax"}, **fake}


class Program:
    """Program

    Returns:
        _type_: Dataframe()
    """

    r: Faker = None

    def __init__(self):
        Faker.seed(random.randint(0, 9999))
        self.r = Faker()
        self.r.add_provider(credit_card)
        self.r.add_provider(internet)
        self.r.add_provider(color)
        self.r.add_provider(geo)
        self.r.add_provider(company)
        self.r.add_provider(date_time)
        self.r.add_provider(address)

    def make_employees(self, n: int) -> List[Employee]:
        """make employees

        Args:
            n (int): number of employees to create

        Returns:
            List[Employee]: list of employees
        """
        employees = []
        efac = EmployeeFactory()
        for _ in range(n):
            employees.append(efac.create_employee(efac.fake_maker("Lending", self.r)))
        for _ in range(n):
            employees.append(efac.create_employee("Avax", self.r))
        for _ in range(1):
            try:
                employees.append(efac.create_employee("remember", self.r))
            except Exception:
                logging.error("Add employee failed, deparment not found.")
        return employees

    def run(self, n: int) -> None:
        logger = logging.getLogger("main")
        logger.setLevel(logging.DEBUG)
        employees = self.make_employees(n)
        logger.info("Creating dataframe")
        return pd.DataFrame(employees)


if __name__ == "__main__":
    df = Program().run(1000)
    df = df.drop("area", axis=1)
    df.to_csv("here.csv", index=False)
