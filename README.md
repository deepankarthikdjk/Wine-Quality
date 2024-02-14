# ML Wine Quality Project

### Workflows

update config.yaml
# configuration for data ingestion
# download data from GITHUB - create folder called artifact/data_ingestion/wine.zip
# unzip file/wine.csv

update schema.yaml
# used for Data Validation
# column name and datatype
# independant and dependant columns

update params.yaml
# initially updating with dummy key:value because the file should not be empty while running, if file is empty - will throw error

update the entity
# entity represents a fundamental unit of data or functionality within the project

update the configuration manager in src config
# updating all the Paths and other details in constants-init.py

update the components
# writing all class and objects for data ingestion(downloading data, extracting zip file) by reading paths from config.yaml

update the pipeline
# telling which function to call first:1.download_file and extract_zip_file 
update the main.py
update the app.py
 