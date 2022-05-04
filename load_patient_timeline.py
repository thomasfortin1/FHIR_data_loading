from fhirclient import client
import


settings = {
    'app_id': 'Anything',
    'api_base': 'http://test.fhir.org/r3/'
}
smart = client.FHIRClient(settings=settings)

import fhirclient.models.procedure as p
search = p.Procedure.where(struct={'status': 'completed'})
procedures = search.perform_resources(smart.server)



def load_timeline(id):
    procedues = load_procedures(id)


def load_procedures(id):
    search = p.Procedure.where(struct=None)
    procedures = search.perform_resources(smart.server)
