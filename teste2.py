import tkinter as tk
from tkinter import messagebox



#frames que estão "presos" na janela=conteudo,topo,rodapé

def ver_intrucoes():
    frame_conteudo.pack_forget()
    frame_topo.pack_forget()
    frame_intrucoes.pack(fill="both",expand=True)

def aviso_procedimento():
    frame_conteudo.pack_forget()
    frame_topo.pack_forget()
    frame_aviso.pack(fill="both",expand=True)
def voltar_menu():
    frame_intrucoes.pack_forget()
    frame_aviso.pack_forget()
    #Retornando os frames para o menu
    frame_topo.pack(fill="x")
    frame_conteudo.pack(fill="both", expand=True)
def anexar_arquivo():
    pass
def ultima_atualizacao():
    pass
def realizar_operacao():
    pass
    
    

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



titulo = tk.Label(frame_topo,text="🤖 BotWhatsapp HC ",bg="#1A73E8",fg="white",font=("Arial", 24, "bold"))

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


#Relief define como obotão aparecerá(pesquisar estilos de botões)
#cursos="mostrar cursos do mouse se clicar em cima"
botao1 = tk.Button(frame_menu,text="📘 Instruções",bg="white",fg="#1A73E8",font=("Arial", 12),bd=0,relief="flat",anchor="w",padx=20,command=ver_intrucoes,cursor="hand2")
#quando pady tiver dois parâmetros(um é para criar espaços para cima,o outro para baixo)
#anchor="w" serve para alinhar o botão em relação a alguma cordenada geográfica
botao1.pack(fill="x", pady=(20, 10))

botao2 = tk.Button(frame_menu,text="🚀 Enviar Mensagens",bg="white",fg="#1A73E8",font=("Arial", 12),bd=0,relief="flat",anchor="w",padx=20,command=aviso_procedimento,cursor="hand2")

botao2.pack(fill="x", pady=10)

botao3=tk.Button(frame_menu,text="📄Anexar arquivo",bg="white",fg="#1A73E8",font=("Arial", 12),bd=0,relief="flat",anchor="w",padx=20,command=anexar_arquivo,cursor="hand2")
botao3.pack(fill="x", pady=10)

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
frame_rodape = tk.Frame(janela, bg="#ffffff", height=30)
frame_rodape.pack(fill="x", side="bottom")
#side="bottom"=Coloque este widget grudado no final da janela (parte inferior).

texto_rodape = tk.Label(frame_rodape,text="Versão 1.0 • Suporte: contato@123.com",bg="#ffffff",fg="#5f6368",font=("Arial", 10))

texto_rodape.pack(pady=5)



#frame instruções
frame_intrucoes=tk.Frame(janela,bg="#ffffff")


#frame aviso
frame_aviso=tk.Frame(janela,bg="#ffffff")
frame_topoaviso=tk.Frame(frame_aviso,bg="#1A73E8", height=80)
frame_topoaviso.pack(fill="x")
label_aviso=tk.Label(frame_topoaviso,text="⚠ ATENÇÃO",bg="#1A73E8",fg="white",font=("Arial", 24, "bold"))
#bold="negrito"
#pack define onde vai ficar o frame de forma mais humana,grid usa coordenadas para colocar o frame no local exato que deseja
label_aviso.pack(pady=50)
#pady=padding y(espaçamento em y)

label_textoaviso=tk.Label(frame_aviso,
                          text="PARA O BOM FUNCIONAMENTO DESSE PROGRAMA,PRESTE ATENÇÃO:\n" 
                          "\n"
                          "-Deixar a interface do computador trabalhar sozinha\n" \
                          "\n" 
                          "-Não toque no mouse nem no teclado\n" \
                          "\n"
                          "-Deve esperar até o sistema parar totalmente(Parar de enviar mensagens por um tempo maior que 10 seg)\n" \
                          "\n"
                          "-Esse programa trabalha sozinho,não necessita de interferência humana em seu funcionamento\n" \
                          "\n" 
                          "-Certifique-se que as instruções estão sendo seguidas corretamente,pois caso esteja errada,você terá que corrigir manualmente\n" \
                          "\n" 
                          "-É de extrema importância que para o bom funcioamento do programa,o arquivo csv esteja organizado da forma correta\n" \
                          "\n"
                          "-Sistema não funcionará apenas se a forma como o arquivo está organizado(nome dos pacientes,tipo de exame,data e hora do exame) ou\n"
                          "não esteja correto ou tenha algum erro de sintaxe",bg="#ffffff",fg="#202935",font=("Arial",10,"bold"), justify="left", wraplength=600

                          )
# justify="left" usar para deixar o texto a esquerda
# wraplength=600 serve para quebrar linha quando atingir 600 pixels
#NÃO É POSSÍVEL USAR GRID E PACK NO MESMO FRAME(PRECISA ESCOLHER ENTRE UM OU OUTRO) 
#O gerenciador pack() organiza os widgets em uma única direção dentro do mesmo contêiner (ou seja, dentro do mesmo frame)

#pack vai organizando de cima para baixo,sendo necessário criar outro frame para os botões para ser possível coloca-los um do lado do outro


label_textoaviso.pack()
#deixar o pack sem nda,irá colocar o texto no centro

frame_botoes = tk.Frame(frame_aviso, bg="#f5f1f1")
frame_botoes.pack(pady=20)  # centraliza o frame dos botões

botao_voltar =tk.Button(frame_aviso,text="Voltar menu",bg="#ffffff",fg="#1A73E8",font=("Arial", 12),bd=0,relief="flat",anchor="center",padx=20,command=voltar_menu,cursor="hand2")
botao_voltar.pack(side="left", padx=10)

botao_realizar=tk.Button(frame_aviso,text="Iniciar programa",bg="#ffffff",fg="#1A73E8",font=("Arial", 12),bd=0,relief="flat",anchor="center",padx=20,command=voltar_menu,cursor="hand2")
botao_realizar.pack(side="left", padx=10)








janela.mainloop()
