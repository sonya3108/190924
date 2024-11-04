class MobPhone:
    def __init__(self, brand, size_h, size_w, price):
        self.brand = brand
        self._size_h = None
        self._size_w = None
        self._price = None
        self.size_h = size_h
        self.size_w = size_w
        self.price = price


    @property
    def size_h(self):
        return self._size_h

    @size_h.setter
    def size_h(self, value):
        if 11 <= value <= 18:
            self._size_h = value
        else:
            raise ValueError("Height must be between 11 and 18 cm.")


    @property
    def size_w(self):
        return self._size_w

    @size_w.setter
    def size_w(self, value):
        if 5 <= value <= 9:
            self._size_w = value
        else:
            raise ValueError("Width must be between 5 and 9 cm.")


    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value >= 0:
            self._price = value
        else:
            raise ValueError("Price cannot be negative.")


    def getData(self):
        print(f"Brand: {self.brand}")
        print(f"Height: {self.size_h} cm")
        print(f"Width: {self.size_w} cm")
        print(f"Price: ${self.price}")



phone1 = MobPhone("Samsung", 15, 7, 999)
phone2 = MobPhone("Apple", 16, 8, 1099)


phone1.getData()
print("\n")
phone2.getData()
