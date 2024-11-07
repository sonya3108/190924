from datetime import datetime, timedelta

class Train:
    def __init__(self, destination: str, train_number: int, departure_time: datetime):

        self._destination = destination
        self._train_number = train_number


        if departure_time < datetime.now():
            raise ValueError("Час відправлення не може бути меншим за поточний час.")
        self._departure_time = departure_time

    def get_train_info(self):
        """
        Повертає інформацію про потяг у вигляді рядка.
        """
        return (
            f"Потяг №{self._train_number} до {self._destination}, "
            f"відправлення: {self._departure_time.strftime('%Y-%m-%d %H:%M:%S')}"
        )


    @property
    def train_number(self):
        return self._train_number

    @property
    def destination(self):
        return self._destination

    @property
    def departure_time(self):
        return self._departure_time

    # 1
    @staticmethod
    def sort_trains_by_number(trains):
        """
        Сортує список потягів за номерами потягів.
        """
        return sorted(trains, key=lambda train: train.train_number)

    # 2
    @staticmethod
    def find_train_by_number(trains, train_number):
        """
        Знаходить і повертає інформацію про потяг за номером.
        """
        found_trains = [train for train in trains if train.train_number == train_number]
        if not found_trains:
            return f"Потяг з номером {train_number} не знайдено."
        return "\n".join(train.get_train_info() for train in found_trains)

    # 3
    @staticmethod
    def sort_trains_by_destination(trains):
        """
        Сортує список потягів за пунктом призначення.
        Якщо пункт призначення однаковий, сортує за часом відправлення.
        """
        return sorted(trains, key=lambda train: (train.destination, train.departure_time))



if __name__ == "__main__":

    trains = [
        Train("Київ", 101, datetime.now() + timedelta(minutes=10)),  # додаємо 10 хвилин до поточного часу
        Train("Львів", 202, datetime.now() + timedelta(minutes=15)),
        Train("Львів", 303, datetime.now() + timedelta(minutes=20)),
        Train("Київ", 404, datetime.now() + timedelta(minutes=25)),
        Train("Одеса", 105, datetime.now() + timedelta(minutes=5))
    ]

    # Сортування потягів за номером потяга (Intermediate)
    sorted_trains_by_number = Train.sort_trains_by_number(trains)
    print("Список потягів після сортування за номером:")
    for train in sorted_trains_by_number:
        print(train.get_train_info())

    print("\n")

    # Пошук потяга за номером (Intermediate)
    print("Пошук потяга за номером 202:")
    print(Train.find_train_by_number(trains, 202))

    print("\n")

    # Advanced
    sorted_trains_by_destination = Train.sort_trains_by_destination(trains)
    print("Список потягів після сортування за пунктом призначення і часом відправлення:")
    for train in sorted_trains_by_destination:
        print(train.get_train_info())







