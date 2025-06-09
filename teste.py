
import tkinter as tk
from tkinter import Label, Button



def ver_intrucoes():
    pass

def aviso_procedimento():
    pass

def fazer_procedimento():
    pass

# Criação da janela principal
janela = tk.Tk()
janela.title("BotWhatsapp HC") #definindo título
janela.geometry("600x600+500+200")#definindo tamanho e onde ficará a  janela
janela.config(bg="white")
janela.resizable(False, False)

#  Criação do Frame de início
frame_inicio = tk.Frame(janela, bg="white")
texto_principal=Label(frame_inicio,text="Bem vindo ao sistema de automação do HC",bg="#1A73E8",fg="white",font=("Arial",16))
texto_principal.grid(column=0, row=0, pady=(0, 40))

mostrar_opcao=Label(frame_inicio,text="Aperte na opção que você deseja",bg="white",fg="blue",font=("Arial",16))
mostrar_opcao.grid(column=0, row=2, pady=(0, 40))


texto_aviso=Label(frame_inicio,text="Antes de fazer procedimento,tenha certeza que está seguindo todas as intruções",bg="white",fg="blue",font="Arial,16")
texto_aviso.grid(column=0, row=3, pady=10)
texto_opcao1 = Button(frame_inicio, text="OPÇÃO 1 (🔍 Ver instruções)", fg="white", bg="#1A73E8",font=("Arial", 16), command=ver_intrucoes)
texto_opcao1.grid(column=0, row=5, pady=10)

texto_opcao2 = Button(frame_inicio, text="OPÇÃO 2 (Enviar mensagens)", fg="white", bg="#1A73E8",font=("Arial",16), command=aviso_procedimento)
texto_opcao2.grid(column=0, row=6, pady=10)








#  Mostra o frame na janela principal
frame_inicio.pack(fill="both", expand=True)






# Loop principal da aplicação
janela.mainloop()
