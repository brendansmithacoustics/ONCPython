# download hydrophone audio data from Ocean Networks Canada as the files come in
# B.Smith. April 20, 2026
from onc import ONC
from datetime import datetime, timezone
import pandas as pd
import time

token = 'xxxxx-xxxx-xxxx-xxxx-xxxxxxxx' # replace with your Oceans 3.0 API token

saveDir = 'C:/Users/Documents/HydrophoneData/' # replace with the path where you want to save your audio files

locCode = "HRBIP" # HRBIP is the location code for Holyrood

# initialize onc
onc = ONC(token,outPath = saveDir)

# audio data download function
def download_hydro_data(locCode):
    print('Downloading data')

    # define search time as 1 hour before and after current hour in UTC (2 hour window) - audio file timestamps are in UTC
    # the onc API Python library will auto-detect any files in your save directory which have already been downloaded and skip them
    date_now = pd.to_datetime(datetime.now(timezone.utc))
    hour_start = date_now.floor('h') - pd.Timedelta(hours=1)
    hour_end = date_now.floor('h') + pd.Timedelta(hours=1)

    # format search times as strings compatible with ONC's API's expeted format
    start_date = str(hour_start.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z")
    end_date = str(hour_end.strftime('%Y-%m-%dT%H:%M:%S.%f')[:-3] + "Z")

    # audio data download parameters (.flac files)
    audioParams = {
        "deviceCategoryCode": "HYDROPHONE",
        "locationCode": locCode,
        "extension": "flac", # audio files are stored as .flac in ONC's archive
        "dateFrom": start_date,
        "dateTo": end_date,
    }

    onc.downloadDirectArchivefile(audioParams) # download audio data

# simple example of executing download function every 5 minutes, but a cron job or other scheduling tool would likely be better
while(True):
    download_hydro_data(locCode)
    time.sleep(300) # wait 300 seconds (5 minutes) between downloads