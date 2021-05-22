# Desafio_Tecnico-Solaris_Capital

Aplicação Web feita em Flask e Python para o processo seletivo para a vaga de  Engenheiro de Software 1 na Solaris Capital (https://www.solcap.com.br/)<br>

- **/youngers/{n}**: Retorna uma lista das n pessoas mais jovens ordenadas ascendentemente
- **/olders/{n}**: Retorna uma lista das n pessoas mais velhas ordenadas ascendentemente
- **/gender-distribution**: Retorna um Json com a distribuição percentual de generos no dataset: Ex.: {"Feminino" 51%, "Masculino": 49%}
- **/people/{cpf_without_punctuation}**: Retorna os dados de uma única pessoa em formato json
- **/blood-type/stats**: Retorna a distribuição absoluta de grupos sanguíneos: {"B-": 20, "O+": 10...}
- **/peoples**: Lista os nomes de todas as pessoas no dataset em ordem alfabética
- **/peoples/search?q=query**: Busca pessoas por nome ou por parte do nome (case insensitive)