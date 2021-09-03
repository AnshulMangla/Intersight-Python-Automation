# Import "intersight_rest" Package
import intersight_rest as isREST

# Import JSON Package
import json

# Import Pandas Package
import pandas as pd #To handle the data frame

# Import Datetime
import datetime as datetime

# Import API Config
import apiConfig as cf

# Set variable values for First API
resource_path = cf.resourcePath
parent_object = cf.parentObject
no_of_rows_to_process = ""
selected_columns = ""
filter = cf.filter

# Set variable values for Second API
resource_path_2 = cf.resourcePath2
selected_columns_2 = cf.selectedColumns2
no_of_rows_to_process_2 = ""

# Set parameter to iterate
iterative_param = cf.iterativeParam

# Load Public/Private Keys
isREST.set_private_key(open("./keys/intersight-private-key.txt", "r") .read())
isREST.set_public_key(open("./keys/intersight-public-key.txt", "r") .read())

query_params = {
    "$top": no_of_rows_to_process,
    "$select": selected_columns,
    "$filter": filter
}

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

result_json = results.json()
#print(result_json['Results']['DeviceMoId'])

list_dev = []
for i in result_json[parent_object]:
    list_dev.append(i[iterative_param])
# for i in result_json['Results']:
#     list_dev.append(i['DeviceMoId'])

list_dev = list(set(list_dev))
print("List of DeviceMoId")
print(list_dev)

int_var = iterative_param + " in ("

dev_name = ""
for x in list_dev:
    dev_name = dev_name + " '" + x + "',"
print("dev_name")
print(dev_name[:-1])

fin_var = int_var + (dev_name[:-1])[1:] + ")"
print("fin_var")
print(fin_var)

### 2nd query starts ##

query_params_2 = {
    "$top": no_of_rows_to_process_2,
    #"$select": "Dn,Serial",
    "$select": selected_columns_2,
    "$filter": fin_var
    #"$filter": "DeviceMoId eq '5f41f5586f72612d31a8ff7f'"
}

#-- Set GET Options --#
options_2 = {
    "http_method": "get",
    "resource_path": resource_path_2,
    "query_params": query_params_2
}

#-- Send GET Request --#
results_2 = isREST.intersight_call(**options_2)
print("Status Code: " + str(results_2.status_code))

##-- Convery returned JSON to CSV and XLS now

raw_json_2 = results_2.json()[parent_object]
#print("raw_json_2")
#print(raw_json_2)

# normalise the raw JSON
normalised_json_2 = pd.json_normalize(raw_json_2)
print(normalised_json_2)

# create the file name for output: syntax = api-name + datetime-stamp
datetime_object = datetime.datetime.now().strftime("%Y_%m_%d-%I:%M:%S_%p")
file_name = resource_path_2.replace("/", "_")

# write normalised JSON to CSV
normalised_json_2.to_csv(file_name[1:] + "-" + datetime_object + '.csv', index=False)

# write normalised JSON to XLS
df = pd.DataFrame(normalised_json_2)
writer = pd.ExcelWriter(file_name[1:] + "-" + datetime_object + '.xlsx', engine='xlsxwriter')
df.to_excel(writer, sheet_name=parent_object, header=None, startrow=0, index=None)
writer.save()