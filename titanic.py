import pyarrow.parquet as pq

table = pq.read_table("titanic.parquet")
df = table.to_pandas()
df

'''import pandas as pd
import matplotlib.pyplot as plt

# Функция для чтения данных, сохранения в CSV и построения гистограммы
def process_titanic_data(parquet_file, output_csv):
    # Чтение данных из parquet файла
    data = pd.read_parquet(parquet_file)

    # Сохранение данных в формат CSV
    data.to_csv(output_csv, index=False, encoding="utf-8-sig")
    print(f"Данные успешно сохранены в файл: {output_csv}")

    # Проверка структуры данных
    print("Первые строки данных:")
    print(data.head())

    # Построение гистограммы
    plot_survival_by_class(data)

# Функция для построения гистограммы
def plot_survival_by_class(data):
    # Группировка данных по классу билета и статусу выживаемости
    survival_data = data.groupby(['Pclass', 'Survived']).size().unstack(fill_value=0)

    # Нормализация данных для отображения в процентах
    survival_percent = survival_data.div(survival_data.sum(axis=1), axis=0) * 100

    # Построение графика
    survival_percent.plot(kind='bar', stacked=True, color=["skyblue", "lightcoral"], figsize=(10, 6))
    plt.title("Выживаемость пассажиров Титаника", fontsize=14)
    plt.xlabel("Класс билета", fontsize=12)
    plt.ylabel("Процент пассажиров", fontsize=12)
    plt.legend(["Выжил", "Не выжил"], loc="upper left", fontsize=10)
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.xticks(ticks=range(len(survival_percent.index)), labels=["Первый класс", "Второй класс", "Третий класс"], rotation=0)
    plt.show()

# Основной код
parquet_file = "titanic.parquet"  # Имя исходного parquet файла
output_csv = "titanic.csv"       # Имя файла для сохранения в формате CSV

process_titanic_data(parquet_file, output_csv)'''