from fhirclient import client
settings = {
    'app_id': 'Anything',
    'api_base': 'http://test.fhir.org/r3/'
}
smart = client.FHIRClient(settings=settings)

import fhirclient.models.procedure as p
search = p.Procedure.where(struct={'status': 'completed'})
procedures = search.perform_resources(smart.server)



