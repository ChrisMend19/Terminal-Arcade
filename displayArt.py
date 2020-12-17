import pyfiglet

def welcome():
    ascii_banner = pyfiglet.figlet_format("Welcome to the Terminal Arcade")
    print(ascii_banner)

def welcomeTTT():
    ascii_banner = pyfiglet.figlet_format("Tic-Tac-Toe")
    print(ascii_banner)

def welcomeHM():
    ascii_banner = pyfiglet.figlet_format("Hang Man")
    print(ascii_banner)

def welcomeBJ():
    ascii_banner = pyfiglet.figlet_format("Black Jack")
    print(ascii_banner)

if __name__ == "__main__":
    welcome()