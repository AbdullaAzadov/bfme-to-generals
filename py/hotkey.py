import keyboard as k
import subprocess

GAME = 'game.dat'
GAME_PATH = r"E:\The Battle for Middle-Earth 2\The Rise of the Witch-king\lotrbfme2ep1.exe"
BAKE_ASSETS_FILE_PATH = r"C:\Users\113\Desktop\mod"
BAKE_ASSETS_FILE_NAME = "makeasset.bat"


def run_game():
    close_game()
    try:
        subprocess.Popen([GAME_PATH], shell=True)
    except:
        pass

def close_game():
    try:
        subprocess.run(['taskkill', '/F', '/IM', GAME], check=True)
    except:
        pass

def bake_assets():
    try:
        subprocess.Popen(['start', 'cmd', '/c', f'cd /d {BAKE_ASSETS_FILE_PATH} && {BAKE_ASSETS_FILE_NAME}'], shell=True)
    except:
        pass

def main():
    # Настраиваем обработчик для клавиши '='
    k.add_hotkey('ctrl + 1', run_game)
    k.add_hotkey('ctrl + 2', close_game)
    k.add_hotkey('ctrl + 3', bake_assets)
    
    # Ждем, пока пользователь не нажмет клавишу 'q' для выхода
    k.wait('shift + /')

if __name__ == "__main__":
    main()

