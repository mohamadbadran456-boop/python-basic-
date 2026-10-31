"""Calculate an average, including the empty-list case."""


def calculate_average(scores):
    if len(scores) == 0:
        return None
    return sum(scores) / len(scores)


def main():
    grades = [80, 90, 70]
    average = calculate_average(grades)
    if average is None:
        print("No grades available")
    else:
        print(f"Average: {average:.2f}")


if __name__ == "__main__":
    main()
