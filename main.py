class PrintedProduct:
    def __init__(self, title, number_of_pages):
        self.title = title
        self.number_of_pages = number_of_pages


class Newspaper(PrintedProduct):
    def __init__(self, title, number_of_pages, page_size, number_of_copies, weekly_frequency):
        super().__init__(title, number_of_pages)
        self.page_size = page_size
        self.number_of_copies = number_of_copies
        self.weekly_frequency = weekly_frequency

    def paper_cost(self):
        return self.page_size * self.number_of_pages * self.number_of_copies * self.weekly_frequency


class Booklet(PrintedProduct):
    def __init__(self, title, number_of_pages, page_size, number_of_copies):
        super().__init__(title, number_of_pages)
        self.page_size = page_size
        self.number_of_copies = number_of_copies

    def paper_cost(self):
        return self.page_size * self.number_of_pages * self.number_of_copies


def sort_and_calculate(products_list):
    costs = []

    for product in products_list:
        costs.append(product.paper_cost())

    total_costs = sum(costs)

    sorted_list = sorted(zip(products_list, costs), key=lambda x: x[1], reverse=True)

    return sorted_list, total_costs


newspaper1 = Newspaper("Газета 1", 12, 0.08, 1000, 3)
newspaper2 = Newspaper("Газета 2", 16, 0.1, 800, 2)
booklet1 = Booklet("Буклет 1", 4, 0.05, 1500)
products_list = [newspaper1, Newspaper("Газета 3", 22, 0.08, 1000, 7), Booklet("Буклет 3", 10, 0.05, 15000),
                 newspaper2, booklet1, Booklet("Буклет 2", 8, 0.15, 1000), Newspaper("Газета 4", 10, 0.15, 1000, 3)]

sorted_list, total_costs = sort_and_calculate(products_list)

print("Відсортовані за спаданням витрат приклади:")
for product, cost in sorted_list:
    print(f"{product.title}: {cost} кв. м.")

print(f"Кінцева вартість: {total_costs} кв. м.")
input("Натисніть Enter для продовження...")
