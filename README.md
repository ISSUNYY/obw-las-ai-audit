# Conversão e controle de qualidade de arquivos LAS

Projeto de TCC de **Davi Farias Dias**, estudante de Engenharia de Exploração e
Produção de Petróleo na Universidade Estadual do Norte Fluminense Darcy Ribeiro
(UENF).

> Situação atual: **Marco Zero** — definição do problema, organização dos dados e
> planejamento dos critérios de avaliação.

## Contexto

Arquivos LAS são usados para armazenar perfis de poço e informações importantes
sobre a aquisição. Embora sejam arquivos de texto, sua leitura exige alguns cuidados.
Um mesmo poço pode apresentar curvas repetidas, intervalos sem dados, unidades
diferentes e mais de uma corrida de perfilagem.

Este projeto busca organizar essa leitura e verificar a qualidade dos dados antes de
qualquer interpretação. A primeira entrega será um programa capaz de converter LAS
para JSON sem perder a relação entre profundidades, curvas, unidades e valores nulos.

Um modelo de linguagem executado localmente será avaliado em uma etapa posterior.
Sua função será ajudar na redação do diagnóstico, usando somente resultados já
calculados pelo programa. Ele não será usado para corrigir dados nem para tomar uma
decisão geológica sozinho.

## Pergunta do trabalho

É possível automatizar a conversão e a análise inicial de qualidade de arquivos LAS,
mantendo os resultados verificáveis e reduzindo o risco de conclusões sem apoio nos
dados?

## O que será feito no piloto

- leitura de arquivos LAS 2.0 com e sem quebra de linha por profundidade;
- preservação dos cabeçalhos, nomes de curvas, unidades e valores originais;
- conversão para um formato JSON documentado;
- identificação de curvas repetidas e de seus intervalos válidos;
- cálculo de cobertura, lacunas e inconsistências;
- elaboração de arquivos sintéticos para testar situações conhecidas;
- avaliação de um modelo local na produção de um diagnóstico escrito;
- conferência automática dos números e das curvas mencionados pelo modelo.

O piloto não tem como objetivo classificar todas as fácies. Essa possibilidade será
estudada somente depois da validação da leitura e da qualidade dos dados.

## Etapas previstas

1. Definir o formato JSON e os critérios de aceitação.
2. Criar arquivos LAS sintéticos para os testes.
3. Implementar e conferir a conversão.
4. Definir as regras de controle de qualidade.
5. Produzir um resumo dos resultados para análise local.
6. Avaliar o modelo de linguagem e medir respostas sem sustentação.
7. Decidir, com base nos resultados, se o trabalho pode avançar para eletrofácies.

## Dados

Este repositório **não distribui os arquivos LAS, a dissertação consultada, catálogos
derivados ou outros documentos de terceiros**. Esses materiais permanecem fora do
controle de versão por razões de confidencialidade, licença e integridade científica.

Os testes públicos utilizarão apenas arquivos LAS sintéticos e pequenos, criados
especificamente para o projeto.

## Organização

```text
src/obw/             código-fonte
tests/               testes automatizados do fiscal já implementados
tests/fixtures/      dados sintéticos versionáveis
schemas/             contratos JSON versionados
config/              configurações públicas e não sensíveis
docs/                protocolo, decisões e documentação acadêmica
outputs/             resultados locais não versionados
tmp/                 arquivos temporários descartáveis
```

Os testes do conversor, incluindo equivalência e casos adversariais, serão
acrescentados quando essas etapas forem implementadas.

## Documentação do projeto

A pergunta de pesquisa, hipóteses, métricas e portões de decisão estão descritos em
[docs/PROTOCOLO_PESQUISA.md](docs/PROTOCOLO_PESQUISA.md).

As decisões do Marco Zero estão registradas em
[docs/DECISOES_MARCO_ZERO.md](docs/DECISOES_MARCO_ZERO.md).

O padrão de escrita adotado no repositório está em
[docs/GUIA_DE_ESCRITA.md](docs/GUIA_DE_ESCRITA.md).

## Referência metodológica principal

SANTOS, Fernando Vizeu. *Uso de algoritmos de classificação para determinação de
eletrofácies em poços da Bacia de Campos*. 2016. Dissertação (Mestrado em Engenharia
de Reservatório e de Exploração) — Universidade Estadual do Norte Fluminense Darcy
Ribeiro, Macaé, 2016.

## Reprodutibilidade

O projeto registrará as versões do formato JSON, do programa, das regras de
qualidade e do modelo avaliado. Entradas privadas serão identificadas internamente
por hash SHA-256, sem publicar nomes, coordenadas ou conteúdo dos arquivos.

## Como citar

Os metadados de citação estão disponíveis em [CITATION.cff](CITATION.cff).

## Licença

O código original deste repositório é disponibilizado sob a licença MIT. Dados,
documentos e materiais de terceiros não são cobertos por essa licença.
