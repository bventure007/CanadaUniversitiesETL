import requests
import pandas as pd
from bs4 import BeautifulSoup as bs
from sqlalchemy import create_engine

def extract_data():
    data_frames = []  # List to store DataFrames for each table
    url = 'https://en.wikipedia.org/wiki/List_of_universities_in_Canada'
    scrapped_data = requests.get(url).content
    soup = bs(scrapped_data, 'lxml') 

    tables = soup.find_all('table')

    for index, table in enumerate(tables):
        html_data = str(table)
        df = pd.read_html(html_data)[0]
        data_frames.append(df)
        df.to_csv(f'multiple_tables/universities_in_canada_{index + 1}.csv', index=False)
        print(f'Data for table {index + 1} successfully written to a csv file')

    return data_frames

# Call the function
# extracted_tables = extract_data()
# print(extracted_tables)




# # TRANFORM DATA







# # transform_data()
    
# # LOAD DATA TO POSTGRESDATA BASE
     
# def load_to_db():
#     data = pd.read_csv('Single_table/raw_oilspill_data.csv')
#     print(data)
#     engine = create_engine(f'postgresql+psycopg2://{db_user_name}:{db_password}@{host}:{port}/{db_name}')
#     data.to_sql('oil_spill_data',con= engine, if_exists='append',index=False)
#     print('Data successfully written to postgreSQL database')
    
    
# # load_to_db()
