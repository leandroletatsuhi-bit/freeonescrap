import os
import glob

# Mensagem informativa antes da entrada do usuário
print()
print("\nNão se esqueça de conferir a quantidade de páginas para coletar em:")
print("https://www.freeones.com/")  # URL base para conferência da quantidade de páginas
print()

def count_json_files(folder_path):
    """Conta o número de arquivos JSON em uma pasta."""
    json_files = glob.glob(os.path.join(folder_path, '*.json'))
    return len(json_files)

def run_scripts_in_order():
    # Arquivos a serem executados em ordem
    file_paths = ["1-babes.py", "2-urls.py", "3-atrizes.py"]


    # Contar arquivos JSON na pasta "atrizes"
    atrizes_folder = "atrizes"
    if os.path.exists(atrizes_folder) and os.path.isdir(atrizes_folder):
        num_atrizes = count_json_files(atrizes_folder)
        print(f"\nJá temos {num_atrizes} atrizes coletadas.")
        print()

    # Mostrar opções para o usuário escolher
    print("\nEscolha qual script deseja rodar:")
    for i, filepath in enumerate(file_paths, 1):
        print(f"{i}. {os.path.basename(filepath)}")

    # Solicitar a escolha do usuário
    while True:
        choice = input("\nDigite o número correspondente ao script que deseja rodar (ou '0' para rodar todos): ")
        if choice.isdigit():
            index = int(choice) - 1  # Converter para índice (0-based)
            if index == -1:
                for filepath in file_paths:
                    if os.path.exists(filepath):  # Verifica se o arquivo existe
                        os.system(f"python {filepath}")  # Executa o arquivo usando Python
                break  # Sai do loop após executar todos os scripts
            elif 0 <= index < len(file_paths):
                target_script = file_paths[index]
                if os.path.exists(target_script):  # Verifica se o arquivo existe
                    os.system(f"python {target_script}")  # Executa o script escolhido
                break  # Sai do loop após executar o script escolhido
            else:
                print("Escolha inválida. Digite um número válido ou '0'.")
        else:
            print("Escolha inválida. Digite um número válido ou '0'.")

if __name__ == "__main__":
    run_scripts_in_order()
