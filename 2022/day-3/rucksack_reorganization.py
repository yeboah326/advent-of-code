def rucksack_reorganization_one():
    lines = open("/home/ultron/Documents/Projects/advent-of-code/2022/day-3/input.txt", "r").readlines()
    
    total = 0
    
    for line in lines:
        left = set(line[:int(len(line) / 2)])
        right = set(line[int(len(line) / 2):])
        
        common = left.intersection(right).pop()
        if 97 <= ord(common) <= 122:
            total += ord(common) % 96
        elif 65 <= ord(common) <= 90:
            total += ord(common) % 64 + 26

    return total

def rucksack_reorganization_two():
    lines = open("/home/ultron/Documents/Projects/advent-of-code/2022/day-3/input.txt", "r").readlines()

    total = 0

    for i in range(0,len(lines),3):
        member1 = set(lines[i].strip())
        member2 = set(lines[i + 1].strip())
        member3 = set(lines[i + 2].strip())

        common = member1.intersection(member2).intersection(member3).pop()
        if 97 <= ord(common) <= 122:
            total += ord(common) % 96
        elif 65 <= ord(common) <= 90:
            total += ord(common) % 64 + 26
        
    return total


if __name__ == "__main__":
    # print(rucksack_reorganization_one())
    print(rucksack_reorganization_two())