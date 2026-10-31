"""Run examples of basic Python concepts."""


def greet(name):
    return f"Hello, {name}!"


def main():
    name = "Mohamad"
    score = 85.5
    is_learning = True
    print(greet(name))
    print(f"Learning: {is_learning}")
    if score >= 50:
        print("Passed")
    else:
        print("Failed")

    tasks = ["Study Python", "Review AI"]
    tasks.append("Practice")
    print(f"First task: {tasks[0]}")
    print(f"Number of tasks: {len(tasks)}")
    for task in tasks:
        print(task)
    for number in range(1, 4):
        print(f"For loop: {number}")
    count = 1
    while count <= 3:
        print(f"While loop: {count}")
        count += 1


if __name__ == "__main__":
    main()
