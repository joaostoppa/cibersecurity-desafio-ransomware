import os
import pyaes

def descriptografar_arquivo(file_name, key):
    if not os.path.exists(file_name):
        print(f"Erro: Arquivo '{file_name}' não encontrado.")
        return

    try:
        with open(file_name, "rb") as file:
            file_data = file.read()

        os.remove(file_name)

        aes = pyaes.AESModeOfOperationCTR(key.encode())
        decrypt_data = aes.decrypt(file_data)

        original_file = file_name.replace(".ransomwaretroll", "")
        with open(original_file, "wb") as file:
            file.write(decrypt_data)

        print(f"Arquivo '{original_file}' descriptografado com sucesso.")
    except Exception as e:
        print(f"Erro ao descriptografar o arquivo: {e}")

if __name__ == "__main__":
    file_name = input("Digite o nome do arquivo para descriptografar: ")
    key = input("Digite a chave de 16 caracteres: ")
    descriptografar_arquivo(file_name, key)
