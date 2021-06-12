import csv
from os import error
from matplotlib import pyplot as plt
import math
import numbers
ERROR_MESSAGES = ["argument count error",
                  "argument type error", "formatting error"]


def parse_table(*args):
    if(len(args) != 1):
        print(F"Введено неверное количество аргументов:")
        print(F"\tОжидалось: {1}")
        print(F"\tВведено: {len(args)}")
        return ERROR_MESSAGES[0]
    empty_string = ""
    file_path = args[0]
    if(type(file_path) != type(empty_string)):
        print(F"Введен неверный тип аргументов:")
        print(F"\tОжидалось: { type(empty_string) }")
        print(F"\tВведено: {type(args[0])}")
        return ERROR_MESSAGES[1]
    if(not file_path.endswith(".csv")):
        print(F"Введен неверный тип аргументов:")
        print(F"\tОжидалось: '*.csv'")
        print(F"\tВведено: '*{file_path[-4:]}'")
        return ERROR_MESSAGES[1]
    try:
        with open(file_path, 'r') as csv_file:
            headers = csv.reader(csv_file)
            next(headers)
            next(headers)
            dict_keys = next(headers)
            csv_reader = csv.DictReader(csv_file, fieldnames=dict_keys)
            data = []
            for line in csv_reader:
                data.append(line)
        return data
    except:
        print(F"По введенному пути невозможно открыть файл")
        return ERROR_MESSAGES[1]


def draw_dependancy_graphs(*args):
    if(len(args) == 0):
        print(F"Не введено ни одного аргумента:")
        return ERROR_MESSAGES[0]
    countries = []
    data = parse_table("CropProduction.csv")
    if(len(args) == 1):
        try:
            in_countries = iter(args[0])
            for country in in_countries:
                if(type(country) != str):
                    return ERROR_MESSAGES[1]
                countries.append(country)
        except:
            if(type(args[0]) == str):
                countries.append(args[0])
        if(len(countries) == 0):
            return ERROR_MESSAGES[1]
    if(len(args) > 1):
        for country in args:
            if(type(country) != str):
                return ERROR_MESSAGES[1]
            countries.append(country)
    subjects_total = []
    per_country_data = {}
    per_country_subjects = {}
    per_country_measures = {}
    for country in countries:
        contains = False
        collected_data = []
        collected_subjects = []
        collected_measures = []
        for line in data:
            if(line["LOCATION"] == country):
                if(not line["SUBJECT"] in collected_subjects):
                    collected_subjects.append(line["SUBJECT"])
                if(not line["MEASURE"] in collected_measures):
                    collected_measures.append(line["MEASURE"])
                if(not line["SUBJECT"] in subjects_total):
                    subjects_total.append(line["SUBJECT"])
                collected_data.append(line)
                contains = True
        if not contains:
            return ERROR_MESSAGES[2]
        per_country_data[country] = collected_data
        per_country_subjects[country] = collected_subjects
        per_country_measures[country] = collected_measures
    figures = {}
    per_subject_measures = {}
    for subject in subjects_total:
        different_measures = []
        for country in countries:
            for line in per_country_data[country]:
                if line["SUBJECT"] == subject:
                    if not line["MEASURE"] in different_measures:
                        different_measures.append(line["MEASURE"])
        per_subject_measures[subject] = different_measures
        figures[subject] = plt.figure(figsize=(len(different_measures)*5, 5))
        figures[subject].suptitle(F"предмет оценивания - {subject}")
    for subject in subjects_total:
        index = 1
        width = len(per_subject_measures[subject])
        for measure in per_subject_measures[subject]:
            sub = figures[subject].add_subplot(1, width, index)
            sub.set_title(
                F"Измерено в {measure}")
            index += 1
            for country in countries:
                x_values = []
                y_values = []
                if(not subject in per_country_subjects[country]):
                    continue
                if(not measure in per_country_measures[country]):
                    continue
                for line in per_country_data[country]:
                    if(line["SUBJECT"] == subject) and (line["MEASURE"] == measure):
                        x_values.append(float(line["TIME"]))
                        y_values.append(float(line["Value"]))
                sub.plot(x_values, y_values, label=country)
            sub.legend()
    plt.show()
    return 0


def take_year(dict):
    return int(dict["YEAR"])


def take_value(line):
    return float(line["VALUE"])


def take_delta(line):
    return line[2]


def task_3(*args):
    if(len(args) != 2):
        print("введено не верное количество аргументов")
        return ERROR_MESSAGES[0]
    error_message = "При вводе параметров, встретились параметры с неверном типом:\n"
    error_state = False
    for argument in args:
        if (not isinstance(argument, int)):
            error_message = error_message + \
                F"\tаргумент {argument} - не целое число\n"
            error_state = True
    if(error_state):
        print(error_message)
        return ERROR_MESSAGES[1]
    data = parse_table("CropProduction.csv")
    amount_of_highest = args[0]
    amount_of_lowest = args[1]
    per_subject_data = {}
    per_subject_decades = {}
    for line in data:
        country = line["LOCATION"]
        subject = line["SUBJECT"]
        measure = line["MEASURE"]
        year = int(line["TIME"])

        value = float(line["Value"])
        if not subject in per_subject_data.keys():
            per_subject_data[subject] = {}
            per_subject_decades[subject] = {}
        if not measure in per_subject_data[subject].keys():
            per_subject_data[subject][measure] = {}
            per_subject_decades[subject][measure] = {}
            per_subject_decades[subject][measure]["START"] = year
            per_subject_decades[subject][measure]["END"] = year
        if not country in per_subject_data[subject][measure].keys():
            per_subject_data[subject][measure][country] = {}
            per_subject_data[subject][measure][country] = []
        per_subject_data[subject][measure][country].append(
            {"YEAR": year, "VALUE": value})
        if year < per_subject_decades[subject][measure]["START"]:
            per_subject_decades[subject][measure]["START"] = year
        if year > per_subject_decades[subject][measure]["END"]:
            per_subject_decades[subject][measure]["END"] = year
    with open("output.csv", 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_NONNUMERIC, delimiter="\t")
        writer.writerow(["SUBJECT", "MEASUREMENT", "DECADE", "ORDER",
                        "RAITING PLACE", "COUNTRY", "ACTUAL TIME", "DELTA"])
        for subject in per_subject_data.keys():
            for measure in per_subject_data[subject].keys():
                measurement_period_start = per_subject_decades[subject][measure]["START"]
                measurement_period_end = per_subject_decades[subject][measure]["END"]
                decade_start = measurement_period_start
                decade_end = measurement_period_start
                per_subject_decades[subject][measure]["DECADES"] = []
                while decade_end < measurement_period_end:
                    decade_end += 10
                    if decade_end <= measurement_period_end:
                        per_subject_decades[subject][measure]["DECADES"].append(
                            {"START": decade_start, "FINISH": decade_end})
                        decade_start = decade_end
                        continue
                    decade_end = measurement_period_end
                    per_subject_decades[subject][measure]["DECADES"].append(
                        {"START": decade_start, "FINISH": decade_end})
                    break
                deltas = {}
                for decade in per_subject_decades[subject][measure]["DECADES"]:
                    start = decade["START"]
                    finish = decade["FINISH"]
                    decade_name = f"decade [{start}..{finish}]"
                    deltas[decade_name] = []
                    for country, per_country_data in per_subject_data[subject][measure].items():
                        per_country_data.sort(key=take_year)
                        current_country_first_year = take_year(
                            per_country_data[0])
                        current_country_last_year = take_year(
                            per_country_data[-1])
                        if current_country_first_year in range(decade["START"], decade["FINISH"]):
                            start = current_country_first_year
                        if current_country_last_year in range(decade["START"], decade["FINISH"]):
                            finish = current_country_last_year

                        start_found = False
                        finish_found = False
                        start_value = 0
                        finish_value = 0
                        for pair in per_country_data:
                            if start_found and finish_found:
                                break
                            else:
                                if take_year(pair) == start:
                                    start_value = take_value(pair)
                                    start_found = True
                                    continue
                                if take_year(pair) == finish:
                                    finish_value = take_value(pair)
                                    finish_found = True
                                    continue
                        delta = finish_value-start_value
                        if(start_found and finish_found):
                            deltas[decade_name].append(
                                (country, f"{start} : {finish}", delta))
                    deltas[decade_name].sort(key=take_delta)
                    for i in range(amount_of_highest):
                        if(len(deltas[decade_name]) >= i+1):
                            written_country = deltas[decade_name][-(i+1)][0]
                            written_time = deltas[decade_name][-(i+1)][1]
                            written_delta = deltas[decade_name][-(i+1)][2]
                            writer.writerow([subject, measure, decade_name, "HIGHEST",
                                            i+1, written_country, written_time, written_delta])
                        else:
                            writer.writerow([subject, measure, decade_name, "HIGHEST",
                                            i+1, "NONE", "NONE", "NONE"])
                    for i in range(amount_of_lowest):
                        written_country = deltas[decade_name][i][0]
                        written_time = deltas[decade_name][i][1]
                        written_delta = deltas[decade_name][i][2]
                        writer.writerow([subject, measure, decade_name, "LOWEST",
                                        i+1, written_country, written_time, written_delta])
    return 0
