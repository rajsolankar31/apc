def unique(lst):
    out = []
    for x in lst:
        if x not in out: out.append(x)
    return out
print(unique(input("Enter list elements: ").split()))
