# Piloto de artigo científico

**Integração de sísmica 4D e aprendizado profundo no ajuste de histórico de reservatórios**

Previsão do avanço de água e análise de incerteza

**Autor:** Davi Farias Dias · Universidade Estadual do Norte Fluminense Darcy Ribeiro (UENF)

Diferentes distribuições de permeabilidade podem explicar os dados dos poços e,
ainda assim, prever avanços de água distintos no reservatório. Esta pesquisa propõe
avaliar se a sísmica 4D reduz essa ambiguidade e se um modelo de aprendizado profundo
permite incorporar essa informação ao ajuste de histórico com menor custo
computacional e incerteza bem caracterizada.

## Leitura do projeto

- [Manuscrito em PDF](artigo/piloto-artigo-cientifico.pdf)
- [Fonte LaTeX do manuscrito](artigo/piloto-artigo-cientifico.tex)
- [Protocolo da pesquisa e estado atual](docs/PROTOCOLO_PESQUISA.md)

O manuscrito desenvolve o problema, as hipóteses, a fundamentação, as equações e os
experimentos propostos. É um piloto de artigo científico em fase de proposta;
não apresenta resultados experimentais próprios nem constitui artigo publicado
em periódico. O simulador, a rede e o ajuste ainda não foram implementados neste
repositório.

## Recorte científico

O estudo utilizará um reservatório sintético bidimensional óleo–água. Um simulador
físico fornecerá a referência de pressão, saturação e produção; um operador
petroelástico produzirá as observações sísmicas. A rede aprenderá a aproximar o
escoamento para auxiliar o ajuste dos modelos de permeabilidade. As previsões
principais serão verificadas no simulador físico.

As comparações separarão o benefício da informação sísmica do efeito da aproximação
aprendida. A avaliação examinará previsões futuras, avanço e produção de água,
incerteza e custo total. As hipóteses físicas, os critérios e as limitações estão
no [protocolo](docs/PROTOCOLO_PESQUISA.md); as referências científicas completas
estão no manuscrito.

## Organização e publicação

`artigo/` reúne o PDF e sua fonte textual. `docs/` reúne o protocolo, as regras de
[dados e privacidade](docs/DADOS_E_PRIVACIDADE.md), o
[guia de escrita](docs/GUIA_DE_ESCRITA.md) e a
[identificação acadêmica](docs/IDENTIFICACAO_ACADEMICA.md).

O PDF foi exportado de um documento editável e revisado visualmente. A fonte
LaTeX contém o mesmo conteúdo, com equações e figuras no próprio arquivo; sua
compilação ainda não foi confirmada. Dados privados, documentos de terceiros,
saídas de trabalho e configurações de agentes ficam fora da publicação.

Os materiais originais deste repositório mantêm a [licença MIT](LICENSE).
As obras citadas conservam seus próprios direitos e não são redistribuídas aqui.

Para citar esta proposta: DIAS, Davi Farias. *Integração de sísmica 4D e aprendizado
profundo no ajuste de histórico de reservatórios: previsão do avanço de água e
análise de incerteza*. Piloto de artigo científico. UENF, 2026.
[Repositório](https://github.com/ISSUNYY/piloto-artigo-cientifico).
