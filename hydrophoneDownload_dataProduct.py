# download hydrophone audio data from Ocean Networks Canada using data product request
# by Brendan Smith - April 24, 2026
from onc import ONC

token = 'xxxxx-xxxx-xxxx-xxxx-xxxxxxxx' # replace with your Oceans 3.0 API token

saveDir = 'C:/Users/Documents/HydrophoneData/' # replace with the path where you want to save your audio files

# define start and end dates
start_date = "2026-04-23T00:00:00.000Z"
end_date = "2026-04-23T00:05:00.000Z"

locCode = "HRBIP" # location code of hydrophone, HRBIP is the code for Holyrood

# initialize onc
onc = ONC(token,outPath = saveDir)

# audio data downsampling and download parameters
params = {
    "deviceCategoryCode": "HYDROPHONE",
    "dataProductCode": "AD", # data product code for audio data
    "locationCode": locCode,
    "extension": "wav", # audio file type selected here
    "dpo_audioFormatConversion": "1", # this is the flag to enable audio format conversion to your chosen file extension type
    "dateFrom": start_date,
    "dateTo": end_date,
}

onc.orderDataProduct(params, includeMetadataFile=False) # order data product and download files