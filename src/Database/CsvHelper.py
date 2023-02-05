import csv


def create_new_csv_file(filename: str, headers: list) -> None:
    with open(f'{filename}.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(headers)

def append_row_to_existing_csv_file(filename: str, row: list) -> None:
    with open(f'{filename}.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(row)
