import csv
import pandas as pd


def load_purchases(
        purchase_file='purchase_log.txt',
        encoding='utf-8',
        skip_header=False
):
    """
    Читает purchase_log.txt в оперативную память.
    Возвращает словарь: user_id -> category.
    """
    purchases = {}

    with open(purchase_file, 'r', encoding=encoding) as f:
        reader = csv.reader(f)

        if skip_header:
            next(reader, None)

        for row in reader:
            if len(row) < 2:
                continue

            user_id, category = row[0], row[1]
            purchases.setdefault(user_id, category)

    return purchases


def process_visits(visit_file='visit_log.xlsx',
                   funnel_file='funnel.csv',
                   purchases=None,
                   encoding='utf-8'):

    if purchases is None:
        purchases = {}

    # Читаем Excel-файл. Первая строка — заголовок.
    df = pd.read_excel(visit_file)
    df['user_id'] = df['user_id'].astype(str)
    df_filtered = df[df['user_id'].isin(purchases.keys())].copy()

    # Добавляем категорию как третий столбец
    df_filtered.insert(2, 'category', df_filtered['user_id'].map(purchases))

    # Записываем результат
    df_filtered.to_csv(funnel_file, index=False, encoding='utf-8')


def main():
    purchases = load_purchases('purchase_log.txt')
    process_visits('visit_log.xlsx', 'funnel.csv', purchases)


if __name__ == '__main__':
    main()