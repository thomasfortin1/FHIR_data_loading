from fhirclient import client
# settings = {
#     'app_id': 'Anything',
#     'api_base': 'https://try.smilecdr.com:8000/baseR4/'
# }
settings = {
    'app_id': 'Anything',
    'api_base': 'http://hapi.fhir.org/baseR4/'
}


smart = client.FHIRClient(settings=settings)

import fhirclient.models.patient as pa
search = pa.Patient.where(None)
patients = search.perform_resources(smart.server)

import fhirclient.models.encounter as en
search = en.Encounter.where(None)
encounters = search.perform_resources(smart.server)

