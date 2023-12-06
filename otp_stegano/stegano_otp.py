# import library stegano
from stegano import lsb

# mengkonversi teks dan key yang di input kedalam ascii
def konversiascii(input_string):
    ascii_values = []
    for char in input_string:
        ascii_value = ord(char)
        ascii_values.append(ascii_value)
    return ascii_values

# mengkonversi teks dan key yang sudah dikonversi kedalam ascii
# kedalam bentuk biner
def konversibiner(ascii_values):
    binary_values = []
    for value in ascii_values:
        binary_value = bin(value)[2:]
        binary_values.append(binary_value)
    return binary_values

# melakukan operasi XOR dari binary key dan binary string
def xor_biner(binary_values_string, binary_values_key):
    result_biner = []
    for i in range(min(len(binary_values_string), len(binary_values_key))):
        result = int(binary_values_string[i], 2) ^ int(binary_values_key[i], 2)
        result_biner.append(bin(result)[2:])
    return result_biner

# mengkonversi hasil XOR kedalam bentuk desimal
def biner_ke_desimal(hasil_xor):
    desimal_values = []
    for value in hasil_xor:
        desimal_value = int(value, 2)
        desimal_values.append(desimal_value)
    return desimal_values

# mengkonversi bentuk desimal kedalam kode ascii
def kodeascii(hasil_desimal):
    karakter_values = ''
    for value in hasil_desimal:
        karakter_value = chr(value)
        karakter_values += karakter_value
    return karakter_values

# menampilkan hasil enkripsi kedalam bentuk karakter
def enkripsi(input_string, key):
    ascii_values_string = konversiascii(input_string)
    ascii_values_key = konversiascii(key)

    hasil_string = konversibiner(ascii_values_string)
    hasil_key = konversibiner(ascii_values_key)

    hasil_xor = xor_biner(hasil_string, hasil_key)

    hasil_desimal = biner_ke_desimal(hasil_xor)

    hasil_karakter = kodeascii(hasil_desimal)

    return hasil_karakter

# function umtuk mendekripsi
def dekripsi(input_string, key):
    return enkripsi(input_string, key)

input_string = input("masukkan plainteks: ")
key = input("masukkan key: ")

encrypted_string = enkripsi(input_string, key)
# print(f"hasil dari enkripsi adalah: {encrypted_string}")

# menggunakan string yang sudah di enkripsi sebagai pesan didalam gambar 
secret = lsb.hide("\Belajar\python\Sc.png", encrypted_string)
secret.save("Sc-sec.png")
print("hasil enkripsi stegano adalah: " + lsb.reveal("Sc-sec.png"))

# Untuk dekripsi pesan yang tersimpan didalam gambar
# hidden_message = lsb.reveal("Sc-sec.png")
# decrypted_string = dekripsi(hidden_message, key)
# print(f"hasil dari dekripsi adalah: {decrypted_string}")