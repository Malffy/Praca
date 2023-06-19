from court import Court


def main() -> None:
    court_1 = Court(address='Słoneczna 10, 10-100 Olsztyn', year_built=1999)
    print(court_1)
    court_2 = Court(500, 500, 'Słoneczna 10, 10-100 Olsztyn', 1999)
    print(court_2)
    court_3 = Court(50, 100, 'Słoneczna 10, 10-100 Olsztyn', 1999)
    print(court_3)
    print(court_1.length)
    court_1.year_built = 1990
    print(court_1)
    print(court_1.area())
    court_1.year_built = 2030
    print(court_1)
    Court.validate(court_1)
    print(court_1)

    print(int(court_1))

if __name__ == '__main__':
    main()
