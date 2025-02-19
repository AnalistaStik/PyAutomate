import pyautogui
import subprocess
import time
import pyperclip 
import logging
import pygetwindow as gw
from datetime import datetime

# Configurações do logging 
logging.basicConfig(
    filename=r"C://Rb_Lupo//PyAutomate//logs//log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Tempos de espera
time_login = 20
time_short = 1
time_medium = 3
time_long = 12

# Posições dos elementos na tela       
coordenadas = {
    "Consulta": (218, 32),
    "Doc. Eletronico": (252, 56),
    "Doc_Eletronico": (494, 51),
    "Filtro": (210, 77),
    "periodo": (279, 91),
    "Empresa": (452, 90),
    "Maximizar Doc. Eletronico": (679, 86),
    "N. Pedido Base": (706, 127),
    "Pos. Acrobat": (104, 41),
    "Fechar Janela": (1894, 15),
    "Fechar_janela_navegador": (1893, 19)
}

logging.info("Programa Iniciado")

pyautogui.confirm(
    text='O programa será iniciado. Clique em OK para continuar.', 
    title='Programa Inicializado', 
    buttons=['OK']
)

#Função que preenche um campo de texto
def preencher_campo(texto):
    pyautogui.press("backspace")
    pyautogui.write(texto)
    
#Função para maximizar uma janela específica ou clicar no botão de maximizar
def maximizar_janela(titulo_parcial, coordenada_maximizar=None):
    try:
        time.sleep(time_short)
        janelas = gw.getWindowsWithTitle(titulo_parcial)
        if janelas:
            janela = janelas[0]
            if not janela.isMaximized:
                janela.maximize()
            logging.info(f"Janela '{titulo_parcial}' maximizada.")
        elif coordenada_maximizar:
            pyautogui.moveTo(coordenada_maximizar)
            pyautogui.click()
            logging.info(f"Maximização via coordenada: {coordenada_maximizar}")
        time.sleep(time_short)
    except Exception as e:
        logging.error(f"Erro ao maximizar a janela {titulo_parcial}: {e}")
        
# --- Função que baixa o XML ---
def baixar_XML():
    try:
        time.sleep(time_short)
        pyautogui.press("F8")
        time.sleep(time_short)

        pyautogui.moveTo(845, 585)
        pyautogui.click()
        time.sleep(time_short)
        
        pyautogui.moveTo(903, 460)
        pyautogui.click()
        time.sleep(time_short)

        for _ in range(34):
            pyautogui.press("down")
            time.sleep(0.2)

        pyautogui.press("enter")
        time.sleep(time_short)
        logging.info("XML baixado com sucesso.")

    except Exception as e:
        logging.error(f"Erro ao baixar XML: {e}")
        
#Função que baixa o PDF
def baixar_pedido(pedido_x, pedido_y):
    try:
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

        pyautogui.moveTo(90, 202)  
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
        logging.info("PDF baixado com sucesso.")

    except Exception as e:
        logging.error(f"Erro ao baixar PDF: {e}")
    
def programar_automatizacao():
    while True:
        agora = datetime.now()
        hora_hoje = datetime(agora.year, agora.month, agora.day, 15, 11)
        # Se o horário chegou, sai do loop e continua o processo
        if agora >= hora_hoje:
            print("Hora de começar o processo de automação!")
            break
        else:
            # Espera 10 segundos antes de checar novamente
            time.sleep(10)

programar_automatizacao()
            
#Entrar e logar no TopManager
for _ in range(3):
    try:
        time.sleep(time_medium)
        pyautogui.hotkey("ctrl", "shift", "t")
        time.sleep(time_medium)

        time.sleep(time_short)
        pyautogui.moveTo(398, 346)
        time.sleep(time_short)
        pyautogui.click()
        preencher_campo("123456")
        pyautogui.press("enter")
        time.sleep(time_login)

        if gw.getWindowsWithTitle("TopManager"):
            logging.info("Login no TopManager realizado com sucesso.")
            maximizar_janela("TopManager")
            break
    except Exception as e:
        logging.error(f"Erro no login: {e}")

#Acessar a aba dos Documentos Eletrônicos
try:
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
    pyautogui.click()
    time.sleep(time_short)
    pyautogui.click(button='left')
    time.sleep(time_short)
    pyautogui.moveTo(274, 212)
    time.sleep(time_short)
    pyautogui.click()
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
    logging.info("Acesso à aba de documentos eletrônicos.")

except Exception as e:
    logging.error(f"Erro ao acessar aba de documentos eletrônicos: {e}")

# Aba dos pedidos e download dos PDF's e XML

# Configurações
pedido_x, pedido_y = coordenadas["N. Pedido Base"]
incremento_y = 18  # Distância entre as linhas dos pedidos
deslocamento_x = 100  # Ajuste lateral para clicar na opção "Abrir Pedido"
deslocamento_y = 10   # Pequeno ajuste vertical se necessário
numero_pedidos = 0
pedido_anterior = None  # Variável para armazenar o pedido anterior

while True:
    try:
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

        logging.info(f"Baixando pedido: {pedido_atual}")
        numero_pedidos += 1

        baixar_XML()
        baixar_pedido(pedido_x, pedido_y)

        pedido_anterior = pedido_atual
        pedido_y += incremento_y

    except Exception as e:
        logging.error(f"Erro no processo de download: {e}")

logging.info(f"Total de pedidos baixados: {numero_pedidos}")

time.sleep(time_medium)  
pyautogui.moveTo(1895, 10)
pyautogui.click()

time.sleep(time_medium)
pyautogui.alert(
    text=f"Total de pedidos baixados: {numero_pedidos}", 
    title="Processo Concluído", 
    button="OK"
)
