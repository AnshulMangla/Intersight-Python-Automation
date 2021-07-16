# Import "intersight_rest" Package
import intersight_rest as isREST

# Import JSON Package
import json

# Import Pandas Package
import pandas as pd #To handle the data frame

# Import Datetime
import datetime as datetime


resource_path = input ("Enter the relative path of the API: ")
parent_object = input("Enter the returned JSON object to process: ")
no_of_rows_to_process = input("Enter the number of rows to process: ")
selected_columns = input("Enter the columns to be selected (for $select param) ")
filter = input("Enter the query strong for the $filter (e.g. MoID eq XXXX) ")


# Load Public/Private Keys
isREST.set_private_key(open("./keys/intersight-private-key.txt", "r") .read())
isREST.set_public_key(open("./keys/intersight-public-key.txt", "r") .read())

# Select Resource Path from https://www.intersight.com/apidocs
#resource_path = '/compute/RackUnits'
#resource_path = '/storage/PhysicalDisks'


query_params = {
    "$top": no_of_rows_to_process,
    #"$select": "Dn,Serial",
    "$select": selected_columns,
    "$filter": filter
    #"$filter": "DeviceMoId eq '5f41f5586f72612d31a8ff7f'"
}

# GET EXAMPLE
#-- Set GET Options --#
options = {
    "http_method": "get",
    "resource_path": resource_path,
    "query_params": query_params
}

#-- Send GET Request --#
results = isREST.intersight_call(**options)
print("Status Code: " + str(results.status_code))
#print(results.json())
#print(json.dumps(results.json(), indent=4))



##-- Convery returned JSON to CSV and XLS now

raw_json = results.json()[parent_object]

# normalise the raw JSON
normalised_json = pd.json_normalize(raw_json)
print(normalised_json)


# create the file name for output: syntax = api-name + datetime-stamp
datetime_object = datetime.datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
file_name = resource_path.replace("/", "_")

# write normalised JSON to CSV
normalised_json.to_csv(file_name[1:] + "-" + datetime_object + '.csv', index=False)

# write normalised JSON to XLS
df = pd.DataFrame(normalised_json)
writer = pd.ExcelWriter(file_name[1:] + "-" + datetime_object + '.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name=parent_object, header=None, startrow=0, index=None)
writer.save()