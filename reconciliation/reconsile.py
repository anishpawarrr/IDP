import json

def reconsile(extracted_data):

    metadata = None
    data = None

    with open('reconciliation_metadata.json', 'r') as f:
        metadata = json.load(f)
    with open(extracted_data, 'r') as f:
        data = json.load(f)
    
    if str(data['CompanyName']+'-'+data['Address']) in metadata['CompaniesIdentifier']:
        print('Company Name matched')
    else:
        print('Company Name not matched')
        metadata['CompaniesIdentifier'] = list(metadata['CompaniesIdentifier'])
        metadata['CompaniesIdentifier'].append(str(data['CompanyName']+'-'+data['Address']))
        with open('reconciliation_metadata.json', 'w') as f:
            json.dump(metadata, f)
        create_table(str(data['CompanyName']+'-'+data['Address']))

def create_table(CompaniesIdentifier):
    CompaniesIdentifier+=".json"
    table = dict({"CompaniesIdentifier": "CompaniesIdentifier","DescriptionSet": [],"ReconciliationStatus":{"Total": 0,"Descrepencies":[]}})
    table = dict(table)
    with open(CompaniesIdentifier, 'w') as f:
        json.dump(table, f)

reconsile('extracted_data1.json')