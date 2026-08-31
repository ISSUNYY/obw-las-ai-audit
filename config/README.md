# Verificação do projeto

O repositório executa uma verificação antes de cada commit. O gancho confere os
arquivos preparados no Git e bloqueia:

- material privado ou de referência;
- texto fora de UTF-8;
- espaços no fim das linhas;
- linhas acima de 100 caracteres;
- arquivos sem quebra de linha final;
- Markdown sem título principal ou sem espaço após títulos;
- títulos Markdown repetidos;
- sintaxe inválida em Python, JSON ou TOML.

Quando um documento público é alterado, o programa também pode solicitar ao Gemini
uma revisão de coerência e da Métrica de Escrita do Projeto Acadêmico (MEPA). Somente
documentos públicos versionados podem ser enviados. LAS, PDFs, referências, saídas,
coordenadas e arquivos ignorados são recusados antes da chamada externa.

## Ativação local

O repositório usa o gancho versionado em `.githooks/pre-commit`. Para ativá-lo:

```powershell
git config core.hooksPath .githooks
```

A chave deve ser armazenada na variável de ambiente `GEMINI_API_KEY`, nunca em um
arquivo do projeto. No Windows, ela pode ser criada em **Variáveis de Ambiente >
Variáveis do usuário**. É necessário abrir um novo terminal depois da alteração.

O modelo padrão é `gemini-3.5-flash-lite`. Outro modelo pode ser escolhido com a
variável `OBW_GEMINI_MODEL`.

Para controlar custo e evitar o envio acidental de documentos muito grandes, uma
revisão aceita no máximo 60.000 caracteres por padrão. O limite pode ser reduzido com
`OBW_GEMINI_MAX_CHARS`.

Por padrão, a indisponibilidade da API produz um aviso, mas não impede o commit se a
verificação determinística tiver sido aprovada. Para exigir a revisão Gemini:

```powershell
git config obw.geminiRequired true
```

Essa opção deve ser ativada somente depois que a chave tiver sido configurada. Para
voltar ao modo tolerante a indisponibilidade externa:

```powershell
git config obw.geminiRequired false
```

## Execução manual

Para verificar todos os arquivos versionados:

```powershell
$env:PYTHONPATH = "src"
python -m obw.project_guard --all
```

Para conferir apenas os arquivos preparados para o próximo commit, execute o comando
sem `--all`.

As formas atuais de autenticação e resposta estruturada podem ser conferidas na
[documentação de chaves](https://ai.google.dev/gemini-api/docs/api-key) e na
[documentação de saída JSON](https://ai.google.dev/gemini-api/docs/structured-output).
