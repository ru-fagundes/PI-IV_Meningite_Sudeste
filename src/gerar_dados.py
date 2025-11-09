"""
Script para gerar dados simulados de Meningite - Região Sudeste (2018-2022)

Este script cria todos os arquivos CSV/Excel necessários para o projeto,
com dados simulados baseados em padrões epidemiológicos reais do SINAN/DataSUS.

Autor: Rubia Fagundes
Data: Outubro 2024

Como usar:
1. Salve este arquivo como "gerar_dados.py"
2. Execute: python gerar_dados.py
3. Os arquivos serão criados na pasta "data/raw/"
"""

import pandas as pd
import numpy as np
import os

# Criar estrutura de pastas
os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)

print("="*80)
print("GERADOR DE DADOS - ANÁLISE DE MENINGITE SUDESTE")
print("="*80)

# ============================================================================
# 1. DADOS DE ETIOLOGIA
# ============================================================================

print("\n📊 Gerando arquivo: Etiologia_sudeste.csv")

etiologia_data = {
    'Ano 1º Sintoma(s)': ['2018', '2019', '2020', '2021', '2022', 'Total'],
    'IGN/EM BRANCO': [14.0, 12.0, 8.0, 9.0, 10.0, 53.0],
    'MCC': [194.0, 188.0, 69.0, 50.0, 92.0, 593.0],
    'MM': [224.0, 213.0, 111.0, 59.0, 130.0, 737.0],
    'MM+MCC': [183.0, 164.0, 47.0, 38.0, 65.0, 497.0],
    'MTBC': [118.0, 100.0, 72.0, 72.0, 94.0, 456.0],
    'MB': [1495.0, 1276.0, 623.0, 548.0, 953.0, 4895.0],
    'MNE': [941.0, 935.0, 507.0, 533.0, 1035.0, 3951.0],
    'MV': [5950.0, 5063.0, 1835.0, 1509.0, 3145.0, 17502.0],
    'MOE': [251.0, 238.0, 159.0, 158.0, 209.0, 1015.0],
    'MH': [78.0, 96.0, 18.0, 38.0, 85.0, 315.0],
    'MP': [614.0, 584.0, 171.0, 207.0, 617.0, 2193.0],
    'Total': [10066.0, 8869.0, 3622.0, 3222.0, 6445.0, 32224.0]
}

df_etiologia = pd.DataFrame(etiologia_data)
df_etiologia.to_csv('data/raw/Etiologia_sudeste.csv', index=False, sep=';', encoding='latin1')
print("   ✅ Arquivo criado: data/raw/Etiologia_sudeste.csv")

# ============================================================================
# 2. DADOS DE IDADE
# ============================================================================

print("\n📊 Gerando arquivo: Idade_sudeste.xlsx")

idade_data = {
    'Ano 1º Sintoma(s)': ['2018', '2019', '2020', '2021', '2022', 'Total'],
    'Em branco/IGN': ['-', '-', '-', '-', '-', '-'],
    '<1 Ano': [1735, 1496, 886, 737, 862, 5716],
    '01-04': [2240, 2020, 413, 318, 1451, 6442],
    '05-09': [1301, 1097, 190, 164, 809, 3561],
    '10-14': [577, 464, 167, 139, 288, 1635],
    '15-19': [373, 323, 152, 123, 213, 1184],
    '20-39': [1665, 1515, 720, 659, 1029, 5588],
    '40-59': [1325, 1148, 645, 625, 1033, 4776],
    '60-64': [290, 266, 130, 124, 209, 1019],
    '65-69': [205, 217, 104, 127, 178, 831],
    '70-79': [247, 219, 156, 144, 260, 1026],
    '80 e +': [108, 104, 59, 62, 113, 446],
    'Total': [10066, 8869, 3622, 3222, 6445, 32224]
}

df_idade = pd.DataFrame(idade_data)
df_idade.to_excel('data/raw/Idade_sudeste.xlsx', index=False)
print("   ✅ Arquivo criado: data/raw/Idade_sudeste.xlsx")

# ============================================================================
# 3. DADOS DE SEXO
# ============================================================================

print("\n📊 Gerando arquivo: Sexo_sudeste.csv")

sexo_data = {
    'Ano 1º Sintoma(s)': ['2018', '2019', '2020', '2021', '2022', 'Total'],
    'Ignorado': ['1', '4', '1', '2', '-', '8'],
    'Masculino': [5759, 5174, 2053, 1786, 3691, 18463],
    'Feminino': [4306, 3691, 1568, 1434, 2754, 13753],
    'Total': [10066, 8869, 3622, 3222, 6445, 32224]
}

df_sexo = pd.DataFrame(sexo_data)
df_sexo.to_csv('data/raw/Sexo_sudeste.csv', index=False, sep=';', encoding='latin1')
print("   ✅ Arquivo criado: data/raw/Sexo_sudeste.csv")

# ============================================================================
# 4. DADOS DE ESCOLARIDADE
# ============================================================================

print("\n📊 Gerando arquivo: Escolaridade_sudeste.xlsx")

escolaridade_data = {
    'Ano 1º Sintoma(s)': ['2018', '2019', '2020', '2021', '2022', 'Total'],
    'Ign/Branco': [3249, 2800, 1353, 1313, 2162, 10877],
    'Analfabeto': [18, 21, 13, 12, 23, 87],
    '1ª a 4ª série incompleta do EF': [356, 304, 105, 98, 222, 1085],
    '4ª série completa do EF': [155, 90, 63, 49, 113, 470],
    '5ª a 8ª série incompleta do EF': [367, 321, 122, 112, 219, 1141],
    'Ensino fundamental completo': [255, 188, 106, 93, 149, 791],
    'Ensino médio incompleto': [188, 189, 75, 74, 142, 668],
    'Ensino médio completo': [482, 496, 255, 226, 387, 1846],
    'Educação superior incompleta': [87, 79, 41, 28, 62, 297],
    'Educação superior completa': [246, 225, 103, 88, 174, 836],
    'Não se aplica': [4663, 4156, 1386, 1129, 2792, 14126],
    'Total': [10066, 8869, 3622, 3222, 6445, 32224]
}

df_escolaridade = pd.DataFrame(escolaridade_data)
df_escolaridade.to_excel('data/raw/Escolaridade_sudeste.xlsx', index=False)
print("   ✅ Arquivo criado: data/raw/Escolaridade_sudeste.xlsx")

# ============================================================================
# 5. DADOS DE EVOLUÇÃO
# ============================================================================

print("\n📊 Gerando arquivo: Evolucao_sudeste.csv")

evolucao_data = {
    'Ano 1º Sintoma(s)': ['2018', '2019', '2020', '2021', '2022', 'Total'],
    'Ign/Branco': [994.0, 1118.0, 497.0, 334.0, 936.0, 3879.0],
    'Alta': [7945.0, 6746.0, 2574.0, 2359.0, 4607.0, 24231.0],
    'Óbito por meningite': [778.0, 720.0, 349.0, 335.0, 657.0, 2839.0],
    'Óbito por outra causa': [349.0, 285.0, 202.0, 194.0, 245.0, 1275.0],
    'Total': [10066.0, 8869.0, 3622.0, 3222.0, 6445.0, 32224.0]
}

df_evolucao = pd.DataFrame(evolucao_data)
df_evolucao.to_csv('data/raw/Evolucao_sudeste.csv', index=False, sep=';', encoding='latin1')
print("   ✅ Arquivo criado: data/raw/Evolucao_sudeste.csv")

# ============================================================================
# 6. CRIAR DATASET CONSOLIDADO
# ============================================================================

print("\n📊 Gerando arquivo consolidado: meningite_sudeste_clean.csv")

# Criar dataset consolidado para análises
anos = [2018, 2019, 2020, 2021, 2022]
dados_consolidados = []

for ano in anos:
    idx = anos.index(ano)
    dados_consolidados.append({
        'ano': ano,
        'total_casos': df_etiologia.loc[idx, 'Total'],
        'mv': df_etiologia.loc[idx, 'MV'],  # Meningite Viral
        'mb': df_etiologia.loc[idx, 'MB'],  # Meningite Bacteriana
        'mp': df_etiologia.loc[idx, 'MP'],  # Meningite Pneumocócica
        'mm': df_etiologia.loc[idx, 'MM'],  # Meningite Meningocócica
        'masculino': df_sexo.loc[idx, 'Masculino'],
        'feminino': df_sexo.loc[idx, 'Feminino'],
        'obitos': df_evolucao.loc[idx, 'Óbito por meningite'],
        'alta': df_evolucao.loc[idx, 'Alta'],
        'menores_5anos': df_idade.loc[idx, '<1 Ano'] + df_idade.loc[idx, '01-04'],
        'maiores_60anos': (df_idade.loc[idx, '60-64'] + df_idade.loc[idx, '65-69'] + 
                          df_idade.loc[idx, '70-79'] + df_idade.loc[idx, '80 e +'])
    })

df_consolidado = pd.DataFrame(dados_consolidados)

# Calcular métricas derivadas
df_consolidado['taxa_letalidade'] = (df_consolidado['obitos'] / df_consolidado['total_casos'] * 100).round(2)
df_consolidado['prop_masculino'] = (df_consolidado['masculino'] / df_consolidado['total_casos'] * 100).round(2)
df_consolidado['prop_menores_5'] = (df_consolidado['menores_5anos'] / df_consolidado['total_casos'] * 100).round(2)

df_consolidado.to_csv('data/processed/meningite_sudeste_clean.csv', index=False)
print("   ✅ Arquivo criado: data/processed/meningite_sudeste_clean.csv")

# ============================================================================
# 7. RESUMO FINAL
# ============================================================================

print("\n" + "="*80)
print("📁 RESUMO DOS ARQUIVOS CRIADOS")
print("="*80)

arquivos_criados = [
    "data/raw/Etiologia_sudeste.csv",
    "data/raw/Idade_sudeste.xlsx", 
    "data/raw/Sexo_sudeste.csv",
    "data/raw/Escolaridade_sudeste.xlsx",
    "data/raw/Evolucao_sudeste.csv",
    "data/processed/meningite_sudeste_clean.csv"
]

for arquivo in arquivos_criados:
    tamanho = os.path.getsize(arquivo) / 1024  # KB
    print(f"   ✅ {arquivo} ({tamanho:.2f} KB)")

print("\n" + "="*80)
print("✅ TODOS OS ARQUIVOS FORAM GERADOS COM SUCESSO!")
print("="*80)

print("""
📊 PRÓXIMOS PASSOS:

1. Execute o notebook: notebooks/analise_meningite_sudeste.ipynb
2. Explore os dados na pasta data/raw/
3. Use o dataset consolidado em data/processed/ para análises

💡 DICA: Os dados são simulados, mas baseados em padrões epidemiológicos
   reais do SINAN/DataSUS da região Sudeste (2018-2022)
""")

# ============================================================================
# 8. CRIAR ARQUIVO DE DOCUMENTAÇÃO DOS DADOS
# ============================================================================

documentacao = """
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
"""

with open('data/DICIONARIO_DADOS.md', 'w', encoding='utf-8') as f:
    f.write(documentacao)

print("   ✅ Documentação criada: data/DICIONARIO_DADOS.md")
