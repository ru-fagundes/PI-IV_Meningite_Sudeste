# 📊 SCRIPT DAX - MEDIDAS POWER BI
## Análise de Meningite - Região Sudeste

---

## 🎯 INSTRUÇÕES DE USO

1. Abra o Power BI Desktop
2. Importe os 6 arquivos CSV de `data/powerbi/`
3. Crie uma tabela chamada "Medidas" (vazia, só para organizar)
4. Copie e cole cada medida abaixo

---

## 📐 MEDIDAS DAX

### 1️⃣ MEDIDAS PRINCIPAIS

```DAX
// Total de Casos
Total_Casos = SUM(fato_casos[total_casos])
```

```DAX
// Total de Óbitos
Total_Obitos = SUM(fato_casos[obito_meningite])
```

```DAX
// Taxa de Letalidade (%)
Taxa_Letalidade = 
DIVIDE(
    SUM(fato_casos[obito_meningite]),
    SUM(fato_casos[total_casos]),
    0
) * 100
```

```DAX
// Total de Altas
Total_Altas = SUM(fato_casos[alta])
```

---

### 2️⃣ MEDIDAS POR TIPO DE MENINGITE

```DAX
// Total Meningite Viral
Total_MV = SUM(fato_casos[mv])
```

```DAX
// Percentual Meningite Viral
Perc_Viral = 
DIVIDE(
    SUM(fato_casos[mv]),
    SUM(fato_casos[total_casos]),
    0
) * 100
```

```DAX
// Total Meningite Bacteriana
Total_MB = SUM(fato_casos[mb])
```

```DAX
// Percentual Meningite Bacteriana
Perc_Bacteriana = 
DIVIDE(
    SUM(fato_casos[mb]),
    SUM(fato_casos[total_casos]),
    0
) * 100
```

```DAX
// Total Meningite Pneumocócica
Total_MP = SUM(fato_casos[mp])
```

```DAX
// Percentual Meningite Pneumocócica
Perc_Pneumococica = 
DIVIDE(
    SUM(fato_casos[mp]),
    SUM(fato_casos[total_casos]),
    0
) * 100
```

```DAX
// Total Meningite Meningocócica
Total_MM = SUM(fato_casos[mm])
```

```DAX
// Percentual Meningite Meningocócica
Perc_Meningococica = 
DIVIDE(
    SUM(fato_casos[mm]),
    SUM(fato_casos[total_casos]),
    0
) * 100
```

---

### 3️⃣ MEDIDAS DEMOGRÁFICAS

```DAX
// Total Casos Masculino
Total_Masculino = SUM(fato_casos[masculino])
```

```DAX
// Total Casos Feminino
Total_Feminino = SUM(fato_casos[feminino])
```

```DAX
// Percentual Masculino
Perc_Masculino = 
DIVIDE(
    SUM(fato_casos[masculino]),
    SUM(fato_casos[total_casos]),
    0
) * 100
```

```DAX
// Percentual Feminino
Perc_Feminino = 
DIVIDE(
    SUM(fato_casos[feminino]),
    SUM(fato_casos[total_casos]),
    0
) * 100
```

---

### 4️⃣ MEDIDAS POR FAIXA ETÁRIA

```DAX
// Casos em Crianças (<5 anos)
Casos_Criancas = 
SUM(fato_casos[menor_1_ano]) + SUM(fato_casos[idade_1_4])
```

```DAX
// Percentual Crianças
Perc_Criancas = 
DIVIDE(
    [Casos_Criancas],
    SUM(fato_casos[total_casos]),
    0
) * 100
```

```DAX
// Casos em Idosos (>60 anos)
Casos_Idosos = 
SUM(fato_casos[idade_60_64]) + 
SUM(fato_casos[idade_65_69]) + 
SUM(fato_casos[idade_70_79]) + 
SUM(fato_casos[idade_80_mais])
```

```DAX
// Percentual Idosos
Perc_Idosos = 
DIVIDE(
    [Casos_Idosos],
    SUM(fato_casos[total_casos]),
    0
) * 100
```

```DAX
// Casos em Adultos (20-59 anos)
Casos_Adultos = 
SUM(fato_casos[idade_20_39]) + SUM(fato_casos[idade_40_59])
```

---

### 5️⃣ MEDIDAS DE ANÁLISE TEMPORAL

```DAX
// Média de Casos por Ano
Media_Casos_Ano = AVERAGE(fato_casos[total_casos])
```

```DAX
// Ano com Maior Número de Casos
Ano_Max_Casos = 
CALCULATE(
    MAX(fato_casos[ano]),
    FILTER(
        fato_casos,
        fato_casos[total_casos] = MAX(fato_casos[total_casos])
    )
)
```

```DAX
// Ano com Menor Número de Casos
Ano_Min_Casos = 
CALCULATE(
    MIN(fato_casos[ano]),
    FILTER(
        fato_casos,
        fato_casos[total_casos] = MIN(fato_casos[total_casos])
    )
)
```

```DAX
// Variação Percentual (Ano Atual vs Ano Anterior)
Var_Perc_Ano_Anterior = 
VAR AnoAtual = MAX(fato_casos[ano])
VAR CasosAnoAtual = 
    CALCULATE(
        SUM(fato_casos[total_casos]),
        fato_casos[ano] = AnoAtual
    )
VAR CasosAnoAnterior = 
    CALCULATE(
        SUM(fato_casos[total_casos]),
        fato_casos[ano] = AnoAtual - 1
    )
RETURN
    DIVIDE(
        CasosAnoAtual - CasosAnoAnterior,
        CasosAnoAnterior,
        0
    ) * 100
```

---

### 6️⃣ MEDIDAS ESPECÍFICAS DA PANDEMIA

```DAX
// Total de Casos Pré-Pandemia (2018-2019)
Casos_Pre_Pandemia = 
CALCULATE(
    SUM(fato_casos[total_casos]),
    fato_casos[ano] IN {2018, 2019}
)
```

```DAX
// Total de Casos Durante Pandemia (2020-2021)
Casos_Durante_Pandemia = 
CALCULATE(
    SUM(fato_casos[total_casos]),
    fato_casos[ano] IN {2020, 2021}
)
```

```DAX
// Total de Casos Pós-Pandemia (2022)
Casos_Pos_Pandemia = 
CALCULATE(
    SUM(fato_casos[total_casos]),
    fato_casos[ano] = 2022
)
```

```DAX
// Redução Percentual Durante Pandemia
Reducao_Pandemia = 
VAR MediaPrePandemia = 
    CALCULATE(
        AVERAGE(fato_casos[total_casos]),
        fato_casos[ano] IN {2018, 2019}
    )
VAR MediaDurantePandemia = 
    CALCULATE(
        AVERAGE(fato_casos[total_casos]),
        fato_casos[ano] IN {2020, 2021}
    )
RETURN
    DIVIDE(
        MediaPrePandemia - MediaDurantePandemia,
        MediaPrePandemia,
        0
    ) * 100
```

```DAX
// Recuperação Pós-Pandemia (%)
Recuperacao_Pos_Pandemia = 
VAR MediaDurantePandemia = 
    CALCULATE(
        AVERAGE(fato_casos[total_casos]),
        fato_casos[ano] IN {2020, 2021}
    )
VAR CasosPosPandemia = 
    CALCULATE(
        SUM(fato_casos[total_casos]),
        fato_casos[ano] = 2022
    )
RETURN
    DIVIDE(
        CasosPosPandemia - MediaDurantePandemia,
        MediaDurantePandemia,
        0
    ) * 100
```

---

### 7️⃣ MEDIDAS DE COMPARAÇÃO E RANKING

```DAX
// Tipo de Meningite Mais Comum
Tipo_Mais_Comum = 
VAR TotalMV = SUM(fato_casos[mv])
VAR TotalMB = SUM(fato_casos[mb])
VAR TotalMP = SUM(fato_casos[mp])
VAR TotalMM = SUM(fato_casos[mm])
VAR MaxTotal = MAX(TotalMV, TotalMB, TotalMP, TotalMM)
RETURN
    SWITCH(
        TRUE(),
        MaxTotal = TotalMV, "Meningite Viral",
        MaxTotal = TotalMB, "Meningite Bacteriana",
        MaxTotal = TotalMP, "Meningite Pneumocócica",
        MaxTotal = TotalMM, "Meningite Meningocócica",
        "Desconhecido"
    )
```

```DAX
// Faixa Etária Mais Afetada
Faixa_Mais_Afetada = 
VAR Menor1 = SUM(fato_casos[menor_1_ano])
VAR Idade1_4 = SUM(fato_casos[idade_1_4])
VAR Idade5_9 = SUM(fato_casos[idade_5_9])
VAR Criancas = Menor1 + Idade1_4
VAR Adultos = SUM(fato_casos[idade_20_39]) + SUM(fato_casos[idade_40_59])
VAR Idosos = SUM(fato_casos[idade_60_64]) + SUM(fato_casos[idade_65_69]) + 
             SUM(fato_casos[idade_70_79]) + SUM(fato_casos[idade_80_mais])
VAR MaxGrupo = MAX(Criancas, Adultos, Idosos)
RETURN
    SWITCH(
        TRUE(),
        MaxGrupo = Criancas, "Crianças (<5 anos)",
        MaxGrupo = Adultos, "Adultos (20-59 anos)",
        MaxGrupo = Idosos, "Idosos (>60 anos)",
        "Outros"
    )
```

---

### 8️⃣ MEDIDAS DE INDICADORES (KPIs)

```DAX
// Taxa de Recuperação (%)
Taxa_Recuperacao = 
DIVIDE(
    SUM(fato_casos[alta]),
    SUM(fato_casos[total_casos]),
    0
) * 100
```

```DAX
// Risco de Letalidade (Classificação)
Classificacao_Risco = 
VAR Taxa = [Taxa_Letalidade]
RETURN
    SWITCH(
        TRUE(),
        Taxa < 5, "🟢 Baixo",
        Taxa < 10, "🟡 Médio",
        Taxa < 15, "🟠 Alto",
        "🔴 Muito Alto"
    )
```

```DAX
// Tendência (Crescimento ou Queda)
Tendencia = 
VAR Variacao = [Var_Perc_Ano_Anterior]
RETURN
    IF(
        Variacao > 5, "📈 Crescimento",
        IF(Variacao < -5, "📉 Queda", "➡️ Estável")
    )
```

```DAX
// Índice de Gravidade (0-100)
Indice_Gravidade = 
VAR TaxaLetalidade = [Taxa_Letalidade]
VAR PropBacteriana = [Perc_Bacteriana]
VAR PropIdosos = [Perc_Idosos]
RETURN
    (TaxaLetalidade * 0.5) + (PropBacteriana * 0.3) + (PropIdosos * 0.2)
```

---

### 9️⃣ MEDIDAS AUXILIARES (Formatação)

```DAX
// Casos Formatados (com "casos")
Casos_Texto = 
FORMAT([Total_Casos], "#,##0") & " casos"
```

```DAX
// Taxa Letalidade Formatada
Taxa_Letalidade_Texto = 
FORMAT([Taxa_Letalidade], "0.00") & "%"
```

```DAX
// Ícone de Tendência
Icone_Tendencia = 
VAR Var = [Var_Perc_Ano_Anterior]
RETURN
    IF(Var > 0, "▲", IF(Var < 0, "▼", "●"))
```

---

## 🎨 FORMATAÇÃO DAS MEDIDAS

Após criar cada medida, configure a formatação:

### Para Medidas de Percentual:
1. Selecione a medida
2. Vá em "Ferramentas de medida" → "Formato"
3. Escolha "Percentual"
4. Casas decimais: 2

### Para Medidas de Valores:
1. Selecione a medida
2. Escolha "Número inteiro"
3. Ative "Separador de milhares"

### Para Medidas de Taxa de Letalidade:
1. Formato: Decimal
2. Casas decimais: 2
3. Adicionar sufixo: %

---

## 📋 ORDEM DE CRIAÇÃO RECOMENDADA

1. ✅ Crie a tabela "Medidas" (vazia)
2. ✅ Copie e cole as medidas principais (1-4)
3. ✅ Teste cada medida em um cartão visual
4. ✅ Continue com medidas demográficas (5-7)
5. ✅ Adicione medidas de análise (8-9)
6. ✅ Formate todas as medidas

---

## 🚀 PRÓXIMO PASSO

Após criar todas as medidas, use o arquivo:
**GUIA_POWERBI.md** para criar as visualizações!

---

**Desenvolvido para: PI-IV - Meningite Sudeste**  
**Data:** Outubro 2024
