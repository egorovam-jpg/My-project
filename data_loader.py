import pandas as pd

# Загрузка данных
FILE_ID = "1M1-EG2MXn_kv-A-sVe50zwn7D6csOfF1"
file_url = f"https://drive.google.com/uc?id={FILE_ID}"
raw_data = pd.read_csv(file_url)
print(raw_data.head(10))
# Проверка текущих типов и данных
print(raw_data.dtypes)  # покажет текущие типы столбцов
print(raw_data.head(10))
print(raw_data.info())  # более полное описание данных, включая количество пропусков
# Проверка текущих типов и данных
numeric_columns = [
    "Year",
    "Savanna fires",
    "Forest fires",
    "Crop Residues",
    "Rice Cultivation",
    "Drained organic soils (CO2)",
    "Pesticides Manufacturing",
    "Food Transport",
    "Forestland",
    "Net Forest conversion",
    "Food Household Consumption",
    "Food Retail",
    "On-farm Electricity Use",
    "Food Packaging",
    "Agrifood Systems Waste Disposal",
    "Food Processing",
    "Fertilizers Manufacturing",
    "IPPU",
    "Manure applied to Soils",
    "Manure left on Pasture",
    "Manure Management",
    "Fires in humid tropical forests",
    "Rural population",
    "Urban population",
    "Total Population - Male",
    "Total Population - Female",
    "total_emission",
    "Average Temperature °C",
]
# Приведение к числовому типу
for str in numeric_columns:
    if str in raw_data.columns:
        raw_data[str] = pd.to_numeric(raw_data[str], errors="coerce")
# Проверка наличия пропусков
print(raw_data.isnull().sum())
# Удаление строк с пропусками
raw_data.dropna(subset=numeric_columns, inplace=True)
# Сохранение обработанных данных
raw_data.to_csv("processed_data.csv", index=False)



