# Análise Estatística da base de dados Diabetes

O diabetes é uma doença crônica grave na qual os indivíduos perdem a capacidade de regular efetivamente os níveis de glicose no sangue e pode levar a uma redução na qualidade de vida e na expectativa de vida.

O Sistema de Vigilância de Fatores de Risco Comportamentais (BRFSS) é uma pesquisa telefônica relacionada à saúde que é coletada anualmente pelo CDC (Centro de Controle e Prevenção de Doenças dos Estados Unidos). 

A cada ano, a pesquisa coleta respostas de milhares de americanos sobre comportamentos de risco relacionados à saúde, condições crônicas de saúde e o uso de serviços preventivos. 

O intuito deste projeto é identificar os principais causas e condições assosciadas ao aparecimento dessa doença. Para o estudo, foi utilizado conjunto de dados disponível no Kaggle para o ano de 2015.

[kaggle](ttps://www.kaggle.com/datasets/alexteboul/diabetes-health-indicators-dataset)

![imagem](imagens/diabetes.jpg)

## Organização do projeto

```
├── .gitignore         <- Arquivos e diretórios a serem ignorados pelo Git
├── ambiente.yml       <- O arquivo de requisitos para reproduzir o ambiente de análise
├── LICENSE            <- Licença de código aberto (MIT)
├── README.md          <- README principal para desenvolvedores que usam este projeto.
|
├── dados              <- Arquivos de dados para o projeto.
|
├── notebooks          <- Cadernos Jupyter.
│
|   └──src             <- Código-fonte para uso neste projeto.
|      │
|      ├── __init__.py  <- Torna um módulo Python
|      ├── config.py    <- Configurações básicas do projeto
|      └── estatistica.py  <- funções criadas para esse projetos
|
├── referencias        <- Dicionários de dados, manuais e todos os outros materiais explicativos.
|
├── imagens         <- Imagens utilizadas no projeto
```

## Configuração do ambiente

1. Faça o clone do repositório.

    ```bash
    git clone git@github.com:BrunoEgitoGava/projeto_teste_bruno.git
    ```

2. Crie um ambiente virtual para o seu projeto utilizando o conda

   ```bash
    conda env create -f > ambiente.yml --name diabetes
    ```

## Um pouco mais sobre a base

[Clique aqui](referencias/01_dicionario_de_dados.md) para ver o dicionario de dados

## Considerações iniciais

Inicialmente foi realizada uma análise na base de dados a fim de conhecer melhor como os dados estão apresentandos, e também para verificar a existência de incoerências, buscando a forma mais adequada para tratá-los.

Os comentários estão descritos no arquivo [Tratando a base](notebooks/01-BESG-tratando_a_base.ipynb)

## Resumo dos principais resultados

A partir da base de dados já tratada, a análise dos dados foi realizada buscando traçar um perfil das pessoas que apresentam possuem Diabetes. Além disso buscou-se a identificação de fatores atenuantes dessa doença, podendo servir de base para um programa de prevenção à diabetes.

Os resultados estão apresentados arquivo [EDA](notebooks/02-BESG-analise_estatistica.ipynb)