def square(x):
    return x * x


def main():
    for i in range(10):
        print("{} squared is {}".format(i, square(i)))
        s = square(i)
        print(f"{i} my squared is {s}")


if __name__ == "__main__":
    main()
