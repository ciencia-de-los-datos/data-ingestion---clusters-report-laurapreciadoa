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
        lines = [line.strip() for line in f.readlines()[4:]]

    concatenated_lines = []
    current_line = ''
    for line in lines:
        if line:
            current_line += ' ' + line
        else:
            concatenated_lines.append(current_line.strip())
            current_line = ''

    processed_data = []
    for line in concatenated_lines:
        match = re.search(r'(^[0-9]+)\W+([0-9]+)\W+([0-9]+)([!#$%&*+-.^_`|~:\[\]]+)(\d+)(\W+)(.+)', line)
        result_line = match.group(1) + '*' + match.group(2) + '*' + match.group(3) + '.' + match.group(5) + '*' + match.group(7)
        processed_data.append(result_line)

    data_set = [line.split('*') for line in processed_data]
    df = pd.DataFrame(data_set, columns=['cluster', 'cantidad_de_palabras_clave', 'porcentaje_de_palabras_clave', 'principales_palabras_clave'])

    df['cluster'] = df['cluster'].astype(int)
    df['cantidad_de_palabras_clave'] = df['cantidad_de_palabras_clave'].astype(int)
    df['porcentaje_de_palabras_clave'] = df['porcentaje_de_palabras_clave'].astype(float)

    principales_palabras_clave = df['principales_palabras_clave'].str.replace('    ', ' ').str.replace('   ', ' ').str.replace('  ', ' ').str.replace('.', '').str.split(',')
    df['principales_palabras_clave'] = principales_palabras_clave.apply(lambda x: ', '.join(map(str.strip, x)))

    return df

