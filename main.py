import csv
import time

from selenium.common import WebDriverException
from selenium.webdriver.support import wait

from modules.navigation import *
from modules.scraper import *
from modules.output import *
import requests

from config import *
from bs4 import BeautifulSoup

from openpyxl import load_workbook


def main():
    while True:
        # get input csv files with the list of surnames
        input_list_names = []
        file_path = name_list_path
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                input_list_names.extend(row)

        counter = 1
        # enter website
        print(f'#### {len(input_list_names)} famílias... ####')
        for l in input_list_names:
            driver, success = make_request_headless('https://www.chevrakadisha.org.br/localize')
            if success:
                print(f'## Buscando nomes da família: {l} ({counter})##')
                load_and_click(driver, '//*[@id="cookies-policy"]/a')
                insert_text(driver, '//*[@id="index-form"]/div/form/div[1]/div[2]/input', l)
                load_and_click(driver, '//*[@id="index-form"]/div/form/footer/button')
                time.sleep(10)
                soup = get_source(driver)

                content_block = find_all(soup, 'header', class_, 'section-header')
                # Names are in the second position onwards and go till the second to last
                if len(content_block) >= 3:
                    for n in content_block[1:-1]:
                        # N A M E  &  D O D
                        name = n.find('h2')
                        # # Name
                        name_text = name.text
                        name_words = name_text.split()
                        first_name = name_words[0]
                        last_name = ' '.join(name_words[1:])
                        ## Final version of first name and last name
                        first_name_list.append(first_name)
                        last_name_list.append(last_name)
                        # Dod
                        dod_block = n.find('p')
                        dod_block_text = dod_block.text
                        new_dod_block_text = dod_block_text.replace("Falecido(a) em:", "")

                        # Separate into Christian and Hebrew dod
                        result_dod = new_dod_block_text.split("|")[0].strip()
                        cristian_dod = result_dod.split('-')[0].strip()
                        hebrew_dod = result_dod.split('-')[1].strip()

                        ## Final version of first name and last name
                        date_of_death_list_cristian.append(cristian_dod)
                        date_of_death_list_hebrew.append(hebrew_dod)

                        # Print Lists
                        # list_count = 0
                        # for f in first_name_list:
                        #     print('First Name:', f)
                        #     print('Last Name', last_name_list[list_count])
                        #     print('DOD Cristian', date_of_death_list_cristian[list_count])
                        #     print('DOD Hebrew', date_of_death_list_hebrew[list_count])
                        #     list_count +=1
            driver.quit()
            counter += 1
            # Save final Lists
            add_lists_to_excel(first_name_list, last_name_list, date_of_death_list_cristian, date_of_death_list_hebrew)

        break

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
