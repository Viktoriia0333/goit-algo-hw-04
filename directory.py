from colorama import Fore, Style
import sys
from pathlib import Path


def output_directory_insides():
    if len(sys.argv) >= 2:
        directory = Path(sys.argv[1])
    else:
        directory = Path()
        print(directory)
    if directory.exists():
        if directory.is_dir():
            print(Fore.LIGHTRED_EX + directory.name)
            for file in directory.rglob('*'):
                level = len(file.relative_to(directory).parts) - 1
                prefix = " " * ((level + 1) * 2) + ("┣ " if file.is_dir() else "┃ ")

                if file.is_dir():
                    print(Fore.BLUE + prefix + file.name + Style.RESET_ALL)
                else:
                    print(Fore.GREEN + prefix + file.name + Style.RESET_ALL)
        else:
            return 'The argument is not a directory'
    else:
        return 'Directory doesn`t exist'


output_directory_insides()