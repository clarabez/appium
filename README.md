<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/appiumwithpython.png">
</p>

Este material é um guia para o setup do ambiente de configuração e uso do Appium para automação de testes em dispositivos móveis. Aqui você vai: 
1. Entender como funciona a ferramenta Appium e como fazer o setup desta aplicação nas plataformas: Windows, Linux e Mac;
2. Como instanciar um dispositivo Android emulado através do Android Studio;
3. Como instalar um aplicativo da PlayStore em seu dispositivo emulado; 
4. Como fazer mapeamento de elementos de uma aplicação em seu dispositivo;
5. Como iniciar testes de UI em sua aplicação através do Appium com a linguagem de programação Python.

Este documento sofrerá ajustes e complementos ao longo do tempo :)

Em breve irei disponibilizar o mesmo conteúdo em inglês e também uma solução usando o Docker, visando tornar mais prática a etapa de configuração.

Qualquer sugestão de melhoria ou correção, por favor entrar em contato <3

# Introdução - Um pouco sobre Appium

Appium é uma ferramenta open-source e multi-plataforma (isso quer dizer que funciona em Windows, Linux e Mac) e cujo foco é de interações via UI em dispositivos móveis, possibilitando a automação de aplicações: nativas, híbridas e sites mobile para as plataformas Android e iOS.

Considero Appium uma excelente ferramenta para quem quer começar a aprender automação em dispositivos móveis ou para quem já é da área de mobile e gostaria de se aprofundar mais sobre o assunto.

**Links importantes para esta seção:**

[Página oficial do Appium](http://appium.io)

[Página oficial do repo do Appium no GitHub](https://github.com/appium/)

Como dito mais acima, a finalidade do Appium é testar aplicações em dispositivos móveis, e aplicações podem ser classificadas em três diferentes naturezas : nativas, híbridas e móveis. Qual a diferença entre elas?
  - **Nativas:** aquelas aplicações que foram desenvolvidas especificamente para Android ou iOS, ou seja, a partir de seus específicos SDKs.
  - **Híbridas:** aquelas que são desenvolvidas em HTML, CSS, JavaScript e que são compatíveis com qualquer plataforma (Android, iOS, Windows).
  - **Móveis:** aquelas que podemos acessar através de um link, via página web.

# Setup do Ambiente - Download

Durante o nosso workshop vamos utlizar algumas ferramentas essenciais para a prática de automação. Baixe e instale as seguintes ferramentas, que são comuns para Windows, MAC ou Linux:
  - **Appium Desktop:** é a interface da ferramenta Appium que será o foco do nosso workshop. O download está [disponível aqui:](https://github.com/appium/appium-desktop/releases/tag/v1.13.0) (aqui tem um acervo para vários Sistemas Operacionais. Baixe apenas aquele que for direcionado para o seu SO.)
  
  - **JDK (JAVA Development Kit):** https://www.java.com/pt_BR/download/ 

  - **Android Studio:** é um pacote do Android Studio que possibilita que possamos instaciar dispositivos móveis de várias configurações e modelos de forma emulada e em vários níveis de API. Para isso, é preciso baixar o Android Studio e, durante o setup, marcar a opção de instalar também o AVD: https://developer.android.com/studio/index.html?hl=pt-br
  
  - **IDE:**
  Escolha uma IDE de sua preferência para desenvolver os testes na linguagem escolhida. Como vamos focar em Python, sugiro PyCharm ou VSCode. Links abaixo para download:
  - PyCharm: https://www.jetbrains.com/pycharm/
  
  - VSCode: https://code.visualstudio.com/
  
  Depois de fazer o download de todo o conteúdo, agora podemos avançar com o setup do ambiente. Podemos configurar as variáveis de ambiente à nível de sistema (abaixo eu deixo detalhado como fazer para cada SO) e também podemos fazer de maneira bem mais simplificada, onde explico melhor após o detalhe de setup para cada SO.
  
# Setup do Ambiente - Variáveis de ambiente - Mac:

Depois de realizadas as instalações do Appium Desktop, JAVA, Android Studio e da sua IDE, é hora de setarmos as variáveis de ambiente para que seu sistema operacional identifique os processos  e as aplicações de forma mais rápida e prática.
Para isso, abra o seu terminal, identifique a localização de instalação dos pacotes e os exporte para a variável PATH.
Após identificar a localização de onde foi instalado o seu Android, copie o caminho da pasta.
Por exemplo, para macOS a localização normalmente fica em:

```bash
/Users/user_name/Library/Android/sdk
```

Então será a partir desta pasta que vamos identificar os outros caminhos necessários, como:
```bash
/Users/user_name/Library/Android/sdk/platform-tools
/Users/user_name/Library/Android/sdk/tools
/Users/user_name/Library/Android/sdk/build-tools
```

Quando você identificar estes caminhos em sua máquina, é hora de exportar esses valores para a variável PATH, como sugere o exemplo a seguir:

```bash
export ANDROID_HOME=/your/path/to/Android/sdk 
export PATH=$ANDROID_HOME/platform-tools:$PATH 
export PATH=$ANDROID_HOME/tools:$PATH 
export PATH=$ANDROID_HOME/build-tools:$PATH 
export JAVA_HOME=/your/path/to/jdk1.8.0_112.jdk/Contents/Home 
export PATH=$JAVA_HOME/bin:$PATH
```
# Setup do Ambiente - Variáveis de ambiente - Windows:
Após o download (link acima) e instalação do JDK do seu ambiente Windows, é hora de configurar as variáveis de ambiente. Para isso, siga as opções de menu:
1. Propriedades do Sistema >> Configurações avançadas do sistema >> Variáveis de ambiente >> Variáveis de usuário >> Novo.
2. Insira o nome da variável como "JAVA_HOME" e insira como valor a localização exata do seu arquivo jre, por exemplo, "C:\Arquivos de Programa\Java\jdk1.2.2_2\jre".
3. Na seção de variáveis de sistema, dê um clique duplo em "Path" e adicione a expressão "%JAVA_HOME%\bin". Isto significa que você está adicionando o mesmo valor criado para JAVA_HOME, só que também contuando para a pasta \bin.
4. É só clicar OK e aplicar as mudanças de configuração.

Agora, para baixar (link acima) e instalar o Android SDK, siga os passos:
1. Siga o mesmo passo #1 descrito acima até alcançar o campo de variáveis de ambiente.
2. Agora, insira o nome da variável como "ANDROID_HOME" e insira como valor a localização exata onde seu Android SDK foi instalado, por exemplo, "C:\android-sdk".
3. Agora, mais uma vez precisamos adicionar o valor da sua nova variável à sua variável global do sistema, que é o Path: "%ANDROID_HOME%\platform-tools" e também "%ANDROID_HOME\tools%".
4. É só clicar OK e aplicar as mudanças de configuração.

# Setup do Ambiente - Variáveis de ambiente - Linux:
A configuração de variáveis de ambiente para Linux funciona de forma muito semelhante a do Mac. Basta que vc identifique o caminho exato de instalação do JDK e do Android e aplicar (através de export) os caminhos no seu arquivo de configuração global, que neste caso é o ~/.bashrc

Por exemplo, para Linux a localização normalmente fica em:

```bash
/Users/user_name/Library/Android/sdk
```

Então será a partir desta pasta que vamos identificar os outros caminhos necessários, como:
```bash
/Users/user_name/Library/Android/sdk/platform-tools
/Users/user_name/Library/Android/sdk/tools
/Users/user_name/Library/Android/sdk/build-tools
```

Quando você identificar estes caminhos em sua máquina, é hora de exportar esses valores para a variável PATH, como sugere o exemplo a seguir:

```bash
export ANDROID_HOME=/your/path/to/Android/sdk 
export PATH=$ANDROID_HOME/platform-tools:$PATH 
export PATH=$ANDROID_HOME/tools:$PATH 
export PATH=$ANDROID_HOME/build-tools:$PATH 
export JAVA_HOME=/your/path/to/jdk1.8.0_112.jdk/Contents/Home 
export PATH=$JAVA_HOME/bin:$PATH
```

**Dica - Windows/Linux/Mac:**
Para identificar onde está a sua pasta para JAVA_HOME, é só usar o seguinte comando no terminal:
```bash
which java
```
Deverá ser retornado o caminho até seu pacote JAVA.

**Dica 2 - Linux/Mac:**
Para evitar que suas variáveis de ambiente percam os valores, salve o conteúdo da variável no seu arquivo bashrc (Linux) ou bash_profile (macOS). Após salvar os valores, não esqueça de "compilar" o arquivo para as mudanças serem refletidas:
Para macOS:
```bash
source ~./bash_profile
```

Para Linux:
```bash
source ~/.bashrc
```

# Setup do Ambiente - Forma simplificada para Windows/Linux/Mac
Se você quiser simplificar a sua configuração de ambiente, é só utilizar o atalho de configuração do Appium
___
# Instalando o Appium

A instalação do Appium é bastante simples e não requer configuração adicional - além da do Android e do JDK. Basta baixar o Appium Desktop na página oficial do Appium(como no link do começo do documento) ou via linha de comando atráves do terminal:

```bash
npm install -g appium
```
ATENÇÃO: Não instale o Appium com sudo.

**Dica - O que é npm?**
Npm é o gerenciador de downloads para pacotes node.js. 

# Como validar se tudo tá configurado ou se falta algo?

Uma funcionalidade bem legal que o Appium oferece é o pacote Appium-doctor, cuja finalidade é conferir o checklist necessário para que seu ambiente funcione. Caso algo esteja faltando, o Appium-doctor te lista exatamente o que falta. Ele também confirma o que tá configurado como esperado. Para instalá-lo, é só instalar o pacote via npm:
```bash
npm install -g appium-doctor --android
```

Estamos usando a flag **--android** para indicar a plataforma que vamos usar o Appium. Caso fóssemos usar o iOS, usaríamos a flag **--ios--**.

Depois de instalado o Appium-doctor, é só fazer a chamada via terminal:

```bash
appium-doctor
```

Abaixo segue um exemplo de como é o retorno do Appium-doctor via terminal:
```bash
➜  bin appium-doctor
info AppiumDoctor Appium Doctor v.1.10.0
info AppiumDoctor ### Diagnostic for necessary dependencies starting ###
info AppiumDoctor  ✔ The Node.js binary was found at: /usr/local/bin/node
info AppiumDoctor  ✔ Node version is 8.11.4
WARN AppiumDoctor  ✖ Xcode is NOT installed!
info AppiumDoctor  ✔ Xcode Command Line Tools are installed in: /Library/Developer/CommandLineTools
info AppiumDoctor  ✔ DevToolsSecurity is enabled.
info AppiumDoctor  ✔ The Authorization DB is set up properly.
info AppiumDoctor  ✔ Carthage was found at: /usr/local/bin/carthage
info AppiumDoctor  ✔ HOME is set to: /Users/BEZERRA
WARN AppiumDoctor  ✖ ANDROID_HOME is NOT set!
WARN AppiumDoctor  ✖ JAVA_HOME is NOT set!
WARN AppiumDoctor  ✖ adb could not be found because ANDROID_HOME is NOT set!
WARN AppiumDoctor  ✖ android could not be found because ANDROID_HOME is NOT set!
WARN AppiumDoctor  ✖ emulator could not be found because ANDROID_HOME is NOT set!
WARN AppiumDoctor  ✖ Bin directory for $JAVA_HOME is not set
info AppiumDoctor ### Diagnostic for necessary dependencies completed, 7 fixes needed. ###
```

Tudo que estiver acompanhado do símbolo **✔** significa que está instalado corretamente.
Tudo que estiver acompanhado do símbolo **✖** significa que *NÃO* está instalado ou identificado. Esses casos você deve ajustar.

O pacote do **Xcode** é específico para iOS, então, para Android, não devemos nos preocupar.

___
# Checklist de tudo o que fizemos até agora

Se você chegou até aqui, significa que provavelmente o seu setup está pronto e agora você já pode usar todos os recursos do Appium! Só para checar, instalamos e configuramnos:
- Appium Desktop
- Android Studio (pacote AVD)
- JAVA
- IDE
- Configuração de variáveis de ambiente

___
# Iniciando com o Appium

Depois de tudo configurado, é hora de iniciarmos com o Appium Desktop.

___
# Comandos ADB
ADB é uma abreviação para Android Debug Brigde. Grosseiramente traduzindo, é uma ferramenta que faz uma "ponte" de comunicação entre o seu computador e o seu dispositivo móvel Android através de linhas de comando. Através do ADB, é possível que possamos manipular o dispositvo através de comandos, de forma muito prática, como:
- Instalar/desintalar aplicativos;
- Mudar configurações internas, como: tempo de desligar tela, bloqueio/desbloqueio de tela, etc.
- Habilitar/desabilitar funções de conexões, como: wifi, dados, modo avião.
- Transfência/manipulação de arquivos;
- Rebootar e desligar o dispositivo - não funciona para ligá-lo (mas isso pode ser resolvido através de frameworks).

É também possível automatizar algumas atividades de rotina combinando comandos ADB e Python Script.

Como o assunto sobre comandos ADB merece maior aprofundamento e dedicação, criei um repositório à parte para falar mais sobre o tema: [repo comandosadb](https://github.com/clarabez/comandosadb)

**Links importantes desta seção:**

**Um pouco mais sobre comandos ADB:** https://developer.android.com/studio/command-line/adb?hl=pt-br
**Um pouco Python Script:** https://realpython.com/run-python-scripts/
**Meu Repositório sobre Comandos ADB:** https://github.com/clarabez/comandosadb

___
# Emulando um dispositivo Android através do Android Studio
Podemos usar o Appium em dispositivos reais, dispositivos emulados ou até mesmo em farms de dispositivos da Amazon, que funcionam com o mesmo conceito de computação em nuvem, onde você aloca recursos sob demanda e paga apenas o que for consumido.
Durante nossos estudos podemos utilizar dispositivos emulados para a realização dos nossos testes. Isso nos dá grande versatilidade pela possibilidade de escolher o tipo de dispositivo e a versão de Android que iremos utilizar. Desta forma, é possível validar o mesmo apk em cenários diversos apenas alterando configurações, onde atingimos uma característica muito forte no Android que é a granularidade de versões: https://developer.android.com/about/dashboards?hl=pt-br

Vamos utilizar um recurso do próprio Android Studio para instanciarmos nosso dispotivo emulado: o Android Virtual Device Manager. Para acessá-lo, basta abrir o seu Android Studio e seguir até o seguinte ícone:

Podemos usar comandos ADB no nosso dispositivo emulado e já ver que ele responde da mesma maneira que um dispositivo real. Tenta os seguintes comandos em seu terminal com seu dispositivo emulado ativo:
Para litar o dispositivo e obter seu identificador:
```bash
adb devices
```

Ou dar um reboot (reiniciar) via terminal:
```bash
adb reboot
```

Alguns pontos importantes sobre este tópico:
- Em breve farei um material falando como emular um dispositivo iOS.
- Existem outras ferramentas que emulam dispositivos Androids mas, das que testei, nenhuma é tão boa quando a do Android Studio. Por esse motivo prefiro me manter nele e recomendo o uso.

___
# Tutorial 1: instalando um apk no meu dispositivo Android emulado
O primeiro de tudo é escolher algum APK disponível na Play Store para a realização dos estudos. Ultimamente tenho utilizado o APK das Casas Bahia, pois tem boa parte de seus elementos mapeados e também porque tem diversos menus, itens e uma excelente usabilidade, o que facilita no processo de aprendizado. 
A seguir estão os passos para você baixar uma aplicação e fazer a instação dela no seu dispositivo:
1. Escolha o APK a ser estudado;
2. Busque o APK no Google Play Store;
3. Copie o link da Play Store do apk (o link do perfil do aplicativo);
4. Cole o link do APK no site Evozi (link abaixo) para fazer o download do apk escolhido;
5. Salve o apk numa pasta de sua escolha;
6. Abra o seu Android Emulado e aguarde que ele fique na tela inicial (home screen);
7. Agora arraste o APK que vc baixou para a página inicial do seu dispositivo emulado.
8. Pode abrir o apk diretamente no dispositivo :) 
8.1. Se desejar fazer via linha de comando, é só abrir o terminal na pasta que está sua aplicação e usar o seguinte comando ADB:
```bash
adb install nome-do-apk
```

**Evozi - APK Downloader:** https://apps.evozi.com/apk-downloader/
**Google Play Store:** https://play.google.com/store/apps?hl=pt_BR

___
# Tutorial 2: Desired Capabilities: o que são e como iniciar uma sessão com o Appium
Um dos pontos mais importantes quando começamos a usar o Appium é entender o funcionamento dos Desired Capabilities (abaixo eu deixo o link oficial listando todos os valores que podemos usar nos desired capabilitites). Desired Capabilities pode ser grosseiramente traduzido por "Configurações desejadas", mas prefiro seguir com a expressão "Desired Capabilities" por achar que essa nossa tradução não funcionou tão bem para essa expressão :) peço desculpas por isso!

Como citado acima, o Appium funciona através de requisições HTTP e, como padrão deste tipo de comunicação, utilizamos arquivos em JSON para indicar qualquer mensagem. O appium nos traz uma interface gráfica com campos de entrada de texto mas, após preenchermos os campos de texto, ao lado ele já converte o que digitamos em um arquivo JSON. Você pode editar diretamente no JSON ou usar o campo de texto. As duas formas funcionam bem.

Para iniciarmos uma sessão vamos precisar de pelo menos 2 campos, que são:

```bash
{
    'platformName': 'Android',
    'deviceName': 'HAHEHHAHE'
}
```

Os nomes são bem intuitivos, e aí estou criando um dicionário com a chave 'platformName' para indicar a plataforma que irei utilizar, que pode ser: Android, Windows, iOS. Já o identificador do dispositivo móvel iremos inserir em 'deviceName', e podemos obter esse valor através do comando adb 'adb devices' que já explicamos mais acima.

Se quisermos estabelecer uma sessão de forma mais direcionada e detalhada, podemos utilizar mais chaves neste dicionário, como:
```bash
{
    'platformName': 'Android',
    'deviceName': 'HAHEHHAHE'
    '': '',
    '': ''
}
```

Mas, para deixarmos nosso aprendizado mais flúido e simples, mas optar inicialmente pelo uso de apenas 2 chaves que não podem faltar: 'platformName' e 'deviceName'.

**Página oficial do Appium listando todos os Desired Capabilities:** http://appium.io/docs/en/writing-running-appium/caps/

# Tutorial 3: Identificando os elementos da nossa aplicação

# Tutorial 4: Realizando atividades de GESTOS via Appium
Uma das características mais marcantes quando estamos trabalhando com Android é o uso de GESTOS. Inclusive, no Android Q uma das grandes mudanças que observamos foi a inclusão de mais gestos nas atividades principais desta plataforma. Via código não é uma tarefa simples simular o arrastar de dedos do usuário para encerrar uma aplicação, por exemplo. Uma das vantagens do Appium é que ele já traz uma funcionalidade que realiza alguns gestos e os traduz em código pra gente <3 Com essa funcionalidade podemos: [DETALHAR MAIS AQUI]

# Tutorial 5: Realizando um fluxo simples de teste funcional

# Tutorial 6: Gravando nossas ações e transformando isso em código

# Tutorial 7: Operações aritméticas com a Calculadora nativa do Android

A partir daqui, considero que o nível de dificuldade de uso e interação com o Appium cresce um pouco e passamos a trabalhar com tutoriais um pouco mais avançados.

# Tutorial 8: Replicando tudo o que fiz utilizando apenas Python

# Tutorial 9: Operações aritméticas com a Calculadora nativa do Android - Fase 2

# Tutorial 10: Operações aritméticas com a Calculadora nativa do Android - Fase 3: organizando o código com padrões de projeto e realizando fluxo de teste funcional
