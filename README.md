

<div align="center">
<img src="/images/appiumwithpython.png">

<i>Material recomendado pela <a href="https://github.com/appium/appium/tree/master/sample-code/python#tutorial">documentação oficial do Appium</a>.</i>
</div>

Se este tutorial te ajudou, não esquece de deixar uma estrelinha ⭐️ 🌟
 
Este material é um guia para o setup do ambiente de configuração e uso do Appium para automação de testes funcionais em dispositivos móveis. Dentro outros aprendizados, destaco os seguintes pontos como principais aprendizados:

<ul>
    <li>Entender como funciona a ferramenta Appium e como fazer o setup desta aplicação nas plataformas: Windows, Linux e Mac;</li>
    <li>Como instanciar um dispositivo Android emulado através do Android Studio;</li>
    <li>Como instalar um aplicativo da PlayStore em seu dispositivo emulado;</li>
    <li>Como fazer mapeamento de elementos de uma aplicação em seu dispositivo;</li>
    <li>Como iniciar testes de UI em sua aplicação através do Appium com a linguagem de programação Python.</li>
</ul>

A versão em inglês deste tutorial está aqui em [appium-en](https://github.com/clarabez/appium-en).
___

🗂 **A organização do tutorial se dá nas seguintes seções:**
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
    <li>Comandos ADB></li>
    <li>Emulando um dispositivo Android através do Android Studio</li>
</ul>

___

✏️ **Tutoriais contidos aqui**

- [Tutorial 1: Instalando uma aplicação no meu dispositivo Android emulado](https://github.com/clarabez/appium/blob/master/README.md#tutorial-1-instalando-uma-aplica%C3%A7%C3%A3o-no-meu-dispositivo-android-emulado)
- [Tutorial 2: Desired Capabilities: o que são e como iniciar uma sessão com o Appium](https://github.com/clarabez/appium/blob/master/README.md#tutorial-2-desired-capabilities-como-iniciar-uma-sess%C3%A3o-com-o-appium)
- [Tutorial 3: Identificando os elementos da nossa aplicação](https://github.com/clarabez/appium/blob/master/README.md#tutorial-3-identificando-os-elementos-da-nossa-aplica%C3%A7%C3%A3o)
- [Tutorial 4: Realizando atividades de GESTOS via Appium](https://github.com/clarabez/appium/blob/master/README.md#tutorial-4-realizando-atividades-de-gestos-via-appium)
- [Tutorial 5: Realizando um fluxo simples de teste funcional](https://github.com/clarabez/appium/blob/master/README.md#tutorial-5-realizando-um-fluxo-simples-de-teste-funcional)
- [Tutorial 6: Gravando nossas ações e transformando isso em código](https://github.com/clarabez/appium/blob/master/README.md#tutorial-6-gravando-nossas-a%C3%A7%C3%B5es-e-transformando-isso-em-c%C3%B3digo)
- [Tutorial 7: Operações aritméticas com a Calculadora nativa do Android](https://github.com/clarabez/appium/blob/master/README.md#tutorial-7-opera%C3%A7%C3%B5es-aritm%C3%A9ticas-com-a-calculadora-nativa-do-android)
- [Tutorial 8: Replicando tudo o que fiz utilizando apenas Python](https://github.com/clarabez/appium/blob/master/README.md#tutorial-8-replicando-tudo-o-que-fiz-utilizando-apenas-python)
- [Tutorial 9: Operações aritméticas com a Calculadora nativa do Android - Fase 2](https://github.com/clarabez/appium/blob/master/README.md#tutorial-9-opera%C3%A7%C3%B5es-aritm%C3%A9ticas-com-a-calculadora-nativa-do-android---fase-2)
- [Tutorial 10: Operações aritméticas com a Calculadora nativa do Android - Fase 3: organizando o código com padrões de projeto e realizando fluxo de teste funcional](https://github.com/clarabez/appium/blob/master/README.md#tutorial-10-opera%C3%A7%C3%B5es-aritm%C3%A9ticas-com-a-calculadora-nativa-do-android---fase-3-organizando-o-c%C3%B3digo-com-padr%C3%B5es-de-projeto-e-realizando-fluxo-de-teste-funcional)
___

🚧 Este documento sofrerá ajustes e complementos ao longo do tempo <i>&#128513;</i>

Em breve irei disponibilizar o mesmo conteúdo em inglês e também uma solução usando o Docker, visando tornar mais prática a etapa de configuração - e também a adição de mais tecnologias aqui.

Qualquer sugestão de melhoria ou correção, por favor entrar em contato <i>&#128525;</i>

Iniciei a elaboração deste tutorial porque pra aprender essa ferramenta tive que recorrer a diferentes fontes e tive que praticar muito pra ter dicas, criar tutoriais, entender melhor a dinâmica, etc. Espero que este documento seja muito útil pra você e te incentivo a também compartilhar o que você for aprendendo <i>&#129304;</i>

___

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/intro.png">
</p>

# Um pouco sobre Appium

_Appium_ é uma ferramenta open-source e multi-plataforma (isso quer dizer que funciona em Windows, Linux e Mac) e cujo foco é de interações via UI em dispositivos móveis, possibilitando a automação de aplicações: nativas, híbridas e sites mobile para as plataformas Android e iOS.

Considero _Appium_ uma excelente ferramenta para quem quer começar a aprender automação em dispositivos móveis ou para quem já é da área de mobile e gostaria de se aprofundar mais sobre o assunto.


**Links importantes para esta seção:**

[Página oficial do Appium](http://appium.io)

[Página oficial do repo do Appium no GitHub](https://github.com/appium/)

Como dito mais acima, a finalidade do _Appium_ é testar aplicações em dispositivos móveis, e aplicações podem ser classificadas em três diferentes naturezas : nativas, híbridas e móveis. Qual a diferença entre elas?
  - **Nativas:** aquelas aplicações que foram desenvolvidas especificamente para Android ou iOS, ou seja, a partir de seus específicos SDKs.
  - **Híbridas:** aquelas que são desenvolvidas em HTML, CSS, JavaScript e que são compatíveis com qualquer plataforma (Android, iOS, Windows).
  - **Móveis:** aquelas que podemos acessar através de um link, via página web.

___

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/setup.png">
</p>

Nesta seção vamos ver os passos para realizarmos o setup do ambiente para Windows, Linux e Mac. Todos os meus projetos faço utilizando o Mac, então tendo a passar informações mais detalhadas para este SO.


✨ **Uma dica muito importante:**

Digo o que fazer para cada sistema operacional, mas você também pode optar por uma configuração mais simples (e efetiva da mesma forma) e que vai te poupar de muito tempo e dor de cabeça - confie em mim :) Se você quiser ir por esse caminho, pode pular direto para o tópico "Forma simplificada para Windows/Linux/Mac". O mesmo procedimento é utilizado para qualquer sistema operacional.

# 📥 Download de tudo que vai ser necessário

Durante o nosso workshop vamos utilizar algumas ferramentas essenciais para a prática de automação. Baixe e instale as seguintes ferramentas, que são comuns para Windows, MAC ou Linux:
  - **Appium Desktop:** é a interface da ferramenta Appium que será o foco do nosso workshop. O download está [disponível aqui:](https://github.com/appium/appium-desktop/releases/tag/v1.13.0) (aqui tem um acervo para vários Sistemas Operacionais. Baixe apenas aquele que for direcionado para o seu SO.)
  
  - **JDK (JAVA Development Kit):** https://www.java.com/pt_BR/download/ 

  - **Android Studio:** é um pacote do Android Studio que possibilita que possamos instanciar dispositivos móveis de várias configurações e modelos de forma emulada e em vários níveis de API. Para isso, é preciso baixar o Android Studio e, durante o setup, marcar a opção de instalar também o AVD: https://developer.android.com/studio/index.html?hl=pt-br
  
  - **IDE:**
  Escolha uma IDE de sua preferência para desenvolver os testes na linguagem escolhida. Como vamos focar em Python, sugiro PyCharm ou VSCode. Links abaixo para download:
  - PyCharm: https://www.jetbrains.com/pycharm/
  
  - VSCode: https://code.visualstudio.com/
  
  Depois de fazer o download de todo o conteúdo, agora podemos avançar com o setup do ambiente. Podemos configurar as variáveis de ambiente à nível de sistema (abaixo eu deixo detalhado como fazer para cada SO) e também podemos fazer de maneira bem mais simplificada, onde explico melhor após o detalhe de setup para cada SO.
  
# Variáveis de ambiente - Mac:

Depois de realizadas as instalações do Appium Desktop, JAVA, Android Studio e da sua IDE, é hora de configurarmos as variáveis de ambiente para que seu sistema operacional identifique os processos  e as aplicações de forma mais rápida e prática.
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

Quando você identificar estes caminhos em sua máquina, é hora de exportar esses valores para a variável PATH.
Para isso, confira se no diretório "/Users/user_name" existe o arquivo ".bash_profile".
Caso não exista, crie:
```bash
touch .bash_profile
```

O próximo passo é abrir o editor de texto do arquivo:
```bash
open -e ~/.bash_profile
```

Digite os comandos como sugere o exemplo a seguir e salve o arquivo:
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
3. Na seção de variáveis de sistema, dê um clique duplo em "Path" e adicione a expressão "%JAVA_HOME%\bin". Isto significa que você está adicionando o mesmo valor criado para JAVA_HOME, só que também para a pasta \bin.
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

✨ **Dica - Windows/Linux/Mac:**
Para identificar onde está a sua pasta para JAVA_HOME, é só usar o seguinte comando no terminal:
```bash
which java
```
Deverá ser retornado o caminho até seu pacote JAVA.

✨ **Dica 2 - Linux/Mac:**
Para evitar que suas variáveis de ambiente percam os valores, salve o conteúdo da variável no seu arquivo bashrc (Linux) ou bash_profile (macOS). Após salvar os valores, não esqueça de "compilar" o arquivo para as mudanças serem refletidas:
Para macOS:
```bash
source ~/.bash_profile
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

A instalação do Appium é bastante simples e não requer configuração adicional - além da do Android e do JDK. Basta baixar o Appium Desktop na página oficial do Appium(como no link do começo do documento) ou via linha de comando através do terminal:

```bash
npm install -g appium
```
**ATENÇÃO:** Não instale o Appium com sudo.

✨ **Dica - O que é npm?**

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

✨ **Dica:**
Estamos usando a flag **--android** para indicar a plataforma que vamos usar o Appium. Caso fôssemos usar o iOS, usaríamos a flag **--ios--**.

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

Se você chegou até aqui, significa que provavelmente o seu setup está pronto e agora você já pode usar todos os recursos do Appium! Só para checar, instalamos e configuramos:
- Appium Desktop **✔**
- Android Studio (pacote AVD) **✔**
- JAVA **✔**
- IDE **✔**
- Configuração de variáveis de ambiente **✔**

___

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/appiumIniciando.png">
</p>

# Iniciando com o Appium

Depois de tudo configurado, é hora de iniciarmos com o Appium Desktop.
Assim que abrimos o Appium Desktop, esta é a carinha inicial que temos contato:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/appiumFirstScreen.png">
</p>

Observe que de cara já temos 2 campos preenchidos:<br>
**HOST:** 0.0.0.0<br>
**Port:** 4723

Estes são valores padrões do Appium e indicam que sempre que você começar a realizar requisições (lembra que o Appium é baseado em servidor HTTP?), o Appium irá utilizar o Host 0.0.0.0 e o serviço irá funcionar na porta 4723. Caso você queira mudar estes valores (quando algum outro serviço já está alocado para esta porta, por exemplo), é só você realizar a customização dessa configuração manualmente clicando no botão **Advanced**, que fica ao lado do já selecionado **Simple**. Você também pode salvar suas configurações personalizadas e exportá-las através do button **Presets**. Eu, particularmente, nunca precisei utilizar nenhuma das configurações além das que já vem por padrão. Também não vi nenhum material pela internet em que fosse necessário customizar a configuração. Se quer um conselho, siga com essa configuração padrão que tudo vai funcionar bem :)

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
    'deviceName': '<InserirOnomeDoSeuDispositivoAqui>'
}
```

🚦 **Atenção:** para entender como obter o valor do nome do seu dispositivo, você vai precisar ler a seção mais adiante sobre [comandos ADB](https://github.com/clarabez/appium/blob/master/README.md#comandos-adb).

Os nomes são bem intuitivos, e aí estou criando um dicionário com a chave <i>'platformName'</i> para indicar a plataforma que irei utilizar, que pode ser: Android, Windows, iOS. 
Já o identificador do dispositivo móvel iremos inserir em <i>'deviceName'</i>, e podemos obter esse valor através do comando adb <i>'adb devices'</i> que já explicamos mais acima. Assim fica um exemplo de preenchimento destes campos básicos e ao lado já o retorno do conteúdo em JSON:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/desiredcap1.png">
</p>


**Página oficial do Appium listando todos os Desired Capabilities:** <br>http://appium.io/docs/en/writing-running-appium/caps/

___
# Emulando um dispositivo Android através do Android Studio
Podemos usar o Appium em dispositivos reais, dispositivos emulados ou até mesmo em farms de dispositivos da Amazon, que funcionam com o mesmo conceito de computação em nuvem, onde você aloca recursos sob demanda e paga apenas o que for consumido.
Durante nossos estudos podemos utilizar dispositivos emulados para a realização dos nossos testes. Isso nos dá grande versatilidade pela possibilidade de escolher o tipo de dispositivo e a versão de Android que iremos utilizar. Desta forma, é possível validar o mesmo apk em cenários diversos apenas alterando configurações, onde atingimos uma característica muito forte no Android que é a granularidade de versões: https://developer.android.com/about/dashboards?hl=pt-br

**Antes de tudo... o que é um dispositivo emulado?**<br>
É a instanciação (criação) de um dispositivo que simula um celular real, só que ele é emulado a partir dos recursos da sua máquina. É como se fosse uma máquina virtual, só que o Sistema Operacional (imagem) utilizado será alguma versão oficial do Android e o formato da máquina será uma réplica do celular de verdade, inclusive sob aspectos de tamanho das telas.

Vamos utilizar um recurso do próprio <i>Android Studio</i> para instanciarmos nosso dispositivo emulado: o <i>Android Virtual Device Manager</i>. Para acessá-lo, basta abrir o seu <i>Android Studio</i> e seguir até o seguinte ícone:

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

**Lembra quando falamos dos Desired Capabilities?** Agora podemos adicionar a configuração para abrir o emulador em conjunto com a requisição de servidor do Appium. 
Faremos isso a partir do nome que demos ao Virtual Device que cadastramos anteriormente. Assim:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/appiumAvd.png">
</p>

**Alguns pontos importantes sobre este tópico:**<br>
- Em breve farei um material falando como emular um dispositivo iOS.<br>
- Existem outras ferramentas que emulam dispositivos Androids mas, das que testei, nenhuma é tão boa quando a do Android Studio. Por esse motivo prefiro me manter nele e recomendo o uso.<br>

___

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/adb.png">
</p>

# Comandos ADB
ADB é uma abreviação para Android Debug Brigde. Grosseiramente traduzindo, é uma ferramenta que faz uma "ponte" de comunicação entre o seu computador e o seu dispositivo móvel Android através de linhas de comando. Através do ADB, é possível que possamos manipular o dispositivo através de comandos, de forma muito prática, como:
- Instalar/desinstalar aplicativos;
- Mudar configurações internas, como: tempo de desligar tela, bloqueio/desbloqueio de tela, etc.
- Habilitar/desabilitar funções de conexões, como: wifi, dados, modo avião.
- Transferência/manipulação de arquivos;
- Reiniciar e desligar o dispositivo - não funciona para ligá-lo (mas isso pode ser resolvido através de frameworks).

É também possível automatizar algumas atividades de rotina combinando comandos ADB e Python Script.

Como o assunto sobre comandos ADB merece maior aprofundamento e dedicação, criei um repositório à parte para falar mais sobre o tema: [repo comandosadb](https://github.com/clarabez/comandosadb)

**Links importantes desta seção:**<br>
**Um pouco mais sobre comandos ADB:** https://developer.android.com/studio/command-line/adb?hl=pt-br<br>
**Um pouco Python Script:** https://realpython.com/run-python-scripts/<br>
**Meu Repositório sobre Comandos ADB:** https://github.com/clarabez/comandosadb<br>

___

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/appiumtutoriais.png">
</p>

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

📝 **Sugestão de exercícios:**<br>
Tente baixar outras aplicações de sua preferência e tente instalar em seu dispositivo via comando ADB e também arrastando o pacote até seu dispositivo.

**Links utilizados neste tutorial:**<br>
**Evozi - APK Downloader:** https://apps.evozi.com/apk-downloader/<br>
**Google Play Store:** https://play.google.com/store/apps?hl=pt_BR<br>

___
# Tutorial 2: Desired Capabilities: como iniciar uma sessão com o Appium

**Para realizar este tutorial é preciso que você tenha:**<br>
<ul>
    <li>Dispositivo emulado ativo - passo a passo na seção anterior</li>
    <li>ADB configurado e funcionando em seu terminal</li>
    <li>Aplicação da Play Store já instalada no dispositivo</li>
    <li>Appium Desktop configurado e funcionando</li>
</ul>

Caso você ainda não tenha lido a seção [**Iniciando com o Appium**](https://github.com/clarabez/appium/blob/master/README.md#tutorial-2-desired-capabilities-o-que-s%C3%A3o-e-como-iniciar-uma-sess%C3%A3o-com-o-appium), recomendo que você dê um pulo lá para ler alguns conceitos que vai ajudar bastante neste segundo tutorial, especialmente porque fala da importância que são os <i>Desired Capabilites</i> para o Appium. Reforçando o que foi dito por lá, os <i>Desired Capabilites</i> são uma parte muito especial e importante quando estamos trabalhando com Appium. É a partir deles que vamos dizer o que queremos fazer exatamente utilizando o Appium.

Como mostra a [documentação oficial do Appium sobre os Desired Capabilites](http://appium.io/docs/en/writing-running-appium/caps/), temos uma extensa lista de opções de uso e podemos partir de um uso mais genérico até um uso mais específico. Aqui vamos realizar a ação destas nesses dois formatos.

**Desired Capabilities - forma genérica**

Para isso, vamos precisar identificar apenas qual o <i>platformName</i> e o <i>deviceName</i>, que querem dizer o a plataforma (Android, iOS, Windows) e o nome do produto (serial number), respectivamente. O primeiro valor é bastante simples de saber, basta indicar a plataforma que você está usando no seu estudo - durante este tutorial irei usar Android. Para saber o <i>Serial Number</i> do seu celular, é só utilizar o seguinte comando ADB em seu terminal:

```bash
    adb devices
```

O comando irá retornar algo mais ou menos assim:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/adb%20devices.png">
</p>

Assim que dou o comando <i>adb devices</i> o serviço ADB é iniciado e em seguida o valor de identificação do meu celular é retornado, que no caso foi: **emulator-5554**. É este o valor que vamos usar no campo <i>deviceName</i>. 

**Uma informação importante:** <br>Estou utilizando um celular emulado, portanto este é o valor padrão do <i>Android Device Manager</i> do <i>Android Studio</i> para 1 dispositivo emulado. Se você estiver utilizando um dispositivo real, este valor será bem diferente do que foi retornado pra mim.

Segue então valores que irei utiliar para o <i>Desired Capabilities</i>:

```bash
{
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'avd': 'AppiumP'
}
```

Agora com os valores identificados, podemos abrir o Appium até chegarmos na tela que temos a aba de <i>Desired Capabilites</i> e preencher os campos como mostra a imagem a seguir:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/desired_generic.png">
</p>

Repare que eu insiro o valor apenas na aba <i>Desired Capabilities</i> e automaticamente o Appium converte tudo em JSON na tela ao lado, onde aponto com uma seta. Uma dica que acrescento é a de salvar essa sua configuração, pois ela será a base de alguns outros tutoriais que vamos fazer. Para isso, é só clicar em **Save As**. Para acessar qualquer capability já salva, é só acessar a aba <i>Save Capability Sets</i>, que fica ao lado da aba <i>Desired Capabilities</i>.

Agora, é só clicar no botão **Start Session** que o Appium irá iniciar uma sessão com base nas informações que indicamos. Com os campos corretos e identificados (ou seja, celular detectado e compatível com o que você informou), agora podemos ver a seguinte tela:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/appimstarted1.png">
</p>

Esta é a tela de início de atividades com o Appium, que veremos nos próximos tutoriais. Aqui já é possível ver que o Appium tirou um <i>screenshot</i> da tela em que estava o nosso celular no momento em que demos início à sessão. Essa é uma das características do Appium: ele espelha a tela exatamente de onde você iniciou a sessão - em casos de uso genérico do <i>Desired Capabilities</i>. Além disso, também já vemos novos botões e novas seções. Agora vamos ver como podemos iniciar uma sessão sendo mais específicos com as informações que queremos que o Appium trate.

**Desired Capabilities - forma específica**

Vimos anteriormente como criamos uma sessão genérica com o <i>Appium</i> e conhecemos também algumas telas e algumas características à medida que fomos avançando as ações.
A finalidade de você iniciar uma sessão de forma mais específica é que vc indica ao <i>Appium</i> **exatamente** a tela que ele deve iniciar a sessão.

**Exemplo:**<br>
Vamos querer automatizar nossa calculadora nativa do Android. Como já sabemos que nosso foco será essa aplicação específica, podemos ir direto para ela, pulando o fluxo em que chamamos a aplicação através de interface gráfica. Para isso, vamos incrementar os valores de <i>Desired Capabilities</i> que já tínhamos preparado no passo anterior, só que agora precisamos dos valores para as chaves: <i>appPackage</i> e <i>appActivity</i>. Segue explicação para cada um dos campos:

**appPackage:**
<br>
É o nome do pacote da sua aplicação. Isso é definido à nível de desenvolvimento da aplicação.

**appActivity:**
<br>
Uma tela em desenvolvimento Android é chamada de activity. Este valor é basicamente para indicar em qual tela da aplicação você quer estar quando a sessão for iniciada.

**E como obter estes valores?**
<br>
Através de comando ADB! <3 Para isso, vamos para nosso celular em teste (emulado ou real) e vamos abrir a aplicação que queremos testar e vamos deixar exatamente na tela que queremos fazer nossos teses. Depois disso, vamos usar o seguinte comando no terminal:

```bash
    adb shell dumpsys window windows | grep -E 'mCurrentFocus'
```

Visualmente fica assim:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/adbcurrentfocus.png">
</p>

Note que deixo em destaque o seguinte trecho do que foi retornado na estrutura:

```bash
com.android.calculator2/com.android.calculator2.Calculator
```

Ess é trecho em que temos tanto o valor de <i>appPackage</i> quanto o de <i>appActivity</i>. A divisão entre os dois campos se dá pela / (barra) que existe bem no meio do trecho. Sempre o que tiver antes da barra será o valor do package. O que tiver depois será o do activity da sua aplicação. Agora é só copiar e preencher nos campos com mostro a seguir:

```bash
{
    'platformName': 'Android',
    'deviceName': 'emulator-5554',
    'avd': 'AppiumP',
    'appPackage': 'com.android.calculator2',
    'appActivity': 'com.android.calculator2.Calculator'
}
```

Visualmente fica assim (em destaque no JSON o que eu acrescentei):

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/desireddetailed.png">
</p>

Agora, com todos os valores preenchidos, você pode salvar novamente esta configuração clicando em <i>Save As...</i> e em seguida podemos iniciar nossa sessão clicando em <i>Start Session</i>. Quando a sessão for iniciada, você verá que agora o print da tela será direto da aplicação Calculadora, que foi a que indiquei nos campos de <i>appPackage</i> e de <i>appActivity</i>. Veja que no seu dispositivo (emulado ou real) também vai estar na mesma tela que você indicou:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/appiumdetailed.png">
</p>

📝 **Sugestão de exercícios:**<br>
Tente utilizar o comando ADB deste tutorial para identificar pacote e activity em aplicações diferentes, inclusive alguma que você baixou no Tutorial 1.

**Links Importantes para este tutorial:**<br>
Página oficial do Appium com os Desired Capabilities listados: http://appium.io/docs/en/writing-running-appium/caps/

___
# Tutorial 3: Identificando os elementos da nossa aplicação

**Para realizar este tutorial é preciso que você tenha:**<br>
<ul>
    <li>Realizado o Tutorial 2</li>
</ul>

Realizar a identificação de elementos é muito fácil quando estamos trabalhando com ferramentas/frameworks que tem o <i>webDriver</i> como base. Inclusive, a simples ação de **mapear elementos** de aplicações móveis também pode ser realizada através do UIAutomator, que é uma funcionalidade nativa também do <i>Android Studio</i>. Se você já trabalhou com Selenium, sabe que para mapearmos elementos de uma página web, basta clicar com o botão direito do mouse e selecionarmos a opção "inspecionar elementos" ou "inspecionar".

Com falei mais acima, identificar elementos é **relativamente simples**, **porém, o grande desafio** do mapeamento de elementos está em mapear de maneira inteligente e eficiente, de maneira que seu código não vá quebrar e, além disso, de maneira que a manutenabilidade do seu código não seja comprometida.
<br>
**Qual a melhor prática?** <br>
No mundo perfeito, todos os elementos de uma aplicação/página web estão identificados seguindo boas práticas de desenvolvimento, com IDs intuitivos e únicos. Outro excelente caminho é se você tem acesso aos desenvolvedores da aplicação e consegue solicitar esse tipo de ajuste a eles. Porém, sabemos que essa é uma realidade muito específica e que não estará presente na maioria das aplicações que formos interagir - especialmente agora na nossa fase de estudos.

Uma ótima prática é utilizar partes estáticas quando temos IDs dinâmicos. No caso de usar IDs dinâmicos, os seus valores serão atualizados a cada acesso, ação normalmente realizada pelo framework utilizado em nível de desenvolvimento. Uma boa dica para isso? CSS Selector.

Em algums casos você vai ter que trabalhar com hierarquia dos seus elementos. Nestas condições, opte sempre pela hierarquia mais próxima ao elemento em foco e, melhor ainda, se o elemento pai/filho possuir IDs únicos.

Outra dica, já acompanhada de um exemplo para tornar o entendimento mais claro, é poder dividir os valores (muitas vezes gigantes) que você pode encontrar por XPATH, tornando-os mais curtos:

```bash
<button type=“submit” class=“signup-button button--black button--active”>Signup Here!</button>
```

Diante deste exemplo simples de XPATH, onde vemos um valor grande, podemos tratá-lo da seguinte maneira:

```bash
WebElement signupXPath = browser.findElement(By.xpath(“//button[contains(@id, ‘signup-button’)]”));
```

Também, de forma muito similar, podemos realizar a identificação do elemento a partir de CSS Selector:

```bash
WebElement signupCSS = browser.findElement(By.cssSelector(“button[class*=‘signup-button’]”));
```

Destas formas seu elemento será sendo identificado da mesma maneira, só que agora de forma mais legível e com menor vulnerabilidade de quebra futura :)

**Qual a prática devemos evitar?** <br>
A prática ruim mais comum que vejo acontecer é o uso de XPATH longos, sem tratamentos, e uso de identificadores dinâmicos, que deixam de fazer sentido numa segunda execução - visto que ele muda a cada load da página.

**Agora identificando elementos no Appium**<br>
Para realizar a identificação de elementos, basta dar um clique no elemento que você deseja mapear e, na barra lateral direita, irá aparecer uma lista de opções de valores que você pode utilizar no seu mapeamento:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/appiumIdentifyElements.png">
</p>
<br>

No meu print, utilizei o elemento "9" e me foi retornado 2 opções: id, xpath. Como o número 9 tem ID e vejo que ele é único (clicando nos demais elementos pude perceber isso), então decidi que o valor de ID é a melhor abordagem para eu seguir na identificação dos elementos da minha calculadora.

📝 **Sugestão de exercício:**
<br>
Para praticar um pouco mais, sugiro que você vá observando a diferença entre elementos da sua aplicação. Tente também mapear elementos de alguma outra aplicação e observar se você tem o campo de ID e XPath.

___
# Tutorial 4: Realizando atividades de GESTOS via Appium

**Para realizar este tutorial é preciso que você tenha:**<br>
<ul>
    <li>Dispositivo emulado ativo - passo a passo na seção anterior</li>
    <li>ADB configurado e funcionando em seu terminal</li>
    <li>Aplicação da Play Store já instalada no dispositivo</li>
    <li>Appium Desktop configurado e funcionando</li>
</ul>
<br>
Uma das características mais marcantes quando estamos trabalhando com Android é o uso de **GESTOS**. Inclusive, no Android Q uma das grandes mudanças que observamos foi a inclusão de mais gestos nas atividades principais desta plataforma. Via código, puramente, não é uma tarefa tão simples simular o arrastar de dedos do usuário para encerrar uma aplicação, por exemplo. Uma das vantagens do Appium é que ele já traz uma funcionalidade nativa que realiza alguns gestos e os traduz em código pra gente <3

Vamos dividir este tutorial para cada uma das funcionalidades: <i>Swipe by Coordinates</i> e <i>Tap by Coordinates</i>.

**Swipe by Coordinates - deslizar o dedo numa coordenada específica**

Esta funcionalidade de fazer <i>swipe</i>, ou melhor, de deslizar o dedo na tela em uma direção é muito utilizada (especialmente no Android) para abrir menu suspenso (inferior ou superior) mudar de tela, encerrar aplicações, inserir senha personalizada de desbloquear tela, etc. No Appium, para utilizar esta funcionalidade, é só clicar no botão que está em destaque na imagem abaixo:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/SwipeByCoordinates.png">
</p>

Para exemplificar o uso dessa funcionalidade, vou realizar a ação de baixar o menu suspenso superior do dispositivo Android. Com minha sessão do Appium iniciada para o meu Android emulado, irei realizar o gesto de deslizar o dedo a partir do topo da tela até mais ou menos a metade.

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/gifcoordinates.gif">
</p>

Note que quando posicionamos o cursor do mouse na tela com a funcionalidade de <i>Swipe</i>, o canto superior esquerdo nos diz a posição do cursor em X e Y. Isso significa a localização que você está na tela e esses valores podem variar de acordo com o tamanho da sua tela. De ação, cliquei bem na margem superior no meio da tela e daí já dá pra ver um ponto indicando a localização do clique. Depois, vou um pouco pra metade pra baixo da dela e realizo outro clique. Em seguida o Appium executa a ação e o menu superior aparece no Appium e no dispositivo emulado.

**Tap by Coordinates - Clicar numa posição específica da tela**

É indiscutível a importância do gesto de toque na tela em um dispositivo móvel :) Como se trata de algo dependente de posição (X, Y) na tela, às vezes isso pode ser um desafio de tratar em automação. Esta funcionalidade também está presente no Appium e pode ser encontrara através do botão que destaco a seguir:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/TapByCoordinates.png">
</p>

Para exemplificar esta funcionalidade, irei realizar a ação de abrir um aplicativo que estiver em minha tela inicial, simplesmente tocando na exata posição que ele está na tela. Vamos ao gif demonstrativo:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/tapcoordinategif.gif">
</p>

Essa ação é composta por menos passos que o de coordenadas, visto que ele é realiza através de um único clique. Da mesma maneira, os valores de X e Y são atualizados à medida que eu vou andando com o cursor na tela. Dei um clique na localização de onde está o aplicativo Dialer (chamadas) e em seguida ele foi executado sem nenhuma ação extra.

📝 **Sugestão de exercícios:**

Tentar utilizar os funcionalidades <i>swipe</i> e <i>tap</i> em outras telas, menus e aplicações.

___
# Tutorial 5: Realizando um fluxo simples de teste funcional

Agora que já sabemos mexer bastante com as principais funcionalidades do Appium, é hora realizarmos um fluxo bem simples de teste funcional em uma aplicação. Como estamos iniciando, vou realizar este tutorial através da aplicação Calculadora nativa do Android emulado. Como estamos falando de um teste funcional, irei estruturar o teste aqui:

<b>Cenário de teste:</b><br>
Realizar operações aritméticas
<br>
<table style="width:100%">
  <caption>Caso de Teste 1 - Realizar operação de soma com 2 valores de entrada</caption>
  <tr>
    <th>Setup</th>
    <th>Passo a passo</th>
    <th>Resultado esperado</th>
  </tr>
  <tr>
    <td>1. Dispositivo conectado (real ou emulado)<br>
        2. Sessão de Appium iniciada<br>
        3. Aplicação Calculadora iniciada<br>
    </td>
    <td>1. Insira 1 entrada numérica válida<br>
        2. Aplique a operação de soma<br>
        3. Insira outra entrada numérica válida<br>
        4. Checar resultado
    </td>
    <td>
        1. Número é inserido corretamente<br>
        2. Operação inserida corretamente<br>
        3. Número inserido corretamente<br>
        4. O resultado condiz com os elementos inseridos.
    </td>
  </tr>
</table>

O caso de teste é bastante simples, vou realizar a soma dos números 2 e 3:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/soma_gif.gif">
</p>

Não tem mistério, é só clicar nos elementos seguindo o fluxo definido e verificar que no final ele retorna o resultado de forma correta. Depois vamos fazer um tutorial para validar isso através de linguagem de programação :)

___
# Tutorial 6: Gravando nossas ações e transformando isso em código

**Para realizar este tutorial é preciso que você tenha:**<br>
<ul>
    <li>Tenha um dispositivo (real ou emulado) ativo</li>
    <li>Uma sessão iniciada no Appium</li>
    <li>Calculadora inicializada</li>
</ul>

Agora é hora de conhecermos uma outra funcionalidade muito boa que o Appium traz, que é o de converter em **código de programação** qualquer ação que você realizar em seu dispositivo, seja esta ação apenas para inicializar uma aplicação, ou até para ações mais elaboradas e interessantes como os que vimos mais acima: <i>swipe</i> e <i>tap coordinates</i>.

Considero essa função uma das que torna o Appium uma excelente aplicação para automação, especialmente se você está iniciando neste mundo ou ainda não tem muito contato com alguma linguagem de programação - de forma geral ou em alguma linguagem específica. O Appium consegue converter código para as seguintes linguagens: Python, JAVA, Ruby, RobotFramework e JS.

A funcionalidade de gravar as ações fica disponível com o seguinte ícone na aplicação:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/StartRecordingIcone.png">
</p>

É só clicar neste ícone e deixar também ativa a função "Select elements", que fica ao lado esquerdo do botão <i>swipe</i>. Vou deixar em destaque na próxima imagem. Ao clicar em cada um dos ícones do teste, teremos que clicar também no botão <i>Tap</i>, que irá realizar a ação de clique no elemento. Este botão também deixo em destaque na imagem que segue: 

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/RecordTap1.png">
</p>

Agora é só realizar alguma ação e irei repetir o fluxo que fizemos no tutorial anterior, só que agora vamos gravar cada uma das ações que realizarmos:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/recordsomagif.gif">
</p>

Observe que à medida que nós vamos inserindo os dígitos na nossa calculadora, o código vai sendo gerado no campo **Recorder** que fica ao lado direito :) veja que o código já faz atribuições às variáveis que ele mesmo cria para receber elementos e assim facilitar acções como o <i>.click</i>. O código gerado será assim para Python:

```bash
el1 = driver.find_element_by_id("com.android.calculator2:id/digit_2")
el1.click()
el2 = driver.find_element_by_accessibility_id("plus")
el2.click()
el3 = driver.find_element_by_id("com.android.calculator2:id/digit_3")
el3.click()
el4 = driver.find_element_by_accessibility_id("equals")
el4.click()

```

É um código que trata apenas das interações que você faz e abstrai imports e demais recursos que você iria precisar para iniciar um projeto de automação. Porém, é possível também obter esse nível de código através do botão <i>BoilerPlate Code</i> como mostramos na imagem a seguir:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/boilerplatecode.png">
</p>

Através desta funcionalidade podemos obter todo o código gerado, inclusive com todos os imports e recursos necessários. O código fica assim para Python:

```bash
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "AppiumP"
caps["avd"] = "AppiumP"
caps["appPackage"] = "com.android.calculator2"
caps["appActivity"] = "com.android.calculator2.Calculator"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element_by_id("com.android.calculator2:id/digit_2")
el1.click()
el2 = driver.find_element_by_accessibility_id("plus")
el2.click()
el3 = driver.find_element_by_id("com.android.calculator2:id/digit_3")
el3.click()
el4 = driver.find_element_by_accessibility_id("equals")
el4.click()

driver.quit()
```

Desta forma fica muito mais tranquilo de gerar um código inicial através do Appium e depois aproveitar muita coisa que foi gerada adicionando ou alterando as partes que quisermos.

Nos tutoriais seguintes iremos focar mais no código, então vamos explicar melhor algumas partes particulares do Appium em Python.

📝 **Sugestão de exercícios:**
Agora que você já conhece também a funcionalidade de gravar suas ações e transformá-las em código, você pode realizar outros fluxos na calculadora ou até utilizar qualquer outra aplicação para gerar ações com gestos, por exemplo. Depois é só exportar o código e fazer alterações de acordo da maneira que você desejar.

___
# Tutorial 7: Operações aritméticas com a Calculadora nativa do Android

A partir daqui, considero que o nível de dificuldade de uso e interação com o Appium cresce um pouco e passamos a trabalhar com tutoriais um pouco mais avançados.

**Para realizar este tutorial é preciso que você tenha:**<br>
<ul>
    <li>Tenha um dispositivo (real ou emulado) ativo</li>
    <li>Uma sessão iniciada no Appium</li>
    <li>Calculadora inicializada</li>
</ul>

No **"Tutorial 5: Realizando um fluxo simples de teste funcional"** vimos um fluxo bem simples da operação de soma com dois números inteiros. Agora que sabemos como converter ações em código, vamos começar a elaborar um pouco mais estas ações e dar continuidade ao uso da Calculadora aplicando as demais operações aritméticas: subtração, divisão e multiplicação.

Para isso, vou mais uma vez utilizar a funcionalidade **Record** do Appium, visto que quero gerar o código destas ações através de Python. Segue gif para representar a sequência que realizei:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/oparitimeticas.gif">
</p>

Note que, como estou usando a função **Record**, o código em Python foi sendo gerado dinamicamente e ao final ficamos com o seguinte código:

```bash
# This sample code uses the Appium python client
# pip install Appium-Python-Client
# Then you can paste this into a file and simply run with Python

from appium import webdriver

caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "AppiumP"
caps["avd"] = "AppiumP"
caps["appPackage"] = "com.android.calculator2"
caps["appActivity"] = "com.android.calculator2.Calculator"

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)

el1 = driver.find_element_by_id("com.android.calculator2:id/digit_1")
el1.click()
el2 = driver.find_element_by_accessibility_id("plus")
el2.click()
el3 = driver.find_element_by_id("com.android.calculator2:id/digit_3")
el3.click()
el4 = driver.find_element_by_accessibility_id("equals")
el4.click()
el5 = driver.find_element_by_accessibility_id("multiply")
el5.click()
el6 = driver.find_element_by_id("com.android.calculator2:id/digit_2")
el6.click()
el7 = driver.find_element_by_accessibility_id("equals")
el7.click()
el8 = driver.find_element_by_accessibility_id("minus")
el8.click()
el9 = driver.find_element_by_id("com.android.calculator2:id/digit_1")
el9.click()
el10 = driver.find_element_by_accessibility_id("equals")
el10.click()
el11 = driver.find_element_by_accessibility_id("divide")
el11.click()
el12 = driver.find_element_by_id("com.android.calculator2:id/digit_2")
el12.click()
el13 = driver.find_element_by_accessibility_id("equals")
el13.click()

driver.quit()
```

Agora temos uma boa parte de código que nos dá uma ideia de como nosso projeto para automação da Calculadora deve seguir. Já temos alguns botões mapeados e também todos os operadores aritméticos.

📝 **Sugestão de exercício:**
<br><br>
Você pode continuar mapeando os demais elementos restantes da calculadora até ter o código de todos os elementos existentes na sua aplicação.

___
# Tutorial 8: Replicando tudo o que fiz utilizando apenas Python

**Para realizar este tutorial é preciso que você tenha:**<br>
<ul>
    <li>Tenha um dispositivo (real ou emulado) ativo</li>
    <li>Uma sessão iniciada no Appium</li>
    <li>Calculadora inicializada</li>
</ul>

Brincamos bastante com o Appium ao longo dos tutoriais e conhecemos as principais funcionalidades gráficas que conseguimos acessar com muita facilidade, basicamente clicando nos elementos e coletando os códigos gerados.

Agora, podemos ir direto pra IDE de sua escolha (eu estou utilizando o PyCharm durante este documento) para replicarmos tudo que já fizemos, só que agora sem interagir diretamente com o Appium. Vamos utilizá-lo agora apenas para mapear elementos que ainda não mapeamos :)

Como estou utilizando o PyCharm, então criei um novo projeto, então um novo arquivo Python e instalei os seguintes pacotes no terminal do projeto:

1. Selenium:

```bash
pip install selenium
```

2. Appium:

```bash
npm install -g appium
```

O princípio se dá importando a biblioteca necessária para que a gente possa utilizar os recursos do Appium em qualquer linguagem de programação. Lembram que já citamos acima que o Appium e o Selenium tem muita coisa em comum? Aqui a gente vê de forma mais explícita que tanto o Appium quanto o Selenium utilizam recursos da biblioteca <i>webdriver</i>, e ele que iremos importar pra dar início ao nosso projeto:

```bash
from appium import webdriver
```

Como já vimos por aqui na seção [Iniciando com o Appium](https://github.com/clarabez/appium/blob/master/README.md#iniciando-com-o-appium), o **Desired Capabilities** é uma parte super importante no Appium pois é através dele que faremos a conexão HTTP entre o Appium e o nosso dispositivo, além de indicarmos se queremos apenas iniciar o dispositivo ou se queremos iniciar numa aplicação em especial, através do uso das chaves: <i>appPackage</i> e <i>appActivity</i>. Nos exemplos anteriores já tivemos uma ideia de como isso acontece, que é através de um dicionário contendo as chaves e valores que precisamos:

```bash
caps = {}
caps["platformName"] = "Android"
caps["deviceName"] = "AppiumP"
caps["avd"] = "AppiumP"
caps["appPackage"] = "com.android.calculator2"
caps["appActivity"] = "com.android.calculator2.Calculator"
```

Foi criado um dicionário chamado <i>caps</i> indicando a plataforma, o nome do dispositivo e as informações da aplicação Calculadora. Lembrando que isso foi gerado pelo Appium, apenas copiei e colei, ainda não fizemos ajustes.

Outro ponto importante é como a conexão é estabelecida. O Appium nos retorna essa solução:

```bash
driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", caps)
```

É aí que começamos a utilizar os recursos da biblioteca <i>WebDriver</i>. Criamos uma variável chamada **driver** e dentro dela armazenamos a instância de uma nova conexão, que se dá através da chamada do recurso <i>Remote</i>. Passamos 2 parâmetros para essa chamada:
1. Localização do nosso serviço: <i>"http://127.0.0.1:4723/wd/hub"</i>, que é composto pelos valores que já conhecemos via interface do Appium. Aí está uma junção dos campos que são preenchidos de forma padrão: Remote Host + Remote Port + Remote Path.
2. <i>Desired capabilities:</i> Como já explicamos anteriormente, nós criamos um dicionário para armazenarmos as chaves e valores do que queremos que o Appium trate. Aqui é só passar o nome deste dicionário.

A partir do código gerado do Appium, fiz alguns ajustes e o começo do meu código ficou assim:

```bash
from appium import webdriver

desired_cap = {
    "platformName": "Android",
    "deviceName": "AppiumP",
    "avd": "AppiumP",
    "appPackage": "com.android.calculator2",
    "appActivity": "com.android.calculator2.Calculator"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)
```

Com isso apenas já é possível estabelecer uma sessão com o Appium utilizando o Python. Uma imagem do meu projeto inicial:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/python1.png">
</p>

Veja que assim que pedi para executar este código, em paralelo o <i>listenning</i> do Appium já abriu e começou a consumir o que eu tinha informado via código.

Em seguida, veja que o código do PyCharm finalizou a execução e, no Appium, me foi retornado o <i>status code</i> 200, que indica que obtive sucesso na minha requisição - lembre-se que no final das contas o Appium trabalha com requisições HTTP e isso fica bem explícito quando analisamos via estes logs:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/python2.png">
</p>

Como resultado destas operações, é só observarmos o nosso dispositivo (real ou emulado) que, na tela, estará presente a aplicação que estamos testando - neste caso segue sendo a Calculadora nativa do Android:

<p align="center">
<img src="https://github.com/clarabez/appium/blob/master/images/python3.png">
</p>

Por fim, veja que com poucas linhas de código em Python nós conseguimos iniciar uma sessão do Appium em um dispositivo indo diretamente para a tela da aplicação Calculadora.

📝 **Sugestão de exercício:**
<br><br>
Tente explorar alguns recursos existentes na biblioteca webdriver. Caso você não a conheça, recomendo que faça uma pesquisa sobre ela e tente explorar mais funcionalidades que ela pode oferecer ao seu projeto.

___
# Tutorial 9: Operações aritméticas com a Calculadora nativa do Android - Fase 2

**Para realizar este tutorial é preciso que você tenha:**<br>
<ul>
    <li>Tenha um dispositivo (real ou emulado) ativo</li>
    <li>Projeto do Tutorial 8</li>
</ul>


No tutorial anterior vimos como funciona a parte inicial do código em Python para o Appium: <i>imports, desired capabilities, webdriver</i>. Este início é basicamente igual (em termos de estrutura) para todos os projetos que você irá fazer utilizando Appium. Agora, vamos ver o mapeamento dos nossos elementos como números e operadores. 

Com os códigos gerados pelo Appium, obtivemos o seguinte código, bem geral:

```bash
el1 = driver.find_element_by_id("com.android.calculator2:id/digit_1")
el1.click()
el2 = driver.find_element_by_accessibility_id("plus")
el2.click()
el3 = driver.find_element_by_id("com.android.calculator2:id/digit_3")
el3.click()
el4 = driver.find_element_by_accessibility_id("equals")
el4.click()
el5 = driver.find_element_by_accessibility_id("multiply")
el5.click()
el6 = driver.find_element_by_id("com.android.calculator2:id/digit_2")
el6.click()
el7 = driver.find_element_by_accessibility_id("equals")
el7.click()
el8 = driver.find_element_by_accessibility_id("minus")
el8.click()
el9 = driver.find_element_by_id("com.android.calculator2:id/digit_1")
el9.click()
el10 = driver.find_element_by_accessibility_id("equals")
el10.click()
el11 = driver.find_element_by_accessibility_id("divide")
el11.click()
el12 = driver.find_element_by_id("com.android.calculator2:id/digit_2")
el12.click()
el13 = driver.find_element_by_accessibility_id("equals")
el13.click()
```

Agora é hora de organizarmos esse código e aproveitarmos para identificarmos todos os elementos restantes da nossa aplicação. **Uma dica muito importante:** como a aplicação da Calculadora é pequena, eu tomei a decisão de mapear todos os elementos. Porém, num projeto de automação, onde normalmente você tem aplicações e páginas complexas com muitos fluxos e elementos, faça o mapeamento apenas daquilo que você irá precisar. Caso contrário, seu trabalho será 80% focado em mapear elementos, e isso não é eficiente =)

Depois de fazer alguns ajustes, deixei meu código organizado da seguinte maneira:

```bash
from appium import webdriver

desired_cap = {
    "platformName": "Android",
    "deviceName": "emulator-5554",
    "avd": "AppiumP",
    "appPackage": "com.android.calculator2",
    "appActivity": "com.android.calculator2.Calculator"
}

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

# numbers
num1 = driver.find_element_by_id("com.android.calculator2:id/digit_1")
num2 = driver.find_element_by_id("com.android.calculator2:id/digit_2")
num3 = driver.find_element_by_id("com.android.calculator2:id/digit_3")
num4 = driver.find_element_by_id("com.android.calculator2:id/digit_4")
num5 = driver.find_element_by_id("com.android.calculator2:id/digit_5")
num6 = driver.find_element_by_id("com.android.calculator2:id/digit_6")
num7 = driver.find_element_by_id("com.android.calculator2:id/digit_7")
num8 = driver.find_element_by_id("com.android.calculator2:id/digit_8")
num9 = driver.find_element_by_id("com.android.calculator2:id/digit_9")
num0 = driver.find_element_by_id("com.android.calculator2:id/digit_0")

# operators
op_mais = driver.find_element_by_accessibility_id("plus")
op_multi = driver.find_element_by_accessibility_id("multiply")
op_menos = driver.find_element_by_accessibility_id("minus")
op_div = driver.find_element_by_accessibility_id("divide")

# common
op_igual = driver.find_element_by_accessibility_id("equals")
```

Já temos os elementos mapeados, mas como podemos realizar as operações em si? A opção mais simples e básica, é reproduzir o comportamento do teste de maneira sequencial, como deixo abaixo o exemplo de uma adição:

```bash
num1.click()
op_mais.click()
num2.click()
op_igual.click()

print('O resultado da soma foi: ', result.text)
```

Agora vimos que é possível adicionar o início de uma validação, que começamos com o print na tela do que a calculadora nos retornou no resultado da tela. Sendo assim, agora podemos comparar se o valor resultado em tela é condizente com o valor da realização da soma feita em Python. De forma simples, fiz dessa maneira:

```bash
somapython = int(num1.text) + int(num2.text)
somaappium = int(result.text)

print('O resultado da soma via Appium foi: ', somaappium)
print('O resultado da soma via Python foi: ', somapython)

assert somapython == int(result.text), 'Resultados divergentes entre o python e o Appium'
```

Minha resolução foi criar uma variável para armazenar a soma dos operadores em Python (<i>somapython</i>) e outra variável para armazenar o resultado encontrado no campo de resultado da calculadora através do Appium (<i>somaappium</i>).

Em seguida imprimo na tela o resultado dos dois campos e em seguida utilizo um <i>assert</i> para comparar os resultados. Se os resultados são iguais, a validação está OK e nada é retornado na tela. Caso contrário, isto é, se os valores forem divergentes, uma mensagem de erro é retornada no terminal: **'Resultados divergentes entre o python e o Appium'**.

O uso de <i>assertions</i> em projetos de automação para qualidade de <i>software</i> é extremamente importante. Sem o uso de <i>assertions</i> não é possível comparar o resultado obtido com o resultado esperado, ou seja, não temos como validar se o comportamento observado está de acordo com o esperado ou se é um <i>bug</i>.

📝 **Sugestão de exercício:**<br><br>
Agora que estamos trabalhando de forma mais direta com o código, sugiro que você complemente o código que já alcançamos até aqui, adicionando as outras operações como subtração, divisão e multiplicação. Não se esqueça de aplicar <i>assertions</i> e, aproveitando, também sugiro que você faça algumas pesquisas sobre isso e a importância do uso deste recurso em automação de teste de <i>software</i>.

___
# Tutorial 10: Operações aritméticas com a Calculadora nativa do Android - Fase 3: organizando o código com padrões de projeto e realizando fluxo de teste funcional

**Para realizar este tutorial é preciso que você tenha:**<br>
<ul>
    <li>Projeto do Tutorial 9</li>
</ul>


**Nota importante:**<br>
Todo o código gerado neste tutorial está commitado neste repositório :)


Até agora chegamos a um código legal, mas sem nenhum tipo de padrão. Esse tipo de código chamamos de <i>espaguette</i> já que ele é bem escorrido :)

Agora vamos organizar um pouco nosso código, separando algumas partes do que programamos e utilizando Classes, construtores e alguns conceitos de Python e Programação Orientada à Objetos.

A primeira coisa que irei fazer, é começar a utilizar alguns conceitos de padrão de projetos (não irei entrar em detalhes de padrões de projeto aqui) para tornar nosso código mais legível, mais bem estruturado para receber automação e de fácil manutenabilidade. Pra isso, irei separar o código responsável pela conexão do Appium, isolando-o num arquivo único, o qual chamarei de <i>webdriver.py</i>, que ficará numa pasta de mesmo nome:

```bash
from appium import webdriver


class Driver:
    def __init__(self):
        desired_cap = {
            'platformName': 'Android',
            'deviceName': 'AppiumP',
            'avd': 'AppiumP',
            'appPackage': 'com.android.calculator2',
            'appActivity': 'com.android.calculator2.Calculator'
        }
        self.instance = webdriver.Remote('http://localhost:4723/wd/hub', desired_cap)

```

Neste código eu apenas criei uma classe com o nome de **Driver** e dentro desta classe criei o construtor **__init__** que é onde adiciono as características dos objetos que vamos instanciar a partir desta classe. Em seguida, modifico a forma que inicio o serviço alterando de 'drive' para 'instance', assim fica mais intuitivo de mostrar que sempre que estivermos iniciando o serviço, na verdade estaremos instanciando um objeto da classe Driver.

Agora, vou criar uma pasta chamada 'pageobjects' e nesta pasta vou criar um arquivo Calc.py, onde irei registrar todos os elementos e as ações que são possíveis de serem realizadas na tela principal da aplicação Calculadora. Caso a aplicação Calculadora tivesse mais telas (ou <i>activities</i>), iríamos criar um arquivo para cada uma das telas para mantermos o código mais bem organizado.

Irei começar o arquivo Calc.py fazendo uso de mais recursos da biblioteca do Selenium, através dos seguintes <i>imports</i>:

```bash
from webdriver.webdriver import Driver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from appium.webdriver.common.mobileby import MobileBy
```

<i>Expected conditions</i>, o qual atribuo o apelido de EC - já que é uma expressão longa, é utilizado para indicar que a condição esperada irá acontecer diante da condição que eu atrelar a este recurso.<br>
<i>WebDriverWait</i> é uma excelente solução para eliminarmos o famoso uso do <i>time.sleep(10)</i> do nosso código. É um recurso que basicamente fica no aguardo da presença de algum elemento e que pode receber um valor de <i>timeout</i> indicado por você. Gosto de usar o valor 10.<br>
<i>MobileBy</i> é o recurso responsável por indicar que estamos em um contexto de dispositivo móvel, daí então podemos acessar tipos de IDs relacionados a este contexto.

Depois dos imports, é hora de criarmos uma classe, a qual dei o nome de Calculadora. Para esta classe também criei um construtor para identificarmos os elementos que caracterizam a nossa classe e, consequentemente, os objetos que iremos instanciar a partir dela. Além dos elementos, também iremos criar os métodos relacionados aos comportamentos da nossa classe que, para a nossa calculadora, iremos definir que são as ações de somar, subtrair, multiplicar e dividir.

Antes de iniciar a reestruturação da identificação dos nossos elementos, vale dizer que todos os nossos dígitos numéricos (do 0 ao 9) possuem a mesma estrutura, mudando apenas o último dígito do valor do elemento. Com isso, podemos tentar usar uma estratégia diferente para otimizar isso. Então, decidi criar um método para tratar disso. Portanto, irei mapear agora apenas os elementos de operações e os mais gerais como o de resultado. Nosso mapeamento fica assim:

```bash
class Calculadora:
    def __init__(self, driver):
        self.driver = driver
        self.result = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located(
            MobileBy.ID, 'com.android.calculator2:id/result'
        ))
        self.soma = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located(
            MobileBy.ACCESSIBILITY_ID, 'plus'
        ))
        self.divisao = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located(
            MobileBy.ACCESSIBILITY_ID, 'divide'
        ))
        self.multiplicacao = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located(
            MobileBy.ACCESSIBILITY_ID, 'multiply'
        ))
        self.subtracao = WebDriverWait(self.driver.instance, 10).until(EC.presence_of_element_located(
            MobileBy.ACCESSIBILITY_ID, 'minus'
        ))
```

Depois de mapeados os elementos, é hora de iniciarmos a elaboração dos métodos da nossa Calculadora. Como falei mais acima, também irei utilizar um método para tratar a identificação dos dígitos, visto que a estrutura de todos são idênticas, mudando apenas o último dígito. Meu código ficou assim:

```bash
    def clicknumber(self, numero):
        _num = str(numero)
        self.driver.instance.find_element(MobileBy.ID, 'com.android.calculator2:id/digit_' + _num).click()
        assert _num in self.result.text, 'Resultado no result não é o esperado com o valor inserido'
```

Esta solução é uma sugestão para termos um código mais enxuto. Você pode fazer algo parecido para aplicarmos o operador.

Agora, também irei utilizar a biblioteca _unitTest_ para controlarmos o fluxo de testes da nossa aplicação. Através desta biblioteca iremos utilizar os métodos _setUp()_ e _tearDown()_. São métodos que fazem muito sentido em projetos de testes, pois o setUp tem por objetivo preparar o que é necessário para iniciarmos os testes, enquanto que o tearDown finaliza a execução encerrando os serviços que foram iniciados durante a execução.
Para organizar isso em um padrão de projetos, irei criar uma pasta chamada "tests" e, dentro desta pasta irei criar um arquivo Python de nome CalculadoraTestes.py, onde farei os imports dos arquivos que fazem parte do meu projeto e, na construção da classe irei definir que esta classe será do tipo casos de teste (unittest.TestCase). Este arquivo será muito simples e nele faremos o setUp, o tearDown e (atenção para esta parte) criaremos métodos que irão realizar nossos testes. Todo método que começar com "test" será executado já que inserimos a biblioteca unitTest. A ordem de execução será de acordo com a distribuição dos métodos neste arquivo.

Bem, em resumo, nossa estrutura terá as seguintes pastas:
- Webdriver: Aqui iremos isolar a conexão do nosso serviço.

- PageObjects: Aqui será o mapeamento da nossa aplicação. Para cada página, uma classe dedicada - não necessariamente em arquivos separados. Todos os elementos e todas as funcionalidades da página serão identificados e trabalhados aqui.

- Tests: Aqui iremos criar nossos métodos de inicialização, finalização e elaboração dos nossos testes. SetUp é o método responsável por inicializar a execução. Setup é o responsável por finalizar a execução. Todo método iniciado com "test" será executado como teste. Essas funcionalidades são abstraídas graças ao uso da biblioteca _unitTest_.

Desta maneira, finalizamos os tutoriais do início do uso do Appium testando nossa aplicação Calculadora nativa do Android.

📝 **Exercícios sugeridos:**

- Como não entramos em detalhes do que são padrões de projeto e quais os padrões especificamente devemos usar, eu deixo como sugestão a pesquisa sobre padrões de projeto em Python, especialmente para automação de teste de <i>software</i>.
- Explorar os recursos existentes na biblioteca Selenium.
- Explorar os recursos e o uso da biblioteca unitTest.
- Com base no método que deixei para a soma, você pode criar ou demais métodos para os outros operadores como multiplicação, divisão e multiplicação.
- Gostaria de de ampliar seu projeto e realizar a automação do modelo Calculadora Científica? Esse é o momento! =)
- Gostaria de aplicar estes conceitos a alguma aplicação que vc baixou na PlayStore? Esta também é uma excelente oportunidade! Não se esqueça de compartilhar seu projeto com a comunidade <3
