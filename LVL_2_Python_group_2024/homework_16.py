class Client:
    def __init__(self, name, balance, checking_account):
        """
        Ініціалізація нового клієнта.
        :param name: Ім'я клієнта (рядок).
        :param balance: Початковий баланс (ціле число).
        :param checking_account: Логічне значення, чи є рахунок валідним.
        """
        self.name = name
        self.balance = balance
        self.checking_account = checking_account

    def withdraw(self, amount):
        """
        Зняття грошей з рахунку.
        :param amount: Сума для зняття (ціле число).
        :return: Рядок із назвою клієнта та оновленим балансом.
        :raises ValueError: Якщо на рахунку недостатньо грошей.
        """
        if amount > self.balance:
            raise ValueError(f"Недостатньо коштів для зняття {amount}. Баланс: {self.balance}")
        self.balance -= amount
        return f"на рахунку у {self.name} в залишку {self.balance}"

    def transfer(self, other_client, amount):
        """
        Переведення коштів на інший рахунок.
        :param other_client: Інший клієнт (об'єкт Client).
        :param amount: Сума для переведення (ціле число).
        :return: Рядок із балансами обох клієнтів.
        :raises ValueError: Якщо недостатньо грошей або рахунок іншого клієнта не валідний.
        """
        if amount > self.balance:
            raise ValueError(f"{self.name} не має достатньо коштів для переведення {amount}. Баланс: {self.balance}")
        if not other_client.checking_account:
            raise ValueError(f"Рахунок у {other_client.name} не валідний для переведення коштів.")

        self.balance -= amount
        other_client.balance += amount
        return (f"на рахунку у {self.name} в залишку {self.balance} "
                f"та на рахунку у {other_client.name} в залишку {other_client.balance}")

    def deposit(self, amount):
        """
        Поповнення рахунку.
        :param amount: Сума для поповнення (ціле число).
        :return: Рядок із назвою клієнта та оновленим балансом.
        """
        self.balance += amount
        return f"на рахунку у {self.name} в залишку {self.balance}"



if __name__ == "__main__":
    Taras = Client('Taras', 1302, True)
    Pavlo = Client('Pavlo', 986, False)

    print(Taras.withdraw(2))

    try:
        print(Pavlo.transfer(Taras, 86))
    except ValueError as e:
        print(e)

    Pavlo.checking_account = True
    print(Pavlo.transfer(Taras, 100))

    try:
        print(Taras.transfer(Pavlo, 474))
    except ValueError as e:
        print(e)

    print(Pavlo.deposit(466))

