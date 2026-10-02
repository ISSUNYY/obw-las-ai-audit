# Protocolo da pesquisa

## Função e estado atual

Este documento concentra o escopo, as decisões metodológicas, as métricas, os
critérios de avaliação e o estado da pesquisa. O manuscrito apresenta essa proposta
em formato acadêmico; este protocolo registra suas condições de execução e revisão.

**Tema:** integração de sísmica 4D e aprendizado profundo no ajuste de histórico de
reservatórios, com previsão do avanço de água e análise de incerteza.

**Natureza:** piloto de artigo científico em fase de proposta. Existem um
[manuscrito em PDF](../artigo/piloto-artigo-cientifico.pdf) e uma
[fonte LaTeX](../artigo/piloto-artigo-cientifico.tex). Não houve implementação do
simulador, treinamento da rede, ajuste de histórico ou obtenção de resultados
experimentais próprios. O texto não declara publicação, aprovação editorial ou
originalidade já demonstrada.

O PDF foi exportado de um documento editável. Suas 15 páginas foram conferidas
visualmente. A fonte LaTeX é autossuficiente quanto ao conteúdo: inclui as 24
equações, o quadro de comparação, as duas figuras e as 12 referências. A compilação
LaTeX não foi confirmada por indisponibilidade do compilador utilizado. O PDF
disponibilizado não foi gerado por compilação dessa fonte.

## Problema, pergunta e contribuição

Dados de produção e pressão dos poços não determinam uma única distribuição de
permeabilidade. Modelos que reproduzem o histórico podem prever avanços de água
distintos entre os poços. A sísmica 4D fornece informação espacial complementar,
mas depende de física de rochas, resolução, repetibilidade e tratamento de erro.
Sua assimilação também pode exigir muitas avaliações do simulador de escoamento.

A pesquisa investigará em quais condições a integração sísmica melhora as
previsões e se uma aproximação aprendida reduz o custo total do ajuste preservando
qualidade compatível com a referência física. O benefício pretendido é produzir
previsões de avanço e produção de água mais bem sustentadas pelas observações,
com limites de confiança explícitos. Uma rede treinada, isoladamente, não será
considerada contribuição científica suficiente.

Serão avaliadas três hipóteses:

- a informação sísmica melhora a previsão futura em relação ao uso exclusivo de
  observações dos poços;
- o modelo substituto reduz o custo total com degradação de qualidade inferior a
  uma tolerância definida previamente;
- a penalização física e o tratamento do erro substituto melhoram a consistência
  das respostas e a caracterização da incerteza.

Resultados desfavoráveis também serão reportados. Redução do erro de ajuste,
isoladamente, não demonstra melhoria da previsão.

## Modelo de reservatório e observações

O caso de referência será bidimensional horizontal, óleo–água, sem gás livre,
com fluxo incompressível, pressão comum e espessura conhecida. Gravidade e
capilaridade serão omitidas. Porosidade, geometria e curvas de permeabilidade
relativa serão fixadas no ensaio de referência.

A permeabilidade positiva será parametrizada por uma base espacial com oito
coeficientes como configuração inicial, sujeita à análise de sensibilidade.
A razão de anisotropia será fixa. Heterogeneidades ausentes dessa base serão
incluídas em casos de teste para examinar o limite da representação.

O caso inicial combinará injetor de vazão prescrita e produtor de pressão
prescrita. Variáveis impostas são controles, não observações independentes
da permeabilidade. Observações dos poços incluirão somente respostas calculadas
ou medidas que não tenham sido impostas como condição de operação.

O escoamento utilizará conservação de volume, lei de Darcy, mobilidades e
transporte de saturação, com curvas do tipo Corey. O simulador de referência
será baseado no MRST. A disponibilidade do ambiente MATLAB e a compatibilidade
dos módulos serão verificadas antes da execução.

A resposta sísmica será calculada por mistura de fluidos, tensão efetiva,
relação fenomenológica para os módulos secos, Gassmann, velocidades, aproximação
de Shuey, convolução e resolução espacial explícita. Cada célula horizontal
representará uma coluna de espessura fixa com encaixantes conhecidas.

Essa formulação não representa propagação tridimensional completa, armazenamento
compressível ou geomecânica. A sensibilidade petroelástica à pressão não elimina
essas limitações do modelo de escoamento. A transferência para campo exigirá
calibração, dados compatíveis e autorização de uso.

## Função do aprendizado profundo e ajuste

O modelo substituto receberá propriedades do reservatório, estado inicial,
controles e tempos. Estimará campos de pressão e saturação; operadores físicos
converterão esses campos em respostas dos poços e diferenças sísmicas.

A arquitetura inicial combinará convoluções e recorrência temporal, comparada
a uma referência de menor porte. A orientação física será uma penalização dos
resíduos discretos de conservação e pressão. Sua contribuição será avaliada
pela retirada dessa penalização. Não se presumirá solução exata das equações
pela rede.

O ajuste inicial será realizado por ES-MDA, um método de atualização de conjuntos
de modelos com assimilação múltipla dos dados. Informação prévia e tratamento
das observações serão comuns às comparações. A covariância do erro substituto
será estimada fora do teste. Sua soma à covariância observacional dependerá de
uma hipótese explícita de independência; discrepância da física de rochas será
examinada separadamente.

Os conjuntos inicial, intermediário e final terão verificações no simulador
de referência. As previsões principais serão calculadas nesse simulador a
partir dos modelos ajustados.

## Comparações e validação

| Caso | Motor do ajuste | Observações | Comparação pretendida |
|---|---|---|---|
| A | Simulador físico | Poços | Referência sem informação sísmica |
| B | Simulador físico | Poços e sísmica 4D | Benefício da informação em relação a A |
| C | Modelo substituto | Mesmas observações de B | Efeito da aproximação e custo em relação a B |
| C₀ | Substituto sem penalização física | Mesmas observações de B | Contribuição da penalização em relação a C |

Cada realização geológica, com todos os tempos e réplicas de ruído, ficará em
uma única partição. Serão reservadas realizações independentes e um período
posterior ao último dado assimilado. Respostas futuras do caso verdadeiro não
entrarão no treinamento, na seleção de arquitetura ou na escolha de tolerâncias.
Controles futuros serão cenários prescritos comuns a todos os métodos.

Os experimentos examinarão ruído crescente e correlacionado, resolução espacial
limitada, discrepância da física de rochas e heterogeneidade não representada.
As comparações serão pareadas por caso; a reamostragem estatística utilizará
realizações completas, preservando sua dependência interna.

## Métricas e critérios de decisão

A avaliação medirá:

- erros de pressão em MPa e de saturação em fração;
- posição dos contornos do avanço de água;
- vazão e produção acumulada de água;
- tempo de chegada de água, com tratamento de casos censurados;
- cobertura e largura dos intervalos de previsão;
- custo total da geração de dados, treinamento, ajuste e verificações físicas.

As fórmulas e os modelos estão desenvolvidos no manuscrito. Unidades, operadores,
normalizações, limiares de chegada de água e tolerâncias serão fixados com dados
de validação antes de consultar o teste reservado. A cobertura será avaliada
junto à largura dos intervalos, pois intervalos arbitrariamente largos não
demonstram uma previsão útil.

O ganho de informação será avaliado por B em relação a A; o efeito do substituto,
por C em relação a B. A redução de custo somente será sustentada se incluir
geração de dados, treinamento e verificações no simulador. O custo de um caso
será distinguido do custo de reutilização em vários casos, com hardware declarado.

## Base científica e proveniência

A bibliografia completa está no manuscrito. As referências abaixo sustentam
decisões específicas do recorte:

- Nóbrega, Moraes e Emerick (2018),
  [DOI 10.1088/1742-2140/aadd68](https://doi.org/10.1088/1742-2140/aadd68):
  integração de produção e sísmica 4D em reservatório da Bacia de Campos.
- Xiao et al. (2022),
  [DOI 10.1016/j.petrol.2021.109287](https://doi.org/10.1016/j.petrol.2021.109287):
  uso de modelos substitutos no ajuste de histórico. O estudo não constitui
  validação de campo do modelo aqui proposto.
- Wang e Durlofsky (2025),
  [DOI 10.1016/j.geoen.2025.213736](https://doi.org/10.1016/j.geoen.2025.213736):
  aprendizado profundo, observações de monitoramento e ajuste de armazenamento
  de CO₂ em caso sintético. A aplicação não valida diretamente óleo–água.
- Luo, Lorentzen e Bhakta (2021),
  [DOI 10.1016/j.petrol.2020.107961](https://doi.org/10.1016/j.petrol.2020.107961):
  aprendizado de discrepâncias do modelo físico no ajuste de histórico.
- Emerick e Reynolds (2013),
  [DOI 10.1016/j.cageo.2012.03.011](https://doi.org/10.1016/j.cageo.2012.03.011):
  formulação do ES-MDA.
- Lie (2019),
  [DOI 10.1017/9781108591416](https://doi.org/10.1017/9781108591416):
  fundamentos e implementação científica do MRST.
- Lew, MacBeth e Côrte (2026),
  [DOI 10.1111/1365-2478.70195](https://doi.org/10.1111/1365-2478.70195):
  inversão 4D de pressão e saturação com aprendizado profundo. Os valores de
  NRMS de 31%, 29% e 32% da primeira figura são dados publicados desse estudo,
  redesenhados para contextualização; não são resultados do piloto nem limites
  universais de qualidade.

As buscas foram dirigidas ao problema de ajuste, aprendizado profundo, sísmica
4D e erro de modelo. Foram conferidos registros institucionais, metadados e
trechos acessíveis das publicações. Não se declara revisão sistemática exaustiva.
A segunda figura é um diagrama original do método proposto.

## Implementação, publicação e próxima investigação

Python será utilizado na organização dos experimentos e no aprendizado, com
NumPy, SciPy, PyTorch, Pandas e Matplotlib. MATLAB/MRST será o ambiente do
simulador de referência. Versões e dependências serão definidas e registradas
quando o caso numérico for implementado; não há ambiente executável publicado
nesta etapa.

Métricas serão calculadas numericamente, preservando unidades, sementes,
configurações e proveniência. A organização dos dados deverá separar controles,
estados simulados e observações, com identificação das realizações e partições.
A publicação de dados obedecerá às regras de
[privacidade](DADOS_E_PRIVACIDADE.md); a escrita e a identificação seguem seus
[documentos](GUIA_DE_ESCRITA.md) [responsáveis](IDENTIFICACAO_ACADEMICA.md).

A próxima investigação é verificar conservação e discretização no caso óleo–água
e a consistência do operador sísmico antes de gerar a base de treinamento.
Essa condição técnica não estabelece cronograma ou prazo de conclusão.

Revisão editorial desta versão: MEPA 12/14, sem critério zero. A pontuação segue
o guia de escrita: problema 2, clareza 2, precisão 2, proporção da IA 2,
naturalidade 1, economia técnica 1 e adequação 2.
