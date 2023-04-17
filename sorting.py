import os
import csv

def read_data(file_name):
    """
    Reads csv file and returns numeric data.

    :param file_name: (str), name of CSV file
    :return: (dict), dictionary with numeric data, keys - csv column names, values - numbers in each column
    """
    cwd_path = os.getcwd()
    file_path = os.path.join(cwd_path, file_name)
    with open(file_path, "r") as csv_file:
        reader = csv.DictReader(csv_file)
        data = {}
        for row in reader:
            for header, value in row.items():
                if header not in data:
                    data[header] = [int(value)]
                else:
                    data[header].append(int(value))
    return data

def selection_sort(seznam_cisel):
    """
    Hledam nejmensi cislo, diky tomu seradim pak cely seznam podle velikosti
    """
    n = len(seznam_cisel)
    for i in range(n):
        min_idx = i
        for num_idx in range(i + 1, n):
            if seznam_cisel[num_idx] < seznam_cisel[min_idx]:
                min_idx = num_idx
        seznam_cisel[i], seznam_cisel[min_idx] = seznam_cisel[min_idx], seznam_cisel[i]
    return seznam_cisel

def bubble_sort(ciselny_seznam):
    n = len(ciselny_seznam)
    for i in range(n - 1):
        for idx in range(n - i - 1):
            if ciselny_seznam[idx] > ciselny_seznam[idx + 1]:
                ciselny_seznam[idx], ciselny_seznam[idx + 1] = ciselny_seznam[idx + 1], ciselny_seznam[idx]

    return ciselny_seznam



def main():
    my_data = read_data('numbers.csv')
    print(my_data['series_1'])
    selection_sort_result = selection_sort(my_data['series_1'])
    print(selection_sort_result)
    bubble_sort_result = bubble_sort(my_data['series_1'])
    print(bubble_sort_result)


if __name__ == '__main__':
    main()
