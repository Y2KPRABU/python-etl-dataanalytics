# `python-etl`

In the following repo, you will find a simple ETL process, using different kinds of tools, but basically, `Python`.

The goal is to download yesterday's data from Spotify, check if it success the validation process and finally, load the information needed into the database.

You will need to create a copy from the `.env.example` and call it `env`. There you can put your personal information (`TOKEN`, `USER-ID`,etc.). 

# `ETL` Concept
**Extract**, **Transform** and **Load** it's the process that allows to move data from multiple sources, clean them and load them into a SQL database, that could be used into a Data warehouse.

# Spotify API
Here we will use the Spotify API. You will need to grab you `USER-ID` and generate a `TOKEN` in order to use it. 
