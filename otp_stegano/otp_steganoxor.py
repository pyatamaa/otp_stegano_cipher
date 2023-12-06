from stegano import lsb

def konversi_ascii(input_string):
    ascii_values = list(map(ord, input_string))
    return ascii_values

def konversi_biner(ascii_values):
    binary_values = list(map(lambda x: bin(x)[2:], ascii_values))
    return binary_values

def xor_biner(binary_values_string, binary_values_key):
    result_biner = [bin(int(str1, 2) ^ int(str2, 2))[2:].zfill(8) for str1, str2 in zip(binary_values_string, binary_values_key)]
    return result_biner

def biner_ke_desimal(hasil_xor):
    desimal_values = [int(x, 2) for x in hasil_xor]
    return desimal_values

def kode_ascii(hasil_desimal):
    karakter_values = ''
    for value in hasil_desimal:
        if 32 <= value <= 126:
            karakter_values += chr(value)
        else:
            karakter_values += '?'
    return karakter_values

def enkripsi(input_string, key):
    ascii_values_string = konversi_ascii(input_string)
    ascii_values_key = konversi_ascii(key)

    hasil_string = konversi_biner(ascii_values_string)
    hasil_key = konversi_biner(ascii_values_key)

    hasil_xor = xor_biner(hasil_string, hasil_key)

    hasil_desimal = [int(x, 2) + 32 for x in hasil_xor]

    hasil_karakter = kode_ascii(hasil_desimal)

    return hasil_karakter

def dekripsi(input_string, key):
    ascii_values_string = konversi_ascii(input_string)
    ascii_values_key = konversi_ascii(key)

    hasil_string = konversi_biner(ascii_values_string)
    hasil_key = konversi_biner(ascii_values_key)

    hasil_xor = xor_biner(hasil_string, hasil_key)

    hasil_desimal = [int(x, 2) - 32 for x in hasil_xor]

    hasil_karakter = kode_ascii(hasil_desimal)

    return hasil_karakter

input_string = input("Masukkan plainteks: ")
key = input("Masukkan key: ")

encrypted_string = enkripsi(input_string, key)
secret = lsb.hide("\Belajar\python\Sc.png", encrypted_string)
secret.save("Sc-sec.png")
print("hasil enkripsi stegano adalah: " + lsb.reveal("Sc-sec.png"))
print("Hasil dari enkripsi adalah:", encrypted_string)

# decrypted_string = dekripsi(encrypted_string, key)
# print("Hasil dari dekripsi adalah:", decrypted_string)
