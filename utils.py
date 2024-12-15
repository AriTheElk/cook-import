import sys


def eprint(*args, **kwargs):
    """
    Print to standard error for the console.
    """
    print(*args, file=sys.stderr, **kwargs)


# Rip from https://www.geeksforgeeks.org/python-print-sublists-list/
def sub_lists(l):
    """
    Create sublists of an entire list
    """
    lists = [[]]
    for i in range(len(l) + 1):
        for j in range(i):
            lists.append(l[j:i])
    return lists


def highlight_replacement_in_text(instructions, match_start, match_end):
    start = match_start - 18
    end = match_end + 18

    if start < 0:
        start = 0

    if end > len(instructions):
        end = len(instructions)

    eprint("...", instructions[start:end], "...")
    eprint(" " * (3 + match_start - start), "^" * (match_end - match_start))


def print_recipe(title, link, total_time, image, instructions, to_file=False):
    """
    Write the recipe to a file
    args:
    @param title the title of the recipe
    @param link the link to the recipe
    @param total_time the total amount of time for the recipe
    @param image the image associated with the recipe
    @param instructions the instructions for the desired recipe
    @param to_file write formatted recipe to file instead to stdout
    """
    recipe = [
        f">> source: {link}",
        f">> time required: {total_time} minutes",
        f">> image: {image}",
        "\n" + instructions,
    ]

    output_file = to_file if to_file else f"{title}.cook"

    if to_file:
        with open(output_file, "w") as outfile:
            outfile.write("\n".join(recipe) + "\n")
    else:
        print("\n".join(recipe))
