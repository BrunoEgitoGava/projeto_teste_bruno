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
def histograma_alvo_categoricas(dataframe, categoricas, alvo, linhas=1, colunas=1):
    """faz o histograma de uma coluna alvo versus as colunas categoricas com 2 opções de valores em um dataframe 

    Parameters
    ----------
    dataframe: pd.DataFrame
        Data Frame completo, base de estudo
    categoricas: pd.DataFrame
        Data Frame com as colunas categoricas
    alvo: str
        indica a coluna alvo da analise
    linhas: int
        indica a quantidade de linhas do grid . Padrão: 1
    colunas: int
        indica a quantidade de colunas do grid . Padrão: 1

    """
    fig, axs = plt.subplots(nrows=linhas, ncols=colunas, figsize=(16,18), sharey=True, tight_layout=True)

    for i,coluna in enumerate(categoricas):
        h = sns.histplot(x=coluna,
                         data=dataframe,
                         hue = alvo,
                         multiple="fill", ax=axs.flat[i],
                         stat="percent",
                         shrink=0.8,
                         common_norm=True)
        
        h.tick_params(axis="x", labelrotation=45)
        h.grid(False)
        h.yaxis.set_major_formatter(PercentFormatter(1))
    
        for barra in h.containers:
            h.bar_label(barra,
                        label_type="center",
                        labels=[f'{parte.get_height():.1%}' for parte in barra],
                        color="white",
                        weight="bold"
                       )
        
        h.set_ylabel("")
        legenda=h.get_legend()
        legenda.remove()
    
    rotulos = [text.get_text() for text in legenda.get_texts()]
    fig.legend(
        handles=legenda.legend_handles,
        labels=rotulos,
        loc="upper center",
        ncols=2,
        title=alvo,
        bbox_to_anchor=(0.5,0.965)
    )
    fig.suptitle(f'{alvo} por variável Categórica\n\n"', fontsize=16)
    
    fig.align_labels()
    plt.show()


#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#
def histograma_categoricas_entre_si(dataframe, analise, alvo, linhas=1, colunas=1):
    """faz o histograma de uma coluna alvo versus as colunas categoricas com 2 opÃ§Ãµes de valores em um dataframe 

    Parameters
    ----------
    dataframe: pd.DataFrame
        Data Frame ccompleto, base de estudo
    analise: pd.DataFrame
        Data Frame com as colunas categoricas
    alvo: str
        indica a nova coluna alvo da analise
    linhas: int
        indica a quantidade de linhas do grid . PadrÃ£o: 1
    colunas: int
        indica a quantidade de colunas do grid . PadrÃ£o: 1

    """
    fig, axs = plt.subplots(nrows=linhas, ncols=colunas, figsize=(12,16))

    for ax,coluna in zip(axs.flatten(), analise):
        h = sns.histplot(x=alvo,
                         data=dataframe,
                         hue = coluna,
                         multiple="fill",
                         ax=ax,
                         stat="percent",
                         shrink=0.8,
                         common_norm=True)
        
        h.tick_params(axis="x", labelrotation=45)
        h.grid(False)
        h.yaxis.set_major_formatter(PercentFormatter(1))
    
        for barra in h.containers:
            h.bar_label(
                barra,
                label_type="center",
                labels=[f'{parte.get_height():.1%}' for parte in barra],
                color="white", weight="bold")
        
        h.set_ylabel("")
        legenda=h.get_legend()
    
        rotulos = [text.get_text() for text in legenda.get_texts()]
        numero_itens = len(dataframe[coluna].cat.categories)
        ax.legend(
            handles = legenda.legend_handles,
            labels = rotulos, 
            loc="upper center",
            ncols=numero_itens if numero_itens <=6 else min(4,numero_itens),
            bbox_to_anchor=(0.5,1.15)
        )
        ax.set_title(f'Distribuição de {coluna} x {alvo}', fontsize=14, pad=55)
    
    plt.subplots_adjust(wspace=0.1, hspace=0.5, top = 0.925)
    plt.show()

#---------------------------------------------------------------------------------------------------------------------#
#---------------------------------------------------------------------------------------------------------------------#

def composicao_histograma_boxplot(dataframe, coluna, intervalos="auto"):
    """cria uma composição tabela de distribuição de frequencias para a coluna de um dataframe
    Espera uma coluna categorica

    Parameters
    ----------
    dataframe: pd.DataFrame
        Data Frame com os dados
    coluna: str
        nome da coluna categorica
    intervalos: bool
        indica . Padrão: False
        

    return
    ------
    dataframe: pd.DataFrame
        Data Frame com a tabela de distribuição de frequencias  

    """
    fig, (ax1,ax2) = plt.subplots(
        nrows=2, 
        ncols=1,
        sharex=True,
        gridspec_kw={
            "height_ratios": (0.15, 0.85),
            "hspace":0.02
        }
    )
    
    sns.boxplot(
        data=dataframe,
        x=coluna,
        showmeans=True,
        meanline=True,
        meanprops={"color":"C1", "linewidth":"1.5", "linestyle":"--"},
        medianprops={"color":"C2", "linewidth":"1.5", "linestyle":"--"},
        ax=ax1
    )
    sns.histplot(data=dataframe, x=coluna, kde=True, bins=intervalos, ax=ax2)
    
    for ax in (ax1, ax2):
        ax.grid(True, linestyle="--", color="gray", alpha=0.5)
        ax.set_axisbelow(True)
    
    ax2.axvline(dataframe[coluna].mean(), color="C1", linestyle="--", label="Média")
    ax2.axvline(dataframe[coluna].median(), color="C2", linestyle="--", label="Mediana")
    ax2.axvline(dataframe[coluna].mode()[0], color="C3", linestyle="--", label="Moda")
    ax2.legend()
    
    plt.show()
