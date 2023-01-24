import os 
import math
import csv 
print()

with open("life-expectancy.csv") as data_set:
    data_set = csv.reader(data_set)
    for line in data_set:
        clean_line = line.strip()
        line_list = clean_line.split(",")

        entity = str(line_list[0])
        code = str(line_list[1])
        year = float(line_list[2])
        life_expectancy = float(line_list[3])

        year_lookup = input("Enter the year of interest: ")

        min_life = math.min(line_list[3])
        max_life = math.max(line_list[3])
        avg_life = math.mean(line_list[3])

        max_life = 0
        if (line_list[3]) > float(max(max_life)):
            max_year = str(line_list[0])
            max_country = int(line_list[2])
        print(f"The overall max life expectancy is:{max_life} from {max_country} in {max_year}.")

        min_data = 0
        if (line_list[3]) > float(min(min_life)):
            min_year = str(line_list[0])
            min_country = str(line_list[2])
        print(f"The overall max life expectancy is:{min_life} from {min_country} in {min_year}.")