# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

people = ["john", "David", "Sara", "Barbara", "Lori", "Mark"]

# for person in people:
#     print(f"Person: {person}")

# break
for person in people:
    if person == "Sara":
        break
    print(f"Person: {person}")

# While loops execute a set of statements as long as a condition is true.

count = 0

while count <= 10:
    print(count)
    count += 1
