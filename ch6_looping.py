def ten_asterisks():
    for i in range(10):
        print("*", end=" ")


def ten_by_ten_asterisks():
    for _ in range(10):
        for _ in range(10):
            print("*", end=" ")
        print()


def m_by_n_asterisks(m, n):
    for _ in range(n):
        for _ in range(m):
            print("*", end=" ")
        print()


def m_by_n_digits(m, n):
    for i in range(n):
        for j in range(m):
            print(i, end=" ")
        print()


def triangle_digits(m):
    counter = 10
    i = 0
    while counter < 55:
        for j in range(i + 1):
            print(counter, end=" ")
            counter += 1
        print()
        i += 1


def o_box(n):
    print("o " * (n-1) + "o")
    for i in range(n - 2):
        print("o " + "  "*(n-2) + "o")
    print("o " * (n - 1) + "o")


def digit_diamond(n):
    def top_left(i, j): return 2*(i + j) + 1

    def top_right(i, j): return 2*(i - j) + 4*n - 1

    def bottom_left(i, j): return 2*(j - i) + 4*n - 1

    def bottom_right(i, j): return -2*(i + j) + 8*n - 3

    max_value = 2*n - 1
    for i in range(2*n):
        for j in range(2*n):
            if i < n:
                if j < n:
                    value = top_left(i, j)
                else:
                    value = top_right(i, j)
            elif j < n:
                value = bottom_left(i, j)
            else:
                value = bottom_right(i, j)

            if value <= max_value:
                print("{:2d}".format(value), end=" ")
            else:
                print("  ", end=" ")
        print()
    print()


if __name__ == "__main__":
    digit_diamond(3)
    digit_diamond(5)
    digit_diamond(12)
