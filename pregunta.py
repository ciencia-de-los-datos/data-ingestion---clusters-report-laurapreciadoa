"""
Ingestión de datos - Reporte de clusteres
-----------------------------------------------------------------------------------------

Construya un dataframe de Pandas a partir del archivo 'clusters_report.txt', teniendo en
cuenta que los nombres de las columnas deben ser en minusculas, reemplazando los espacios
por guiones bajos; y que las palabras clave deben estar separadas por coma y con un solo 
espacio entre palabra y palabra.


"""
import pandas as pd
import re
def ingest_data():

    with open('clusters_report.txt') as f:
        data = [line.strip() for line in f.readlines()[4:]]

    data_word = []
    word = ''
    for line in data:
        if line:
            word += ' ' + line
        else:
            data_word.append(word.strip())
            word = ''

    block = []
    for i in data_word:
        regular = re.search(r'(^[0-9]+)\W+([0-9]+)\W+([0-9]+)([!#$%&*+-.^_`|~:\[\]]+)(\d+)(\W+)(.+)', i)
        linea = regular.group(1) + '*' + regular.group(2) + '*' + regular.group(3) + '.' + regular.group(5) + '*' + regular.group(7)
        block.append(linea)

    data_set = [line.split('*') for line in block]
    df = pd.DataFrame(data_set, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

    df['cluster'] = df['cluster'].astype(int)
    df['cantidad_de_palabras_clave'] = df['cantidad_de_palabras_clave'].astype(int)
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].astype(float)

    principales_palabras_clave = df['principales_palabras_clave'].str.replace('    ', ' ').str.replace('   ', ' ').str.replace('  ', ' ').str.replace('.', '').str.split(',')
    df['principales_palabras_clave'] = principales_palabras_clave.apply(lambda x: ', '.join(map(str.strip, x)))

    return df
