import os; os.chdir(os.path.dirname(os.path.abspath(__file__)))
def strip_comment(line):
    quote = None
    for i, ch in enumerate(line):
        if quote:
            if ch == quote: quote = None
        elif ch in "'\"": quote = ch
        elif ch == "#": return line[:i].rstrip()
    return line.rstrip()
with open("script.py") as src, open("script_no_comments.py", "w") as out:
    for line in src:
        clean = strip_comment(line)
        if clean.strip(): out.write(clean + "\n")
print(open("script_no_comments.py").read())
