def count_occurrences(lst, el):
    c = 0
    for x in lst:
        if x == el: c += 1
    return c
lst = input("Enter list elements: ").split(); el = input("Element to count: ")
print("Occurrences:", count_occurrences(lst, el))
