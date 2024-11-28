from colorama import Fore
import sys
from pathlib import Path


def output_directory_insides():
    if len(sys.argv) >= 2:
        directory = Path(sys.argv[1])
    else:
        directory = Path()
    if directory.exists():
        if directory.is_dir():
            print(Fore.LIGHTRED_EX + directory.name)
            ident = 2
            for file in directory.iterdir():
                print(Fore.YELLOW + '-' * ident + file.name + Fore.RESET)
        else:
            return 'The argument is not a directory'
    else:
        return 'Directory doesn`t exist'

