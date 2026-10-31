"""Rule-based priority example. This is not a trained ML model."""


def get_priority(days_left):
    if days_left < 0:
        return "Overdue"
    elif days_left <= 1:
        return "High"
    elif days_left <= 3:
        return "Medium"
    else:
        return "Low"


def main():
    task_name = input("Enter task name: ").strip()
    if not task_name:
        print("Please enter a task name.")
        return
    try:
        days_left = int(input("Days until deadline: "))
    except ValueError:
        print("Please enter a whole number, such as -1, 0, or 5.")
        return
    print(f"Task: {task_name}")
    print(f"Priority: {get_priority(days_left)}")


if __name__ == "__main__":
    main()
