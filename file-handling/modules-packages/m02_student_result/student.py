def total_marks(marks): return sum(marks)
def percentage(marks, max_per_subject=100): return sum(marks) / (len(marks) * max_per_subject) * 100
def grade(p):
    if p >= 90: return "A+"
    if p >= 80: return "A"
    if p >= 70: return "B"
    if p >= 60: return "C"
    if p >= 40: return "D"
    return "F"
