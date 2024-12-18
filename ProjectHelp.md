# Project Description

## Overview

This project is a simple ETL process designed to download artist data from Spotify, validate the data, and load the required information into an Azure Data Lake Storage (ADLS) in Parquet format.

## ETL Concept

ETL stands for Extract, Transform, and Load, which is a process that enables the movement of data from multiple sources, cleaning it, and then loading it into a storage system that can be used in a data warehouse.

## Project Structure

- **main.py**: This is the main entry point for the ETL process. It orchestrates the extraction, validation, and loading processes.

- **utils/extract.py**: This module handles the extraction of data from Spotify. It includes functions to get the authentication token and to download artist data using Spotify's API.

- **utils/validation.py**: This module validates the extracted data. It checks for empty data frames, ensures that primary keys are unique, and checks for null values.

- **utils/LoadIntoADLS.py**: This module handles the loading of data into Azure Data Lake Storage. It includes functions to convert data frames to Parquet files and upload them to ADLS.

## Environment Setup

You need to create a copy of the `.env.example` file and rename it to `.env`. Update the variables in this file with your personal information (e.g., Spotify API credentials, ADLS account details).

## How to Run the Project

1. Clone the repository.
2. Create a virtual environment called `env`.
3. Activate the environment and install the requirements with `pip install -r requirements.txt`.
4. Copy the `.env.example` file and rename it to `.env`.
5. Update the variables in the `.env` file with your personal information.
6. Run the code with `python3 main.py`.

Alternatively, if you want to use Poetry, you can skip the first three steps and run `poetry install`. To run the code, execute `poetry run python3 main.py`.

## Spotify API

The project uses the Spotify API to download artist data. You need to provide your `client_id` and `client_secret` to generate a token, which is used for authentication during the API calls.

## Azure ADLS2 Container File Upload

For each run, the artist information is uploaded into an ADLS2 account, container, filesystem, directory, and filename based on the configuration in the `.env` file.

## Logger Initialization

Logging is initialized in both the `main.py` and `utils/extract.py` files to provide information on the process flow and any issues encountered.

## Sample Commands for Testing Spotify API Endpoints

```bash
curl -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id=your-client-id&client_secret=your-client-secret"

curl -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id='yourid'&client_secret='secretsample'"
{"access_token":"actual_token_returned","token_type":"Bearer","expires_in":3600}

curl "https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb" \
     -H "Authorization: Bearer actual_token_returned"
```

## Python Version

The code is compatible with Python version `3.9.5`.
