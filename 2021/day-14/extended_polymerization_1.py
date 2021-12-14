from collections import Counter

def extended_polymerization():
    file = open("input.txt", "r").readlines()

    # Hold the initial polymer template
    polymer_template = file[0][:-1]

    # Hold the incoming polymer template
    new_polymer_template = []

    pair_insertion_rules = {}

    for rule in file[2:]:
        pair_insertion_rules[rule[:2]] = rule[6]

    for j in range(10):
        for i in range(len(polymer_template) - 1):
            new_polymer_template.append(
                polymer_template[i] + pair_insertion_rules[polymer_template[i : i + 2]]
            )
        new_polymer_template.append(polymer_template[-1])
        polymer_template = "".join(new_polymer_template)
        new_polymer_template = []

    counter = Counter(polymer_template)
    most_common = counter.most_common()

    return most_common[0][1] - most_common[-1][1]

if __name__ == "__main__":
    result = extended_polymerization()
    print(result)