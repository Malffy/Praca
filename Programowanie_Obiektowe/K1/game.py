class Game:
    __name: str
    __genre: str
    __pegi: int
    __price: float
    __reputation: float

    def __init__(self, name: str, genre: str, pegi: int, price: float, reputation: float) -> None:
        self.__name = name
        self.__genre = genre
        if 0 <= pegi <= 18:
            self.__pegi = pegi
        else:
            self.__pegi = 18
        if price > 0:
            self.__price = price
        else:
            self.__price = 50.99
        if 1 <= reputation <= 6:
            self.__reputation = reputation
        else:
            self.__reputation = 1.0

    @property
    def name(self) -> str:
        return self.__name

    @property
    def genre(self) -> str:
        return self.__genre

    @property
    def pegi(self) -> int:
        return self.__pegi

    @property
    def price(self) -> float:
        return self.__price

    @property
    def reputation(self) -> float:
        return self.__reputation

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @genre.setter
    def genre(self, value: str) -> None:
        self.__genre = value

    @pegi.setter
    def pegi(self, value: int) -> None:
        if 0 <= value <= 18:
            self.__pegi = value
        else:
            print('Podana nieprawidłowa wartość')

    @price.setter
    def price(self, value: float) -> None:
        if value > 0:
            self.__price = value
        else:
            print('Podana nieprawidłowa wartość')

    @reputation.setter
    def reputation(self, value: float) -> None:
        if 1 <= value <= 6:
            self.__reputation = value
        else:
            print('Podana nieprawidłowa wartość')

    @staticmethod
    def check_pegi(game: 'Game') -> None:
        if 0 <= game.__pegi <= 18:
            if game.__pegi > 13:
                game.__reputation = game.__reputation + 1
        else:
            print('Podana nieprawidłowa wartość')

    def __str__(self) -> str:
        return f'Szczegóły:\n' \
               f'Nazwa: {self.name}.\n' \
               f'Gatunek: {self.genre}.\n' \
               f'PEGI: {self.pegi}.\n' \
               f'Cena: {self.price}.\n' \
               f'Średnia recenzja: {self.reputation}.'

    def __lt__(self, other: 'Game') -> bool:
        return self.reputation < other.reputation
