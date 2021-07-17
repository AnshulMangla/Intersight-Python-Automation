[![published](https://static.production.devnetcloud.com/codeexchange/assets/images/devnet-published.svg)](https://developer.cisco.com/codeexchange/github/repo/AnshulMangla/Intersight-Python-Automation)

# Intersight-Python-Automation

# Description
This Intersight Python Automation toolkit is a set Python library which allows the user to run various Intersight GET REST APIs and offers various API param options, including the filters. This also exports the returned JSON format to a CSV format.

# Installation

## Environment

Required

* Python 3.9 (and above)
* Python modules mentioned in the requirements.txt file

## Downloading

If you have git installed, clone the repository

    git clone https://github.com/AnshulMangla/Intersight-Python-Automation.git
    
## Installing

After downloading, set up the Intersight Private and Public keys

    cd Intersight-API-Toolkit
    mkdir keys
    
Download the Private and Public keys from your Intersight instance and save them as .txt files with following names under the 'keys' directory:

    intersight-public-key.txt
    intersight-private-key.txt
    
# Usage

Execute the python file from the 'Intersight-API-Toolkit' directory

    $ python3 intersight-api-to-csv.py
    
Command line will prompt you for the relative path of the Intersight API you want to execute:

    Enter the relative path of the API: /compute/RackUnits
   
Command line will prompt you to enter the returned JSON object you want the script to convert to CSV format (e.g. Results in this case):

    Enter the returned JSON object to process: Results
 
Command line will prompt you to enter number of Rows of the JSON object you want to output in CSV file (e.g. 100 below) ~ $top param in the API:

    Enter the number of rows to process: 100

    Note: Optional field. Press enter if you do not wish to enter any value

Command line will prompt you to enter fields of JSON object you want to output as columns in CSV file (e.g. Dn,DeviceMoId below) ~ $select in the API :

    Enter the columns to be selected (for $select param) Dn,DeviceMoId
    
    Note: Optional field. Press enter if you do not wish to enter any value
    
Command line will prompt you to enter the filter string on on the basis of which the API will query the output to CSV file ~ $filter in the API :

    Enter the query strong for the $filter (e.g. MoID eq XXXX) DeviceMoId eq '5f41f5586f72612d31a8ff7f'
    
    Note: Optional field. Press enter if you do not wish to enter any value
  
