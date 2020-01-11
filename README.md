# Objetivo do documento

Este material é um guia para o setup do ambiente de configuração e uso do Appium para automação de testes móveis. Aqui você vai: 
1. Entender como funciona o Appium e como fazer mapeamento de elementos de uma aplicação;
2. Como instanciar um dispositivo Android emulado através do Android Studio; 
3. Como organizar o código de uma automação utilizando padrões de código como o PageObjects; 
4. Como escrever testes através do framework PyTest.

Muito provavelmente este documento sofrerá ajustes e complementos ao longo do tempo :)

Em breve irei disponibilizar o mesmo conteúdo em inglês e também uma solução usando o Docker, visando tornar mais prática a etapa de configuração.

Qualquer sugestão de melhoria ou correção, por favor entrar em contato <3

# Um pouco sobre Appium

Appium é uma ferramenta open-source e multi-plataforma com foco em automação de aplicações: nativas, híbridas e sites mobile para as plataformas Android e iOS.

**Página oficial:** http://appium.io

**Página oficial do repo no GitHub:** https://github.com/appium/

# Nativas, híbridas e móveis? Qual a diferença entre elas?
  - **Nativas:** aquelas aplicações que foram desenvolvidas especificamente para Android ou iOS, ou seja, a partir de seus específicos SDKs.
  - **Híbridas:** aquelas que são desenvolvidas em HTML, CSS, JavaScript e que são compatíveis com qualquer plataforma (Android, iOS, Windows).
  - **Móveis:** aquelas que podemos acessar através de um link, via página web.

# Iniciando o Setup - Download

Durante o nosso Learning Session vamos utlizar algumas ferramentas essenciais para a prática de automação. Baixe e instale as seguintes ferramentas:
  - **Appium Desktop:** é a interface da ferramenta Appium que será o foco do nosso workshop. O download está disponível aqui: https://github.com/appium/appium-desktop/releases/tag/v1.13.0 (aqui tem um acervo para vários Sistemas Operacionais. Baixe apenas aquele que for direcionado para o seu SO.)
  
  - **JAVA:** https://www.java.com/pt_BR/download/ 

  - **Android Virtual Device (AVD):** é um pacote do Android Studio que possibilita que possamos instaciar dispositivos móveis de várias configurações e modelos de forma emulada e em vários níveis de API. Para isso, é preciso baixar o Android Studio e, durante o setup, marcar a opção de instalar também o AVD: https://developer.android.com/studio/index.html?hl=pt-br
  
  - **PyCharm** (ou alguma outra IDE de sua preferência e que dê suporte a Python): https://www.jetbrains.com/pycharm/
  
  - **VSCode** (caso seja sua IDE de preferência. Basta escolher entre o PyCharm e o VSCode): https://code.visualstudio.com/
  
# Setup - Variáveis de ambiente:

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

**Dica:**
Para identificar onde está a sua pasta para JAVA_HOME, é só usar o seguinte comando no terminal:
```bash
which java
```
Deverá ser retornado o caminho até seu pacote JAVA.

**Dica 2:**
Para evitar que suas variáveis de ambiente percam os valores, salve o conteúdo da variável no seu arquivo bashrc (Linux) ou bash_profile (macOS). Após salvar os valores, não esqueça de "compilar" o arquivo para as mudanças serem refletidas:
Para macOS:
```bash
source ~./bash_profile
```

Para Linux:
```bash
source ~/.bashrc
```
___

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
# Checklist

Se você chegou até aqui, significa que provavelmente o seu setup está pronto e agora você já pode usar todos os recursos do Appium! Só para checar, instalamos e configuramnos:
- Appium Desktop
- Android Studio (pacote AVD)
- JAVA
- IDE
- Configuração de variáveis de ambiente

___
# Iniciando com o Appium

Depois de tudo configurado, é hora de iniciarmos com o Appium Desktop.
