from stegano import lsb

def encrypt_modulo26(message, key):
    message = message.upper()
    key = key.upper()

    if len(message) != len(key):
        raise ValueError("Panjang kunci harus sama dengan teks.")

    encrypted_text = ''

    for i in range(len(message)):
        if message[i].isalpha():
            message_char = ord(message[i]) - ord('A')
            key_char = ord(key[i]) - ord('A')

            # Menggunakan perhitungan modulo 26
            encrypted_char = (message_char + key_char) % 26
            encrypted_text += chr(encrypted_char + ord('A'))
        else:
            encrypted_text += message[i]

    return encrypted_text


def decrypt_modulo26(encrypted_text, key):
    encrypted_text = encrypted_text.upper()
    key = key.upper()

    if len(encrypted_text) != len(key):
        raise ValueError("Panjang kunci harus sama dengan teks.")

    decrypted_text = ''

    for i in range(len(encrypted_text)):
        if encrypted_text[i].isalpha():
            encrypted_char = ord(encrypted_text[i]) - ord('A')
            key_char = ord(key[i]) - ord('A')

            # Menggunakan perhitungan modulo 26 untuk dekripsi
            decrypted_char = (encrypted_char - key_char + 26) % 26
            decrypted_text += chr(decrypted_char + ord('A'))
        else:
            decrypted_text += encrypted_text[i]

    return decrypted_text


def main():
    # Input teks dan kunci
    text = input("Masukkan teks: ")
    key = input("Masukkan kunci: ")

    # Enkripsi
    encrypted_result = encrypt_modulo26(text, key)
    print("Teks terenkripsi:", encrypted_result)

    # Use the encrypted string as the secret message in the image
    secret = lsb.hide("\Belajar\python\Sc.png", encrypted_result)
    secret.save("Sc-sec.png")

    # Decrypt the message hidden in the image
    hidden_message = lsb.reveal("Sc-sec.png")
    decrypted_string = decrypt_modulo26(hidden_message, key)
    print("Teks terdekripsi:", decrypted_string)


if __name__ == "__main__":
    main()
