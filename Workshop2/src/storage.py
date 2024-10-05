"""
This module manage files for have a way to save products.

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

import pickle
from products import Product


class Storage:
    """
    Manages a collection of Product objects, allowing for saving, loading on a file.

    Attributes:
        __list_products: A list to store Product objects.

    Methods:

        save_products: Saves the list of Product objects to a file using pickle.
        load_products: Loads the list of Product objects from a file using pickle.
        add_product: Adds a Product object to the list of products.
        total_prices: Calculates the total price of all products in the list.
        show_products:  Prints the details of all products in the list.
        show_warnings: Prints the details of products that are out of stock.
    """

    def __init__(self):
        self.__list_products: []

    def save_products(self):
        """
        Saves the list of Product objects to a file using pickle.

        The list of products is serialized and written to a file named 'products.pkl'.
        """
        with open("products.pkl", "wb") as file:
            pickle.dump(self.__list_products, file)

    def load_products(self):
        """
        Loads the list of Product objects from a file using pickle.

        The list of products is deserialized from a file named 'products.pkl'
        and loaded into the __list_products attribute.
        """

        with open("products.pkl", "rb") as file:
            self.__list_products = pickle.load(file)

    def add_product(self, product: Product):
        """
        Adds a Product object to the list of products.

        Args:
            product (Product): The Product object to add to the list.
        """

        self.__list_products.append(product)

    def total_prices(self) -> float:
        """
        Calculates the total price of all products in the list.

        Iterates through the list of products and sums their prices.

        Returns:
            float: The total price of all products.
        """
        price = 0.0
        for product in self.__list_products:
            price += product.__price

    def show_products(self):
        """
        Prints the details of all products in the list.

        Iterates through the list of products and prints each one.
        """
        for product in self.__list_products:
            print(product)

    def show_warnings(self):
        """
        Prints the details of products that are out of stock.

        Iterates through the list of products and prints those that have no stock.
        """
        for product in self.__list_products:
            if product.is_no_stock:
                print(product)
