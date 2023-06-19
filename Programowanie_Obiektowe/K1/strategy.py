from game import Game


class Strategy(Game):
    __strategy_type: str
    __players: int

    def __init__(self, name: str, genre: str, pegi: int, price: float, reputation: float, strategy_type: str,
                 players: int) -> None:
        super().__init__(name, genre, pegi, price, reputation)
        if len(strategy_type) <= 3:
            self.__strategy_type = strategy_type
        else:
            self.__strategy_type = 'RTS'
        if players > 0:
            self.__players = players
        else:
            self.__players = 5

    @property
    def strategy_type(self) -> str:
        return self.__strategy_type

    @property
    def players(self) -> int:
        return self.__players

    @strategy_type.setter
    def strategy_type(self, value: str) -> None:
        if len(value) <= 3:
            self.__strategy_type = value
        else:
            print('Podana nieprawidłowa wartość')

    @players.setter
    def players(self, value: int) -> None:
        if value > 0:
            self.__players = value
        else:
            print('Podana nieprawidłowa wartość')

    def __eq__(self, other: 'Strategy') -> bool:
        return self.players == other.players

    def __str__(self) -> str:
        return f'Szczegóły:\n' \
               f'Nazwa: {self.name}.\n' \
               f'Gatunek: {self.genre}.\n' \
               f'PEGI: {self.pegi}.\n' \
               f'Cena: {self.price}.\n' \
               f'Średnia recenzja: {self.reputation}.\n' \
               f'Rodzaj gry strategicznej: {self.strategy_type}.\n' \
               f'Liczba graczy: {self.players}.'
