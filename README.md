# 📊 Análise Epidemiológica de Meningite — Região Sudeste (2018–2022)

Análise de 32.224 casos de meningite notificados na Região Sudeste do Brasil (SP, RJ, MG, ES). O projeto inclui:
- Dashboard interativo (Plotly Dash)
- Notebooks de EDA e modelagem (Random Forest)
- Scripts de processamento e artefatos (gráficos, modelos)

---

Badges

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/)
[![Dash](https://img.shields.io/badge/Dash-2.14-brightgreen.svg)](https://dash.plotly.com/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## Destaques

- Período analisado: **2018–2022**
- Total de casos: **32.224**
- Redução de notificações durante a pandemia (2020–2021): **~63%**
- Taxa de letalidade média: **~9%**
- Tipo predominante: **Meningite Viral (~54%)**
- Grupos mais vulneráveis: **<5 anos** e **≥60 anos**

---

## Estrutura do repositório
PI-IV_Meningite_Sudeste/
- src/
  - dashboard_app.py       — Aplicação Plotly Dash
  - gerar_dados.py         — Scripts de processamento
- notebooks/
  - gerar_dados.ipynb      — EDA e preparação
  - analise_ml.ipynb       — Modelagem e avaliação
- data/
  - raw/                   — Dados brutos (SINAN/DataSUS)
  - processed/             — Dados limpos (meningite_sudeste_clean.csv)
- assets/
  - graficos/              — Gráficos exportados
  - modelos/               — Modelos treinados (.pkl)
- requirements.txt
- Procfile
- runtime.txt
- README.md

> Observação: referências e arquivos relacionados ao Power BI e à pasta docs foram removidos do README, conforme solicitado. Se desejar, posso remover a pasta docs do repositório em um commit separado.

---

## Tecnologias
- Python 3.11+
- Pandas, NumPy
- Plotly Dash
- Matplotlib / Seaborn
- Scikit-learn (Random Forest)
- Jupyter Notebook

---

## Quick start (local)

1. Clone o repositório:
```bash
git clone https://github.com/ru-fagundes/PI-IV_Meningite_Sudeste.git
cd PI-IV_Meningite_Sudeste
```

2. Instale dependências:
```bash
pip install -r requirements.txt
```

3. Executar o dashboard:
```bash
cd src
python dashboard_app.py
```
Abra http://localhost:8050

4. Abrir notebooks:
```bash
jupyter notebook
# abrir notebooks/gerar_dados.ipynb e notebooks/analise_ml.ipynb
```

---

## Machine Learning (resumo)
- Algoritmo principal: Random Forest Classifier  
- Objetivo: prever letalidade e identificar preditores mais importantes  
- Métricas e análises: ver notebooks/analise_ml.ipynb (métricas, matriz de confusão, feature importance)

Principais preditores identificados (exemplo):
1. Meningite Bacteriana  
2. Meningite Viral  
3. Meningite Meningocócica  
(Ver notebook para porcentagens e interpretação)

---

## Deploy
Sugestão simples (Render):
- Build command: `pip install -r requirements.txt`
- Start command: `gunicorn src.dashboard_app:server`

Arquivos de suporte já incluídos: Procfile, runtime.txt

---

## Insights e recomendações rápidas
- Investir em vacinação e vigilância para menores de 5 anos.  
- Priorizar detecção e tratamento de meningites bacterianas (maior letalidade).  
- Monitorar recuperação das notificações pós-pandemia e ajustar vigilância epidemiológica.

---

## Como contribuir
1. Faça fork do repositório  
2. Crie uma branch: `git checkout -b feature/nome-da-feature`  
3. Faça commits claros e atômicos  
4. Envie o push e abra um Pull Request  

Por favor, verifique issues abertas para tarefas ou solicitações antes de implementar grandes mudanças.

---

## Dados e fonte
- Sistema: SINAN (Sistema de Informação de Agravos de Notificação)  
- Base: DataSUS  
- Período: 2018–2022  
- Região: Sudeste (SP, RJ, MG, ES)  
- Arquivo consolidado: `data/processed/meningite_sudeste_clean.csv`

---

## Licença
Projeto aberto para fins educacionais e de pesquisa (ver LICENSE).

---

## Contato
Para dúvidas, sugestões ou problemas, abra uma issue: https://github.com/ru-fagundes/PI-IV_Meningite_Sudeste/issues

⭐ Se este repositório te ajudou, deixe uma estrela!