# Protocolo e estado atual da pesquisa

Última revisão: 31 de agosto de 2026.

## Função deste documento

Este é o documento diretor do projeto. Ele reúne o estado atual, a pergunta de
pesquisa, a relação com a dissertação de Fernando Vizeu Santos, o modelo conceitual
dos dados, as formas de avaliação e a sequência de trabalho.

O README apresenta somente uma visão geral. Regras permanentes de privacidade,
escrita, identificação acadêmica e decisões do Marco Zero permanecem nos documentos
específicos já existentes. Quando houver mudança de etapa, este protocolo deverá ser
atualizado em vez de ser criado um novo arquivo de plano ou situação do projeto.

## Estado atual

O projeto permanece no Marco Zero. A organização pública, as regras de privacidade e
o escopo inicial estão definidos, mas ainda não existem o contrato JSON, o arquivo
LAS sintético de referência, o conversor ou os testes de equivalência.

A análise dos materiais locais mostrou que o catálogo JSON legado e os programas
`main*.py` ajudam a reconstruir como os dados foram selecionados na dissertação. Eles
serão tratados como referências históricas, não como código do novo sistema.

As evidências dessa reconstrução permanecem nos materiais locais de referência, que
não podem ser publicados nem enviados à revisão externa. Antes da versão científica,
cada afirmação derivada desses materiais deverá ser confirmada por uma citação pública
da dissertação ou apresentada explicitamente como hipótese de reprodução.

A próxima entrega é a definição do contrato conceitual dos dados e de um caso
sintético mínimo. Nenhuma etapa de classificação ou uso de modelo de linguagem deve
começar antes da validação da conversão.

## Problema de Engenharia de Petróleo

Arquivos LAS podem conter curvas repetidas, diferentes nomes para o mesmo tipo de
perfil, intervalos sem dados, unidades ausentes, profundidades irregulares e mais de
uma aquisição no mesmo poço. Uma conversão que não preserve essas condições pode
alterar silenciosamente o conjunto usado em análises posteriores.

O primeiro problema do trabalho é verificar se o conteúdo relevante do LAS pode ser
representado de forma estruturada sem perda da relação entre profundidade, curva,
unidade, valor ausente e origem da aquisição.

## Pergunta principal

É possível converter arquivos LAS para uma representação estruturada e produzir um
diagnóstico inicial de qualidade mantendo cada resultado ligado a informações
verificáveis do arquivo original?

Uma etapa posterior avaliará se um modelo de linguagem local consegue explicar esse
diagnóstico sem introduzir afirmações que não estejam nos resultados calculados.

## Hipóteses de trabalho

1. Um conversor determinístico consegue preservar estrutura, valores e proveniência
   do LAS em um contrato versionado.
2. Regras explícitas de qualidade conseguem identificar problemas conhecidos em
   arquivos sintéticos sem depender de interpretação por modelo de linguagem.
3. Um modelo local pode auxiliar na redação do diagnóstico quando recebe somente um
   conjunto limitado de resultados e quando cada afirmação é verificada.

## Relação com a dissertação de Fernando Vizeu Santos

A dissertação estudou a classificação de eletrofácies a partir de perfis de poço da
bacia de Campos. Foram avaliados o número de poços usados no treinamento, os perfis
selecionados, a padronização, a redução de dimensionalidade, diferentes algoritmos e
o agrupamento de fácies que não podiam ser distinguidas adequadamente pelos perfis.

Os materiais locais indicam o seguinte fluxo operacional:

```text
catálogo JSON legado
        ↓
identificação do LAS e dos mnemônicos de cada aquisição
        ↓
leitura dos valores diretamente no LAS
        ↓
seleção das amostras consideradas válidas
        ↓
formação da matriz de perfis e da classe litológica
        ↓
padronização, treinamento, validação e comparação
```

O catálogo legado não é uma conversão completa do LAS. Ele associa arquivos e
aquisições aos mnemônicos usados pelos programas e também armazena algumas
estatísticas derivadas. Os valores numéricos dos perfis continuam sendo lidos nos
arquivos LAS.

Os cinco papéis de curva encontrados no fluxo legado são caliper (`CALI`), raios
gama (`GR`), densidade (`RHOB`), porosidade neutrônica (`NPHI`) e sônico (`DT`). A
classificação descrita na dissertação utiliza `GR`, `RHOB`, `NPHI` e `DT`. O caliper
não é uma variável de classificação, embora o código legado o inclua na regra que
descarta amostras com valores ausentes. Essa diferença deverá ser reproduzível e
também testada como uma regra alternativa.

Os programas antigos também retiram a profundidade ao formar a matriz de
classificação. O novo projeto deverá preservar essa ligação, pois ela é necessária
para localizar evidências, analisar continuidade vertical e devolver resultados à
posição correta no poço.

Outras decisões implícitas que precisam se tornar explícitas são:

- quais aquisições pertencem a cada conjunto analítico;
- como tratar aquisições sobrepostas;
- quais curvas definem a validade de uma amostra;
- como tratar uma litologia ausente ou desconhecida;
- por que um poço ou intervalo foi incluído ou excluído;
- quais transformações foram ajustadas apenas com dados de treinamento;
- como manter separados os poços de treinamento e validação.

O objetivo inicial não é reproduzir todas as classificações da dissertação. O estudo
de Vizeu serve para definir quais informações precisam ser preservadas agora para que
uma reprodução ou extensão futura seja possível.

## Modelo conceitual dos dados

O projeto trabalhará com três níveis relacionados, mas independentes.

### 1. Documento canônico do LAS

Representa o conteúdo lido sem decisão geológica ou classificação. Deve registrar:

- versão do contrato;
- hash e proveniência do arquivo de origem;
- versão do leitor;
- seções e cabeçalhos originais;
- índice de profundidade;
- mnemônico, unidade e descrição originais de cada curva;
- valores numéricos e valores ausentes;
- ordem original das curvas;
- ocorrências repetidas do mesmo mnemônico;
- avisos produzidos durante a leitura.

Nomes, unidades e valores originais não serão substituídos. Uma designação comum,
como `GR`, poderá ser acrescentada sem apagar o mnemônico recebido.

### 2. Seleção analítica

Registra como uma parte do documento canônico foi preparada para uma análise. Deve
informar:

- referência ao documento de origem;
- curvas selecionadas e motivo da seleção;
- correspondência entre papel comum e mnemônico original;
- intervalo ou aquisição utilizada;
- regra de validade das amostras;
- referências das profundidades incluídas e excluídas;
- variável de resposta, quando houver;
- contagens recalculadas para aquela seleção.

As estatísticas derivadas não serão armazenadas como se fossem dados originais. Elas
deverão indicar a regra e a versão do programa que as produziu.

### 3. Registro do experimento

Documenta uma conversão, auditoria ou classificação realizada sobre uma seleção.
Deve informar:

- entradas e respectivas versões;
- poços ou blocos usados em cada etapa;
- transformações aplicadas;
- parâmetros e versões dos métodos;
- métricas calculadas;
- resultados e limitações;
- referências para as evidências que sustentam cada conclusão.

Resultados produzidos por modelo de linguagem não poderão alterar o documento
canônico nem substituir métricas calculadas.

## Representação e eficiência

O contrato conceitual não deve obrigar todo o sistema a carregar um único JSON muito
grande na memória. A primeira versão usará JSON nos casos sintéticos porque ele é
legível e adequado para conferir a equivalência. Antes de processar conjuntos
maiores, serão comparadas representações que permitam leitura por partes, mantendo o
mesmo significado e os mesmos vínculos de proveniência.

Qualquer formato adicional será apenas uma representação física. O modelo conceitual
e as regras de preservação continuarão sendo a referência.

## Unidades de avaliação

- arquivos LAS sintéticos com comportamento conhecido;
- arquivos privados avaliados somente no ambiente local;
- documentos canônicos produzidos pelo conversor;
- resultados determinísticos do controle de qualidade;
- respostas do modelo local, apenas quando os portões anteriores forem atendidos.

## Métricas da conversão

- preservação de curvas, ordem, unidades e metadados;
- equivalência dos valores e das profundidades;
- tratamento correto de nulos e arquivos com `WRAP=YES` ou `WRAP=NO`;
- identificação de curvas e profundidades repetidas;
- determinismo entre execuções;
- tempo de execução e uso de memória.

## Métricas do controle de qualidade

- verdadeiros positivos;
- falsos positivos;
- falsos negativos;
- concordância com o resultado esperado dos casos sintéticos;
- concordância com revisão humana nos casos autorizados.

## Métricas do modelo de linguagem

- respostas válidas pelo esquema definido;
- afirmações associadas a evidência existente;
- números, curvas ou entidades sem correspondência nos resultados;
- alertas relevantes omitidos;
- consistência entre execuções;
- abstinências corretas quando faltarem informações.

## Sequência de trabalho

1. Incorporar as correções documentais do Marco Zero.
2. Definir a primeira versão do documento canônico do LAS.
3. Criar um LAS sintético mínimo e escrever manualmente o resultado esperado.
4. Definir testes de equivalência antes de implementar o leitor.
5. Implementar e validar a conversão.
6. Definir regras determinísticas de qualidade e seus casos sintéticos.
7. Produzir um conjunto compacto de resultados para o diagnóstico escrito.
8. Avaliar um modelo local e verificar automaticamente suas afirmações.
9. Decidir se existem condições para estudar classificação de eletrofácies.

## Próxima entrega

A próxima alteração deverá definir, em `schemas/`, o contrato mínimo do documento
canônico e criar, em `tests/fixtures/`, um único LAS sintético acompanhado de seu
resultado esperado. O primeiro caso deve conter profundidade, quatro curvas, unidade,
valor ausente e um mnemônico alternativo, sem qualquer dado real.

## Portões de decisão

1. O conversor não será aceito sem equivalência entre LAS e representação canônica.
2. O controle de qualidade não avançará sem casos sintéticos com resultado conhecido.
3. O modelo de linguagem só será integrado depois da validação dos cálculos.
4. O relatório só será aceito quando cada afirmação puder ser conferida.
5. A classificação só será estudada após definição das classes e validação por poço
   ou bloco de profundidade.
6. Métodos complexos só serão comparados depois de referências simples.

## Limites atuais

Não fazem parte da primeira entrega:

- classificação completa de eletrofácies;
- preenchimento automático de valores ausentes;
- alteração dos LAS originais;
- publicação de dados privados ou materiais de terceiros;
- uso de coordenadas ou identificadores reais em testes públicos;
- interpretação geológica autônoma por modelo de linguagem;
- criação de interface gráfica antes da estabilização do núcleo.

## Controle de atualização

Antes de acrescentar documentação, deve-se procurar neste protocolo e nos documentos
especializados uma seção com a mesma finalidade. A regra é atualizar a fonte já
existente, retirar trechos superados e apontar para a seção responsável. Um novo
documento só poderá ser criado quando possuir finalidade independente e após
autorização explícita.
