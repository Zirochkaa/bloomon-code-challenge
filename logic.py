import re
import sys

from files import read_from_file, write_to_file


def get_total_flowers_count(total_flowers: dict):
    """
    Returns sum of flowers stored in 'total_flowers' variable.

    Parameters:
    total_flowers (dict) - contains accumulative info about flowers count, like {'cL': 129, 'bL': 123, ...}.
    """
    return sum([v for k, v in total_flowers.items()], 0)


def get_flowers_count(flowers: list):
    """
    Returns sum of flowers stored in 'flowers' parameter.

    Parameters:
    flowers (list) - list of wlowers with their quantities, like ['10a', '15b', '5c'].
    """
    return sum([int(item[:-1]) for item in flowers], 0)


def can_do_bouquet(flowers: list, flower_size: str, total_flowers_in_bouquet: int, total_flowers: dict):
    """
    Checks if we can create bouquet from given flowers by subtracting flower quantity from 'total_flowers'.
    First, we need to check that we have enough of each flower.
    Second, we need to check that we have enough flowers in general (for situation when total quantity of
    flowers in the bouquet is bigger than the sum of the flower quantities).

    Parameters:
    flowers (list) - list of flowers with their quantities, like ['10a', '15b', '5c'].
    flower_size (str) - L (large) or S (small).
    total_flowers_in_bouquet (int) - total quantity of flowers in the bouquet, like 30.
    total_flowers (dict) - contains accumulative info about flowers count, like {'cL': 129, 'bL': 123, ...}.
    """
    for item in flowers:
        # Here I write flower info in same format as I have in 'total_flowers'.
        flower = item[-1] + flower_size
        flower_quantity = int(item[:-1])

        if total_flowers[flower] - flower_quantity < 0:
            return False

    return True if total_flowers_in_bouquet <= get_total_flowers_count(total_flowers=total_flowers) else False


def subtract_flowers(flowers: list, flower_size: str, total_flowers: dict):
    """
    Subtracts quantities of flowers in bouquet from 'total_flowers'.

    Parameters:
    flowers (list) - list of wlowers with their quantities, like ['10a', '15b', '5c'].
    flower_size (str) - L (large) or S (small).
    total_flowers (dict) - contains accumulative info about flowers count, like {'cL': 129, 'bL': 123, ...}.
    """
    for item in flowers:
        flower = item[-1] + flower_size
        flower_quantity = int(item[:-1])
        total_flowers[flower] -= flower_quantity


def provide_and_get_any_flower(flowers: list, flower_quantity: int, total_flowers: dict, bouquet_size: str):
    """
    Counts amount of extra space in a bouquet and finds right flower to fill that space.

    Parameters:
    flowers (list) - list of wlowers with their quantities, like ['10a', '15b', '5c'].
    flower_quantity (int) - total quantity of flowers in the bouquet, like 30.
    total_flowers (dict) - contains accumulative info about flowers count, like {'cL': 129, 'bL': 123, ...}.
    bouquet_size (str) - L (large) or S (small).

    Returns:
    quantity and name of extra flower (like 5a), if one is needed, else None.
    """
    for item in flowers:
        flower_quantity -= int(item[:-1])

    # Since total quantity of flowers in the bouquet is bigger than the sum of the flower quantities, we can append
    # bouquet with any flowers we want. But it has to be in right size. In the line below I filter flowers and get
    # only ones with right size for the bouquet.
    flowers_with_right_size = filter(lambda key: key[-1] == bouquet_size, total_flowers.keys())

    # And here I get flower with max quantity of flowers. I decided that I would do just that, take the flower with
    # the max quantity and fill with it extra space.
    _max_quantity_flower = max(flowers_with_right_size, key=total_flowers.get)
    total_flowers[_max_quantity_flower] -= flower_quantity

    return f'{flower_quantity}{_max_quantity_flower[0]}' if flower_quantity else None


def parse_bouquet(bouquet: str):
    """
    Parses bouquet string.

    Parameters:
    bouquet (str) - bouquet info, like AL10a15b5c30.

    Returns:
    name_and_size (str) - bouquet name and bouquet size, like AL.
    total_flowers_in_bouquet (int) - total quantity of flowers in the bouquet, like 30.
    parsed_flowers (list) - list of flowers with their quantities, like ['10a', '15b', '5c'].
    """
    # Here I have 4 groups (let's use this example - AL10a15b5c30):
    # 1 group: first 2 letters (AL)
    # 2 group: all flower quantities with their species (10a15b5c)
    # 3 group: last flower quantity with its specie (5c)
    # 4 group: total quantity of flowers in bouquet (30)
    #
    # Now I want to know all groups of flower quantity with its specie.
    # I tried to do it with one regex, but it didn't work. So, I will use two regex.
    parsed_bouquet = re.match(r'([A-Z][LS])((\d+[a-z])+)(\d+)', bouquet)

    name_and_size = parsed_bouquet.groups()[0]
    flowers = parsed_bouquet.groups()[1]
    total_flowers_in_bouquet = int(parsed_bouquet.groups()[3])

    # In 'parsed_flowers' I store list of flowers with their quanity, like ['10a', '15b', '5c'].
    parsed_flowers = re.findall(r'\d+[a-z]', flowers)
    return name_and_size, total_flowers_in_bouquet, parsed_flowers


def handle_bouquet(bouquet: str, total_flowers: dict):
    """
    Handles single bouquet.

    Parameters:
    bouquet (str) - line with bouquet info, like AL10a15b5c30.
    total_flowers (dict) - contains accumulative info about flowers count, like {'cL': 129, 'bL': 123, ...}.

    Returns:
    bouquet (with or without extra flowers), if one can be created from the available flowers, else None.
    """
    name_and_size, total_flowers_in_bouquet, flowers = parse_bouquet(bouquet=bouquet)
    bouquet_size = name_and_size[-1]

    if can_do_bouquet(
        flowers=flowers,
        flower_size=bouquet_size,
        total_flowers_in_bouquet=total_flowers_in_bouquet,
        total_flowers=total_flowers
    ):
        subtract_flowers(flowers=flowers, flower_size=bouquet_size, total_flowers=total_flowers)
        extra_flower = provide_and_get_any_flower(flowers=flowers, flower_quantity=total_flowers_in_bouquet,
                                                  total_flowers=total_flowers, bouquet_size=bouquet_size)

        return_bouquet = f"{name_and_size}{''.join(flowers)}"
        return return_bouquet + extra_flower if extra_flower else return_bouquet


def get_bouquets(input_file_name: str, output_file_name: str):
    """
    Main function for this task. This function is being called in script.py file.
    It handles all bouquets and does the following:
        1. reads input info from 'input_file_name' file.
        2. handles bouquets and flowers info.
        3. writes output info into 'output_file_name' file.
    """
    total_bouquets, total_flowers = read_from_file(file_name=input_file_name)

    bouquets_for_writing_to_file = list()

    for bouquet in total_bouquets:
        handled_bouquet = handle_bouquet(bouquet=bouquet, total_flowers=total_flowers)
        if handled_bouquet:
            bouquets_for_writing_to_file.append(handled_bouquet)

    write_to_file(file_name=output_file_name, data=bouquets_for_writing_to_file)
