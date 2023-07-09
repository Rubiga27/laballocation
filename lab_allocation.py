def allocate_lab(x, y, z, n):
    remaining_capacity = [x - n, y - n, z - n]
    valid_labs = [(i, cap) for i, cap in enumerate(remaining_capacity) if cap >= 0]
    sorted_labs = sorted(valid_labs, key=lambda x: x[1])
    if len(sorted_labs) == 0:
        return None
    return "L" + str(sorted_labs[0][0] + 1)


# Get inputs from the user
x = int(input("Capacity of lab L1: "))
y = int(input("Capacity of lab L2: "))
z = int(input("Capacity of lab L3: "))
n = int(input("Number of students in the class: "))

# Call the function to allocate the lab
allocated_lab = allocate_lab(x, y, z, n)
if allocated_lab is None:
    print("No lab has enough capacity for", n, "students.")
else:
    print(allocated_lab)
    