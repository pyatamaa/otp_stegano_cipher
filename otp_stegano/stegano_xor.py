from stegano import lsb

def encrypt_xor(message, key):
    message = message.upper()
    key = key.upper()

    if len(message) != len(key):
        print("<p class='mt-3 alert alert-danger'>Panjang kunci harus sama dengan teks.</p>")
        return

    encrypted_text = ''

    for i in range(len(message)):
        if message[i].isalpha():
            message_char = ord(message[i]) - ord('A')
            key_char = ord(key[i]) - ord('A')

            # Menggunakan operasi XOR
            encrypted_char = message_char ^ key_char
            encrypted_text += chr(encrypted_char + ord('A'))
        else:
            encrypted_text += message[i]

    return encrypted_text

def decrypt_xor(encrypted_text, key):
    encrypted_text = encrypted_text.upper()
    key = key.upper()

    if len(encrypted_text) != len(key):
        print("<p class='mt-3 alert alert-danger'>Panjang kunci harus sama dengan teks.</p>")
        return

    decrypted_text = ''

    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            encrypted_char = ord(encrypted_text[i]) - ord('A')
            key_char = ord(key[i]) - ord('A')

            # Menggunakan operasi XOR untuk dekripsi
            decrypted_char = encrypted_char ^ key_char
            decrypted_text += chr(decrypted_char + ord('A'))
        else:
            decrypted_text += encrypted_text[i]

    return decrypted_text

# Input plaintext dan key
plaintext = input("Masukkan plaintext: ")
key = input("Masukkan key: ")

# Enkripsi
encrypted_result = encrypt_xor(plaintext, key)
# print("Hasil enkripsi:", encrypted_result)

# Use the encrypted string as the secret message in the image
secret = lsb.hide("\Belajar\python\Sc.png", encrypted_result)
secret.save("Sc-sec.png")

print("hasil enkripsi stegano adalah: " + lsb.reveal("Sc-sec.png"))

# Decrypt the message hidden in the image
hidden_message = lsb.reveal("Sc-sec.png")
decrypted_string = decrypt_xor(hidden_message, key)
print("Teks terdekripsi didalam gambar:", decrypted_string)

# Dekripsi
# decrypted_result = decrypt_xor(encrypted_result, key)
# print("Hasil dekripsi:", decrypted_result)
