"""19. Write program for building restaurant menu using class in Python."""


class MenuItem:
    def __init__(self, name, description, price):
        self.name = name
        self.description = description
        self.price = price

    def display(self):
        return f"{self.name}: {self.description} - ${self.price:.2f}"


class RestaurantMenu:
    def __init__(self):
        self.menu_items = []

    def add_item(self, item):
        self.menu_items.append(item)

    def display_menu(self):
        print("Restaurant Menu:")
        for item in self.menu_items:
            print(item.display())


def main():
    menu = RestaurantMenu()

    menu.add_item(MenuItem("Spaghetti", "Pasta with marinara sauce", 8.99))
    menu.add_item(MenuItem("Caesar Salad", "Romaine lettuce with Caesar dressing", 6.99))
    menu.add_item(MenuItem("Cheeseburger", "Beef patty with cheddar cheese", 10.99))

    menu.display_menu()


if __name__ == "__main__":
    main()
