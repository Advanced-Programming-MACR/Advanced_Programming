"""
This module is the represents of the shopping cart and all its funcionalities

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

from products import Product


class Shopping_cart:

    def __init__(self):
        self.__products_on_cart: []

    def add_product(self, product: Product):
        pass

    def clean_cart(self):
        pass

    def is_cart_empty(self) -> bool:
        pass

    def remove_product(self, product: Product):
        pass

    def show_cart(self):
        pass

    def calculate_total_price(self) -> float:
        pass
