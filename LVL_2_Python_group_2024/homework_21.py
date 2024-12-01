class List:
    def __init__(self, elements):
        self.elements = elements

    def remove_elements(self, values_to_remove):
        """
        Видаляє всі вказані елементи з основного списку.
        :param values_to_remove: список значень для видалення
        :return: список після видалення елементів
        """
        self.elements = [element for element in self.elements if element not in values_to_remove]
        return self.elements



list_1 = [1, 1, 2, 3, 1, 2, 3, 4]
val = [1, 3]

my_list = List(list_1)
result = my_list.remove_elements(val)
print(result)
