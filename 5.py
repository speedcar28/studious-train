# tw = ("tw", "u", "p", "l", "e", 0, 1, 2, 3, 4, 0.1, 1j)
# print(tw[5:10])

# tw=("tuple")
# print(type(tw))
# tw=("tuple",)
# print(type(tw))

# twe = "hello", "tuple", 2
# h, t, tw = twe
# print(t, tw)

two = "hello", "tuple", 2
edit = list(two)
edit.append(56)
print(tuple(edit))