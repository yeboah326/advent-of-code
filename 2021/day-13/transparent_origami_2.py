def transparent_origami():
    file = open("input.txt", "r").readlines()

    coordinates = []
    instructions = []

    max_x = 0
    max_y = 0

    # Temporary holding place when instructions are being performed
    temp_coordinates = []

    for line in file:
        # Remove line endings first
        if line == "\n":
            continue
        if line.endswith("\\n"):
            line = line[:-2]
        # Check whether line is a coordinate or a position
        if line[0] != "f":
            temp = line.split(",")
            coordinate = (int(temp[0]), int(temp[1]))
            coordinates.append(coordinate)
        else:
            temp = line.split(" ")
            instructions.append(temp[2])

    for instruction in instructions:
        temp_coordinates = []
        # Remove all coordinates on that line
        axis = instruction[0]
        value = int(instruction[2:])
        for coordinate in coordinates:
            if axis == "x" and coordinate[0] != value:
                if coordinate[0] > value:
                    coordinate = (
                        coordinate[0] - 2 * (coordinate[0] - value),
                        coordinate[1],
                    )
                temp_coordinates.append(coordinate)
            if axis == "y" and coordinate[1] != value:
                if coordinate[1] > value:
                    coordinate = (
                        coordinate[0],
                        coordinate[1] - 2 * (coordinate[1] - value),
                    )
                temp_coordinates.append(coordinate)

        coordinates = list(set(temp_coordinates))

    # Find max size of the x and y coordinate for the
    for coordinate in coordinates:
        max_x = coordinate[0] + 1 if coordinate[0] > max_x else max_x
        max_y = coordinate[1] + 1 if coordinate[1] > max_y else max_y

    # Create the zero matrix
    print_grid = [([" "] * max_y) for i in range(max_x)]

    # Fill the grid
    for coordinate in coordinates:
        print_grid[coordinate[0]][coordinate[1]] = "X"

    # Print the grid
    for row in print_grid:
        print("".join(row))

    return len(coordinates)


if __name__ == "__main__":
    result = transparent_origami()
    print(result)
