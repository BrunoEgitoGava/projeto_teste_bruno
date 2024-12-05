import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from scipy.stats import f_oneway, friedmanchisquare, kruskal, mannwhitneyu, shapiro,levene, ttest_ind, ttest_rel, wilcoxon
from matplotlib.ticker import PercentFormatter
    
def remove_outliers(dados, largura_bigodes = 1.5):
    q1 = dados.quantile(0.25)
    q3 = dados.quantile(0.75)
    iqr = q3-q1
    return dados[(dados >= q1-largura_bigodes*iqr) & (dados <= q3+largura_bigodes*iqr)]
#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#
def analise_levene(dataframe, alpha = 0.05, centro = "mean"):
    """cria um relatorio , onde analisa a homogeneidade das variâncias das amostras de um dataframe
    Espera um dataframe, alpha e o centro

    PARAMÉTRICO

    Parameters
    ----------
    dataframe: pd.DataFrame
        Data Frame com os dados
    aplha: int
        indica o nivel de significância . Padrão: 0.05
    centro: str
        indica a medida realizada para a analise. Padrão = MEAN

    """
    print("Teste de Levene")
    print("_______________")
    print()
    for coluna in dataframe.columns:
        estatistica_levene, valor_p_levene = levene(
            *[dataframe[coluna] for coluna in dataframe.columns],
            center=centro,
            nan_policy="omit"
        )

    print(f'Estatística {estatistica_levene = :.3f}')
    if valor_p_levene > alpha:
        print(f'Variâncias Iguais. (PVALUE = {valor_p_levene:.3f})')
    else:
        print(f'Ao menos uma variancia é diferente. (PVALUE = {valor_p_levene:.3f})')

#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#

def analise_ttest_ind(dataframe, alpha=0.05, variancias_iguais=True, alternativa="two-sided"):
    """função que realiza o teste T student para 1 amostra, quando o desvio padrão não é conhecido

    PARAMÉTRICO
    
    Parameters
    ----------
    dataframe: pd.DataFrame
        Data Frame com os dados
    aplha: int
        indica o nivel de significância . Padrão: 0.05
    variancias_iguais: str
        indica se as variancias observadas são iguais. Padrâo: True
    alternativa: str
        indica o tipo de teste a ser realizado (igual, maior ou menor). Padrão: two-sided

    """
    print("Teste de T Student Independentes")
    print("_______________")
    print()
    for coluna in dataframe.columns:
        estatistica_ttest, valor_p_ttest = ttest_ind(
            *[dataframe[coluna] for coluna in dataframe.columns],
            equal_var = variancias_iguais,
            alternative = alternativa,
            nan_policy="omit"
        )
    print(f'Estatística {estatistica_ttest = :.3f}')
    if valor_p_ttest > alpha:
        print(f'Não rejeita a hipotese nula. (PVALUE = {valor_p_ttest:.3f})')
    else:
        print(f'Rejeita a hipotese nula. (PVALUE = {valor_p_ttest:.3f})')

#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#
def analise_mannwhitneyu(dataframe, alpha=0.05, alternativa="two-sided"):
    """função que realiza o teste Mann-Whitney student para 2 amostras independentes não pareadas (quantitativa, ou
    qualitatia ordinal
    NÃO PARAMÉTRICO

    Parameters
    ----------
    dataframe: pd.DataFrame
        Data Frame com os dados
    aplha: int
        indica o nivel de significância . Padrão: 0.05
    alternativa: str
        indica o tipo de teste a ser realizado (igual, maior ou menor). Padrão: two-sided

    """
    print("Teste Mann-Whitney")
    print("_______________")
    print()
    for coluna in dataframe.columns:
        estatistica_mw, valor_p_mw = mannwhitneyu(
            *[dataframe[coluna] for coluna in dataframe.columns],
            nan_policy="omit",
            alternative = alternativa
        )
    print(f'Estatística {estatistica_mw = :.3f}')
    if valor_p_mw > alpha:
        print(f'Não rejeita a hipotese nula. (PVALUE = {valor_p_mw:.3f})')
    else:
        print(f'Rejeita a hipotese nula. (PVALUE = {valor_p_mw:.3f})')

#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#