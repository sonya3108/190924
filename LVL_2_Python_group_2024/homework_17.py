class CardError(Exception):
    """Базовий клас для всіх помилок, пов'язаних із класом Card."""
    pass


class InvalidCardValueError(CardError):
    """Виключення для недопустимих значень карти."""
    def __init__(self, value):
        self.message = f"Некоректне значення карти: {value}. Дозволені значення: Ace, King, Queen, Jack."
        super().__init__(self.message)


class InvalidCardSuitError(CardError):
    """Виключення для недопустимих мастей карти."""
    def __init__(self, suit):
        self.message = f"Некоректна масть карти: {suit}. Дозволені масті: heart, diamond, club, spades."
        super().__init__(self.message)



class Card:
    """Клас, який реалізує методи та властивості гральної стандартної карти."""

    def __init__(self, type: str, k: str):
        self.toolType = type
        self.kit = k
        self.__SetScore()

    @property
    def toolType(self) -> str:
        return self.__toolType

    @toolType.setter
    def toolType(self, t: str):
        if t in ("Ace", "King", "Queen", "Jack"):
            self.__toolType = t
        else:
            raise InvalidCardValueError(t)

    @property
    def kit(self) -> str:
        dict_kit_smiles = {'spades': '♠️', 'heart': '❤️', 'club': '♣️', 'diamond': '♦️'}
        return dict_kit_smiles.get(self.__kit)

    @kit.setter
    def kit(self, k: str):
        if k in ('spades', 'heart', 'club', 'diamond'):
            self.__kit = k
        else:
            raise InvalidCardSuitError(k)

    def __SetScore(self):
        if self.__toolType == 'Ace':
            self.score = 11
        elif self.__toolType == 'King':
            self.score = 4
        elif self.__toolType == 'Queen':
            self.score = 3
        elif self.__toolType == 'Jack':
            self.score = 2
        else:
            self.score = 0

    def __str__(self) -> str:
        return f'{self.toolType} {self.kit}'

    def __eq__(self, other: 'Card') -> bool:
        return self.__toolType == other.__toolType and self.__kit == other.__kit

    __repr__ = __str__



def main():
    """Тести для перевірки роботи класу Card і виключень."""
    try:
        card1 = Card("King", "heart")
        print(card1)
    except CardError as e:
        print(f"Помилка: {e}")

    try:
        card2 = Card("Dragon", "spades")
    except CardError as e:
        print(f"Помилка: {e}")

    try:
        card3 = Card("Queen", "stars")
    except CardError as e:
        print(f"Помилка: {e}")


if __name__ == "__main__":
    main()


