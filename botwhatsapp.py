import pyautogui
import time
from datetime import timedelta,datetime
import pandas as pd
import tkinter as tk
from tkinter import Label, Button



def ver_intrucoes():
    pass

def aviso_procedimento():
    pass

def fazer_procedimento():
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

# Criação da janela principal
janela = tk.Tk()
janela.title("BotWhatsapp HC") #definindo título
janela.geometry("600x600+500+200")#definindo tamanho e onde ficará a  janela
janela.config(bg="white")
janela.resizable(False, False)

#  Criação do Frame de início
frame_inicio = tk.Frame(janela, bg="white")
texto_principal=Label(frame_inicio,text="Bem vindo ao sistema de automação do HC",bg="white",fg="blue",font=("Arial",16))
texto_principal.grid(column=0, row=0, pady=(0, 40))

mostrar_opcao=Label(frame_inicio,text="Aperte na opção que você deseja",bg="white",fg="blue",font=("Arial",16))
texto_principal.grid(column=0, row=2, pady=(0, 40))


texto_aviso=Label(frame_inicio,text="Antes de fazer procedimento,tenha certeza que está seguindo todas as intruções",bg="white",fg="blue",font="Arial,16")
texto_aviso.grid(column=0, row=3, pady=10)
texto_opcao1 = Button(frame_inicio, text="OPÇÃO 1 (🔍 Ver instruções)", fg="white", bg="#1A73E8",font=("Arial", 16), command=ver_intrucoes)
texto_opcao1.grid(column=0, row=5, pady=10)

texto_opcao2 = Button(frame_inicio, text="OPÇÃO 2 (Enviar mensagens)", fg="blue", bg="white",font=("Arial",16), command=aviso_procedimento)
texto_opcao2.grid(column=0, row=6, pady=10)








#  Mostra o frame na janela principal
frame_inicio.pack(fill="both", expand=True)






# Loop principal da aplicação
janela.mainloop()
