import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import skew
import statsmodels.api as sm

# configuração de estilo visual
sns.set_theme(style="whitegrid")

# lendo o csv
dataframe_goty = pd.read_csv(
    './data/Games Awards Goty Nominees and Winners 2014-2024.csv')

# forçando conversão numérica inicial para evitar erros na limpeza
cols_to_numeric = ['User-Score', 'Votes', 'Meta-Score', 'Reviews']
for col in cols_to_numeric:
    dataframe_goty[col] = pd.to_numeric(dataframe_goty[col], errors='coerce')

# removendo linhas sem notas ou com valores nulos nas colunas críticas
dataframe_goty.dropna(
    subset=['User-Score', 'Votes', 'Meta-Score', 'Reviews'], inplace=True)

# --- análise do skewness ---
skewness_votes = skew(dataframe_goty['Votes'])
print(f'skewness (assimetria) da coluna votes: {skewness_votes:.2f}')

# transformação logarítmica para normalizar a distribuição de dados muito assimétricos
dataframe_goty['logaritmo_votes'] = np.log1p(dataframe_goty['Votes'])
print("transformação log aplicada na coluna 'votes' para normalizar a escala.")
print('-' * 50)

# --- estatísticas descritivas ---
# selecionando colunas de interesse para o resumo
colunas_descritivas = ['Meta-Score', 'Reviews', 'User-Score', 'Votes']
dataframe_descritiva = dataframe_goty[colunas_descritivas]

# gerando resumo estatístico (tendência central, dispersão, quartis)
resumo_estatistico = dataframe_descritiva.describe()

print("### resumo estatístico completo")
print(resumo_estatistico.round(2))

# --- regressão linear ---
# variável independente (x) = logaritmo_votes (proxy de popularidade)
# variável dependente (y) = user-score (qualidade percebida pelo usuário)

x = dataframe_goty['logaritmo_votes']
y = dataframe_goty['User-Score']
# adiciona a constante (intercepto) necessária para o statsmodels
x_sm = sm.add_constant(x)

# ajustando o modelo de mínimos quadrados ordinários (ols)
model = sm.OLS(y, x_sm).fit()

print(model.summary())

# verificação da hipótese estatística
coef = model.params['logaritmo_votes']
p_value = model.pvalues['logaritmo_votes']

print('--- resultado da hipótese ---')
print(f'coeficiente: {coef:.4f}')
print(f'p-value: {p_value:.4f}')

# lógica de validação da hipótese baseada em p-value < 0.05
if p_value < 0.05 and coef < 0:
    print('hipótese comprovada')
    print('existe uma correlação negativa estatisticamente relevante')
    print('quanto maior a quantidade de votos, menor tende a ser o user-score')
elif p_value < 0.05 and coef > 0:
    print('hipótese invertida')
    print('jogos mais populares tendem a ter notas maiores.')
else:
    print('hipótese negada')
    print('não há evidência estatística suficiente.')

# --- geração de gráficos ---
plt.figure(figsize=(18, 6))

# gráfico 1: histograma de distribuição (analisa normalidade e skewness)
plt.subplot(1, 3, 1)
sns.histplot(x=dataframe_goty['Votes'], bins=40, kde=True, color='purple')
plt.title(f'Distribuição de votos (Skewness: {skewness_votes:.2f})')
plt.xlabel('Quantidade de votos (Votes)')
plt.ylabel('Frequência')
# limitando visualmente outliers extremos para facilitar leitura
plt.xlim(0, dataframe_goty['Votes'].quantile(0.95))
plt.tight_layout()
plt.show()

# gráfico 2: scatter plot com linha de regressão (visualização da correlação)
plt.subplot(1, 3, 2)
sns.scatterplot(data=dataframe_goty, x='logaritmo_votes',
                y='User-Score', alpha=0.4, color='gray')
sns.regplot(data=dataframe_goty, x='logaritmo_votes',
            y='User-Score', scatter=False, color='red')
plt.title(f'Regressão: Popularidade vs User-Score\n(Coef: {coef:.2f})')
plt.xlabel('Popularidade (Logaritmo Votes)')
plt.ylabel('User-Score')
plt.tight_layout()
plt.show()

# gráfico 3: boxplot comparativo (vencedores vs não vencedores)
# converte para string para tratamento categórico no seaborn
dataframe_goty['Wins'] = dataframe_goty['Wins'].astype(str)
plt.subplot(1, 3, 3)
sns.boxplot(data=dataframe_goty, x='Wins', y='logaritmo_votes',
            hue='Wins', palette={'0': "#2F9500", '1': "#ffcd03"},
            legend=False)
plt.title('Vencedores GOTY são mais populares?')
plt.xlabel('Venceu GOTY? (0=Não, 1=Sim)')
plt.ylabel('Popularidade (Logaritmo Votes)')
plt.xticks([0, 1], ['Não Venceu', 'Venceu'])
plt.tight_layout()
plt.show()

# ajuste final de layout e exibição
