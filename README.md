# Como configurar/instalar/usar o `configurar certificado digital com o Kleopatra` no `Linux Ubuntu`

## Resumo

Neste documento estão contidos os principais comandos e configurações para configurar/instalar/usar o `configurar certificado digital com o Kleopatra` no `Linux Ubuntu`.

## _Abstract_

_This document contains the main commands and settings for configuring/installing/using the `reset, reset and reinstall XFCE Window Manager` on `Linux Ubuntu`._

## Descrição [2]

### Certificado digital

Um certificado digital é um documento eletrônico que vincula uma chave criptográfica à identidade de uma pessoa, organização ou dispositivo, permitindo a autenticação e a segurança em comunicações online. Ele funciona como uma identidade virtual, garantindo que as partes em uma transação digital sejam quem afirmam ser. Os certificados digitais são emitidos por Autoridades Certificadoras (CAs) e contêm informações como o nome do titular, a chave pública, a validade e a assinatura digital da CA. São amplamente utilizados em aplicações como comércio eletrônico, assinaturas digitais, e-mail seguro e autenticação de websites, contribuindo para a confiança e a integridade das comunicações na internet.

### `Kleopatra`

Kleopatra é uma ferramenta de gerenciamento de chaves e interface gráfica para o Gpg4win e o GnuPG, projetada para facilitar a criptografia e a assinatura de dados em ambientes Linux e Windows. Ela permite que os usuários gerenciem suas chaves criptográficas, importem e exportem chaves públicas, e realizem operações de criptografia e assinatura em arquivos e mensagens de forma intuitiva. Com uma interface amigável, o Kleopatra é amplamente utilizado por profissionais que precisam proteger informações sensíveis, garantir a autenticidade de documentos e comunicar-se de maneira segura.


## 1. Como configurar/instalar/usar o `configurar certificado digital com o Kleopatra` no `Linux Ubuntu` [1][3]

Para configurar/instalar/usar o `configurar certificado digital com o Kleopatra` no `Linux Ubuntu`, você pode seguir estes passos:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Certifique-se de que seu sistema esteja limpo e atualizado.

    2.1 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
    
    2.2 Remover pacotes `.deb` antigos ou duplicados do cache local. É útil para liberar espaço, pois remove apenas os pacotes que não podem mais ser baixados (ou seja, versões antigas de pacotes que foram atualizados). Digite o seguinte comando: `sudo apt autoclean`

    2.3 Remover pacotes que foram automaticamente instalados para satisfazer as dependências de outros pacotes e que não são mais necessários. Digite o seguinte comando: `sudo apt autoremove -y`

    2.4 Buscar as atualizações disponíveis para os pacotes que estão instalados em seu sistema. Digite o seguinte comando e pressione `Enter`: `sudo apt update`

    2.5 **Corrigir pacotes quebrados**: Isso atualizará a lista de pacotes disponíveis e tentará corrigir pacotes quebrados ou com dependências ausentes: `sudo apt --fix-broken install`

    2.6 Limpar o `cache` do gerenciador de pacotes `apt`. Especificamente, ele remove todos os arquivos de pacotes (`.deb`) baixados pelo `apt` e armazenados em `/var/cache/apt/archives/`. Digite o seguinte comando: `sudo apt clean` 
    
    2.7 Para ver a lista de pacotes a serem atualizados, digite o seguinte comando e pressione `Enter`:  `sudo apt list --upgradable`

    2.8 Realmente atualizar os pacotes instalados para as suas versões mais recentes, com base na última vez que você executou `sudo apt update`. Digite o seguinte comando e pressione `Enter`: `sudo apt full-upgrade -y`
    

### 1.1 Certificado de Assinatura Digital Autogerado (Certificado de Autoassinatura)

Para obter um certificado digital gratuito para assinar um arquivo `.pdf`, você pode usar algumas opções disponíveis, embora certificados digitais gratuitos tenham limitações e sejam menos comuns. Aqui estão alguns métodos que podem atender a sua necessidade:

Você pode criar um certificado digital localmente e usá-lo para assinar documentos. Este tipo de certificado **NÃO** é emitido por uma autoridade certificadora (AC) confiável para terceiros, mas é suficiente para validar a integridade de um documento, especialmente se o uso for interno ou pessoal.

Ferramentas como o `OpenSSL` permitem criar certificados autogerados.

O certificado não será reconhecido como confiável por sistemas ou terceiros, mas é útil para uso privado.
Passos para criar o certificado usando `OpenSSL`:

1. **Gerar uma chave privada**:

```
openssl genrsa -out private_key.pem 2048
```

2. **Gerar um certificado digital utilizando a chave privada**:

```
openssl req -new -x509 -key private_key.pem -out certificate.pem -days 365
```

Você pode usar este certificado para assinar um PDF utilizando _software_ como o Adobe Acrobat ou outras ferramentas que permitam importar certificados personalizados.


### 1.2 Converter o Certificado para um Formato Compatível (PKCS#12)

Alguns programas leitores de `.pdf` usam a infraestrutura do sistema `KDE` para gerenciar certificados. O formato `.pem` que você gerou precisa ser convertido para um formato `PKCS#12` (`.p12`), que é mais comumente reconhecido por ferramentas que fazem a gestão de certificados, ou seja, esses programas **NÃO** reconhecem o certificado gerado com o `OpenSSL`, pois ele requer que o certificado esteja disponível em um formato específico e em um local onde o sistema possa gerenciá-lo adequadamente. Vou detalhar o que você pode fazer para que esses programas reconheçam o certificado:

Para converter o certificado e a chave privada em um arquivo `.p12`, use o seguinte comando:

```
openssl pkcs12 -export -out certificate.p12 -inkey private_key.pem -in certificate.pem -name "Meu Certificado"
```

Este comando vai gerar um arquivo `.p12` que inclui tanto a chave privada quanto o certificado em um formato que pode ser importado pelos gerenciadores de certificados.

Durante a execução, ele vai pedir uma senha para proteger o arquivo `.p12`. Lembre-se dessa senha, pois será necessária ao importá-lo no sistema.


### 1.3 Instalar o `Kleopatra`

o `Kleopatra` é a ferramenta recomendada para gerenciar e importar certificados no `KDE`, e é a forma mais fácil de garantir que o seu certificado esteja acessível para o programa leitor de `.pdf`.

No ambiente `KDE`, o `Kleopatra` é frequentemente usado para manipular certificados digitais, incluindo certificados do tipo `.p12` que você gerou. Ele faz a integração com o sistema e torna esses certificados disponíveis para outras aplicações.

1. **Como Instalar o `Kleopatra`**: Você pode instalar o `Kleopatra` usando o gerenciador de pacotes da sua distribuição `Linux Ubuntu`. No caso de distribuições baseadas em `Debian/Ubuntu`, como o `Xubuntu`, você pode instalar com o seguinte comando:

```
sudo apt install kleopatra -y
```

Depois de instalado, siga os passos descritos anteriormente para importar o certificado no `Kleopatra`. Isso permitirá que o `Okular` acesse o certificado e você possa usá-lo para assinar documentos `.pdf`.


### 1.3 Importar o Certificado no `KDE` com o `Kleopatra`

O `Kleopatra` é o gerenciador de certificados do `KDE`, e você pode usá-lo para importar o arquivo `.pem` ou o `.p12`.

1. **Abra o `Kleopatra`**.

2. Vá para `File -> Import Certificates`.

3. Selecione o arquivo `certificate.p12` que você acabou de criar.

4. Durante a importação, você precisará fornecer a senha definida no passo anterior.

    Isso deve tornar o certificado disponível para o leitor de `.pdf`.


### 1.4 Importar certificado no Firefox

O `Okular` utiliza a biblioteca `Poppler` e o `NSS` para gerenciar certificados. Isso significa que, para que o `Okular` reconheça seu certificado, ele precisa ser adicionado ao armazenamento de certificados do `NSS`, que pode ser o do `Firefox` ou o diretório padrão do sistema.

Aqui estão os passos que você pode seguir para corrigir o problema:

O `Firefox` usa o NSS para gerenciar seus certificados e o `Okular` pode utilizar o armazenamento de certificados do Firefox. Se você tiver o Firefox instalado, pode adicionar o seu certificado nele, e o Okular poderá reconhecê-lo.

Siga os passos para importar o certificado no Firefox:

1. Abra o Firefox.

2. Vá para o menu `Configurações -> Privacidade e Segurança`.

3. Role até a seção `Certificados` e clique em `Ver Certificados`.

4. Na aba `Seus Certificados`, clique em `Importar`.

5. Selecione o arquivo `certificate.p12` que você gerou anteriormente e forneça a senha que você definiu durante a criação do certificado.

6. Após importar, feche o Firefox.

Agora, tente novamente no `Okular`. Como ele usa o mesmo armazenamento de certificados, ele deve reconhecer o certificado que você importou no Firefox.

### 1.5 Adicionar Certificado ao Banco NSS

Se você não quiser usar o Firefox, pode adicionar o certificado diretamente ao banco de dados do `NSS` do sistema. Para isso, você pode usar o utilitário `certutil`:

1. **Instale o certutil (caso **NÃO** tenha instalado)**:

    ```
    sudo apt install libnss3-tools
    ```

2. **Extrair o Certificado do Arquivo `.p12`**: Vamos extrair o certificado no formato `PEM` a partir do arquivo `.p12`:

    ```
    openssl pkcs12 -in certificate.p12 -clcerts -nokeys -out certificate.crt
    ```

3. **Adicionar o Certificado ao Banco NSS**: Agora, com o certificado no formato correto, você pode usar o certutil para adicioná-lo ao banco de dados NSS:

    ```
    certutil -A -d sql:$HOME/.pki/nssdb -n "Meu Certificado" -t "C,," -i certificate.crt
    ```

    Esse comando deve funcionar agora, já que estamos passando apenas o certificado (sem a chave privada).

4. **Verificar se o Certificado Foi Adicionado**: Para verificar se o certificado foi importado corretamente, você pode listar os certificados no banco NSS:

    ```
    certutil -L -d sql:$HOME/.pki/nssdb
    ```

    Se o certificado aparecer na lista, o `Okular` já deve ser capaz de reconhecê-lo e permitir a assinatura digital dos PDFs.

5. Copie os certificados da pasta `/home/edenedfsls` para a pasta `/home/edenedfsls/.pki/nssdb`:

    ```
    sudo cp -r /home/edenedfsls/certificate.crt /home/edenedfsls/certificate.p12 /home/edenedfsls/.pki/nssdb/
    ```

### 1.6 Usar o Certificado no, por exemplo, leitor de `.pdf` Okular

Após importar o certificado usando, tente novamente o seguinte:

1. Abra o documento no `Okular`.

2. Vá em `Tools -> Digital Sign` e selecione a área do documento onde deseja aplicar a assinatura.

3. Agora o `Okular` deve listar o seu certificado recém-importado, permitindo que você o use para assinar o documento.


### 1.1 Código completo para configurar/instalar/usar

Para configurar/instalar/usar o `configurar certificado digital com o Kleopatra` no `Linux Ubuntu` sem precisar digitar linha por linha, você pode seguir estas etapas:

1. Abra o `Terminal Emulator`. Você pode fazer isso pressionando: `Ctrl + Alt + T`

2. Digite o seguinte comando e pressione `Enter`:

    ```
    NÃO há.
    ```


## Referências

[1] OPENAI. ***Certificado digital gratuito PDF.*** Disponível em: <https://chatgpt.com/c/67000153-c484-8002-9c54-ac7a463fa508> (texto adaptado). Acessado em: 07/10/2024 10:36.

[2] OPENAI. ***Vs code: editor popular.*** Disponível em: <https://chat.openai.com/c/b640a25d-f8e3-4922-8a3b-ed74a2657e42> (texto adaptado). Acessado em: 07/10/2024 10:36.

