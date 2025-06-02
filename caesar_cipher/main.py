# main.py

from cipher import encrypt, decrypt

def menu():
    print("=== Caesar Cipher ===")
    print("1. Enkripsi")
    print("2. Dekripsi")
    print("3. Keluar")

def get_key():
    while True:
        try:
            key = int(input("Masukkan kunci (1-25): "))
            if 1 <= key <= 25:
                return key
            else:
                print("Kunci harus antara 1 hingga 25.")
        except ValueError:
            print("Input tidak valid. Masukkan angka.")

def main():
    while True:
        menu()
        choice = input("Pilih menu (1/2/3): ")

        if choice == "1":
            text = input("Masukkan teks yang ingin dienkripsi: ")
            key = get_key()
            encrypted = encrypt(text, key)
            print("Hasil Enkripsi:", encrypted)

        elif choice == "2":
            text = input("Masukkan teks yang ingin didekripsi: ")
            key = get_key()
            decrypted = decrypt(text, key)
            print("Hasil Dekripsi:", decrypted)

        elif choice == "3":
            print("Terima kasih telah menggunakan program ini.")
            break

        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

if __name__ == "__main__":
    main()
