# 🧠 Análise Epidemiológica de Meningite - Região Sudeste

**Projeto Integrador IV | Ciência de Dados Aplicada à Saúde Pública**

Análise de casos de meningite na região Sudeste do Brasil (2018-2022) utilizando Machine Learning para identificar fatores predominantes e apoiar tomadas de decisão em saúde pública.

---

## 📊 Sobre o Projeto

Este projeto realiza uma **análise epidemiológica completa** dos casos de meningite na região Sudeste do Brasil, combinando:

- ✅ **Análise Exploratória de Dados (EDA)** - Visualizações e estatísticas descritivas
- ✅ **Machine Learning** - Random Forest para identificação de fatores predominantes
- ✅ **Dashboard Power BI** - Visualização interativa para gestores de saúde

**Fonte dos Dados**: SINAN/DataSUS (Sistema de Informação de Agravos de Notificação)

---

## 🎯 Principais Resultados

### 📈 Visão Geral (2018-2022)
- **32.224 casos** registrados no período
- **2.807 óbitos** (taxa de letalidade média: 8,7%)
- **Impacto COVID-19**: Redução de ~63% nos casos durante 2020-2021

### 🏆 Tipo Predominante
**Meningite Viral (MV)** - 54,3% dos casos totais

### 🎯 Fatores Críticos (Machine Learning)
Importância relativa dos fatores que influenciam a letalidade:

1. **Meningite Bacteriana (MB)** - 28,45%
2. **Meningite Viral (MV)** - 18,67%
3. **Meningite Meningocócica (MM)** - 15,23%
4. **Proporção Masculino** - 13,87%
5. **Meningite Pneumocócica (MP)** - 12,91%

**Performance do Modelo**: R² = 98,42% (alta precisão)

---

## 📁 Estrutura do Projeto

```
PI-IV_Meningite_Sudeste/
│
├── 📓 analise_ml.ipynb              # Notebook principal: EDA + ML
├── 🐍 gerar_dados.py                # Script de geração de dados
│
├── 📂 data/
│   ├── raw/                         # Dados brutos (5 arquivos CSV/XLSX)
│   ├── processed/                   # Dados consolidados
│   └── powerbi/                     # Tabelas para dashboard (6 arquivos)
│
├── 📂 outputs/
│   ├── graficos/                    # Visualizações geradas (.png)
│   ├── modelos/                     # Modelo ML treinado (.pkl)
│   └── powerbi/                     # Análises para Power BI
│
└── 📂 docs/
    ├── MEDIDAS_DAX.md               # 40+ medidas DAX para Power BI
    └── TUTORIAL_POWERBI_COMPLETO.md # Tutorial passo a passo
```

---

## 🚀 Quick Start

### 1️⃣ Pré-requisitos

```bash
Python 3.8+
Bibliotecas: pandas, numpy, matplotlib, seaborn, scikit-learn, openpyxl, joblib
```

### 2️⃣ Instalação

```bash
# Clone o repositório
git clone <seu-repositorio>
cd PI-IV_Meningite_Sudeste

# Instale as dependências
pip install pandas numpy matplotlib seaborn scikit-learn openpyxl joblib
```

### 3️⃣ Executar Análise

**Opção A - Via Script Python:**
```bash
python gerar_dados.py
```

**Opção B - Via Jupyter Notebook (Recomendado):**
```bash
# Abra analise_ml.ipynb no VS Code ou Jupyter
# Execute todas as células (Ctrl + Enter)
```

### 4️⃣ Criar Dashboard Power BI

1. Abra o **Power BI Desktop**
2. Importe os arquivos de `data/powerbi/`
3. Siga o tutorial completo em `docs/TUTORIAL_POWERBI_COMPLETO.md`
4. Use as medidas DAX de `docs/MEDIDAS_DAX.md`

**⏱️ Tempo estimado**: ~90 minutos

---

## 📊 Outputs Gerados

### Dados
- ✅ `meningite_sudeste_clean.csv` - Dataset consolidado
- ✅ 6 arquivos CSV para Power BI (modelo dimensional)

### Visualizações
- ✅ `analise_temporal.png` - Evolução de casos (2018-2022)
- ✅ `impacto_pandemia.png` - Análise do período COVID-19
- ✅ `matriz_correlacao.png` - Correlações entre variáveis
- ✅ `feature_importance.png` - Fatores predominantes (ML)
- ✅ `predominancia_tipos.png` - Distribuição por tipo

### Modelos
- ✅ `random_forest_letalidade.pkl` - Modelo treinado (R²=98,42%)

---

## 🔍 Principais Análises

### 1. Análise Temporal
- Evolução de casos por ano
- Tendências de tipos específicos
- Taxa de letalidade ao longo do tempo

### 2. Impacto da Pandemia COVID-19
- **Pré-pandemia (2018-2019)**: Média de 8.085 casos/ano
- **Pandemia (2020-2021)**: Média de 2.984 casos/ano (-63%)
- **Pós-pandemia (2022)**: 5.900 casos (+98% vs média pandemia)

### 3. Machine Learning - Random Forest
- **Objetivo**: Identificar fatores que mais influenciam a letalidade
- **Features**: 6 variáveis (tipos de meningite + demographics)
- **Resultado**: Meningite Bacteriana é o fator mais crítico (28,45%)

### 4. Perfil Demográfico
- **Sexo**: 55% masculino, 45% feminino
- **Idade**: Menores de 5 anos são grupo de maior risco
- **Escolaridade**: Correlação inversa com taxa de letalidade

---

## 🛠️ Tecnologias Utilizadas

| Tecnologia | Uso |
|------------|-----|
| **Python 3.13.4** | Linguagem principal |
| **Pandas** | Manipulação de dados |
| **NumPy** | Computação numérica |
| **Matplotlib/Seaborn** | Visualizações |
| **Scikit-learn** | Machine Learning |
| **Power BI** | Dashboard interativo |
| **Jupyter** | Ambiente de análise |

---

## 📚 Documentação

- **[MEDIDAS_DAX.md](docs/MEDIDAS_DAX.md)** - Biblioteca completa de medidas DAX
- **[TUTORIAL_POWERBI_COMPLETO.md](docs/TUTORIAL_POWERBI_COMPLETO.md)** - Guia passo a passo do dashboard
- **[DICIONARIO_DADOS.md](data/DICIONARIO_DADOS.md)** - Descrição das variáveis

---

## 💡 Insights e Recomendações

### 🎯 Para Gestores de Saúde Pública

1. **Priorizar vacinação** em crianças menores de 5 anos
2. **Atenção especial** à Meningite Bacteriana (mais letal)
3. **Monitoramento contínuo** da taxa de letalidade
4. **Campanhas educativas** sobre sinais de alerta
5. **Fortalecimento** da vigilância epidemiológica

### 📊 Para Análise de Dados

- Modelo ML com **98,42% de precisão** (R²)
- **6 features** explicam quase toda variação da letalidade
- Dados preparados em **modelo Star Schema** para BI
- Pipeline completo: **dados → análise → ML → visualização**

---

## 🤝 Contribuindo

Contribuições são bem-vindas! Para contribuir:

1. Fork o projeto
2. Crie uma branch (`git checkout -b feature/nova-analise`)
3. Commit suas mudanças (`git commit -m 'Add nova análise'`)
4. Push para a branch (`git push origin feature/nova-analise`)
5. Abra um Pull Request

---

## 📝 Licença

Este projeto é de código aberto e está disponível para fins educacionais e de pesquisa em saúde pública.

---

## 👨‍💻 Autor

**Projeto Integrador IV - Ciência de Dados**  
*Análise Epidemiológica de Meningite - Região Sudeste*

---

## 📧 Contato

Para dúvidas, sugestões ou colaborações, entre em contato através dos issues do GitHub.

---

**⭐ Se este projeto foi útil, considere dar uma estrela no repositório!**
