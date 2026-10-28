def result(m1, m2, m3, m4, m5):
    p = (m1 + m2 + m3 + m4 + m5) / 5
    g = "A" if p >= 80 else "B" if p >= 60 else "C" if p >= 40 else "F"
    return p, g
marks = [float(input(f"Subject {i} marks: ")) for i in range(1, 6)]
p, g = result(*marks); print(f"Percentage: {p}%  Grade: {g}")
