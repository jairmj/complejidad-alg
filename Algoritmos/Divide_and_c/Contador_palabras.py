def wc(lines, i, j):
    if i == j:
        return len(lines[i].strip().split(" "))
    med = (i + j) // 2
    return wc(lines, i, med) + wc(lines, med + 1, j)

def wordCount(text):
    lines = text.strip().split("\n")
    return wc(lines, 0, len(lines) - 1)
#45 palabras
texto = """ 
At quaeque adversarium ius, sed at integre persius verterem.
Sit summo tibique at, eam et fugit complectitur, vis te natum vivendum mandamus.
Iudico quodsi cum ad, dicit everti sensibus in sea, ea eius paulo deterruisset pri.
Pro id aliquam hendrerit definitiones. Per et legimus delectus.
"""

print(wordCount(texto))