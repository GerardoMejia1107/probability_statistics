import pandas as pd

# Esta función se encarga de leer una columna  y devolver un DataFrame de pandas.
def frecuency_by_range(column, bins_numbers, label_names):
    serie_grouped = pd.Series(column).round(2)
    intervals_variable = pd.cut(serie_grouped, bins=bins_numbers, labels=label_names, right=False, include_lowest=True)
    return intervals_variable.value_counts().sort_index()

# Esta función se encarga de leer los rangos y devolver un array con las clases modales.
def xi_classes (range_indexes):
    xi = []
    for i in range(len(range_indexes)):
        x = float(range_indexes.str.split("-").str[0][i])
        y = float(range_indexes.str.split("-").str[1][i])
        xi.append((x+y)/2)
    return xi

# Esta función devuelve un Dataframe
def grouped_data_table(variable, range_series):
    grouped_table = pd.DataFrame({
        "L -": range_series.index.str.split("-").str[0],
        "L": range_series.index.str.split("-").str[1],
        "xi": xi_classes(range_series.index),
        "fi abs": range_series.values,
        "fi sum": range_series.cumsum(),
        "fi %": (range_series.values / range_series.sum()) * 100,
    })
    return grouped_table

# Esta función se encarga de exportar el DataFrame a un archivo CSV.
def export_grouped_csv(grouped_dataframe_table, variable_name, route):
    grouped_dataframe_table.to_csv(f"{route}{variable_name}.csv")
