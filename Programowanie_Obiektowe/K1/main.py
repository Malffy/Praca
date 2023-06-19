from game import Game


def main() -> None:
    g_1 = Game('NFS2', 'Racing', 16, 50.50, 6.0)
    g_2 = Game('MW2', 'Shooting', 18, 100.99, 5.5)
    print(g_1)
    print(g_2)
    if __name__ == '__main__':
        main()
