# `python-etl-dataanlytics`

In the following repo, you will find a simple ETL process, using different kinds of tools, but basically, `Python`.

The goal is download Artist's data from Spotify, check if the validation process is approved and finally, load the information needed into an Azure ADLS2 Parquet file.

You will need to create a copy from the `.env.example` and call it `env`. There you can put your personal information (`sas-token`, `Adls account name`,etc.). 

# `ETL` Concept
**Extract**, **Transform** and **Load** it's the process that allows to move data from multiple sources, clean them and load them into a ADLS2 store , that could be used into a Data warehouse.

# Spotify API
Here we will use the Spotify API. You will need to change the `clienid` and `secret` . This autogenerates a TOKEN, inside the code during execution in order to use it. 

#Azure ADLS2 Container file upload 
For every run, the artist information is uploaded into ADLS 2 account, container, filesystem, directory and filename, based on the config in .env file.
# Installation steps

With pip, you can follow this steps:
1. Clone the repository
2. Create a virtual environment called `env`
3. Activate the environment and install the requirements with `pip install -r requirements.txt`
4. Copy the `.env.example` and call it `env`
5. Change the variables for the ones that you need: `DATABASE_LOCATION`, and from Spotify, `USER_ID`, `TOKEN`.
6. Then, you can run your code with `python3 main.py`


# Sample commands for testing the Spotify API endpoints 

curl -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id=your-client-id&client_secret=your-client-secret"
curl -X POST "https://accounts.spotify.com/api/token" \
     -H "Content-Type: application/x-www-form-urlencoded" \
     -d "grant_type=client_credentials&client_id='yourid'&client_secret='secretsample'"
{"access_token":"actual_token_returned","token_type":"Bearer","expires_in":3600}% 

curl "https://api.spotify.com/v1/artists/4Z8W4fKeB5YxbusRsdQVPb" \
     -H "Authorization: Bearer  actual_token_returned"


If you want to use poetry instead, you can skip the first 3 steps and run `poetry install`. You need to keep in mind that, to run the code, you'll need to execute: `poetry run python3 main.py`

Python version: `3.9.5`
