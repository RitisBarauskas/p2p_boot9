
class SomeClass:
    def __init__(self):
        pass

    def some_method(self):
        pass

    def another_method(self):
        pass


def main():
    data = input("Enter the data: ")
    some_list = [1, 2, 3, 4, 5]
    some_var = SomeClass()
    print(some_list)
    print(f'data: {data}')
    print(some_var)
    if data == "hello":
        print("Hello, World!")
    elif data == "bye":
        print("Goodbye, World!")
    else:
        print("Invalid data!")


if __name__ == "__main__":
    main()
