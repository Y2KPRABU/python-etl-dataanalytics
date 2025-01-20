# ProjectHelp

## Project Overview
This project is a simple ETL (Extract, Transform, Load) process implemented in Python. The main objective is to extract artist data from Spotify, validate the data, and then load it into an Azure Data Lake Storage (ADLS) as a Parquet file.

## ETL Process Description

### Extract
The extraction process involves downloading data from the Spotify API. The `extract_data` function in `utils/extract.py` fetches artist data from Spotify using their API.

### Transform
The transformation process involves validating the extracted data to ensure it meets certain criteria. The `check_if_valid_data` function in `utils/validation.py` validates the extracted data. This step is crucial to ensure that only clean and accurate data is loaded into the database.

### Load
The final step is loading the validated data into a database. The `createFileFromdata` and `pushtoADLS` functions in `utils/LoadIntoADLS.py` convert the data into a Parquet file and upload it to ADLS. This step ensures that the data is stored in a structured format for easy access and analysis.

### Tools and Libraries Used
- **Python**: The primary programming language used for the ETL process.
- **Pandas**: A powerful data manipulation library used for data transformation.
- **Spotify API**: Used to extract data related to the user's listening history.
- **Azure Data Lake Storage (ADLS)**: Used for storing the processed data.
- **numpy, pyarrow, python-dotenv, pytz, requests, azure-storage-file-datalake**: Various libraries used for data processing and storage.

## Repository Structure
- **.env.example**: Template for environment variables.
- **.gitignore**: Specifies files and directories to be ignored in the repository.
- **.vscode/launch.json**: Configuration for debugging in Visual Studio Code.
- **README.md**: Project documentation.
- **localartistspot.parquet**: Sample Parquet file.
- **main.py**: Main script that orchestrates the ETL process.
- **pyproject.toml**: Project metadata and dependencies for Poetry.
- **requirements.txt**: List of dependencies for pip.
- **utils/LoadIntoADLS.py**: Contains functions to load data into ADLS.
- **utils/extract.py**: Contains functions to extract data from Spotify.
- **utils/sampleresponseartist.json**: Sample JSON response from Spotify.
- **utils/validation.py**: Contains functions to validate the data.

## Setting Up the Project
1. Clone the repository to your local machine.
2. Create a virtual environment and install dependencies using `pip install -r requirements.txt`.
3. Create a copy of the `.env.example` file and rename it to `.env`. Fill in your personal information (`sas-token`, `Adls account name`, etc.).

## Execution
Run the ETL process with:
```sh
python3 main.py
```

## Conclusion
This project provides a simple yet effective way to implement an ETL process using Python. By following the steps outlined above, you can set up and run the ETL process to extract, transform, and load data from the Spotify API into Azure Data Lake Storage as a Parquet file.