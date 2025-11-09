"""
Dashboard Interativo - Análise de Meningite no Sudeste do Brasil
Desenvolvido com Plotly Dash para visualização profissional
"""

import dash
from dash import dcc, html, Input, Output
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import numpy as np

# ==================== CONFIGURAÇÃO E CARREGAMENTO DE DADOS ====================

# Carregar dados principais
df_casos = pd.read_csv('../data/processed/meningite_sudeste_clean.csv')

# Preparar dados para visualização
df_casos['periodo'] = df_casos['ano'].apply(lambda x: 'Pré-Pandemia' if x < 2020 else 'Pandemia')

# Calcular KPIs
total_casos = df_casos['total_casos'].sum()
total_obitos = df_casos['obitos'].sum()
taxa_letalidade_media = df_casos['taxa_letalidade'].mean()
casos_viral = df_casos['mv'].sum()

# ==================== INICIALIZAÇÃO DO APP ====================

app = dash.Dash(__name__, 
                meta_tags=[{"name": "viewport", "content": "width=device-width, initial-scale=1"}])
app.title = "Dashboard de Meningite - Região Sudeste"

# Servidor para deploy
server = app.server

# CSS para prevenir overflow
app.index_string = '''
<!DOCTYPE html>
<html>
    <head>
        {%metas%}
        <title>{%title%}</title>
        {%favicon%}
        {%css%}
        <style>
            * {
                box-sizing: border-box;
            }
            body {
                margin: 0;
                padding: 0;
                overflow-x: hidden;
            }
            .js-plotly-plot .plotly {
                max-width: 100% !important;
            }
        </style>
    </head>
    <body>
        {%app_entry%}
        <footer>
            {%config%}
            {%scripts%}
            {%renderer%}
        </footer>
    </body>
</html>
'''

# ==================== CORES E ESTILO ====================

colors = {
    'background': '#f8f9fa',
    'text': '#2c3e50',
    'primary': '#3498db',
    'secondary': '#e74c3c',
    'success': '#2ecc71',
    'warning': '#f39c12',
    'card': '#ffffff'
}

# ==================== FUNÇÕES AUXILIARES ====================

def create_kpi_card(titulo, valor, subtitulo="", cor=colors['primary']):
    """Cria um cartão KPI estilizado"""
    return html.Div([
        html.Div([
            html.H4(titulo, style={'color': '#7f8c8d', 'fontSize': '14px', 'marginBottom': '5px'}),
            html.H2(valor, style={'color': cor, 'fontSize': '32px', 'marginBottom': '5px', 'fontWeight': 'bold'}),
            html.P(subtitulo, style={'color': '#95a5a6', 'fontSize': '12px', 'margin': '0'})
        ], style={'padding': '20px'})
    ], style={
        'backgroundColor': colors['card'],
        'borderRadius': '8px',
        'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
        'margin': '10px',
        'textAlign': 'center'
    })

# ==================== KPIs ====================

kpi_total_casos = f"{int(total_casos):,}".replace(',', '.')
kpi_total_obitos = f"{int(total_obitos):,}".replace(',', '.')
kpi_taxa_letalidade = f"{taxa_letalidade_media:.2f}%"
kpi_casos_viral = f"{int(casos_viral):,}".replace(',', '.')

# ==================== LAYOUT DO DASHBOARD ====================

app.layout = html.Div([
    
    # Header
    html.Div([
        html.Div([
            html.H1("📊 Dashboard de Meningite - Região Sudeste", 
                   style={'color': colors['card'], 'marginBottom': '5px'}),
            html.P("Análise epidemiológica de casos de meningite (2018-2022)",
                  style={'color': '#ecf0f1', 'fontSize': '16px'})
        ], style={'padding': '30px', 'textAlign': 'center'})
    ], style={
        'backgroundColor': colors['primary'],
        'marginBottom': '20px',
        'boxShadow': '0 2px 8px rgba(0,0,0,0.1)'
    }),
    
    # Container principal
    html.Div([
        
        # Seção KPIs
        html.Div([
            html.Div([
                create_kpi_card("Total de Casos", kpi_total_casos, "2018-2022", colors['primary'])
            ], className='kpi-col'),
            html.Div([
                create_kpi_card("Total de Óbitos", kpi_total_obitos, "Período completo", colors['secondary'])
            ], className='kpi-col'),
            html.Div([
                create_kpi_card("Taxa de Letalidade", kpi_taxa_letalidade, "Média geral", colors['warning'])
            ], className='kpi-col'),
            html.Div([
                create_kpi_card("Meningite Viral", kpi_casos_viral, "Tipo predominante", colors['success'])
            ], className='kpi-col'),
        ], style={
            'display': 'grid',
            'gridTemplateColumns': 'repeat(auto-fit, minmax(250px, 1fr))',
            'gap': '10px',
            'marginBottom': '30px'
        }),
        
        # Filtros
        html.Div([
            html.Div([
                html.Label('Selecione o Período:', style={'fontWeight': 'bold', 'marginBottom': '10px'}),
                dcc.Dropdown(
                    id='filtro-periodo',
                    options=[
                        {'label': 'Todos os períodos', 'value': 'todos'},
                        {'label': 'Pré-Pandemia (2018-2019)', 'value': 'Pré-Pandemia'},
                        {'label': 'Pandemia (2020-2022)', 'value': 'Pandemia'}
                    ],
                    value='todos',
                    style={'marginBottom': '20px'}
                )
            ], style={
                'backgroundColor': colors['card'],
                'padding': '20px',
                'borderRadius': '8px',
                'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                'marginBottom': '20px'
            })
        ]),
        
        # Gráfico: Evolução Temporal
        html.Div([
            html.H3("📈 Evolução Temporal dos Casos", style={'color': colors['text'], 'marginBottom': '15px'}),
            dcc.Graph(id='grafico-evolucao')
        ], style={
            'backgroundColor': colors['card'],
            'padding': '20px',
            'borderRadius': '8px',
            'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
            'marginBottom': '20px'
        }),
        
        # Row com 2 gráficos
        html.Div([
            # Gráfico: Tipos de Meningite
            html.Div([
                html.H3("🦠 Distribuição por Tipo", style={'color': colors['text'], 'marginBottom': '15px'}),
                dcc.Graph(id='grafico-tipos', config={'displayModeBar': False}, style={'height': '400px'})
            ], style={
                'backgroundColor': colors['card'],
                'padding': '20px',
                'borderRadius': '8px',
                'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                'flex': '1',
                'minWidth': '400px',
                'maxWidth': '50%'
            }),
            
            # Gráfico: Taxa de Letalidade
            html.Div([
                html.H3("⚠️ Taxa de Letalidade por Ano", style={'color': colors['text'], 'marginBottom': '15px'}),
                dcc.Graph(id='grafico-letalidade', config={'displayModeBar': False}, style={'height': '400px'})
            ], style={
                'backgroundColor': colors['card'],
                'padding': '20px',
                'borderRadius': '8px',
                'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
                'flex': '1',
                'minWidth': '400px',
                'maxWidth': '50%'
            })
        ], style={
            'display': 'flex',
            'gap': '20px',
            'marginBottom': '20px',
            'flexWrap': 'nowrap',
            'overflow': 'hidden'
        }),
        
        # Gráfico: Distribuição por Faixa Etária
        html.Div([
            html.H3("👥 Distribuição por Faixa Etária", style={'color': colors['text'], 'marginBottom': '15px'}),
            dcc.Graph(id='grafico-faixa-etaria')
        ], style={
            'backgroundColor': colors['card'],
            'padding': '20px',
            'borderRadius': '8px',
            'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
            'marginBottom': '20px'
        }),
        
        # Gráfico: Comparação Pré-Pandemia vs Pandemia
        html.Div([
            html.H3("🔄 Impacto da Pandemia", style={'color': colors['text'], 'marginBottom': '15px'}),
            dcc.Graph(id='grafico-pandemia')
        ], style={
            'backgroundColor': colors['card'],
            'padding': '20px',
            'borderRadius': '8px',
            'boxShadow': '0 2px 4px rgba(0,0,0,0.1)',
            'marginBottom': '20px'
        }),
        
        # Footer
        html.Div([
            html.P([
                "📌 Fonte: Sistema de Informação de Agravos de Notificação (SINAN) | ",
                "Desenvolvido com Plotly Dash"
            ], style={'textAlign': 'center', 'color': '#7f8c8d', 'fontSize': '14px'})
        ], style={'marginTop': '30px', 'paddingBottom': '20px'})
        
    ], style={
        'maxWidth': '1400px',
        'margin': '0 auto',
        'padding': '0 20px'
    })
    
], style={'backgroundColor': colors['background'], 'minHeight': '100vh', 'fontFamily': 'Arial, sans-serif'})

# ==================== CALLBACKS ====================

@app.callback(
    [Output('grafico-evolucao', 'figure'),
     Output('grafico-tipos', 'figure'),
     Output('grafico-letalidade', 'figure'),
     Output('grafico-faixa-etaria', 'figure'),
     Output('grafico-pandemia', 'figure')],
    [Input('filtro-periodo', 'value')]
)
def update_graphs(periodo_selecionado):
    
    # Filtrar dados
    if periodo_selecionado == 'todos':
        df_filtrado = df_casos.copy()
    else:
        df_filtrado = df_casos[df_casos['periodo'] == periodo_selecionado].copy()
    
    # ===== GRÁFICO 1: Evolução Temporal =====
    fig_evolucao = go.Figure()
    
    fig_evolucao.add_trace(go.Scatter(
        x=df_filtrado['ano'],
        y=df_filtrado['total_casos'],
        mode='lines+markers',
        name='Total de Casos',
        line=dict(color=colors['primary'], width=3),
        marker=dict(size=10),
        fill='tozeroy',
        fillcolor='rgba(52, 152, 219, 0.1)'
    ))
    
    fig_evolucao.add_trace(go.Scatter(
        x=df_filtrado['ano'],
        y=df_filtrado['obitos'],
        mode='lines+markers',
        name='Óbitos',
        line=dict(color=colors['secondary'], width=3),
        marker=dict(size=10)
    ))
    
    fig_evolucao.update_layout(
        template='plotly_white',
        hovermode='x unified',
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
        xaxis_title='Ano',
        yaxis_title='Número de Casos',
        height=400,
        autosize=True
    )
    
    # ===== GRÁFICO 2: Tipos de Meningite =====
    tipos_data = df_filtrado[['mv', 'mb', 'mp', 'mm']].sum()
    tipos_labels = ['Viral', 'Bacteriana', 'Pneumocócica', 'Meningocócica']
    
    fig_tipos = go.Figure(data=[go.Pie(
        labels=tipos_labels,
        values=tipos_data,
        hole=0.4,
        marker=dict(colors=['#3498db', '#e74c3c', '#f39c12', '#9b59b6']),
        textinfo='percent',
        textposition='inside',
        hovertemplate='%{label}<br>%{value} casos<br>%{percent}<extra></extra>'
    )])
    
    fig_tipos.update_layout(
        template='plotly_white',
        height=400,
        showlegend=True,
        legend=dict(orientation='v', yanchor='middle', y=0.5, x=1.1),
        margin=dict(l=10, r=100, t=30, b=10),
        autosize=True
    )
    
    # ===== GRÁFICO 3: Taxa de Letalidade =====
    fig_letalidade = go.Figure()
    
    # Criar cores baseadas nos valores (sem colorbar para evitar problemas de layout)
    cores_letalidade = ['#fee5d9' if x < 8 else '#fcae91' if x < 9 else '#fb6a4a' if x < 10 else '#de2d26' 
                        for x in df_filtrado['taxa_letalidade']]
    
    fig_letalidade.add_trace(go.Bar(
        x=df_filtrado['ano'],
        y=df_filtrado['taxa_letalidade'],
        marker=dict(color=cores_letalidade),
        text=df_filtrado['taxa_letalidade'].round(2),
        textposition='outside',
        texttemplate='%{text}%',
        hovertemplate='Ano: %{x}<br>Taxa: %{y:.2f}%<extra></extra>'
    ))
    
    fig_letalidade.update_layout(
        template='plotly_white',
        xaxis_title='Ano',
        yaxis_title='Taxa de Letalidade (%)',
        height=400,
        showlegend=False,
        margin=dict(l=50, r=50, t=30, b=50),
        autosize=True
    )
    
    # ===== GRÁFICO 4: Faixa Etária =====
    faixas = ['menores_5anos', 'maiores_60anos']
    labels_faixas = ['Menores de 5 anos', 'Maiores de 60 anos']
    
    valores_faixas = df_filtrado[faixas].sum()
    outros = df_filtrado['total_casos'].sum() - valores_faixas.sum()
    valores_faixas = pd.concat([valores_faixas, pd.Series([outros], index=['outros'])])
    labels_faixas.append('Outras faixas etárias')
    
    # Criar gradiente de cores sem colorbar
    cores_faixas = px.colors.sample_colorscale('Viridis', [i/(len(valores_faixas)-1) for i in range(len(valores_faixas))])
    
    fig_faixa_etaria = go.Figure(data=[go.Bar(
        x=labels_faixas,
        y=valores_faixas,
        marker=dict(color=cores_faixas),
        text=valores_faixas,
        textposition='outside',
        hovertemplate='Faixa Etária: %{x}<br>Casos: %{y}<extra></extra>'
    )])
    
    fig_faixa_etaria.update_layout(
        template='plotly_white',
        xaxis_title='Faixa Etária',
        yaxis_title='Número de Casos',
        height=400,
        showlegend=False,
        margin=dict(l=50, r=50, t=30, b=50),
        autosize=True
    )
    
    # ===== GRÁFICO 5: Impacto da Pandemia =====
    comparacao = df_casos.groupby('periodo').agg({
        'total_casos': 'sum',
        'obitos': 'sum',
        'taxa_letalidade': 'mean'
    }).reset_index()
    
    fig_pandemia = go.Figure()
    
    fig_pandemia.add_trace(go.Bar(
        name='Casos',
        x=comparacao['periodo'],
        y=comparacao['total_casos'],
        marker_color=colors['primary'],
        text=comparacao['total_casos'],
        textposition='outside'
    ))
    
    fig_pandemia.add_trace(go.Bar(
        name='Óbitos',
        x=comparacao['periodo'],
        y=comparacao['obitos'],
        marker_color=colors['secondary'],
        text=comparacao['obitos'],
        textposition='outside'
    ))
    
    fig_pandemia.update_layout(
        template='plotly_white',
        barmode='group',
        xaxis_title='Período',
        yaxis_title='Quantidade',
        height=400,
        legend=dict(orientation='h', yanchor='bottom', y=1.02, xanchor='right', x=1),
        autosize=True
    )
    
    return fig_evolucao, fig_tipos, fig_letalidade, fig_faixa_etaria, fig_pandemia

# ==================== EXECUTAR APP ====================

if __name__ == '__main__':
    print("=" * 60)
    print("Dashboard de Meningite - Região Sudeste")
    print("=" * 60)
    print("\nAcesse o dashboard em: http://localhost:8050")
    print("\nPressione CTRL+C para parar o servidor")
    print("=" * 60)
    
    app.run(debug=True, port=8050)
