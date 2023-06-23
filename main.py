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
        file_path = input_file_folder_path
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip the header row
            for row in reader:
                input_list_names.extend(row)

        # enter website
        driver, success = make_request('https://www.chevrakadisha.org.br/localize')
        if success:
            insert_text(driver, '//*[@id="index-form"]/div/form/div[1]/div[2]/input', input_list_names[0])
            load_and_click(driver, '//*[@id="index-form"]/div/form/footer/button')
            time.sleep(10)
        break






# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
