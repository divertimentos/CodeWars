from string import ascii_lowercase
letras = ascii_lowercase[:13]

def printer_error(s):
    bad = 0
    for i in s:
        if i not in letras:
            bad += 1
    return f"{bad}/{len(s)}"
