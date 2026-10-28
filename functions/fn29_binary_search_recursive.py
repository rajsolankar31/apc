def bsearch(lst, target, lo, hi):
    if lo > hi: return -1
    mid = (lo + hi) // 2
    if lst[mid] == target: return mid
    return bsearch(lst, target, mid + 1, hi) if lst[mid] < target else bsearch(lst, target, lo, mid - 1)
lst = sorted(int(x) for x in input("Enter numbers: ").split()); t = int(input("Search for: "))
i = bsearch(lst, t, 0, len(lst) - 1); print(f"Found at index {i} of {lst}" if i != -1 else "Not found")
