import pyautogui
import subprocess
import time
import pyperclip 
import logging
import pygetwindow as gw
from datetime import datetime
import tkinter as tk
from tkinter import messagebox

# Posições dos elementos na tela       
coordenadas = {
    "Consulta": (218, 32),
    "Doc. Eletronico": (252, 56),
    "Doc_Eletronico": (494, 51),
    "Filtro": (210, 77),
    "periodo": (255, 91),
    "Empresa": (452, 90),
    "Maximizar Doc. Eletronico": (679, 86),
    "N. Pedido Base": (706, 127),
    "Pos. Acrobat": (104, 41),
    "Fechar Janela": (1894, 15),
    "Fechar_janela_navegador": (1893, 19)
}

# Tempos de espera
time_short = 1
time_medium = 3
time_long = 5

def start_countdown(seconds):
    root = tk.Tk()
    root.title("Contagem Regressiva")
    root.attributes("-topmost", True)
    label = tk.Label(root, font=("Helvetica", 20), padx=20, pady=20)
    label.pack()

    def update():
        nonlocal seconds
        if seconds >= 0:
            hours, remainder = divmod(seconds, 3600)
            mins, secs = divmod(remainder, 60)
            timer = '{:02d}:{:02d}:{:02d}'.format(hours, mins, secs)
            label.config(text=f"Tempo restante: {timer}")
            seconds -= 1
            # Atualiza a cada 1 segundo
            root.after(1000, update)
        else:
            root.destroy()
    update()
    root.mainloop()

def programar_automatizacao():
    agora = datetime.now()
    hora_hoje = datetime(agora.year, agora.month, agora.day, 23, 50)
    
    # Calcular o tempo restante até as 23:50
    tempo_restante = (hora_hoje - agora).total_seconds()
    
    if tempo_restante > 0:
        print(f"Aguardando {int(tempo_restante)} segundos até as 23:50...")
        start_countdown(int(tempo_restante))

programar_automatizacao()

# --- Função que preenche um campo de texto ---
def preencher_campo(texto):
    pyautogui.press("backspace")
    pyautogui.write(texto)
    
# --- Função para maximizar uma janela específica ou clicar no botão de maximizar ---
def maximizar_janela(titulo_parcial, coordenada_maximizar=None):
    time.sleep(time_short)
    janelas = gw.getWindowsWithTitle(titulo_parcial)
    if janelas:
        janela = janelas[0]
        if not janela.isMaximized:
            janela.maximize()
        time.sleep(time_short)
    elif coordenada_maximizar:
        pyautogui.moveTo(coordenada_maximizar)
        pyautogui.click()
        time.sleep(time_short)

# --- Função que baixa o XML ---
def baixar_XML():
    time.sleep(time_short)
    pyautogui.click(button="right")
    time.sleep(time_short)
    
    for _ in range(6):  
        pyautogui.press("down")
        time.sleep(0.2)

    pyautogui.press("enter")  
    time.sleep(time_short)

    pyautogui.moveTo(845, 585)
    pyautogui.click()
    time.sleep(time_short)
    
    pyautogui.moveTo(903, 460)
    pyautogui.click()
    time.sleep(time_short)

    for _ in range(29):
        pyautogui.press("down")
        time.sleep(0.2)

    pyautogui.press("enter")
    time.sleep(time_short) 
        
# --- Função que baixa o PDF ---
def baixar_pedido(pedido_x, pedido_y):
    time.sleep(time_short)
    pyautogui.click(button="right")  # Clicar com botão direito no pedido atual
    time.sleep(time_short)

    for _ in range(11):
        pyautogui.press("down")
        time.sleep(0.2)  

    pyautogui.press("enter")  
    time.sleep(time_long)

    pyautogui.moveTo(coordenadas['Pos. Acrobat'])
    pyautogui.click()
    time.sleep(time_long)

    # Salvar PDF
    pyautogui.moveTo(1797, 126)  
    pyautogui.click()
    time.sleep(time_long)

    pyautogui.moveTo(99, 240)  
    pyautogui.click()
    time.sleep(time_long)

    pyautogui.moveTo(791, 507)  
    pyautogui.click()
    time.sleep(time_long)

    pyautogui.moveTo(coordenadas['Fechar_janela_navegador'])
    pyautogui.click()
    time.sleep(time_long)
    pyautogui.moveTo(coordenadas['Fechar Janela'])
    pyautogui.click()
    time.sleep(time_long) 
            
# --- Entrar e logar no TopManager ---
time.sleep(time_short)
pyautogui.hotkey("ctrl", "shift", "t")
time.sleep(time_medium)

pyautogui.moveTo(398, 346)
time.sleep(time_short)
pyautogui.click()
preencher_campo("123456")
pyautogui.press("enter")
time.sleep(20)

maximizar_janela("TopManager")

# --- Acessar a aba dos Documentos Eletrônicos ---
pyautogui.moveTo(coordenadas['Consulta'])
pyautogui.click()
time.sleep(time_short)

pyautogui.moveTo(coordenadas['Doc. Eletronico'])
pyautogui.click()
time.sleep(time_short)

pyautogui.moveTo(coordenadas['Doc_Eletronico'])
pyautogui.click()
time.sleep(time_short)

maximizar_janela('Doc. Eletronico', coordenadas["Maximizar Doc. Eletronico"])
time.sleep(time_short)

pyautogui.moveTo(coordenadas['Filtro'])
pyautogui.click()
time.sleep(time_short)

pyautogui.moveTo(coordenadas['periodo'])
pyautogui.click(button='left')
time.sleep(time_short)
pyautogui.write('o')
time.sleep(time_short)
pyautogui.press("tab")
time.sleep(time_short)
pyautogui.press("tab")
time.sleep(time_short)
preencher_campo('2')
time.sleep(time_short)
pyautogui.press('tab')
time.sleep(time_short)
pyautogui.press('tab')
time.sleep(time_short)
pyautogui.press('tab')
time.sleep(time_short)

pyautogui.press('enter')
time.sleep(time_medium)
preencher_campo('lupo')
time.sleep(time_short)
pyautogui.press('enter')
time.sleep(time_short)
pyautogui.press('enter')
time.sleep(time_short)
pyautogui.press('enter')
time.sleep(time_short)

pyautogui.press('F5')
time.sleep(time_long)

# --- Aba dos pedidos e download dos PDF's e XML ---

# Configurações
pedido_x, pedido_y = coordenadas["N. Pedido Base"]
incremento_y = 18  # Distância entre as linhas dos pedidos
numero_pedidos = 0
pedido_anterior = None  # Variável para armazenar o pedido anterior

while True:
    # Selecionar a célula do pedido atual
    pyautogui.moveTo(pedido_x, pedido_y)
    pyautogui.click()
    time.sleep(time_short)

    # Copiar o conteúdo
    pyautogui.hotkey("ctrl", "c")
    time.sleep(time_short)
    pedido_atual = pyperclip.paste().strip()

    # Verificar se a célula está vazia (último pedido atingido)
    if not pedido_atual:
        print("Nenhum pedido encontrado ou fim da lista.")
        break

    # Verificar se o pedido atual é o mesmo que o anterior
    if pedido_atual == pedido_anterior:
        print("Pedido repetido, encerrando a busca")
        pedido_y += incremento_y  # Pular para a próxima linha
        break

    print(f"Pedido encontrado: {pedido_atual}")
    numero_pedidos += 1

    # Baixar o XML
    baixar_XML()

    # Baixar o PDF
    baixar_pedido(pedido_x, pedido_y)

    # Atualizar o pedido anterior
    pedido_anterior = pedido_atual

    # Mover para a próxima linha
    pedido_y += incremento_y

print(f"Total de pedidos baixados: {numero_pedidos}")

time.sleep(time_medium)  
pyautogui.moveTo(1895, 10)
pyautogui.click()

# --- Notifica o usuário com um pop-up ao final do processo ---
pyautogui.alert(text=f"Total de pedidos baixados: {numero_pedidos}", 
                title="Processo Concluído", 
                button="OK")
