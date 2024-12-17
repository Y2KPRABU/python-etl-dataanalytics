import os
import pandas as pd
import requests
import logging
# Env variables
from dotenv import load_dotenv


# Logger initialization
logging.basicConfig(format='[%(levelname)s]: %(message)s', level=logging.DEBUG)

# Recover env variables
load_dotenv()


# Database Location
DATABASE_LOCATION = os.getenv('DATABASE_LOCATION')
# User ID on Spotify
USER_ID = os.getenv('USER_ID')
# Token generated on Spotify for Developers
TOKEN = os.getenv('TOKEN')
REQ1=os.getenv('REQ_1')
REQ2=os.getenv('REQ_2')
REQ_TOKEN=os.getenv('REQ_TOKEN')


def get_token():
    """
    Function that allows the extraction of bearer token from 
    Spotify
    """

    ### Prepare the headers ###
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }

    ### Perform the request ###
    try:
        r = requests.post(
            REQ_TOKEN,
            headers = headers,
            data= "grant_type=client_credentials&client_id=a191cb83822f41ddbf96abed791c948b&client_secret=bc752de6f811427687731d64f4e4924d") 
    except:
        raise Exception(f'The Spotify request went wrong')
    
    if r.status_code != 200:
        raise Exception(f'AUTHN request error: {r.status_code}')

    # Grab the data
    data = r.json()
    print (data)
    return data['access_token']
    
def extract_data():
    """
    Function that allows the download of information from 
    Spotify
    """
    TOKEN = get_token()
    ### Prepare the headers ###
    headers = {
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {TOKEN}'
    }

    ### Perform the request ###
    try:
        r = requests.get(
            REQ1,
            headers = headers)
    except:
        raise Exception(f'The Spotify request went wrong')
    
    if r.status_code != 200:
        raise Exception(f'Something in the Spotify request went wrong: {r.status_code}')

    # Grab the data
    data = r.json()
    
    # The fields we are looking for
    heights = []
    widths = []
    images = []
    names = []


    ### Loop through each song to get the info we want ###
    for song in data['images']:
            heights.append(song['height'])
            widths.append(song['width'])
        
            images.append(song['url'])
            names.append(data['name'])
    
    # Create the dict in order to create the pandas dataframe
    song_dict = {
        'Image_Url': images,
        'Image_Height': heights,
        'Image_Width': widths,
        'Names': names
    }

    # Songs dataframe
    song_df = pd.DataFrame(
        song_dict,
        columns = ['Image_Url', 'Image_Height', 'Image_Width', 'Names']
        )

    logging.info(song_df)
    
    return song_df
    