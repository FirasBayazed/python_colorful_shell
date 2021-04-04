import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)

# https://www.ppaste.org/

print(Fore.BLUE + Back.YELLOW+"Erste Zeile in blau auf gelb")
print(Back.BLACK + "Zweite Zeile auf schwarz")
print(Fore.GREEN + "Dritte Zeile in grün")
print(Fore.RED + "let's go")
print(Fore.CYAN + "nice")