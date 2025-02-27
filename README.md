# testetargert
testes
https://github.com/Maicolc137/Desenvolvedor-de-Sistemas-Jr..git
1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0;
Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; }
Imprimir(SOMA);
Ao final do processamento, qual será o valor da variável SOMA?



O código inicializa INDICE como 13, SOMA como 0 e K como 0.

Em um loop while, ele incrementa K e adiciona K à SOMA até que K seja igual a INDICE.

No final, ele imprime o valor de SOMA, que será a soma dos números de 1 a 13.



O código processa a lista de dicionários dados, que contém os valores de cada dia.

Ele calcula a soma de todos os valores usando a função sum() e uma compreensão de lista.

No final, ele imprime a soma dos valores.


A primeira parte do código imprimirá SOMA: 91, que é a soma dos números de 1 a 13.

A segunda parte do código imprimirá a soma de todos os valores presentes na lista de dicionários.


2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

Implementação da Sequência de Fibonacci: Vamos criar uma função que gera a sequência de Fibonacci até um determinado limite ou até que o próximo número da sequência seja maior que o número informado.

Verificação de Pertencimento à Sequência: Após gerar a sequência, verificaremos se o número informado pertence à sequência.

O código ignora valores zero (0.0) na verificação dos dados fornecidos, pois zero não é considerado um número válido para a sequência de Fibonacci no contexto do problema.

A sequência de Fibonacci é gerada dinamicamente até o número informado, o que garante que a verificação seja eficiente.



3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
• O menor valor de faturamento ocorrido em um dia do mês;
• O maior valor de faturamento ocorrido em um dia do mês;
• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

IMPORTANTE:
a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

Filtragem de dias com faturamento: Ignoramos os dias com valor 0.0 (finais de semana e feriados).

Cálculo do menor e maior faturamento: Usamos as funções min e max para encontrar os valores extremos.

Cálculo da média mensal: Somamos os valores de faturamento dos dias válidos e dividimos pelo número de dias com faturamento.

Contagem de dias acima da média: Verificamos quantos dias tiveram faturamento superior à média.
O código pode ser adaptado para ler diretamente de um arquivo JSON ou XML, se necessario.


4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:
• SP – R$67.836,43
• RJ – R$36.678,66
• MG – R$29.229,88
• ES – R$27.165,48
• Outros – R$19.849,53

Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.  

Dados de Faturamento por Estado: um dicionario faturamento_estados onde cada chave é um estado e o valor é o faturamento correspondente.

Dados de Faturamento Diário: Temos uma lista de dicionários faturamento_diario, onde cada dicionário contém o dia e o valor de faturamento correspondente.

Cálculo do Total Mensal: Somamos todos os valores de faturamento diário para obter o total mensal.

Cálculo dos Percentuais: Para cada estado, calculando o percentual de representação dividindo o faturamento do estado pelo total mensal e multiplicando por 100.

Exibição dos Resultados: Por fim, exibimos o percentual de representação de cada estado.

5) Escreva um programa que inverta os caracteres de um string.

IMPORTANTE:
a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
b) Evite usar funções prontas, como, por exemplo, reverse;

NÃO SE ESQUEÇA DE INSERIR O LINK DO SEU REPOSITÓRIO NO GITHUB COM O CÓDIGO FONTE QUE VOCÊ DESENVOLVEU

função inverter_string:

Recebe uma string s como entrada.

Inicializa uma variável string_invertida como uma string vazia.

Usa um loop for para percorrer a string de trás para frente. O loop começa no último índice (len(s) - 1) e vai até o primeiro índice (0), decrementando (-1) a cada iteração.

A cada iteração, o caractere correspondente é concatenado à variável string_invertida.

Retorna a string invertida.

tipo:

Define uma string de exemplo ("Hello, World!").

Chama a função inverter_string para inverter a string.

Exibe a string original e a string invertida.
