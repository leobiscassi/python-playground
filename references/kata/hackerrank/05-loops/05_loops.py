if __name__ == '__main__':
    n = int(input())
    i = 0

    if n in range(1, 21):
        while i < n:
            print(i ** 2)
            i += 1

