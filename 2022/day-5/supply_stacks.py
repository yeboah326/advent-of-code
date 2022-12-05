def supply_stacks_one():
    lines = open("/home/ultron/Documents/Projects/advent-of-code/2022/day-5/input.txt", "r").readlines()

    # Get our columns
    no_of_cols = int(len(lines[0]) / 4)
    cols = [[]] * no_of_cols
    instructions_line = 0
    final_string = ""

    for index, line in enumerate(lines):
        if line.strip()[0] != "1":
            for i in range(0,len(lines[0]),4):
                val = line[i:i+3].strip()
                if val:
                    cols[int(i / 4)] = cols[int(i/4)] + [val]
        else:
            instructions_line = index + 2
            break
    
    for instruction in lines[instructions_line:]:
        instruction_mod = instruction.strip().split(" ")
        count, from_, to_ = int(instruction_mod[1]), int(instruction_mod[3]) - 1, int(instruction_mod[5]) - 1
        cols[to_] = cols[from_][0:count][::-1] + cols[to_]
        cols[from_] = cols[from_][count:]
    
    for col in cols:
        if col:
            final_string += col[0][1]
    
    print(final_string)

def supply_stacks_two():
    lines = open("/home/ultron/Documents/Projects/advent-of-code/2022/day-5/input.txt", "r").readlines()

    # Get our columns
    no_of_cols = int(len(lines[0]) / 4)
    cols = [[]] * no_of_cols
    instructions_line = 0
    final_string = ""

    for index, line in enumerate(lines):
        if line.strip()[0] != "1":
            for i in range(0,len(lines[0]),4):
                val = line[i:i+3].strip()
                if val:
                    cols[int(i / 4)] = cols[int(i/4)] + [val]
        else:
            instructions_line = index + 2
            break
    
    for instruction in lines[instructions_line:]:
        instruction_mod = instruction.strip().split(" ")
        count, from_, to_ = int(instruction_mod[1]), int(instruction_mod[3]) - 1, int(instruction_mod[5]) - 1
        cols[to_] = cols[from_][0:count] + cols[to_]
        cols[from_] = cols[from_][count:]
    
    for col in cols:
        if col:
            final_string += col[0][1]
    
    print(final_string)

        
            

if __name__ == "__main__":
    supply_stacks_two()