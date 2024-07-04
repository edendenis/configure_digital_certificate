#!/usr/bin/env python
# coding: utf-8

# # Como configurar/instalar/usar o `alterar a aparência do ambiente de desktop` no `Linux Ubuntu`
# 
# ## Resumo
# 
# Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `aparência do ambiente de desktop` no `Linux Ubuntu`.
# 
# ## _Abstract_
# 
# _This document contains the main commands and settings for configuring/installing/using the `aparência do ambiente de desktop` on `Linux Ubuntu`._

# ## Descrição [2]
# 
# ### `Appearance`
# 
# A aparência do ambiente de desktop se refere à estética visual e à disposição dos elementos gráficos na interface do usuário de um sistema operacional. Isso inclui o tema geral, como cores, ícones, fontes e estilo das janelas, bem como a organização e o layout dos painéis, menus e widgets. A personalização da aparência permite aos usuários adaptar o ambiente de trabalho às suas preferências estéticas e funcionais, melhorando a experiência de uso do sistema operacional.
# 

# ## 1. Como configurar/instalar/usar o `alterar a aparência do ambiente de desktop` no `Linux Ubuntu` [1][3]
# 
# Para configurar/instalar/usar o `alterar a aparência do ambiente de desktop` no `Linux Ubuntu`, você pode seguir estes passos:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

# 2. Certifique-se de que seu sistema esteja limpo e atualizado.
# 
#     2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`
# 
#     2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`
# 
#     2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`
# 
#     2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`
# 
#     2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
#     
#     2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`
# 
#     2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
#     

# Para `alterar a aparência do seu ambiente de desktop` para o padrão do `XFCE` ou outro no `Ubuntu 22.04 LTS`, você precisará instalar o ambiente de desktop `XFCE` e configurar sua sessão para usá-lo. Aqui estão os passos para fazer isso:
# 
# 1. **Instalar o `XFCE`**: Abra um terminal.
# 
# 2. **Execute o seguinte comando para instalar o `XFCE`**:
# 
#     ```
#     sudo apt update
#     sudo apt install xubuntu-desktop
#     ```
# 
#     Isso instalará o ambiente de desktop XFCE e todos os pacotes associados.
# 
# 2. **Selecionar o `XFCE` na Tela de Login**:
# 
#     2.1 Faça logout da sua sessão atual.
# 
#     2.2 Na tela de login, clique no ícone de engrenagem ou no botão de opções de sessão (geralmente no canto inferior direito ou próximo ao campo de entrada de senha).
# 
#     2.3 Selecione `"Xubuntu Session"` ou `"XFCE Session"` na lista de opções.
# 
#     2.4 Faça login com suas credenciais.
# 
# 3. **Ajustar as Configurações do `XFCE`**
# 
#     3.1 Depois de fazer login no `XFCE`, você pode ajustar as configurações da aparência e do comportamento do desktop através do `"Configurações"` do `XFCE`.
# 
#     3.2 Vá para `"Menu" -> "Configurações" -> "Ajustes"` para ajustar temas, ícones, fontes e outras opções de aparência.
# 
# 4. **Remover o Ambiente de Desktop `GNOME` (Opcional)**:
# 
#     Se você desejar remover o ambiente de desktop `GNOME` para liberar espaço e simplificar a configuração, você pode fazer isso com o seguinte comando:
#     
#     ```
#     sudo apt purge ubuntu-desktop gnome-shell gdm3
#     sudo apt autoremove
#     ```
# 
# **Conclusão**
# 
# Após seguir esses passos, você deverá estar usando o ambiente de desktop XFCE com a aparência padrão do Xubuntu no Ubuntu `22.04 LTS`. Se precisar de mais alguma coisa ou tiver outras perguntas, estou à disposição para ajudar!
# 

# ### 1.1 Código completo para configurar/instalar/usar
# 
# Para configurar/instalar/usar o `alterar a aparência do ambiente de desktop` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:
# 
# 1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`
# 
# 2. Digite o seguinte comando e pressione `Enter`:
# 
#     ```
#     NÃO há.
#     ```
# 

# ## Referências
# 
# [1] OPENAI. ***Alterar a aparência do ambiente de desktop.*** Disponível em: <https://chatgpt.com/c/3f876076-72b6-4270-b6d9-e559c94bf490> (texto adaptado). Acessado em: 18/03/2023 17:11.
# 
# [2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 18/03/2024 17:10.
# 
