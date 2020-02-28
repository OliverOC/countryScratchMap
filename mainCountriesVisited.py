from functionLib import if_no_json_create_new, add_countries, rearrange_dict_by_country, \
    extract_country_by_year, plot_by_year


if __name__ == "__main__":
    file_name = 'countries_visited'
    if_no_json_create_new(file_name)
    add_country = raw_input('would you like to add a new country?:(Y or N)')

    if add_country.lower() == 'y':
        add_countries(file_name)
    else:
        pass

    rearranged_dict_name = 'cv_by_year'
    rearrange_dict_by_country(file_name, rearranged_dict_name)

    year_from = 1996
    year_to = 2020
    years = range(year_from, year_to + 1)
    countries_by_year_list = extract_country_by_year(rearranged_dict_name, years, include_none=True)
    plot_by_year(years, countries_by_year_list)







