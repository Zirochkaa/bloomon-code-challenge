from collections import defaultdict


def read_from_file(file_name: str):
    """ Reads file and saves its data into 'bouquets' and 'flowers' variables """
    if not file_name or not isinstance(file_name, str):
        raise ValueError(f"'file_name' argument must have 'str' type and not {type(file_name)}.")

    total_bouquets = list()
    total_flowers = defaultdict(int)
    with open(file_name, 'r') as f:
        for line in f:
            if len(line) == 3:  # 3 is because 'line' has '\n' as trailing symbol
                total_flowers[line.strip()] += 1
            elif len(line) > 3:
                total_bouquets.append(line.strip())

    return total_bouquets, total_flowers


def write_to_file(file_name: str, data: list):
    """ Writes 'data' into file """
    with open(file_name, 'w') as f:
        f.write('\n'.join(data))
