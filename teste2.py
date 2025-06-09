import tkinter as tk
from tkinter import messagebox



#frames que estão "presos" na janela=conteudo,topo,rodapé

def ver_intrucoes():
    frame_conteudo.pack_forget()
    frame_topo.pack_forget()
    frame_intrucoes.pack(fill="both",expand=True)

def aviso_procedimento():
    messagebox.showinfo("Aviso", "Certifique-se de que todos os dados estão preenchidos corretamente antes de prosseguir.")

# Configuração da janela principal
janela = tk.Tk()
janela.title("BotWhatsapp ")
janela.geometry("800x600+400+150")
janela.config(bg="#f0f2f5")
janela.resizable(False, False)

#Criasse um frame apenas para parte do cabeçalho do topo 

frame_topo = tk.Frame(janela, bg="#1A73E8", height=80)
#pack(fill="x") faz o cabeçalho (topo) ocupar toda a largura da janela (eixo X), mas apenas a altura necessária para o conteúdo.
frame_topo.pack(fill="x")



titulo = tk.Label(frame_topo,text="🤖 BotWhatsapp ",bg="#1A73E8",fg="white",font=("Arial", 24, "bold"))

titulo.pack(pady=20)


# Divisão em colunas principais (menu lateral e conteúdo)
#Esse frame serve apenas para ser base para outros frames
frame_conteudo = tk.Frame(janela, bg="#f0f2f5")
frame_conteudo.pack(fill="both", expand=True)



# Menu lateral,preencherá apenas a parte em relação ao eixo y
#preencherá apenas a parte esqueda da tela em relação ao eixo y 
#width=200 serve para indicar quantos pixels o frame deverá usar na largura
frame_menu = tk.Frame(frame_conteudo, bg="white", width=200)
#caso não use o fill,o frame ocupará apenas o espcaço necessário para o conteúdo
frame_menu.pack(side="left", fill="y")

botao1 = tk.Button(frame_menu,text="📘 Instruções",bg="white",fg="#1A73E8",font=("Arial", 12),bd=0,relief="flat",anchor="w",padx=20,command=ver_intrucoes,cursor="hand2")
botao1.pack(fill="x", pady=(20, 10))

botao2 = tk.Button(frame_menu,text="🚀 Enviar Mensagens",bg="white",fg="#1A73E8",font=("Arial", 12),bd=0,relief="flat",anchor="w",padx=20,command=aviso_procedimento,cursor="hand2")

botao2.pack(fill="x", pady=10)

# Area principal de conteúdo
#padx=30, pady=30 serve para criar espaços em relação ao frame
frame_principal = tk.Frame(frame_conteudo, bg="#ffffff", padx=30, pady=30)
frame_principal.pack(side="left", fill="both", expand=True)

texto_bem_vindo = tk.Label(frame_principal,text="Bem-vindo ao sistema de automação ",bg="white",fg="#202124",font=("Arial", 18, "bold"))
texto_bem_vindo.pack(pady=(0, 20))

texto_instrucao = tk.Label(frame_principal,text="Antes de iniciar, leia atentamente as instruções para garantir o correto funcionamento do sistema.",bg="white",fg="#5f6368",wraplength=500,justify="left",font=("Arial", 12))
texto_instrucao.pack()
#usando apenas o pack,o texto será colocado em qualquer lugar

#Criando frame do rodapé
#height=100 é usado para definir a altura do frame
frame_rodape = tk.Frame(janela, bg="#e8eaed", height=30)
frame_rodape.pack(fill="x", side="bottom")
#side="bottom"=Coloque este widget grudado no final da janela (parte inferior).

texto_rodape = tk.Label(frame_rodape,text="Versão 1.0 • Suporte: contato@123.com",bg="#e8eaed",fg="#5f6368",font=("Arial", 10))

texto_rodape.pack(pady=5)



#frame instruções
frame_intrucoes=tk.Frame(janela,bg="#ffffff")







janela.mainloop()
