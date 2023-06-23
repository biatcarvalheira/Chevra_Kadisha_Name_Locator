import pandas as pd
import time
import os
import datetime
import sys

input_list = []
first_name_list = []
last_name_list = []
date_of_death_list_cristian = []
date_of_death_list_hebrew = []

def add_lists_to_excel(first_name_list, last_name_list, date_of_death_list_cristian, date_of_death_list_hebrew):
    # Create a DataFrame from the lists
    data = {
        'Nome': first_name_list,
        'Sobrenome': last_name_list,
        'Data de Falecimento - Calendario Hebraico': date_of_death_list_hebrew,
        'Data de Falecimento - Calendario Cristão': date_of_death_list_cristian
    }


    df = pd.DataFrame(data)
    now = datetime.datetime.now()
    datestamp = now.strftime('%Y-%m-%d')
    script_dir = os.path.dirname(sys.argv[0])
    file_path = os.path.join(script_dir, f'Chevra_Kadisha_Resultado_de_Busca_{datestamp}.xlsx')

    # Create a new Excel writer
    writer = pd.ExcelWriter(file_path, engine='xlsxwriter')
    # Write the DataFrame to different sheets
    df.to_excel(writer, sheet_name= 'Resultado', index=False)
    # Save the Excel file and close the writer
    writer.close()

    print('#################### Program #################### ')
