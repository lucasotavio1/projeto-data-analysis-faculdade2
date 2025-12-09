<h1 align="center">análise estatística da indústria de games: popularidade vs. percepção de qualidade</h1>

<h3 align="left">objetivo</h3>
<p>
O objetivo deste projeto é realizar uma análise estatística avançada em um conjunto de dados de alta relevância da indústria de videogames, aplicando técnicas de manipulação, estatística descritiva e modelagem de regressão. O foco é garantir a replicabilidade da análise em um contexto acadêmico e técnico.
</p>

<h3 align="left">descrição do projeto</h3>
<p>
Neste projeto, foi escolhido o conjunto de dados "Games Awards Goty Nominees and Winners 2014-2024" (disponível no <a href="https://www.kaggle.com/datasets/alejandrobelda/games-awards-nominees-2014-2024" target="_blank">kaggle</a>), focado em títulos indicados e vencedores do prêmio Game of the Year. A hipótese levantada foi a do "efeito bola de neve" ou "maldição da popularidade": jogos com maior popularidade (alto volume de votos) tendem a apresentar notas de Usuário (user-score) mais baixas devido à exposição de massa, mas essa popularidade não prejudica suas chances de vitória no prêmio principal. 
  
as etapas incluiram:
  
  - cálculo e análise de skewness
  - estatísticas descritivas (média, mediana, desvio padrão, quartis)
  - modelagem por Regressão Linear OLS
  - visualização dos resultados (3 gráficos)
  - verificação da hipótese
</p>

<h3 align="left">estrutura do projeto</h3>
  
```
|-- data
|   `-- Games Awards Goty Nominees and Winners 2014-2024.csv
|
|-- reports
|   `-- figures
|       |-- distribuicao_votos.png
|       |-- regressao_popularidade_vs_score.png
|       `-- boxplot_vencedores_vs_popularidade.png
|
|-- src
|   |-- __init__.py
|   `-- analise_goty.py
|
|-- LICENSE
|-- README.md
|-- requirements.txt
```

---

<h3 align="left">autor</h3>

feito com o ❤️ por Lucas Otávio e <a href="https://github.com/Bernardofbs" target="_blank">@Bernardofbs</a>
