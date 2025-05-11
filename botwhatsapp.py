import pyautogui
import time
from datetime import timedelta,datetime
import pandas as pd


tabela=pd.read_csv("botwhatsapp.csv") #abre o arquivo csv excluindo a linha do cabeçalho

# Data atual (data do sistema)
data_hoje = datetime.now().date()

pyautogui.press("win")
time.sleep(0.5)
pyautogui.write("Whatsapp")
time.sleep(1)
pyautogui.press("Enter")
time.sleep(3)


for linha in tabela.index:

    # .loc[] é um método que permite acessar valores específicos no DataFrame.
    #"Acesse o valor da coluna 'nome' na linha com índice linha."
    nome = tabela.loc[linha, "nome"]

    procedimento = tabela.loc[linha, "procedimento"]

    data_consulta_str = tabela.loc[linha, "data_consulta_str"]

    hora_consulta=tabela.loc[linha,"horario"]


    #convertendo a string em data normal
    data_consulta=datetime.strptime(data_consulta_str, "%d/%m/%Y").date()



    # Verifica se a data da consulta - 1 dia == hoje
    if data_consulta - timedelta(days=1) == data_hoje:
        pyautogui.click(189, 115)

        # Procurando pelo nome do contato
        pyautogui.write(nome)
        time.sleep(1)
        pyautogui.click(222, 159)
        time.sleep(1)
        pyautogui.click(937, 1017)
        time.sleep(1)

        #ESSA AQUI SERIA A MENSAGEM PADRÃO ENVIADA PARA TODOS OS PACIENTES
        import pyperclip
        #pyautogui não funciona bem com acentos,então a melhor opção seria copiar e colar diretamente a mensagem


        # ESSA AQUI SERIA A MENSAGEM PADRÃO ENVIADA PARA TODOS OS PACIENTES
        mensagem = (
            f"(mensagem automática) Bom dia {nome}. "
            f"Passando apenas para lembrar que você tem um procedimento ({procedimento}), "
            f" amanhã ({data_consulta}) às {hora_consulta}. "
            f"Caso tenha algum imprevisto, peço o aviso prévio. Tenha um bom dia!!"
        )

        pyperclip.copy(mensagem)  # Copia com todos os acentos certinho
        pyautogui.hotkey('ctrl', 'v')  # Cola no WhatsApp


        pyautogui.press("enter")
        time.sleep(2)

#for linha in tabela.index:#para cada linha da tabela
   # pyautogui.click(856, 265)

    #Dessa forma os valores serão definidos a partir do loop de cada linha em relação ao tipo de dado
    #de cada coluna
    #codigo =tabela.loc[linha,"codigo"]
   # marca = tabela.loc[linha,"marca"]
    #tipo = tabela.loc[linha,"tipo"]
    #categoria = str(tabela.loc[linha,"categoria"]) #usar str para transforma int/float em str
    #preco_unitario = str(tabela.loc[linha,"preco_unitario"])
    #custo = str(tabela.loc[linha,"custo"])
    #obs = str(tabela.loc[linha,"obs"])