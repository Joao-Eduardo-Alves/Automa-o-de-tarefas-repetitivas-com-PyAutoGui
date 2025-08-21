# Automação de Tarefas repetitivas com Python

Este projeto foi desenvolvido como parte do evento online ao vivo "jornada Python" ministrada pela Hashtag Treinamentos.

Seu objetivo é automatizar uma tarefa repetitiva, como preenchimentos e cadastros em um sistema com dados de uma planilha.

A planilha de dados e o sistema utilizado neste código são modelos disponibilizados pela hashtag treinamentos para teste desta automação https://dlp.hashtagtreinamentos.com/python/intensivao/login

## Bibliotecas utilizadas

- pyautogui
- pandas

## O que o projeto faz?

- Abertura automática do sistema via navegador.
- Login automatizado no sistema
- Lê uma base de dados utilizando a biblioteca `pandas`.
- Usa a blibioteca `pyautogui` para preencher automaticamente qualquer sistema ou aplicação com os dados da tabela de forma automática por meio de comandos automáticos de mouse e teclado.
- Otimiza tempo automatizando uma tarefa repetitiva que seria feita manualmente.


## Como executar a automação

1. Clone este repositório.

2. Instale as bibliotecas necessárias:

- pip install pyautogui

- pip install pandas

3. Mapeie sua tela utilizando o arquivo: `pegar_posicao.py`

O que é "mapear a tela"?
Mapear a tela é o processo de descobrir as coordenadas exatas (x, y) onde o pyautogui.click() deve clicar. Isso depende da resolução da tela e do zoom do navegador, então cada usuário precisa fazer esse mapeamento no próprio computador ou onde será utilizado a automação.

- Execute o arquivo `pegar_posicao.py`

- Posicione o mouse onde deseja clicar (campo de login, botão, etc). O tempo definido por padrão para posicionar o mouse é de 5 segundos.

- Após o tempo definido por padrão o terminal mostrará as coordenadas do mouse (x,y).

- Copie os valores e use na área desejada no seu código principal, por exemplo:
pyautogui.click(x=641, y=377)

4. Coloque a base de dados no diretório BD/.

5. Execute o arquivo principal: `main.py`

## Compatibilidade com Aplicações Desktop
Embora este projeto tenha sido desenvolvido para automação de um sistema web, o código pode ser facilmente adaptado para automação de aplicações desktop, porque:

A biblioteca pyautogui funciona controlando o mouse e teclado em qualquer janela visível na tela.

Isso significa que, ao invés de abrir um navegador, o script pode clicar, digitar e interagir com qualquer programa que esteja aberto.

Para isso, basta ajustar as coordenadas de clique e os comandos conforme a interface da aplicação desktop desejada.

Utilize o arquivo mapear_tela.py para identificar as posições corretas na tela da aplicação desktop.

## Atenção

As coordenadas usadas pelo pyautogui são sensíveis à resolução e ao posicionamento da janela, então ajuste o mapeamento quando mudar de máquina ou monitor.