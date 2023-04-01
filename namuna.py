fib = lambda x: x if x <= 1 else fib(x-1) + fib(x-2)


if __name__ == "__main__":
    print(fib(7))