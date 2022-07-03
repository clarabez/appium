Projeto da disciplica de especialização em Testes Ágeis

Roteiro:
- Identificar aplicação na PlayStore (https://play.google.com/store)
- Colar o link da aplicação no Evozi (https://apps.evozi.com/apk-downloader) para fazer o download do aplicativo no formato APK
- Instalar o aplicativo Resultados em seu dispositivo Android (adb install -r NomeDoApk.apk)
- Iniciar uma sessão do Appium para o seu dispositivo iniciar a aplicação Resultados
  desired_cap = {
  'platformName': 'Android',
  'deviceName': 'ID_Aqui',
  'app':'caminho/ate/seu/apk'}
- Se preferir: realizar um fluxo através do modo Record do Appium e organizar o código na linguagem escolhida (caso prefira fazer o projeto em código corrido, sem padrão de projeto ou framework);  
- Proposição de frameworks por linguagem: python com pytest (ou unittest), java com junit (ou testng) ruby com rspec, JS com mocha - fique à vontade em escolher a que vc mais se sente confortável.
- Utilizar recursos específicos do framework escolhido para resolver problemas da sua automação (seja gerando um setUp e tearDown, seja organizando o fluxo da sua automação, seja tratando a resolução de popups de sistema pedindo acesso a serviços - como o que resolvemos via 'grantPermission' com Appium). Deixar em destaque o que utilizou a mais e como isso te ajudou no projeto.
- Utilize algum padrão de projeto (de sua preferência e escolha) para elaborar o projeto. Sinta-se livre e escolha o que melhor atenda a sua necessidade de projeto.
  
 
 Dia de entrega:
 Até dia 13/dezembro.
 
 Pode ser feito:
 individual, dupla ou trio.
 

Entregáveis esperados:
 
- O fluxo que vc optou por automatizar (por exemplo: percorrer tela de boas vindas, alcançar tela de resultados, realizar busca por prefeitura de Recife, buscar cidades em branco, listar vereadores).
- Dentro do seu código, faça comentário do que cada método/função está cobrindo em termos de cenário de teste. em python, existe o padrão @docstring para comentários em código. vale a pena dar uma olhada caso vc tenha optado por seguir com python :)


Dicas adicionais (não é obrigatório, são apenas dicas):
- Comitar projeto no seu perfil do GitHub
- Elaborar um ReadME do seu projeto explicando a estrutura, composição e dicas de como executá-lo
- Utilizar um report html para exibir os resultados da sua automação
- Utilizar recursos extras do appium (qq um!) para resolver problemas que vc encontrou na automação, e deixa uma breve explicação sobre isso.
- Vc pode utilizar o projeto HackerNews (https://github.com/clarabez/HackerNews/) para te guiar nestes aspectos de boas práticas. Não significa que ele seja o padrão esperado, vc pode ir além e tb propor sua organização, desde que seu projeto fique de fácil leitura para quem qusier utilizá-lo :)


Objetivo da disciplina:
Que vc saia dela entendendo o potencial de uso de recursos mobile como o Appium Desktop e o pacote de Appuim dentro de qualquer linguagem de programação; que vc entenda que é possível emular um dispositivo Android para resolver problemas de automação; que vc saiba como pensar em projetar uma arquitetura de automação para dispositivos móveis (e também web); que vc entenda a relação próxima que existe entre os frameworks Selenium e Appium; que vc saiba da existência de vários padrões de projeto, mas que não existe o melhor, existe o mais adequado para cada situação; que vc conheça alguns dos inúmeros benefícios de se utilizar um frameworks de teste de software dentro da sua automação.
