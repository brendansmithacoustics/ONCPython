# download hydrophone audio data from Ocean Networks Canada
# B.Smith. April 17, 2026
from onc import ONC

token = 'xxxxx-xxxx-xxxx-xxxx-xxxxxxxx' # replace with your Oceans 3.0 API token

saveDir = 'C:/Users/Documents/HydrophoneData/' # replace with the path where you want to save your audio files

# define start and end dates
start_date = "2026-04-17T09:00:00.000Z"
end_date = "2026-04-17T10:00:00.000Z"

locCode = "HRBIP" # location code of hydrophone, HRBIP is the code for Holyrood

# initialize onc
onc = ONC(token,outPath = saveDir)

# audio data download parameters (.flac files)
audioParams = {
    "deviceCategoryCode": "HYDROPHONE",
    "locationCode": locCode,
    "extension": "flac",
    "dateFrom": start_date,
    "dateTo": end_date,
}

onc.downloadDirectArchivefile(audioParams) # download audio data