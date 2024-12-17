
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
from azure.storage.filedatalake import DataLakeServiceClient

# Replace with your details
account_name = 'sunadls'
file_system_name = 'sunfs' #filesystem is same as container in ADLS terms
directory_name = 'artists'
file_name = 'artistspot.parquet'
local_file_path = 'localartistspot.parquet'
sas_token = 'sv=2022-11-02&ss=bfqt&srt=sco&sp=rwdlacupyx&se=2024-12-18T01:48:36Z&st=2024-12-17T17:48:36Z&spr=https&sig=WiJm1p2a4Y42oPDwBpkSMFlKhCVqUHWgVnvApYm2glk%3D'
# Create a DataFrame
def createFileFromdata(pandas_dataframe):

    # Convert the DataFrame to a Parquet file
    table = pa.Table.from_pandas(pandas_dataframe)
    pq.write_table(table, local_file_path)

# Function to upload the Parquet file to ADLS
def upload_file_to_adls(account_name, file_system_name, directory_name, file_name, local_file_path, sas_token):
    service_client = DataLakeServiceClient(account_url=f"https://{account_name}.dfs.core.windows.net", credential=sas_token)
    file_system_client = service_client.get_file_system_client(file_system_name)
    directory_client = file_system_client.get_directory_client(directory_name)
    file_client = directory_client.create_file(file_name)

    with open(local_file_path, 'rb') as file:
        file_contents = file.read()
        file_client.append_data(data=file_contents, offset=0, length=len(file_contents))
        file_client.flush_data(len(file_contents))


def pushtoADLS():
    upload_file_to_adls(account_name, file_system_name, directory_name, file_name, local_file_path, sas_token)