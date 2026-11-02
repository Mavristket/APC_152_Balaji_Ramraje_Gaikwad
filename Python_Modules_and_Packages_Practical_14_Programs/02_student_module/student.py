def total_marks(marks): return sum(marks)
def percentage(marks): return total_marks(marks) / len(marks)
def grade(p):
    if p >= 75: return "A"
    elif p >= 60: return "B"
    elif p >= 50: return "C"
    elif p >= 40: return "D"
    else: return "Fail"
