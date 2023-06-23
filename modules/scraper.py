import time

import requests
from bs4 import BeautifulSoup
import re
import json


def get_source(driver):
    html = driver.page_source
    soup = BeautifulSoup(html, 'lxml')
    return soup


def find(soup, section, attribute, att_identifier):
    find_result = soup.find(section, {attribute: att_identifier})
    return find_result


def find_all(soup, section, attribute, att_identifier):
    result_find_all = soup.find_all(section, {attribute: att_identifier})
    return result_find_all


def append_simple(source_list, target_list):
    for f in source_list:
        target_list.append(f)
    return target_list


def append_to_list_text(source_list, target_list):
    for f in source_list:
        #      print(f.text)
        target_list.append(f.text)
    return target_list


def append_to_list_href(source_list, target_list):
    for h in source_list:
        #     print(h['href'])
        target_list.append(h['href'])
    return target_list


def get_source_requests(link):
    page = requests.get(link)
    soup = BeautifulSoup(page.text, 'lxml')
    return soup


''''This function identifies year patterns in a string, gets the non year content in a list and the year content in another'''


def split_content_year(string):
    pattern = r'\b\d{4}\b'  # Regular expression pattern to match a 4-digit number (year)
    matches = re.findall(pattern, string)  # Find all matches of the pattern in the string
    matches = str(matches)
    # Remove the matched years from the original string
    content = re.sub(pattern, '', string).strip()
    return content, matches


def find_pattern_position(list, pattern):
    if pattern in list:
        i = list.index(pattern)
    else:
        i = 'None'
    # print('pattern not found')
    return i


def find_pattern_position_multiple(list, pattern1, pattern2):
    if pattern1 in list:
        i = list.index(pattern1)
    elif pattern2 in list:
        i = list.index(pattern2)
    else:
        i = 'None'
    #     print('pattern not found')
    return i
    #     print('pattern not found')
    return i


def find_pattern_position_multiple_return_all(list, pattern1, pattern2):
    pattern_position_list = []
    for p in list:
        if pattern1 in list:
            i = list.index(pattern1)
            pattern_position_list.append(i)
        if pattern2 in list:
            i = list.index(pattern2)
            pattern_position_list.append(i)
        else:
            i = 'None'
        #      print('pattern not found')
        return pattern_position_list
    return


# checks if a string matches any in a list of patterns
def find_pattern_in_string(patterns, string):
    for pattern in patterns:
        match = re.search(pattern, string)
        if match:
            return match.group()  # Returns the matched pattern
    return None  # Returns None if no match is found


def find_and_extract_pattern_in_string(pattern, string):
    match = re.search(pattern, string)
    if match:
        extracted_zip_code = match.group(1)
        return extracted_zip_code
        print(extracted_zip_code)
    else:
        extracted_zip_code = 'N/A'
        return extracted_zip_code


def extract_pattern_in_string(string, pattern):
    p = pattern
    match = re.search(p, string)
    if match:
        return match.group()
    else:
        return None


def find_pattern_in_list(pattern, input_list):
    for item in input_list:
        match = re.search(pattern, item)
        if match:
            return match.group(0)  # Returns the first matching pattern found
    return None  # Returns None if no match is found


def find_all_patterns_in_list(pattern, input_list):
    matches = []  # Create an empty list to store all the matching patterns
    for item in input_list:
        pattern_matches = re.findall(pattern, item)
        if pattern_matches:
            matches.extend(pattern_matches)  # Add the matching patterns to the list
    if matches:
        return matches
    return None  # Returns None if no match is found


def retrieve_numbers_from_string(string):
    numbers = re.findall(r'\d+', string)
    converted_int = int(''.join(map(str, numbers)))
    number_clean = int(converted_int)
    return number_clean


def check_if_none(variable):
    if type(variable) == type(None):
        #   print("Variable is of type NoneType")
        return True
    else:
        # print("Variable is not of type NoneType")
        return False


def convert_string_to_list(string):
    try:
        lst = json.loads(string)
        int_list = [int(x) for x in lst]
        return int_list
    except ValueError:
        int_list = 0
        return int_list


def convert_html_item_to_text(html_text):
    new_text = ''
    try:
        new_text = html_text.text
    except AttributeError:
        pass

    return new_text


def empty_list(lst):
    lst.clear()


def remove_duplicates_from_list(list_to_be_modified):
    new_list = list(set(list_to_be_modified))
    return new_list


def remove_item_from_list(old_list, new_list, pattern):
    for item in old_list:
        if pattern not in item:
            new_list.append(item)


def remove_2_items_from_list(old_list, new_list, pattern1, pattern2):
    for item in old_list:
        if pattern1 not in item:
            new_list.append(item)
        if pattern2 not in item:
            new_list.append(item)

def add_line_break(string):
    pattern = r'(\S\S)'
    replacement = r'\1\n'
    new_string = re.sub(pattern, replacement, string)
    return new_string

def keep_last_characters(number, string):
    return string[-number:]


def remove_non_numeric(string):
    # Remove all non-numeric characters using regex
    numeric_string = re.sub(r'\D', '', string)
    return numeric_string


def remove_from_second_http(string):
    pattern = r'(https?://.*?)(https?://.*)'
    match = re.search(pattern, string)
    if match:
        return match.group(1)
    return string