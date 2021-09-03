
# Config details for the first API
# This resource path is the relative path of the first API e.g. /compute/RackUnits'
resourcePath = '/first/api/relative/path'

# parentObject is the parent object of the JSON returned by the APIs e.g. 'Results'
parentObject = 'ParentObject'
filter = ''


# Config details for the second API
# This resource path is the relative path of the second API e.g. storage/PhysicalDisks'
resourcePath2 = '/storage/PhysicalDisks'

# The values entered in this fields determines the columns of the generated CSV e.g. 'Dn,DeviceMoId,Serial'
selectedColumns2 = 'Field1,Field2,Field3,Field4'

# parameter common to both queries; whose output values from first query need to be iterated through second query
# e.g. 'DeviceMoId'
iterativeParam = 'IterativeParam1'
