"""Add two numbers entered by the user."""


def main():
    try:
        first = float(input("Enter the first number: "))
        second = float(input("Enter the second number: "))
    except ValueError:
        print("Please enter valid numbers, such as 10 or 2.5.")
        return
    print(f"Total: {first + second}")


if __name__ == "__main__":
    main()
