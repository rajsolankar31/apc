def is_eligible(attended, total, required=75):
    return attended / total * 100 >= required
