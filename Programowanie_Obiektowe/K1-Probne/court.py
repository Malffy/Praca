from datetime import datetime


class Court:
    __width: float
    __length: float
    __address: str
    __year_built: int

    def __init__(self, width: float = 68.0, length: float = 100.0,
                 address: str = '', year_built: int = 0) -> None:
        if 45 <= width <= 90 <= length <= 120:
            self.__width = width
            self.__length = length
        else:
            self.__width = 68.0
            self.__length = 100.0
        self.__address = address
        self.__year_built = year_built

    @property
    def width(self) -> float:
        return self.__width

    @property
    def length(self) -> float:
        return self.__length

    @property
    def address(self) -> str:
        return self.__address

    @property
    def year_built(self) -> int:
        return self.__year_built

    @width.setter
    def width(self, value: float) -> None:
        if 90 <= value <= 120:
            self.__width = value
        else:
            print('Nieprawidłowa wielkość')

    @length.setter
    def length(self, value: float) -> None:
        if 90 <= value <= 120:
            self.__length = value
        else:
            print('Nieprawidłowa wielkość')

    @address.setter
    def address(self, value: str) -> None:
        self.__address = value

    @year_built.setter
    def year_built(self, value: int) -> None:
        self.__year_built = value

    def area(self) -> float:
        return self.__length * self.__width

    @staticmethod
    def validate(court: 'Court') -> None:
        x = int(datetime.now().year)
        if court.__year_built <= 0 or court.__year_built > x:
            court.__year_built = x

    def __str__(self):
        return f'Boisko wybudowane w roku' \
               f' {self.__year_built},'f' o ' \
               f'długości {self.__length} metrów i ' \
               f'szerokości {self.__width} metrów.\nPole' \
               f'powierzchni: {self.area()} mkw.\nAdres:' \
               f' {self.__address} '

    def __eq__(self, other: 'Court') -> bool:
        return self.area() == other.area

    def __ne__(self, other: 'Court') -> bool:
        return self.area() != other.area

    def __int__(self):
        return 5
