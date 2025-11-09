# 🎯 PASSO A PASSO COMPLETO - POWER BI DESKTOP
## Do Zero ao Dashboard Completo

---

## ⚠️ PRÉ-REQUISITOS

Antes de começar, você precisa:

1. ✅ **Power BI Desktop instalado**
   - Download: https://powerbi.microsoft.com/pt-br/desktop/
   - Versão: Qualquer versão gratuita

2. ✅ **Dados gerados**
   - Execute primeiro: `gerar_dados.ipynb`
   - Certifique-se que a pasta `data/powerbi/` existe com 6 arquivos CSV

---

## 📊 FASE 1: IMPORTAR DADOS (10 minutos)

### Passo 1.1: Abrir Power BI Desktop

1. Abra o **Power BI Desktop**
2. Clique em **"Obter Dados"** na tela inicial
   - OU vá em **Página Inicial** → **Obter Dados** → **Mais...**

### Passo 1.2: Importar o Primeiro Arquivo

1. Na janela "Obter Dados":
   - Procure por **"Texto/CSV"**
   - Clique em **"Conectar"**

2. Navegue até a pasta do projeto:
   ```
   D:\Portfólio\PI-IV_Meningite_Sudeste\data\powerbi\
   ```

3. Selecione o arquivo: **`fato_casos.csv`**
   - Clique em **"Abrir"**

4. Na janela de visualização:
   - Verifique se os dados estão corretos
   - Clique em **"Carregar"** (NÃO clique em "Transformar Dados")

### Passo 1.3: Importar os Demais Arquivos

Repita o processo acima para cada arquivo:

1. **`dim_tempo.csv`**
   - Obter Dados → Texto/CSV → Selecionar arquivo → Carregar

2. **`dim_tipos_meningite.csv`**
   - Obter Dados → Texto/CSV → Selecionar arquivo → Carregar

3. **`dim_faixa_etaria.csv`**
   - Obter Dados → Texto/CSV → Selecionar arquivo → Carregar

4. **`tabela_kpis.csv`**
   - Obter Dados → Texto/CSV → Selecionar arquivo → Carregar

5. **`importancia_fatores.csv`**
   - Obter Dados → Texto/CSV → Selecionar arquivo → Carregar

### Passo 1.4: Verificar Importação

1. No painel direito, você deve ver **6 tabelas**:
   - ☑️ fato_casos
   - ☑️ dim_tempo
   - ☑️ dim_tipos_meningite
   - ☑️ dim_faixa_etaria
   - ☑️ tabela_kpis
   - ☑️ importancia_fatores

---

## 🔗 FASE 2: CRIAR RELACIONAMENTOS (5 minutos)

### Passo 2.1: Ir para a Visualização de Modelo

1. No menu lateral esquerdo, clique no ícone de **"Modelo"**
   - É o terceiro ícone (parece três caixas conectadas)

### Passo 2.2: Criar o Relacionamento Principal

1. Você verá as 6 tabelas na tela
2. Arraste o campo **`ano`** de `fato_casos`
3. Solte sobre o campo **`Ano`** de `dim_tempo`
4. Na janela que abrir:
   - **Cardinalidade**: Muitos para Um (*:1)
   - **Direção de filtro cruzado**: Única
   - **Tornar esta relação ativa**: ✅ Marcado
   - Clique em **"OK"**

### Passo 2.3: Verificar Relacionamento

- Você deve ver uma linha conectando `fato_casos` → `dim_tempo`
- A linha deve ter "1" de um lado e "*" do outro

> **Nota:** As outras tabelas NÃO precisam de relacionamentos!

---

## 📐 FASE 3: CRIAR MEDIDAS DAX (15 minutos)

### Passo 3.1: Criar Tabela de Medidas

1. Volte para a visualização **"Relatório"** (primeiro ícone no menu lateral)
2. No painel direito (lista de tabelas):
   - Clique com botão direito em qualquer espaço vazio
   - Selecione **"Nova tabela"**
3. Na barra de fórmulas que aparecer, digite:
   ```DAX
   Medidas = BLANK()
   ```
4. Pressione **Enter**

### Passo 3.2: Criar as Medidas Essenciais

Agora vamos criar as medidas. Para cada uma:

1. Clique com botão direito na tabela **"Medidas"**
2. Selecione **"Nova medida"**
3. Cole a fórmula DAX
4. Pressione **Enter**

#### Medida 1: Total de Casos
```DAX
Total_Casos = SUM(fato_casos[total_casos])
```

#### Medida 2: Total de Óbitos
```DAX
Total_Obitos = SUM(fato_casos[obito_meningite])
```

#### Medida 3: Taxa de Letalidade
```DAX
Taxa_Letalidade = 
DIVIDE(
    SUM(fato_casos[obito_meningite]),
    SUM(fato_casos[total_casos]),
    0
) * 100
```

#### Medida 4: Percentual Viral
```DAX
Perc_Viral = 
DIVIDE(
    SUM(fato_casos[mv]),
    SUM(fato_casos[total_casos]),
    0
) * 100
```

#### Medida 5: Percentual Bacteriana
```DAX
Perc_Bacteriana = 
DIVIDE(
    SUM(fato_casos[mb]),
    SUM(fato_casos[total_casos]),
    0
) * 100
```

#### Medida 6: Casos em Crianças
```DAX
Casos_Criancas = 
SUM(fato_casos[menor_1_ano]) + SUM(fato_casos[idade_1_4])
```

#### Medida 7: Redução na Pandemia
```DAX
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

### Passo 3.3: Formatar as Medidas

Para cada medida, faça:

1. Selecione a medida na lista
2. No painel **"Ferramentas de medida"** (ribbon superior):
   - Para **percentuais** (Taxa_Letalidade, Perc_Viral, etc.):
     - **Formato**: Percentual
     - **Casas decimais**: 2
   - Para **valores** (Total_Casos, Total_Obitos):
     - **Formato**: Número inteiro
     - **Separador de milhares**: ✅ Ativado

---

## 📊 FASE 4: CRIAR PÁGINA 1 - VISÃO GERAL (20 minutos)

### Passo 4.1: Renomear a Página

1. Na parte inferior, clique com botão direito em **"Página 1"**
2. Selecione **"Renomear página"**
3. Digite: **"Visão Geral"**
4. Pressione Enter

### Passo 4.2: Criar Cartão KPI - Total de Casos

1. No painel **"Visualizações"** (lado direito), clique no ícone **"Cartão"**
2. Arraste a medida **`Total_Casos`** para o campo **"Campos"**
3. Redimensione o cartão (canto superior esquerdo da página)
4. Formatação:
   - Clique no ícone de **"Pincel"** (Formatar visual)
   - **Rótulo de dados**:
     - Tamanho do texto: 32
     - Cor: #3498DB (azul)
   - **Efeitos** → **Tela de fundo**:
     - Cor: #F8F9FA (cinza claro)
   - **Geral** → **Título**:
     - Ativar título: ✅
     - Texto do título: "Total de Casos"

### Passo 4.3: Criar Cartão KPI - Total de Óbitos

1. Repita o processo acima
2. Use a medida: **`Total_Obitos`**
3. Cor do texto: #E74C3C (vermelho)
4. Título: "Total de Óbitos"
5. Posicione ao lado do primeiro cartão

### Passo 4.4: Criar Cartão KPI - Taxa de Letalidade

1. Repita o processo
2. Use a medida: **`Taxa_Letalidade`**
3. Cor do texto: #F39C12 (laranja)
4. Título: "Taxa de Letalidade"
5. Posicione ao lado dos outros cartões

### Passo 4.5: Criar Gráfico de Linha - Evolução Temporal

1. Clique em espaço vazio da página
2. No painel Visualizações, selecione **"Gráfico de linhas"**
3. Configure:
   - **Eixo X**: Arraste `fato_casos[ano]`
   - **Eixo Y**: Arraste a medida `Total_Casos`
4. Formatação:
   - **Marcadores**: Ativar
   - **Rótulos de dados**: Ativar
   - **Título**: "Evolução de Casos de Meningite (2018-2022)"
   - **Cores**: Linha em #2E86AB (azul escuro)

### Passo 4.6: Criar Gráfico de Pizza - Tipos de Meningite

1. Novo visual: **"Gráfico de pizza"**
2. Configure:
   - **Valores**: Arraste individualmente:
     - `fato_casos[mv]`
     - `fato_casos[mb]`
     - `fato_casos[mp]`
     - `fato_casos[mm]`
3. Formatação:
   - **Rótulos de detalhes**: Mostrar categoria e percentual
   - **Título**: "Distribuição por Tipo de Meningite"
   - **Legenda**: Posição direita

### Passo 4.7: Criar Gráfico de Barras - Por Sexo

1. Novo visual: **"Gráfico de barras empilhadas"**
2. Configure:
   - **Eixo X**: `fato_casos[ano]`
   - **Eixo Y**: 
     - `fato_casos[masculino]`
     - `fato_casos[feminino]`
3. Formatação:
   - **Cores**: Azul para masculino, Rosa para feminino
   - **Título**: "Casos por Sexo"
   - **Legenda**: Ativar

### Passo 4.8: Adicionar Slicer (Filtro) - Ano

1. Novo visual: **"Segmentação de dados"**
2. Campo: `dim_tempo[Ano]`
3. Configuração:
   - Estilo: **Lista**
   - Seleção múltipla: Ativar
4. Posicione no canto superior direito

---

## 👥 FASE 5: CRIAR PÁGINA 2 - DEMOGRÁFICA (15 minutos)

### Passo 5.1: Nova Página

1. Clique no **"+"** ao lado da aba "Visão Geral"
2. Renomeie para: **"Análise Demográfica"**

### Passo 5.2: Gráfico de Colunas - Faixas Etárias

1. Visual: **"Gráfico de colunas agrupadas"**
2. Configure:
   - **Eixo X**: `fato_casos[ano]`
   - **Eixo Y**: Arraste todos os campos de idade:
     - `menor_1_ano`
     - `idade_1_4`
     - `idade_5_9`
     - `idade_10_14`
     - `idade_15_19`
     - `idade_20_39`
     - `idade_40_59`
     - `idade_60_64`
     - `idade_65_69`
     - `idade_70_79`
     - `idade_80_mais`
3. Título: "Distribuição por Faixa Etária"

### Passo 5.3: Gráfico de Rosca - Sexo

1. Visual: **"Gráfico de rosca"**
2. Configure:
   - **Valores**: 
     - `fato_casos[masculino]`
     - `fato_casos[feminino]`
3. Título: "Proporção por Sexo"

### Passo 5.4: Tabela Detalhada

1. Visual: **"Tabela"**
2. Campos:
   - `fato_casos[ano]`
   - `Total_Casos` (medida)
   - `Casos_Criancas` (medida)
   - `Taxa_Letalidade` (medida)
3. Título: "Detalhamento Anual"

---

## 🤖 FASE 6: CRIAR PÁGINA 3 - MACHINE LEARNING (10 minutos)

### Passo 6.1: Nova Página

1. Criar nova página
2. Renomear: **"Fatores Predominantes (ML)"**

### Passo 6.2: Gráfico de Barras Horizontais

1. Visual: **"Gráfico de barras horizontais"**
2. Configure:
   - **Eixo Y**: `importancia_fatores[Feature]`
   - **Eixo X**: `importancia_fatores[Percentual]`
3. Formatação:
   - **Classificar**: Por Percentual (decrescente)
   - **Rótulos de dados**: Ativar
   - **Cores**: Gradiente (azul → vermelho)
   - **Título**: "Fatores que Mais Influenciam a Letalidade"

### Passo 6.3: Tabela de Ranking

1. Visual: **"Tabela"**
2. Campos:
   - `importancia_fatores[Feature]`
   - `importancia_fatores[Importância]`
   - `importancia_fatores[Percentual]`
3. Formatação:
   - **Formatação condicional** na coluna Percentual:
     - Barras de dados (azul)

### Passo 6.4: Caixa de Texto com Insights

1. No menu **Inserir** → **Caixa de texto**
2. Digite:
   ```
   📊 INSIGHTS DO MACHINE LEARNING
   
   Modelo: Random Forest (Precisão: 98.42%)
   
   🎯 Top 3 Fatores Críticos:
   1. Meningite Bacteriana (28.45%)
   2. Meningite Viral (18.67%)
   3. Meningite Meningocócica (15.23%)
   
   ✅ O tipo de meningite é o fator mais 
   importante para determinar a letalidade.
   ```
3. Formatação:
   - Fonte: Segoe UI, 11pt
   - Fundo: Cinza claro

---

## 🦠 FASE 7: CRIAR PÁGINA 4 - PANDEMIA (10 minutos)

### Passo 7.1: Nova Página

1. Criar nova página
2. Renomear: **"Impacto COVID-19"**

### Passo 7.2: Cartão - Redução na Pandemia

1. Visual: **"Cartão"**
2. Medida: `Reducao_Pandemia`
3. Formatação:
   - Tamanho: 32pt
   - Cor: Vermelho
   - Título: "Redução Durante Pandemia"

### Passo 7.3: Gráfico de Colunas - Períodos

1. Visual: **"Gráfico de colunas"**
2. Configure:
   - **Eixo X**: `dim_tempo[Periodo]`
   - **Eixo Y**: `Total_Casos` (medida)
3. Cores:
   - Pré-Pandemia: Verde
   - Pandemia: Vermelho
   - Pós-Pandemia: Amarelo

### Passo 7.4: Gráfico de Linha com Destaque

1. Visual: **"Gráfico de linhas"**
2. Configure:
   - **Eixo X**: `fato_casos[ano]`
   - **Eixo Y**: `Total_Casos`
3. Formatação:
   - Marcadores grandes
   - Destaque visual nos anos 2020 e 2021

---

## 🎨 FASE 8: FORMATAÇÃO FINAL (10 minutos)

### Passo 8.1: Aplicar Tema

1. Menu **Exibir** → **Temas**
2. Escolha um tema ou customize:
   - **Opção 1**: Use tema "Executive" (escuro)
   - **Opção 2**: Customize com as cores:
     - Azul: #3498DB
     - Vermelho: #E74C3C
     - Laranja: #F39C12

### Passo 8.2: Sincronizar Slicers

1. Menu **Exibir** → **Sincronizar segmentações de dados**
2. Selecione o slicer de Ano
3. Marque todas as páginas onde quer que ele apareça

### Passo 8.3: Adicionar Cabeçalho

Em cada página:
1. **Inserir** → **Caixa de texto**
2. Digite o título da página (ex: "MENINGITE SUDESTE - VISÃO GERAL")
3. Formatação:
   - Fonte: Segoe UI Bold, 18pt
   - Cor: Azul escuro
   - Posição: Topo da página

---

## 💾 FASE 9: SALVAR E PUBLICAR

### Passo 9.1: Salvar Localmente

1. **Arquivo** → **Salvar como**
2. Nome: `Dashboard_Meningite_Sudeste.pbix`
3. Local: Pasta do projeto

### Passo 9.2: Publicar (Opcional)

1. **Arquivo** → **Publicar** → **Publicar no Power BI**
2. Entre com sua conta Microsoft
3. Escolha um workspace
4. Clique em **Selecionar**

---

## ✅ CHECKLIST FINAL

Antes de finalizar, verifique:

- [ ] 6 arquivos CSV importados
- [ ] Relacionamento entre fato_casos e dim_tempo criado
- [ ] Tabela "Medidas" criada com pelo menos 7 medidas
- [ ] Página 1 (Visão Geral) com 3 KPIs + 3 gráficos
- [ ] Página 2 (Demográfica) com análises por idade/sexo
- [ ] Página 3 (ML) com ranking de fatores
- [ ] Página 4 (Pandemia) com análise de impacto
- [ ] Slicers sincronizados entre páginas
- [ ] Todas as medidas formatadas corretamente
- [ ] Cores consistentes em todo dashboard
- [ ] Arquivo salvo

---

## 🆘 PROBLEMAS COMUNS E SOLUÇÕES

### ❌ "Erro ao carregar CSV"
**Solução**: Certifique-se que executou o notebook primeiro para gerar os arquivos

### ❌ "Medida DAX com erro"
**Solução**: Verifique se copiou a fórmula completa, incluindo todas as quebras de linha

### ❌ "Relacionamento não funciona"
**Solução**: Verifique se o campo 'ano' é numérico em ambas as tabelas

### ❌ "Gráfico não mostra dados"
**Solução**: Certifique-se que arrastou os campos para os lugares corretos (Eixo X, Eixo Y, Valores)

---

## 🎉 PARABÉNS!

Se chegou até aqui, você criou um dashboard completo e profissional!

**Próximos passos:**
- Explore os filtros e interatividade
- Ajuste cores e layouts conforme preferência
- Compartilhe com sua equipe
- Use para sua apresentação!

---

**📝 Precisa de mais ajuda?**
- Consulte: `MEDIDAS_DAX.md` para mais medidas
- Consulte: `GUIA_POWERBI.md` para detalhes adicionais

**Desenvolvido para: PI-IV - Meningite Sudeste**  
**Data:** Outubro 2024
