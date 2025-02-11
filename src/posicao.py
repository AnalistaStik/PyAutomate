import pyautogui
import time
import keyboard
def capturar_posicao():
    print("Mova o mouse para o local desejado e pressione ENTER.")
    while True:
        if keyboard.is_pressed('enter'):  # Verifica se a tecla ENTER foi pressionada
            posicao = pyautogui.position()  # Captura a posição do mouse
            print(f"A posição do mouse é: {posicao}")
            return posicao  # Retorna a posição
        time.sleep(0.1)  # Aguardar um pouco antes de verificar novamente

capturar_posicao()