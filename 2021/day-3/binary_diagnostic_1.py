def binary_diagonistic():
    file = open("input.txt", "r").readlines()


    gamma = ''
    epsilon = ''

    # Populate columns with zeros
    columns = []
    for _ in range(len(file[0])):
        columns.append('0')

    # Split the words into various lists first
    for line in file:
        for i in range(len(line)):
            try:
                columns[i] = columns[i] + line[i]
            except IndexError:
                columns[i] = line[i]

    # Find the most occuring
    for string in columns[:12]: 
        if string.count('1') > string.count('0'):
            gamma = gamma + '1'
            epsilon = epsilon + '0'
        else:
            gamma = gamma + '0'
            epsilon = epsilon + '1'
    return int(gamma, 2) * int(epsilon, 2)

if __name__ == "__main__":
    result = binary_diagonistic()
    print(result)