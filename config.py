import os
from selenium.webdriver.chrome.options import Options

#Selenium ChromeDriver
TIMEOUT = 10
current_path = os.path.dirname(os.path.abspath(__file__))
chromeDriverFile = "chromedriver"
folder_path = os.path.join(current_path, chromeDriverFile)

name_list = 'nomes_de_familias.csv'
name_list_path = os.path.join(current_path, name_list)
#URLS
bmw_url_list = ['https://www.bmwusa.com/inventory/results?FuelType=E', 'https://www.bmwusa.com/certified-preowned-search.html#/results?FuelType=Electric&Year=2020%7C2021%7C2022%7C2023', 'https://www.bmw.ca/en/ssl/InventorySearch.html', 'https://www.bmw.ca/en/ssl/PreOwnedSearch.html#/bookmark=aHR0cHM6Ly9ibXduYXRpb25hbGludmVudG9yeS5yaWNobW9uZGRheS5jb20vZW4vUHJlT3duZWRJbnZlbnRvcnlTZWFyY2g/ZGw9JHt1cmxQYXJhbWV0ZXIuZGx9JnNuPSR7dXJsUGFyYW1ldGVyLnNufSZyaWQ9JHt1cmxQYXJhbWV0ZXIucmlkfSZuPSR7dXJsUGFyYW1ldGVyLm59JmF0PSR7dXJsUGFyYW1ldGVyLmF0fQ==']
mercedes_url_list = ['https://www.mbusa.com/en/inventory/search?class=EQB:SUV,EQE:SDN,EQS:SDN,EQS:SUV&place=ChIJOwg_06VPwokRYv534QaPC8g', 'https://www.mbusa.com/en/cpo/inventory/search?model=EQB300W4,EQB350W4,EQB250W,EQS450X,EQS580X4,EQS450X4,EQE500V4,EQE350V,AMGEQEV4,EQE350V4,EQS53V4,EQS580V4,EQS450V,EQS450V4,AMGEQSV4&place=ChIJOwg_06VPwokRYv534QaPC8g', 'https://www.mercedes-benz.ca/en/inventory/search?place=ChIJoajRnzS1WEwRIABNrq0MBAE', 'https://www.mercedes-benz.ca/en/cpo/inventory/search?place=ChIJDbdkHFQayUwR7-8fITgxTmU']
polestar_url_list_usa = [
'https://www.polestar.com/us/preconfigured-cars?dealercode=USBOS0018&zipcode=02134'
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USRKV0016&zipcode=20855',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USNYC0031&zipcode=10023'
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USEHA0011&zipcode=07078',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USWPR0011&zipcode=06880',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USLRV0011&zipcode=08648',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USCMH0017&zipcode=43213',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USFHI0012&zipcode=48335',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USCLT0024&zipcode=28262',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USATL0019&zipcode=30341',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USTPA0024&zipcode=33614',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USGVY0011&zipcode=MN%2055416',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USPBI0020&zipcode=33409',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USFLL0022&zipcode=33317',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USAPF0013&zipcode=FL%2034109',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USGPV0011&zipcode=76051',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USHOU0039&zipcode=77094',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USAUS0020&zipcode=78752',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USLTO0013&zipcode=80206',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USPHX0026&zipcode=85251',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USTUK0012&zipcode=98004',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USMJI0012&zipcode=92651',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USBVW0012&zipcode=97005',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USVNY0011&zipcode=90212',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USSNN0011&zipcode=95050',
'https://www.polestar.com/us/preconfigured-cars/?dealercode=USSRF0013&zipcode=94925'
]
polestar_url_list_canada = ['https://www.polestar.com/en-ca/preconfigured-cars/?dealercode=CALAV0017&zipcode=H7T%202W3', 'https://www.polestar.com/en-ca/preconfigured-cars/?dealercode=CATOR0015&zipcode=M5R%203L2', 'https://www.polestar.com/en-ca/preconfigured-cars/?dealercode=CAVAN0014&zipcode=V7T%202Y5']

polestar_url_list_usa_used = [
    'https://www.polestar.com/us/preowned-cars/search-result/polestar-1/',
    'https://www.polestar.com/us/preowned-cars/search-result/polestar-2/',
    'https://www.polestar.com/us/preowned-cars/search-result/polestar-3/'
]
polestar_url_list_canada_used = [
    'https://www.polestar.com/en-ca/preowned-cars/search-result/polestar-1/',
    'https://www.polestar.com/en-ca/preowned-cars/search-result/polestar-2/',
    'https://www.polestar.com/en-ca/preowned-cars/search-result/polestar-3/'
]
#BMW - USA New/Used - XPaths

bmw_location_field = '//*[@id="zipentry-input"]'
bmw_shop_now_button = '//*[@id="app"]/div/div/div/div[3]/form/button'
bmw_select_result = '//*[@id="app"]/div/div/div/div[4]/div/div[2]/div[1]/div[2]/button'
bmw_vehicles_available_now = '//*[@id="app"]/div/div[2]/div/div[1]/label/span'
bmw_pre_owned_selection = '//*[@id="app"]/div/div[4]/div/div[1]/div[2]/label/div'
bmw_fuel_type = '//*[@id="app"]/div/div[2]/div/div[9]/button/span'
bmw_fuel_type_used = '//*[@id="app"]/div/div[4]/div/div[11]/button/i'
bmw_electric_checkbox = '//*[@id="fueltype"]/div/label[1]/span[1]'
bmw_electric_checkbox_used = '//*[@id="fueltype"]/div/label[3]/div'
bmw_confirm_popup = '/html/body/div[3]/div/button'
bmw_set_range = '//*[@id="app"]/div/div[1]/div[2]/div/div[1]/button/span'
bmw_select_10_miles = '//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[4]/button[1]'
bmw_select_range_50_miles = '//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[4]/button[3]'
bmw_select_range_100_miles = '//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div[4]/button[4]'
bmw_update_range = '//*[@id="app"]/div/div[1]/div[2]/div/div[1]/div/div/div[2]/button[2]'
bmw_next_page = '//*[@id="scroll-top-target"]/div[4]/button[2]'

#BMW - Canada New/Used - XPaths

bmw_ca_ok_cookies_button = '/html/body/epaas-consent-drawer-shell//html/body/div/div/section/div[3]/div/div[2]/button/span'
bmw_ca_close_initial_location_window = '//*[@id="province-selection--modal-close"]'
bmw_ca_select_provinces_list = '//*[@id="dlProvince"]'
bmw_ca_select_bc = '//*[@id="dlProvince"]/option[3]'
bmw_ca_select_quebec = '//*[@id="dlProvince"]/option[9]'
bmw_ca_continue_button = '//*[@id="province-selection--button"]'
bmw_ca_select_retailer = '//*[@id="FilterContainer"]/div/div[1]/div[2]/div[4]/span/div/button'
bmw_ca_select_all_retailers = '//*[@id="multiselect_006jdl93hu1wv_0_0"]'
bmw_ca_select_advanced_search = '//*[@id="FilterContainer"]/div/div[1]/div[2]/div[5]/div[1]'
bmw_ca_select_fuel_type = '//*[@id="dlFuelType"]'
bmw_ca_select_electric = '//*[@id="dlFuelType"]/option[2]'
bmw_ca_confirm_search = '//*[@id="FilterContainer"]/div/div[3]/div[3]/div[2]/div[2]/button'
bmw_ca_next_page = '//*[@id="VehicleDiv"]/div[2]/div[1]/a'



bmw_confirm_popup_used = '/html/body/div[3]/div/button'
bmw_set_range_used = '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/button/span'
bmw_select_range_50_miles_used = '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div/div[2]/div[4]/button[3]'
bmw_select_range_nationwide_used = '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div[1]/div[3]/div[4]/button[5]'
bmw_update_range_used = '//*[@id="app"]/div/div[3]/div[2]/div/div[1]/div/div/div[2]/button[2]'


#Mercedes - XPaths

merc_enter_location_field = '//*[@id="_li7tjl3qqexjh"]'
merc_select_first_choice = '//*[@id="listbox_li7tnh1h852j7"]/li[1]'
merc_confirm_choice_location = '//*[@id="inventory-container"]/div/div/div/div/div/div[2]/button'


#Polestar - XPaths
pol_accept_cookies = '//*[@id="onetrust-accept-btn-handler"]'
pol_location_field = '//*[@id="autocomplete-field-2"]'
pol_select_first_option = '//*[@id="autocomplete-field-2-popover-0"]'
pol_load_all_locations = '//*[@id="root"]/div[2]/div[4]/div[2]/div/div/section/div/div/div/div/div[1]/div[6]/button'
pol_select_first_location = '//*[@id="root"]/div[2]/div[4]/div[2]/div/div/section/div/div/div/div/div[1]/div[6]/div[1]/button'
pol_select_all_available_cars = '//*[@id="featuredInventorySection"]/div/div[3]/div[1]/a'
pol_used_location_field = '//*[@id="text-field-1"]'
pol_confirm_used_location = '//*[@id="root"]/div[2]/div[6]/div[2]/div/div/div/div[3]/button'

#html terms
button = 'button'
div = 'div'
class_ = 'class'
section = 'section'
href = 'a'
h1 = 'h1'
h2 = 'h2'
h3 = 'h3'
span = 'span'
li = 'li'
id_ = 'id'
p = 'p'

mile_pattern = 'Miles'
price_pattern = r'\$\d{1,3}(?:,\d{3})*(?:\.\d+)?'
price_pattern_2 = r'\$ \d{1,3}(?:,\d{1,3})?\*'
us_zip_pattern = r'\b\d{5}(?:-\d{4})?\b'
canada_zip_pattern = r"\b([A-Z]\d[A-Z] \d[A-Z]\d)\b"
address_pattern = r'^(\d+)\s+(.*?)\s+(St|Street|Ave|Avenue),\s+(.*?),\s+([A-Z]{2})\s+(\d{5})$'
us_state_pattern = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA', 'HI', 'ID', 'IL', 'IN', 'IA', 'KS', 'KY', 'LA', 'ME', 'MD', 'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ', 'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC', 'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']
us_address_pattern = '^\d+\s\w+\s\w+,\s\w+,\s\w+\s\d+$'
km_pattern = r'^\d{1,4}(?:,\d{1,3})?[ \n]*(?:backspace\s*)*km\b'
vin_number = r'\b[A-HJ-NPR-Z0-9]{17}\b'
pol_range_field_pattern = r'\b\d{1,4}\b.*?\bmiles\b.*?\(EPA\)'

initial_display_messages = ['USA New', 'USA Used', 'Canada New', 'Canada Used']

country_options_list = ['United States', 'Canada']



brand_names_list = ['BMW', 'Mercedes', 'Polestar', 'Tesla', 'Audi']

state_abbreviations = [
    'NY',
    'NJ',
    'CT',
    'NJ',
    'MA',
    'MD',
    'OH',
    'MI',
    'NC',
    'GA',
    'FL',
    'MN',
    'FL',
    'FL',
    'TX',
    'TX',
    'CO',
    'AZ',
    'WA',
    'CA',
    'CA',
    'OR',
    'CA',
    'CA',
    'CA'
]
quebec_zip_code_list = ['H7T 2X3', 'G6V 8X4', 'H4P 1V5', 'J3E 3R6', 'J1N 2A8', 'J8C 1W3', 'G1M 4A6', 'H9P 2N4', 'J6V 0A8', 'J7C 5T7', 'J4X 1C2', 'G8T 8P6']
bc_zip_code_list = ['V6X 1K8', 'V3A 0C2', 'V9T 3Y3', 'V9A 3K8', 'V5M 4W5', 'V1X 7X5', 'V7P 3R8', 'V6J 3H5']

quebec_retailer_list = ['BMWi Laval', 'BMW Levis', 'BMW Montreal Centre', 'BMW Saint-Julie', 'BMW Sherbrooke', 'BMW / MINI Ste-Agathe', 'BMW ville de Quebec', 'BMW West Island', 'Grenier BMW', 'Hamel BMW', 'Park Avenue BMW', 'Trois-Rivieres BMW']

bc_retailer_list = ['Auto West BMW', 'BMW Langley', 'BMW Nanaimo (BMW-MINI)', 'BMW Victoria', 'Brian Jessel BMW', 'Kelowna BMW', 'Park Shore BMW', 'The BMW Store']

polestar_usa_city_state_list = {
    "Manhattan": "NY",
    "Washington": "DC",
    "Detroit": 'MI',
    "Charlotte": 'NC',
    "Atlanta": 'GA',
    "Minneapolis": 'MN',
    "Palm Beach": 'FL',
    "Fort Lauderdale": 'FL',
    "Naples": 'FL',
    "Grapevine": 'TX',
    "Houston": 'TX',
    "Austin": 'TX',
    "Bellevue": 'WA',
    "South Coast": 'CA',
    "Portland": 'WA',
    "Los Angeles": 'CA',
    "San Jose": 'CA',
    "Marin": 'CA',
    "Boston": "MA",
    "Westport": "CT",
    "Princeton": "NJ",
}

polestar_usa_used_zip_code_list = {
    "Manhattan": "10023",
    "Washington": "20855",
    "Detroit": '48335',
    "Charlotte": '28262',
    "Atlanta": '30341',
    "Minneapolis": '2055416',
    "Palm Beach": '33409',
    "Fort Lauderdale": '33317',
    "Naples": '2034109',
    "Grapevine": '76051',
    "Houston": '77094',
    "Austin": '78752',
    "Bellevue": '98004',
    "South Coast": '92651',
    "Portland": '97005',
    "Los Angeles": '90212',
    "San Jose": '95050',
    "Marin": '94925',
    "Boston": "02134",
    "Westport": "06880",
    "Princeton": "08648"

}
temporary_distance_list_polestar_usa = {
    "NY": '601 km aprox.',
    "DC": '947 km aprox.',
    "MI": '1036 km aprox.',
    "NC": '1498 km aprox.',
    "GA": '1952 km aprox.',
    "MN": '2028 km aprox.',
    "FL": '2424 km aprox.',
    "TX": '3070 km aprox.',
    "WA": '4696 km aprox.',
    "CA": '4735 km aprox.',
    "MA": '405 km aprox.',
    "CT": '436 km aprox.',
    "NJ": '592 km aprox.',

}

polestar_canada_city_state_list = {"MONTREAL": "QC", "TORONTO": "ON", "VANCOUVER": "BC", "Montreal": "QC", "Toronto": "ON", "Vancouver": "BC"}

polestar_canada_city_state_list_used = {
    "Montreal": "QC",
    "Toronto": "ON",
    "Vancouver": "BC"
}
temporary_distance_list_polestar_canada = {
    "QC": '0 km',
    "ON": '542.3 km',
    "BC": '4.560 km'
}
polestar_canada_used_zip_code_list = {
    "Montreal": "H7T 2W3",
    "Vancouver": "M5R 3L2",
    "Toronto": 'V7T 2W4'
}