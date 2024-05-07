import pandas as pd

datos = pd.read_csv("mines.csv", sep="|")

datos.columns = datos.columns.str.replace("|", "_")
sql_datos_cabecera="insert into mines VALUES ("


def return_insert(values):
    txt_data = ""
    for i in values:
        if str(i) == "nan":
            txt_data = txt_data + "\'\',"
        elif isinstance(i, (int, float)):
            txt_data = txt_data + str(i) + ","
        else:
            txt_data = txt_data + "\'" + str(i) + "\',"

    return txt_data



SQL_FINAL = ""
for indice, fila in datos.iterrows():
    txt = return_insert(fila.values)
    txt = txt[0:-1]  # Eliminar la última coma

    SQL_FINAL = SQL_FINAL + sql_datos_cabecera + str(indice+1) + "," + txt + ");\n"


with open("mines.sql", "w", encoding="UTF-8") as f:
    f.write(SQL_FINAL)