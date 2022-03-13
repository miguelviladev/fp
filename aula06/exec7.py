import os, sys

# Poderão existir incompatibilidades no que toca ao formato dos paths dependendo do sistema operativo que se use. (no meu caso uso linux)

# Este script exige que se passe um argumento quando se interpreta o mesmo. Assim deve-se executálo desta forma: "python3 exec7.py caminho_do_diretorio"

def main():
    try:
        dir_list = os.listdir(sys.argv[1])
        print(f'{"FILE":30s}{"SIZE":15s}')
        for elm in dir_list:
            full_path = f"{sys.argv[1]}/{elm}"
            if os.path.isfile(full_path):
                print(f"{elm:30s}{os.stat(full_path).st_size:<15d}")
    except FileNotFoundError:
        print("ERROR: Invalid path!")

main()