<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/appiumwithpython.png">
</p>

Este material é um guia para o setup do ambiente de configuração e uso do Appium para automação de testes funcionais em dispositivos móveis. Dentro outros aprendizados, destaco os seguintes pontos como principais aprendizados:

<ul>
    <li>Entender como funciona a ferramenta Appium e como fazer o setup desta aplicação nas plataformas: Windows, Linux e Mac;</li>
    <li>Como instanciar um dispositivo Android emulado através do Android Studio;</li>
    <li>Como instalar um aplicativo da PlayStore em seu dispositivo emulado;</li>
    <li>Como fazer mapeamento de elementos de uma aplicação em seu dispositivo;</li>
    <li>Como iniciar testes de UI em sua aplicação através do Appium com a linguagem de programação Python.</li>
</ul>

___

**A organização do tutorial se dá nas seguintes seções:**
<ul>
    <li>Introdução</li>
    <li>Setup do ambiente</li>
    <ul>
        <li>Download de tudo que precisa</li>
        <li>Configuração Windows</li>
        <li>Configuração Linux</li>
        <li>Configuração Mac</li>
        <li>Setup simplificado para todos os SOs</li>
        <li>Instalação do Appium</li>
    </ul>
    <li>Appium Doctor: como validar se tá tudo configurado?</li>
    <li>Checklist</li>
    <li>Iniciando o Appium</li>
    <liComandos ADB></li>
    <li>Emulando um dispositivo Android através do Android Studio</li>
</ul>

___

**Tutoriais contidos aqui**

- Tutorial 1: Instalando um apk no meu dispositivo Android emulado
- Tutorial 2: Desired Capabilities: o que são e como iniciar uma sessão com o Appium
- Tutorial 3: Identificando os elementos da nossa aplicação
- Tutorial 4: Realizando atividades de GESTOS via Appium
- Tutorial 5: Realizando um fluxo simples de teste funcional
- Tutorial 6: Gravando nossas ações e transformando isso em código
- Tutorial 7: Operações aritméticas com a Calculadora nativa do Android
- Tutorial 8: Replicando tudo o que fiz utilizando apenas Python
- Tutorial 9: Operações aritméticas com a Calculadora nativa do Android - Fase 2
- Tutorial 10: Operações aritméticas com a Calculadora nativa do Android - Fase 3: organizando o código com padrões de projeto e realizando fluxo de teste funcional
___

Este documento sofrerá ajustes e complementos ao longo do tempo <i>&#128513;</i>

Em breve irei disponibilizar o mesmo conteúdo em inglês e também uma solução usando o Docker, visando tornar mais prática a etapa de configuração - e também a adição de mais tecnologias aqui.

Qualquer sugestão de melhoria ou correção, por favor entrar em contato <i>&#128525;</i>

Iniciei a elaboração deste tutorial porque pra aprender essa ferramenta tive que recorrer a diferentes fontes e tive que praticar muito pra ter dicas, criar tutoriais, entender melhor a dinâmica, etc. Espero que este documento seja muito útil pra você e te incentivo a também compartilhar o que você for aprendendo <i>&#129304;</i>

___

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/intro.png">
</p>

# Um pouco sobre Appium

Appium é uma ferramenta open-source e multi-plataforma (isso quer dizer que funciona em Windows, Linux e Mac) e cujo foco é de interações via UI em dispositivos móveis, possibilitando a automação de aplicações: nativas, híbridas e sites mobile para as plataformas Android e iOS.

Considero Appium uma excelente ferramenta para quem quer começar a aprender automação em dispositivos móveis ou para quem já é da área de mobile e gostaria de se aprofundar mais sobre o assunto.


**Links importantes para esta seção:**

[Página oficial do Appium](http://appium.io)

[Página oficial do repo do Appium no GitHub](https://github.com/appium/)

Como dito mais acima, a finalidade do Appium é testar aplicações em dispositivos móveis, e aplicações podem ser classificadas em três diferentes naturezas : nativas, híbridas e móveis. Qual a diferença entre elas?
  - **Nativas:** aquelas aplicações que foram desenvolvidas especificamente para Android ou iOS, ou seja, a partir de seus específicos SDKs.
  - **Híbridas:** aquelas que são desenvolvidas em HTML, CSS, JavaScript e que são compatíveis com qualquer plataforma (Android, iOS, Windows).
  - **Móveis:** aquelas que podemos acessar através de um link, via página web.

___

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/setup.png">
</p>

Nesta seção vamos ver os passos para realizarmos o setup do ambiente para Windows, Linux e Mac. Todos os meus projetos faço utilizando o Mac, então tendo a passar informações mais detalhadas para este SO.


**Uma dica muito importante:**

Digo o que fazer para cada sistema operacional, mas você também pode optar por uma configuração mais simples (e efetiva da mesma forma) e que vai te poupar de muito tempo e dor de cabeça - confie em mim :) Se você quiser ir por esse caminho, pode pular direto para o tópico "Forma simplificada para Windows/Linux/Mac". O mesmo procedimento é utilizado para qualquer sistema operacional.

# Download de tudo que vai ser necessário

Durante o nosso workshop vamos utlizar algumas ferramentas essenciais para a prática de automação. Baixe e instale as seguintes ferramentas, que são comuns para Windows, MAC ou Linux:
  - **Appium Desktop:** é a interface da ferramenta Appium que será o foco do nosso workshop. O download está [disponível aqui:](https://github.com/appium/appium-desktop/releases/tag/v1.13.0) (aqui tem um acervo para vários Sistemas Operacionais. Baixe apenas aquele que for direcionado para o seu SO.)
  
  - **JDK (JAVA Development Kit):** https://www.java.com/pt_BR/download/ 

  - **Android Studio:** é um pacote do Android Studio que possibilita que possamos instaciar dispositivos móveis de várias configurações e modelos de forma emulada e em vários níveis de API. Para isso, é preciso baixar o Android Studio e, durante o setup, marcar a opção de instalar também o AVD: https://developer.android.com/studio/index.html?hl=pt-br
  
  - **IDE:**
  Escolha uma IDE de sua preferência para desenvolver os testes na linguagem escolhida. Como vamos focar em Python, sugiro PyCharm ou VSCode. Links abaixo para download:
  - PyCharm: https://www.jetbrains.com/pycharm/
  
  - VSCode: https://code.visualstudio.com/
  
  Depois de fazer o download de todo o conteúdo, agora podemos avançar com o setup do ambiente. Podemos configurar as variáveis de ambiente à nível de sistema (abaixo eu deixo detalhado como fazer para cada SO) e também podemos fazer de maneira bem mais simplificada, onde explico melhor após o detalhe de setup para cada SO.
  
# Variáveis de ambiente - Mac:

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
# Variáveis de ambiente - Windows:
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

# Variáveis de ambiente - Linux:
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

# Forma simplificada para Windows/Linux/Mac
Se você quiser simplificar a sua configuração de ambiente, é só utilizar o atalho de configuração do Appium e inserir manualmente os caminhos para as suas variáveis ANDROID_HOME e JAVA_HOME. Esta etapa é bem mais simples e da mesma forma efetiva para uso da ferramenta. Basta seguir os passos adiante:

Abra sua ferramenta Appium Desktop e clique no botão "Edit Configurations".
<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/appiumFirstScreen.png">
</p>

Quando você clicar em "Edit Configurations", um popup vai abrir com 2 campos: ANDROID_HOME e JAVA_HOME. É só você identificar estes caminhos na sua máquina (no setup de configuração para cada SO eu deixei comandos e dicas para obter estes valores), copiar e colar nestes campos e em seguida clicar em "Save and Restart". Pronto, configuração do Appium realizada com sucesso :)

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/appiumSecondScreen.png">
</p>

___

# Instalando o Appium

A instalação do Appium é bastante simples e não requer configuração adicional - além da do Android e do JDK. Basta baixar o Appium Desktop na página oficial do Appium(como no link do começo do documento) ou via linha de comando atráves do terminal:

```bash
npm install -g appium
```
**ATENÇÃO:** Não instale o Appium com sudo.

**Dica - O que é npm?**

Npm é o gerenciador de downloads para pacotes node.js. 

___

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/appium-doctor.png">
</p>

# Como validar se tudo tá configurado ou se falta algo?

Uma funcionalidade bem legal que o Appium oferece é o pacote <em>Appium-doctor</em>, cuja finalidade é conferir o checklist necessário para que seu ambiente funcione. Caso algo esteja faltando, o Appium-doctor te lista exatamente o que falta. Ele também confirma o que tá configurado como esperado. Para instalá-lo, é só instalar o pacote npm no seu terminal:

```bash
npm install -g appium-doctor --android
```

**Dica:**
Estamos usando a flag **--android** para indicar a plataforma que vamos usar o Appium. Caso fóssemos usar o iOS, usaríamos a flag **--ios--**.

Depois de instalado o <em>Appium-doctor</em>, é só fazer a chamada via terminal:

```bash
appium-doctor
```

Abaixo segue um exemplo de como é o retorno do <em>Appium-doctor</em> via terminal:
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
- Appium Desktop **✔**
- Android Studio (pacote AVD) **✔**
- JAVA **✔**
- IDE **✔**
- Configuração de variáveis de ambiente **✔**

___
# Iniciando com o Appium

Depois de tudo configurado, é hora de iniciarmos com o Appium Desktop.
Assim que abrimos o Appium Desktop, esta é a carinha inicial que temos contato:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/appiumFirstScreen.png">
</p>

Observe que de cara já temos 2 campos preenchidos:<br>
**HOST:** 0.0.0.0<br>
**Port:** 4723

Estes são valores padrões do Appium e indicam que sempre que você começar a realizar requições (lembra que o Appium é baseado em servidor HTTP?), o Appium irá utilizar o Host 0.0.0.0 e o serviço irá funcionar na porta 4723. Caso você queira mudar estes valores (quando algum outro serviço já está alocado para esta porta, por exemplo), é só você realizar a customização dessa configuração manualmente clicando no botão **Advanced**, que fica ao lado do já selecionado **Simple**. Você também pode salvar suas configurações personalizadas e exportá-las através do button **Presets**. Eu, particularmente, nunca precisei utilizar nenhuma das configurações além das que já vem por padrão. Também não vi nenhum material pela internet em que fosse necessário customizar a configuração. Se quer um conselho, siga com essa configuração padrão que tudo vai funcionar bem :)

Explicada essa tela inicial, agora podemos clicar em **Start Server** e observar já a segunda tela do Appium: uma escuta da chamada HTTP. Observe que ele indica aí exatamente o endereço onde o serviço está sendo executado (que são inseridos nos campos de <i>Host</i> e <i>Port</i> da tela anterior, onde deixamos os valores padrões).

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/AppiumStarted2.png">
</p>

Agora podemos ir para a tela seguinte do Appium, onde vamos começar iniciar uma sessão (essa é a expressão utilizada quando vamos iniciar o uso do Appium), e pra isso vamos clicar no ícone da lupa, onde diz: **Start Inspector Session** (como a imagem abaixo).

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/startsession.png">
</p>

Agora podemos ver uma tela com vários campos para o Appium, mas aqui podemos seguir na aba <i>Custom Server</i>, que já vem escolhida por padrão. Observamos também os seguintes campos já preenchidos:<br>
**Remote Host:**  127.0.0.1<br>
**Remote Path:** /wd/hub<br>
**Remote Port:** 4327<br>

O **Remote Port** já falamos anteriormente. **Remote Host** tá com o valor de <i>localhost</i> para o serviço, mais uma vez você pode alterar caso já tenha algum serviço rodando local. Caso contrário, pode deixar esse valor mesmo. **Remote Path** também é um valor padrão do Appium e nunca precisei alterar, sempre deixo esse mesmo valor.

**Agora chegou o momento de aprendermos um dos pontos mais importantes quando começamos a usar o Appium: entender o funcionamento dos Desired Capabilities** (abaixo eu deixo o link oficial listando todos os valores que podemos usar nos desired capabilitites). <i>Desired Capabilities</i> pode ser grosseiramente traduzido por "Configurações desejadas". É onde você vai informar ao Appium o que é pra ele fazer exatamente.

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/appiumscreen3.png">
</p>

Como citado mais acima, o Appium funciona através de requisições HTTP e, como padrão deste tipo de comunicação, utilizamos arquivos em JSON para indicar qualquer mensagem. O appium nos traz uma interface gráfica com campos de entrada de texto mas, após preenchermos os campos de texto, ao lado ele já converte o que digitamos em um arquivo JSON. Você pode editar diretamente no JSON ou usar o campo de texto, como quiser. As duas formas funcionam bem.

Para iniciarmos uma sessão vamos precisar de pelo menos 2 campos, que são:

```bash
{
    'platformName': 'Android',
    'deviceName': '<InserirOnomeAqui>'
}
```

Os nomes são bem intuitivos, e aí estou criando um dicionário com a chave <i>'platformName'</i> para indicar a plataforma que irei utilizar, que pode ser: Android, Windows, iOS. 
Já o identificador do dispositivo móvel iremos inserir em <i>'deviceName'</i>, e podemos obter esse valor através do comando adb <i>'adb devices'</i> que já explicamos mais acima. Assim fica um exemplo de preenchimento destes campos básicos e ao lado já o retorno do conteúdo em JSON: [VER SE FICA LEGAL MESMO DEIXAR ESSA PARTE DO ADB DEVICES POR AQUI E EXPLICAR COMO PEGAR]

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/desiredcap1.png">
</p>


[TIRAR ESSA PARTE DAQUI E JOGAR MAIS ADIANTE]
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

___
# Emulando um dispositivo Android através do Android Studio
Podemos usar o Appium em dispositivos reais, dispositivos emulados ou até mesmo em farms de dispositivos da Amazon, que funcionam com o mesmo conceito de computação em nuvem, onde você aloca recursos sob demanda e paga apenas o que for consumido.
Durante nossos estudos podemos utilizar dispositivos emulados para a realização dos nossos testes. Isso nos dá grande versatilidade pela possibilidade de escolher o tipo de dispositivo e a versão de Android que iremos utilizar. Desta forma, é possível validar o mesmo apk em cenários diversos apenas alterando configurações, onde atingimos uma característica muito forte no Android que é a granularidade de versões: https://developer.android.com/about/dashboards?hl=pt-br

**Antes de tudo... o que é um dispositivo emulado?**<br>
É a instanciação (criação) de um dispositivo que simula um celular real, só que ele é emulado a partir dos recursos da sua máquina. É como se fosse uma máquina virtual, só que o Sistema Operacional (imagem) utilizado será alguma versão oficial do Android e o formato da máquina será uma réplica do celular de verdade, inclusive sob aspectos de tamanho das telas.

Vamos utilizar um recurso do próprio <i>Android Studio</i> para instanciarmos nosso dispotivo emulado: o <i>Android Virtual Device Manager</i>. Para acessá-lo, basta abrir o seu <i>Android Studio</i> e seguir até o seguinte ícone:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/avdmanager.png">
</p>

Assim que você clicar no ícone do <i>AVD Manager</i>, o seguinte popup vai abrir e você vai clicar em <i>+ Create Virtual Device...</i> para criar o seu novo dispositivo emulado, como na imagem a seguir:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/avdmanager2.png">
</p>

Nesta nova tela, podemos escolher qual o tipo de dispositivo que queremos: TV, Phone, Wear OS, Tablet; além da marca do produto, tamanho e resoluções de tela e também a densidade. Você pode emular qualquer variação desses produtos. Vamos focar em **phone** e eu gosto bastante de utilizar o produto <i>Pixel 2</i> em meus estudos, já que é um produto da Google e que tem um ótimo tamanho de tela, mas você fique à vontade de utilizar a variação de Phone que você achar melhor. Escolhido isso, é só clicar em <i>Next</i>.

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/avdmanager3.png">
</p>

Escolhido o produto que você quer prosseguir em seus estudos, agora é hora de escolher a versão do Android que você irá emular em seu produto. Veja que existe uma lista com várias versões anteriores do Android disponíveis para download. Neste exato momento, estamos na versão do **Android Q** no mercado e o Android R já está com sua versão Beta disponível para download. Usei algumas vezes o Android Q mas não achei a imagem tão completa em termos de recursos como o **Android P**, que é minha versão favorita atualmente. Vou prosseguir nos testes com o Android P, mas fique à vontade para baixar a versão que você quiser. Ah, você pode criar dispositivos com versões de Android diferentes e ir usando pra ver qual versão você acha que atende melhor às suas necessidades. Caso a imagem ainda não esteja disponível para você, clique em download. Caso já tenha baixado, é só selecionar a imagem e clicar em <i>Next</i>

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/avdmanager4.png">
</p>

Estou usando a seguinte configuração para meu dispositivo emulado:<br>
**Modelo de Device:** Pixel 2<br>
**Versão de Android:** Android P<br>

Dispositivo criado, tente realizar algumas ações nele como abrir aplicativos, utilizar botões de acesso como Home, Back, Recent Apps.

Um mundo de possibilidades que também podemos explorar com dispositivos Android é que podemos usar comandos ADB no nosso dispositivo emulado e já ver que ele responde da mesma maneira que um dispositivo real. A próxima seção vai falar um pouco sobre isso.

**Alguns pontos importantes sobre este tópico:**<br>
- Em breve farei um material falando como emular um dispositivo iOS.<br>
- Existem outras ferramentas que emulam dispositivos Androids mas, das que testei, nenhuma é tão boa quando a do Android Studio. Por esse motivo prefiro me manter nele e recomendo o uso.<br>

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/adb.png">
</p>

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

**Links importantes desta seção:**<br>
**Um pouco mais sobre comandos ADB:** https://developer.android.com/studio/command-line/adb?hl=pt-br<br>
**Um pouco Python Script:** https://realpython.com/run-python-scripts/<br>
**Meu Repositório sobre Comandos ADB:** https://github.com/clarabez/comandosadb<br>

___
# Tutorial 1: instalando uma aplicação no meu dispositivo Android emulado

**Para realizar este tutorial é preciso que você tenha:**
<ul>
    <li>Dispositivo emulado ativo - passo a passo na seção anterior</li>
    <li>ADB configurado e funcionando em seu terminal</li>
    <li>Conta na Play Store</li>
</ul>

O primeiro de tudo é escolher algum aplicativo disponível na <i>Play Store</i> para a realização dos estudos. Ultimamente tenho utilizado o aplicativo das **Casas Bahia**, pois tem boa parte de seus elementos mapeados e também porque tem diversos menus, itens e uma excelente usabilidade, o que facilita no processo de aprendizado. Daí, vamos procurar pelo aplicativo das Casas Bahia na Play Store e vamos chegar na página do aplicativo que deve parecer como esta abaixo:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/casasbahia.png">
</p>

Agora, é só copiar a URL da página principal do aplicativo, que no meu caso é o seguinte valor:

https://play.google.com/store/apps/details?id=com.novapontocom.casasbahia

Agora vamos acessar um site chamado Evozi, que tem como objetivo baixar qualquer aplicativo da Play Store tendo como base apenas o endereço URL da aplicação da Play Store, como mostro a seguir:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/evozi.png">
</p>

Agora é só clicar em **Generate Download Link** e realizar o download da sua aplicação. Veja que ela será baixada no formato <i>.apk</i>. Agora é só salvar em alguma pasta do seu computador e vamos instalar essa aplicação em seu dispositivo emulado, e isso podemos fazer de duas maneiras: segurando e arrastando o aplicativo; utilizando comando ADB. Vou ensinar as duas formas.

**Segurando e arrastando:**<br>
Essa forma é super simples, basta que você esteja com seu dispositivo emulado ativo e em paralelo abra a pasta que sua aplicação está. Agora, segure o seu aplicativo e arraste até o seu dispositivo móvel e, quando chegar no dispositivo, pode soltar. Você verá que vai aparecer uma imagem de <i>instalando...</i> e em poucos segundos sua aplicação estará disponível em seu dispositivo. É só acessar via menu e utilizar para ver que funciona direitinho.

**Através de comandos ADB:**<br>
Esta forma é mais elegante. É só você abrir o terminal, ir até a pasta que está sua aplicação (via terminal mesmo) e utilizar o seguinte comando:<br>
```bash
adb install nome-do-apk
```

Com isso, o aplicativo deve ser instalado corretamente e já aparecer disponível na lista de aplicações do seu dispositivo.

**Observação:**<br>
Aplicações na Play Store normalmente são bem ativas e constantemente sofrem alguma atualização de versão. Nessas atualizações, pode ser que alguma aplicação pare de funcionar em seu dispositivo. Por exemplo, já me aconteceu de a aplicação das Casas Bahia não mais funcionar em meu dispositivo porque deixou de ser compatível com a arquitetura dos dispositivos emulados. Isso pode acontecer. Caso isso aconteça com você, é só escolher uma outra aplicação para seguir seus estudos.

**Links utilizados neste tutorial:**<br>
**Evozi - APK Downloader:** https://apps.evozi.com/apk-downloader/<br>
**Google Play Store:** https://play.google.com/store/apps?hl=pt_BR<br>

___
# Tutorial 2: Desired Capabilities: o que são e como iniciar uma sessão com o Appium

[EM BREVE]
___
# Tutorial 3: Identificando os elementos da nossa aplicação

[EM BREVE]
___
# Tutorial 4: Realizando atividades de GESTOS via Appium
Uma das características mais marcantes quando estamos trabalhando com Android é o uso de GESTOS. Inclusive, no Android Q uma das grandes mudanças que observamos foi a inclusão de mais gestos nas atividades principais desta plataforma. Via código não é uma tarefa simples simular o arrastar de dedos do usuário para encerrar uma aplicação, por exemplo. Uma das vantagens do Appium é que ele já traz uma funcionalidade que realiza alguns gestos e os traduz em código pra gente <3 Com essa funcionalidade podemos: [DETALHAR MAIS AQUI]

[EM BREVE]

___
# Tutorial 5: Realizando um fluxo simples de teste funcional

[EM BREVE]
___
# Tutorial 6: Gravando nossas ações e transformando isso em código

[EM BREVE]
___
# Tutorial 7: Operações aritméticas com a Calculadora nativa do Android

A partir daqui, considero que o nível de dificuldade de uso e interação com o Appium cresce um pouco e passamos a trabalhar com tutoriais um pouco mais avançados.

[EM BREVE]
___
# Tutorial 8: Replicando tudo o que fiz utilizando apenas Python

[EM BREVE]
___
# Tutorial 9: Operações aritméticas com a Calculadora nativa do Android - Fase 2

[EM BREVE]
___
# Tutorial 10: Operações aritméticas com a Calculadora nativa do Android - Fase 3: organizando o código com padrões de projeto e realizando fluxo de teste funcional

[EM BREVE]
