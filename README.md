# OBW LAS AI Audit

Pipeline local, rastreável e assistido por inteligência artificial para conversão,
normalização e auditoria de qualidade de arquivos LAS.

> Status: **Marco Zero** — governança, contrato de dados e protocolo de pesquisa.

## Objetivo

O projeto investiga se arquivos LAS podem ser convertidos para uma representação
JSON confiável e auditados por uma IA local sem aceitar afirmações que não estejam
sustentadas por evidências calculadas.

O princípio da arquitetura é:

> O programa calcula. A IA explica. O verificador confere.

O modelo de linguagem não será responsável por alterar dados, preencher valores
ausentes ou classificar litologias no piloto inicial.

## Escopo do piloto

- leitura determinística de LAS 2.0, incluindo `WRAP=YES` e `WRAP=NO`;
- preservação dos metadados, curvas, unidades e valores originais;
- conversão versionada para JSON;
- normalização de curvas por regra explícita e intervalo;
- controle de qualidade calculado por código;
- geração de um pacote compacto de evidências;
- auditoria explicativa com modelo local via Ollama;
- validação automática das evidências citadas pela IA;
- medição de respostas inválidas, omissões e afirmações não sustentadas.

Classificação de eletrofácies, continuidade vertical e física de rochas são linhas
de evolução posteriores ao piloto.

## Arquitetura prevista

```text
LAS imutável
    -> parser e validação
    -> normalização por intervalo
    -> JSON canônico
    -> controle de qualidade determinístico
    -> pacote de evidências
    -> IA local
    -> verificador de afirmações
    -> relatório aceito ou rejeitado
```

## Dados

Este repositório **não distribui os arquivos LAS, a dissertação consultada, catálogos
derivados ou outros documentos de terceiros**. Esses materiais permanecem fora do
controle de versão por razões de confidencialidade, licença e integridade científica.

Os testes públicos utilizarão apenas arquivos LAS sintéticos e pequenos, criados
especificamente para o projeto.

## Organização

```text
src/obw/             código-fonte
tests/               testes unitários, integrados e adversariais
tests/fixtures/      dados sintéticos versionáveis
schemas/             contratos JSON versionados
config/              configurações públicas e não sensíveis
docs/                protocolo, decisões e documentação acadêmica
outputs/             resultados locais não versionados
tmp/                 arquivos temporários descartáveis
```

## Protocolo de pesquisa

A pergunta de pesquisa, hipóteses, métricas e portões de decisão estão descritos em
[docs/PROTOCOLO_PESQUISA.md](docs/PROTOCOLO_PESQUISA.md).

As decisões do Marco Zero estão registradas em
[docs/DECISOES_MARCO_ZERO.md](docs/DECISOES_MARCO_ZERO.md).

## Referência metodológica principal

SANTOS, Fernando Vizeu. *Uso de algoritmos de classificação para determinação de
eletrofácies em poços da Bacia de Campos*. 2016. Dissertação (Mestrado em Engenharia
de Reservatório e de Exploração) — Universidade Estadual do Norte Fluminense Darcy
Ribeiro, Macaé, 2016.

## Reprodutibilidade

O projeto registrará versões do esquema, parser, regras de qualidade, prompt e
modelo local. Entradas privadas serão identificadas internamente por hash SHA-256,
sem publicar nomes, coordenadas ou conteúdo dos arquivos.

## Como citar

Os metadados de citação estão disponíveis em [CITATION.cff](CITATION.cff).

## Licença

O código original deste repositório é disponibilizado sob a licença MIT. Dados,
documentos e materiais de terceiros não são cobertos por essa licença.

