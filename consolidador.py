import os
from pathlib import Path

import pandas as pd
import sqlite3

file = Path('filiados.sqlite')
created = False
if not file.exists():
    created = True
    file.touch()

conn = sqlite3.connect('filiados.sqlite')
c = conn.cursor()

if not created:
    c.execute('DROP TABLE IF EXISTS filiados')

c.execute(
    '''
    CREATE TABLE filiados
    (
        partido text,
        uf text,
        municipio text,
        zona text,
        nome text,
        titulo text,
        data_filiacao date,
        situacao text
    )
    '''
)

for file in os.listdir('planilhas'):
    if file.endswith('.csv'):
        print(f'Importando {file}')
        df = pd.read_csv(f'planilhas/{file}', encoding='iso-8859-1')
        df.rename(
            columns={
                'Partido': 'partido',
                'UF': 'uf',
                'Município': 'municipio',
                'Zona': 'zona',
                'Nome do eleitor': 'nome',
                'Título de eleitor': 'titulo',
                'Data de filiação': 'data_filiacao',
                'Situação': 'situacao'
            },
            inplace=True
        )
        df.to_sql('filiados', conn, if_exists='append', index=False)
