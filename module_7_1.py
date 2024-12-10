import os

class Product():
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return f'{self.name}, {self.weight}, {self.category}'


class Shop():
    def __init__(self):
        self.file_name = 'списокпродуктов.txt'

    def get_products(self):
        if not os.path.exists(self.file_name):
            with open(self.file_name, 'w') as file:
                pass  # создаем пустой файл, если его нет

        with open(self.file_name, 'r') as file:
            return file.read().strip()  # убираем лишние пробелы и переносы строк

    def add(self, *products):
        self.products = products

        for product in self.products:
            if product.name not in self.get_products():
                with open(self.file_name, 'a') as file:
                    file.write(f'\n{product}')  # добавляем продукт в конец файла
            else:
                print(f'Продукт {product.name} уже есть в магазине')

if __name__ == '__main__':
    s1 = Shop()
    p1 = Product('Potato', 50.5, 'Vegetables')
    p2 = Product('Spaghetti', 3.4, 'Groceries')
    p3 = Product('Potato', 5.5, 'Vegetables')

    print(p2)  # __str__

    s1.add(p1, p2, p3)

    print(s1.get_products())

