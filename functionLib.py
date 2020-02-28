import json
import os
import matplotlib.pyplot as plt
import pandas as pd
from collections import defaultdict


def if_no_json_create_new(file_name):
    if os.path.exists(str(file_name)+'.json'):
        pass
    else:
        empty_dict = {}
        with open((str(file_name))+'.json', 'w') as f:
            json.dump(empty_dict, f)


def add_countries(file_name):
    add_more = True
    while add_more:
        with open((str(file_name))+'.json', 'r') as f:
            countries = json.load(f)

        accepted_country = False
        while not accepted_country:

            def check_country(country_to_check):
                with open('country_list.json', 'r') as f2:
                    countries_json = json.load(f2)

                if country_to_check.title() in countries_json.keys():
                    accepted = True
                    return accepted
                else:
                    accepted = False
                    print('Error: country not recognised. '
                          'This might be due to a spelling error.')
                    see_list = input('Press ''L'' to see a list of all countries, or press ''X'' to continue...')
                    if see_list.lower() == 'l':
                        string_countries_list = [str(x) for x in sorted(countries_json.keys())]
                        print(string_countries_list)
                    elif see_list.lower() == 'x':
                        pass
                    return accepted

            input_country = input('What country did you visit?:')
            accepted_country = check_country(input_country)

        input_year = input('What year did you visit? (if multiple visits include list, e.g. 2010, 2016):')
        split_input_years = input_year.split(',')
        split_input_years_strip = [int(i.strip()) for i in split_input_years]
        if input_country.title() in countries.keys():
            for year in range(len(split_input_years_strip)):
                countries[input_country.title()].append(split_input_years_strip[year])
        else:
            countries[input_country.title()] = split_input_years_strip

        with open((str(file_name)+'.json'), 'w') as f:
            json.dump(countries, f)

        add_again = input("Would you like to add another country?(Y or N):")

        if add_again.lower() == 'y':
            add_more = True
        elif add_again.lower() == 'n':
            add_more = False


def rearrange_dict_by_country(json_file_name, new_file_name):
    with open((str(json_file_name)+'.json'), 'r') as f:
        dictionary = json.load(f)

    dictionary_values = list(dictionary.values())
    dictionary_keys = list(dictionary.keys())
    dictionary_keys_new_list = []
    dictionary_values_new_list = []

    for i in range(len(dictionary_keys)):
        if len(dictionary_values[i]) > 1:
            for ii in range(len(dictionary_values[i])):
                dictionary_keys_new_list.append(dictionary_values[i][ii])
                dictionary_values_new_list.append(dictionary_keys[i]+str(ii+1))
        else:
            dictionary_keys_new_list.append(dictionary_values[i][0])
            dictionary_values_new_list.append(dictionary_keys[i])

    new_dictionary = dict(zip(dictionary_values_new_list, dictionary_keys_new_list))
    new_dictionary_inverted = defaultdict(list)
    {new_dictionary_inverted[v].append(k) for k, v in new_dictionary.items()}

    with open((str(new_file_name)+'.json'), 'w') as f2:
        json.dump(new_dictionary_inverted, f2)


def extract_country_by_year(file_name, year, include_none=False):
    with open(str(file_name)+'.json') as f:
        countries_by_year = json.load(f)

    if type(year) == int:
        if str(year) in list(countries_by_year.keys()):
            output = countries_by_year[str(year)]
            return output
        else:
            print('no countries visited in ' + str(year))

    elif type(year) == list:
        output_countries = []
        for i in range(len(year)):
            if str(year[i]) in list(countries_by_year.keys()):
                output_countries.append(countries_by_year[str(year[i])])
            else:
                if include_none:
                    output_countries.append('')
                else:
                    print('no countries visited in ' + str(year[i]))
        return output_countries


def plot_by_year(years, countries):
    country_number = []
    for i in range(len(countries)):
        if countries[i] == "":
            country_number.append(0)
        else:
            country_number.append(len(countries[i]))
    plt.bar(years, country_number, color='green', width=1, align='center')
    plt.xlabel('Year', labelpad=20, fontsize=20)
    plt.xticks(years, rotation=90)
    plt.ylabel('Countries Visited', labelpad=20, fontsize=20)
    plt.yticks(range(0, max(country_number) + 2))
    plt.show()
