# Dados, privacidade e publicação

## Classificação dos materiais

| Material | Classificação | Publicação |
|---|---|---|
| Código original | Público | Permitida sob MIT |
| Documentação original | Pública | Permitida |
| Esquemas e regras genéricas | Públicos | Permitida |
| Fixtures LAS sintéticas | Públicas | Permitida |
| LAS reais | Privados/restritos | Proibida sem autorização |
| Coordenadas e identificadores | Sensíveis | Proibida por padrão |
| Dissertações e artigos | Terceiros | Apenas referência bibliográfica |
| Tokens e chaves | Secretos | Sempre proibida |
| Saídas derivadas de dados reais | Restritas | Revisão antes da publicação |

## Revisão antes de publicar

Todo artefato derivado deve ser verificado quanto a:

- nomes e identificadores de poços;
- coordenadas;
- caminhos pessoais;
- metadados de aquisição;
- segredos e tokens;
- conteúdo protegido de terceiros;
- possibilidade de reidentificação por combinação de atributos.

## Uso de serviços externos

O fluxo principal será local. Serviços externos somente poderão receber dados
sintéticos, anonimizados ou formalmente autorizados.

