from termcolor import colored

def greska(poruka):
    print(colored(poruka, "red"))
    raise poruka

