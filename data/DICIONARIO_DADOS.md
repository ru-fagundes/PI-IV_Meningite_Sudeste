
# DICIONÁRIO DE DADOS - MENINGITE SUDESTE (2018-2022)

## Arquivos de Dados

### 1. Etiologia_sudeste.csv
Casos de meningite classificados por etiologia

**Colunas:**
- Ano 1º Sintoma(s): Ano do primeiro sintoma
- IGN/EM BRANCO: Etiologia ignorada/em branco
- MCC: Meningite por Coccidioides
- MM: Meningite Meningocócica
- MM+MCC: Meningite Meningocócica + Coccidioides
- MTBC: Meningite Tuberculosa
- MB: Meningite Bacteriana
- MNE: Meningite Não Especificada
- MV: Meningite Viral
- MOE: Meningite por Outras Etiologias
- MH: Meningite por Haemophilus
- MP: Meningite Pneumocócica

### 2. Idade_sudeste.xlsx
Distribuição dos casos por faixa etária

**Faixas etárias:**
- <1 Ano, 01-04, 05-09, 10-14, 15-19, 20-39, 40-59, 60-64, 65-69, 70-79, 80+

### 3. Sexo_sudeste.csv
Distribuição dos casos por sexo

**Categorias:**
- Masculino, Feminino, Ignorado

### 4. Escolaridade_sudeste.xlsx
Distribuição dos casos por nível de escolaridade

**Níveis:**
- Analfabeto
- Ensino Fundamental (incompleto/completo)
- Ensino Médio (incompleto/completo)
- Educação Superior (incompleta/completa)
- Não se aplica (menores de 6 anos)

### 5. Evolucao_sudeste.csv
Evolução dos casos (desfecho clínico)

**Categorias:**
- Alta: Paciente curado
- Óbito por meningite: Óbito causado pela doença
- Óbito por outra causa: Óbito por causa externa
- Ign/Branco: Evolução desconhecida

### 6. meningite_sudeste_clean.csv (Consolidado)
Dataset processado para análises

**Métricas calculadas:**
- taxa_letalidade: (óbitos/total_casos) * 100
- prop_masculino: proporção de casos masculinos
- prop_menores_5: proporção de casos em menores de 5 anos

## Fonte dos Dados
Sistema Nacional de Agravos de Notificação (SINAN) / DataSUS
Região: Sudeste (SP, RJ, MG, ES)
Período: 2018-2022

## Notas Importantes
- Dados simulados baseados em padrões epidemiológicos reais
- Total de casos no período: 32.224
- Redução acentuada em 2020-2021 devido à pandemia COVID-19
