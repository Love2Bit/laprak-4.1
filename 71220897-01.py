def cek_angka(a, b, c):
    if a != b and a != c and b != c:
        if a + b == c or a + c == b or b + c == a:
            return True
        else:
            return False
    else:
        return False