from court import Court


class Stadium(Court):
    __name: str
    __common_name: str
    __capacity: int

    def __init__(self, width: float, length: float,
                 address: str, year_built: int, name: str,
                 common_name: str = '', capacity: int = 0) -> None:
        super().__init__(width, length, address, year_built)
        self.__name = name
        self.__common_name = common_name
        if capacity >= 0:
            self.__capacity = capacity
        else:
            self.__capacity = 0

    @property
    def name(self) -> str:
        return self.__name

    @property
    def common_name(self) -> str:
        return self.__common_name

    @property
    def capacity(self) -> int:
        return self.__capacity

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    @common_name.setter
    def common_name(self, value: str) -> None:
        self.__common_name = value

    @capacity.setter
    def capacity(self, value: int) -> None:
        if value < 0:
            print('Attribute error')
        else:
            self.__capacity = value

    def __eq__(self, other: 'Stadium') -> bool:
        return self.capacity == other.capacity and \
               self.area() == other.area()

    def __ne__(self, other: 'Stadium') -> bool:
        return self.capacity != other.capacity or \
               self.area() != other.area()

    def __str__(self) -> str:
        if self.__common_name != '':
            return f'Boisko wybudowane w roku ' \
                   f'{self.year_built}, o długości ' \
                   f'{self.length} metrów i szerokości {self.width} metrów.' \
                   f'\nPole powierzchni: {self.area()} mkw.' \
                   f'\nAdres: {self.address}.' \
                   f'\nNazwa: {self.name}.' \
                   f'\nPojemność stadionu: {self.capacity} osób.'
        else:
            return f'Boisko wybudowane w roku ' \
                   f'{self.year_built}, o długości ' \
                   f'{self.length} metrów i szerokości {self.width} metrów.' \
                   f'\nPole powierzchni: {self.area()} mkw.' \
                   f'\nAdres: {self.address}.' \
                   f'\nNazwa: {self.name}.' \
                   f'\nNazwa zwyczajowa: {self.common_name}.' \
                   f'\nPojemność stadionu: {self.capacity} osób.'
