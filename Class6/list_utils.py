def print_numbered_list(input_list: list, title: str="Contents of List"):

    counter = 1

    print(title)
    print()

    for item in input_list:
        print(f"{counter}: {item}")
        counter += 1

colours = ["red", "Green", "Blue"]

print_numbered_list(colours, "List of Colours")
print_numbered_list(colours)


def print_bullet_list(input_list: list, title: str="Contents of List"):


    print(title)
    print()

    for item in input_list:
        print(f"- {item}")

colours = ["red", "Green", "Blue"]

print_bullet_list(colours, "List of Colours")
