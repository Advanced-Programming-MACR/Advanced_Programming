"""
This module is the represents the users that will interact with the app

Author: Miguel Andres Contreras Rodriguez <macontrerasr@udistrital.edu.co>

This file is part of Workshop2.

Workshop2 is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of 
the License, or (at your option) any later version.

Workshop2 is distributed in the hope that it will be useful, 
but WITHOUT ANY WARRANTY; without even the implied warranty of 
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU 
General Public License for more details.

You should have received a copy of the GNU General Public License 
along with Workshop2. If not, see <https://www.gnu.org/licenses/>. 
"""

from abc import ABC, abstractmethod

# =============================== Abstract user ================= #


class AbstractUser(ABC):

    def __init__(self, name: str, email: str):
        self.__name = name
        self.__email = email
        self.__grants = {}

    @abstractmethod
    def validate_grants(self, grant: str):

# =========================== employee =========================== #

class Employee(AbstractUser);

    def __init__(self, name:str, email:str):
        super().__init__(self, name:str,email:str):
        self.__create_grants()

    def __create_grants(self):
        self.__grants = {
            "shopping_cart": False,
            "add_categories": True,
            "add_products": True,
        }
    
    def validate_grants(self, grant: str):