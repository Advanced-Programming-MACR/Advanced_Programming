"""
This module contains two classes, the categories and catalog classes.

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

# =============================== Category class ========================= #


class Category:
    """
    Represents a category that contains a collection of Product objects.

    Attributes:
        __name: The name of the category.
        __description: A brief description of the category.
        __products: A list to store Product objects.

    Methods:

        add_product: Adds a Product object to the list of products.
        delete_product: Removes a Product object from the list of products if it exists.
        show_products: Prints the details of all products in the category.
        show_products_by_brand: Prints the details of products that match the specified brand.
        clean_no_stock_products: Removes products that are out of stock from the list of products.
    """

    def __init__(self, name: str, description: str):
        self.__name = name
        self.__description = description
        self.__products = []

    def __str__(self) -> str:
        return f"{self.__name}: {self.__description}"

    def add_product(self, product: Product):
        """
        Adds a Product object to the list of products.

        Args:
            product (Product): The Product object to add to the list.
        """
        self.__products.append(product)

    def delete_product(self, product: Product):
        """
        Removes a Product object from the list of products if it exists.

        Args:
            product (Product): The Product object to remove from the list.
        """
        for product1 in self.__products:
            if product1 == product:
                self.__products.remove(product1)

    def show_products(self):
        """
        Prints the details of all products in the category.

        Iterates through the list of products and prints each one.
        """
        for product1 in self.__products:
            print(product1)

    def show_products_by_brand(self, brand: str):
        """
        Prints the details of products that match the specified brand.

        Args:
            brand (str): The brand to filter products by.
        """
        for product1 in self.__products:
            if brand in product1.is_brand:
                print(product1)

    def clean_no_stock_products(self):
        """
        Removes products that are out of stock from the list of products.

        Iterates through the list of products and removes those that have no stock.
        """
        for product in self.__products:
            if product.is_no_stock is True:
                self.delete_product(product)


# ================================= Catalog class ========================= #


class Catalog:

    def __init__(self):
        self.__categories = {}

    def add_category(self, cetregory: Category):
        pass

    def remove_category(self, name: str):
        pass

    def show_categories(self):
        pass

    def search_products_by_name(self, name: str):
        pass

    def search_products_by_category(self, name: str):
        pass

    def search_products_by_brand(self, brand: str):
        pass
