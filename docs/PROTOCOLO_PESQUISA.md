# Protocolo de pesquisa

## Pergunta principal

É possível converter arquivos LAS para uma estrutura JSON confiável e usar uma IA
local para explicar problemas de qualidade sem aceitar afirmações não sustentadas
pelos dados?

## Hipótese

Uma arquitetura híbrida, na qual cálculos são determinísticos e a IA atua apenas
sobre evidências estruturadas, reduz a aceitação de afirmações não sustentadas sem
eliminar a utilidade da explicação automática.

## Unidades de avaliação

- arquivos LAS sintéticos com comportamento conhecido;
- arquivos LAS privados mantidos fora do repositório;
- respostas estruturadas geradas pela IA;
- achados e evidências conferidos automaticamente.

## Métricas da conversão

- curvas e metadados preservados;
- equivalência de valores e profundidades;
- tratamento correto de nulos e arquivos wrapped;
- determinismo entre execuções;
- tempo e memória.

## Métricas do controle de qualidade

- verdadeiros positivos;
- falsos positivos;
- falsos negativos;
- concordância com revisão humana.

## Métricas da IA

- respostas válidas pelo esquema;
- afirmações com evidência existente;
- números ou entidades inventadas;
- alertas omitidos;
- consistência entre execuções;
- abstinências corretas.

## Portões de decisão

1. A IA só será integrada após equivalência LAS-JSON comprovada.
2. O relatório só será aceito após validação das evidências.
3. A classificação só será estudada após definição das classes e validação por poço.
4. Modelos complexos só serão comparados depois de baselines simples.

