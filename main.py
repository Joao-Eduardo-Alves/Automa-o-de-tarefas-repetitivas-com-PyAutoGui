
# Passo 1: Entrar no sistema

import pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar 
# pyautogui.hotkey -> combinação de teclas

pyautogui.PAUSE = 0.3 # -> define um tempo de espera entre cada ação executada pelo pyautogui

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(3) # -> define um tempo de espera de 3 segundos entre a última ação executada e a próxima a ser executada.

# entrar no link 
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login") #(site modelo disponibilizado pela hashtag treinamentos para teste da automação).
pyautogui.press("enter")
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=645, y=372)
# preencher as credenciais 
pyautogui.write("email@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua_senha")
pyautogui.click(x=819, y=540) # clique no botao de login
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar

import os # Usado para manipular caminhos de arquivos e pastas de forma compatível com qualquer sistema operacional

import pandas as pd # Biblioteca para ler, analisar e manipular dados em tabelas

caminho_arquivo = os.path.join("BD","produtos.csv")

tabela = pd.read_csv(caminho_arquivo)

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    
    # clicar no campo de código
    pyautogui.click(x=697, y=256)

    # Pegando o valor da coluna "codigo" da linha atual e armazenando na variável 'codigo'
    codigo = tabela.loc[linha, "codigo"]

    # preencher o campo
    pyautogui.write(str(codigo))

    # passar para o proximo campo
    pyautogui.press("tab")

    # preencher todos os campos
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    # Pegando o valor da coluna "obs" (observações) da linha atual
    obs = tabela.loc[linha, "obs"]

    # Verifica se o campo "obs" não está vazio (ou seja, não é NaN)
    if not pd.isna(obs):

        # Se houver uma observação, escreve o conteúdo no campo atual da página
        pyautogui.write(str(tabela.loc[linha, "obs"]))

    pyautogui.press("tab")

    pyautogui.press("enter") # cadastra o produto (botao enviar)

    # dar scroll pra cimatopo da página
    pyautogui.scroll(5000)
    
    # Passo 5: Repetir o processo de cadastro até o fim
