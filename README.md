# TSE Tools
Um consolidador simples das planilhas do TSE para um banco de dados SQLite

## Instalação

Requisitos:
* Python 3
* Pandas

### Certifique-se de ter o [Python 3](https://www.python.org/) instalado
```console
python -V
```

Deve retornar a versão do Python instalada. Exemplo: ```Python 3.10.7```

### Instale o Pandas
```console
pip install pandas
```

## Como executar

* Salve o *consolidador.py* em uma pasta, e crie uma subpasta chamada "planilhas".
* Descompacte os arquivos CSV do TSE na pasta "planilhas".
* Execute o consolidador.py

```console
python consolidador.py
```

Será criado um banco de dados SQLite chamado filiados.sqlite

## Como consultar o Banco de Dados

Para consultar o banco, recomendo o [DB Browser for SQLite](https://sqlitebrowser.org/).

![Consultando o DB](/images/tse01.png?raw=true "Consultando o DB")

Em ```Navegar dados``` é possível visualizar a tabela completa.

Em ```Executar SQL``` é possível executar comandos de consulta avançados.

### Comandos SQL

Obter todos os filiados de um determinado partido:
```
SELECT * FROM filiados WHERE partido = "NOME DO PARTIDO"
```

Obter todos os filiados de um determinado partido em um determinado estado:
```
SELECT * FROM filiados WHERE partido = "NOME DO PARTIDO" AND uf = "UF"
```

Obter todos os filiados com um nome parcial, de um determinado partido e em um determinado estado:
```
SELECT * FROM filiados WHERE
    partido = "NOME DO PARTIDO"
    AND uf = "UF"
    AND nome LIKE "JOAO%SILVA%"
```

Consultando múltiplos nomes simultaneamente:

```
SELECT * FROM filiados WHERE
    partido = "NOME DO PARTIDO"
    AND uf = "UF"
    AND (
	nome LIKE "JOAO%SILVA%"
	OR nome LIKE "ANA%MARIA%"
        OR nome LIKE "PEDRO%SANTOS%"
    )
```
### Exportando os resultados

Para salvar os resultados de uma consulta:

![Consultando o DB](/images/tse02.png?raw=true "Consultando o DB")
