def camp_cleanup_one():
    lines = open("/home/ultron/Documents/Projects/advent-of-code/2022/day-4/input.txt", "r").readlines()
    count = 0

    for line in lines:
        period = line.strip().split(",")
        periodOne = period[0].split("-")
        periodTwo = period[1].split("-")
        if(((int(periodTwo[0]) >= int(periodOne[0])) and (int(periodTwo[1]) <= int(periodOne[1]))) or ((int(periodOne[0]) >= int(periodTwo[0])) and (int(periodOne[1]) <= int(periodTwo[1])))):
            count += 1

    return count

def camp_cleanup_two():
    lines = open("/home/ultron/Documents/Projects/advent-of-code/2022/day-4/input.txt", "r").readlines()
    count = 0

    for line in lines:
        period = line.strip().split(",")
        periodOne = period[0].split("-")
        periodTwo = period[1].split("-")

        # Taking of disjoint periods
        if not((int(periodTwo[0]) > int(periodOne[1])) or (int(periodOne[0]) > int(periodTwo[1]))):
            count += 1
    
    return count
     


if __name__ == "__main__":
    # print(camp_cleanup_one())
    print(camp_cleanup_two())