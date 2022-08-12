

#def print_numbered_list(input_list: list, title= "Contents of List"):

#str is not needed here, the " ... " is self-evident
def print_numbered_list(input_list: list, title: str="Contents of List"):

    counter = 1

    print(title)
    print()

#When going through a list, its a FOR loop ( Q!!)
    for item in input_list:
        print(f"{counter}: {item}")
        counter += 1

colours = ["red", "Green", "Blue"]

print_numbered_list(colours, "List of Colours")
print_numbered_list(colours)

# print_numbered_list("Guillermo", "List of colours")