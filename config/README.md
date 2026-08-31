# Verificação do projeto

O fiscal ajuda a manter o repositório concentrado no estudo dos dados de perfis de
poço. Ele combina regras locais, que são sempre executadas, com uma leitura
consultiva da Luna. Nenhuma recomendação da IA remove ou altera arquivos.

As regras locais bloqueiam material privado, erros de sintaxe e problemas básicos
de formatação. A Luna avalia a escrita pela Métrica de Escrita do Projeto Acadêmico
(MEPA) e procura indícios de:

- documentação que repete outro arquivo;
- testes que não correspondem mais ao comportamento do programa;
- scripts sem função identificável no fluxo atual;
- configurações sem uso e arquivos possivelmente duplicados.

Uma sugestão de remoção precisa apresentar pelo menos duas evidências. Mesmo assim,
ela permanece apenas como recomendação para revisão humana. O parecer mais recente
fica em `outputs/project_guard/luna-latest.json`, pasta que não é versionada.

## Proteção dos dados

Somente arquivos públicos de texto, aceitos pelo Git, participam da revisão externa.
LAS reais, PDFs, documentos de referência, coordenadas, saídas e arquivos ignorados
não são enviados. As solicitações usam `store: false`, para que a resposta não seja
armazenada pela API para recuperação posterior.

## Chave e modelo

A chave deve permanecer nas variáveis do usuário, nunca em um arquivo do projeto. O
fiscal procura primeiro `OPENAI_API_KEY` e também aceita o nome `open_api` por
compatibilidade. O modelo padrão é `gpt-5.6-luna`.

Para trocar o modelo ou reduzir o limite padrão de 120.000 caracteres, podem ser
usadas as variáveis `OBW_OPENAI_MODEL` e `OBW_OPENAI_MAX_CHARS`.

## Verificação antes do commit

O repositório usa o gancho versionado em `.githooks/pre-commit`. A ativação local é:

```powershell
git config core.hooksPath .githooks
git config obw.lunaRequired true
```

Quando a segunda opção está ativa, a indisponibilidade da API impede o commit. Isso
evita que uma falha silenciosa seja confundida com uma revisão aprovada.

## Acompanhamento durante a edição

O modo abaixo observa apenas textos públicos do projeto. Alterações próximas são
agrupadas por dois segundos para evitar chamadas repetidas enquanto o arquivo ainda
está sendo salvo.

```powershell
$env:PYTHONPATH = "src"
python -m obw.project_guard --watch --require-luna
```

No Windows, o projeto pode registrar esse comando para iniciar no acesso do usuário.
O monitor não examina pastas privadas e não faz chamadas quando elas são alteradas.

## Execução manual

Para verificar todos os arquivos versionados e produzir uma auditoria completa:

```powershell
$env:PYTHONPATH = "src"
python -m obw.project_guard --all --require-luna
```

Para conferir apenas os arquivos preparados para o próximo commit, retire `--all`.
O uso da Responses API, da saída estruturada e do parâmetro de armazenamento segue a
[documentação oficial da OpenAI][responses].

[responses]: https://developers.openai.com/api/reference/resources/responses/methods/create
