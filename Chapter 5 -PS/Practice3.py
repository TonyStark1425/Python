# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)

set1 = {9, "9.0"}
print(set1)

values = {
    ("float", 9.0),
    ("int", 9)
}

print(values)