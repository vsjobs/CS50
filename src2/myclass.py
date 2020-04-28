class MyPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def main():
    p = MyPoint(5, 6)
    print(p.x)
    print(p.y)


if __name__ == "__main__":
    main()
