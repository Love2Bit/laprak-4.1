def cek_digit_belakang(a, b, c):
    # Ambil digit terakhir dari setiap bilangan menggunakan modulo 10
    a_digit = a % 10
    b_digit = b % 10
    c_digit = c % 10

    # Periksa apakah minimal dua digit terakhir sama
    if a_digit == b_digit or a_digit == c_digit or b_digit == c_digit:
        return True
    else:
        return False
