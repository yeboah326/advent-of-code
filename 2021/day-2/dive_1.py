def dive():
    horizontal = 0
    depth = 0

    file = open("input.txt", "r").readlines()

    for item in file:
        command, value = item.split(" ")

        if command == "forward":
            horizontal += int(value)
        elif command == "down":
            depth += int(value)
        elif command == "up":
            depth -= int(value)

    return horizontal * depth


if __name__ == "__main__":
    result = dive()
    print(result)
