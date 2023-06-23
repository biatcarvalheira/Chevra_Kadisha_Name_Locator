import os
from selenium.webdriver.chrome.options import Options

#Selenium ChromeDriver
TIMEOUT = 10
current_path = os.path.dirname(os.path.abspath(__file__))
print(current_path)
chromeDriverFile = "chromedriver"
folder_path = os.path.join(current_path, chromeDriverFile)


#input file
input_file = 'nomes de familias.csv'
input_file_folder_path = os.path.join(current_path, input_file)

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