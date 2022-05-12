import matplotlib.pyplot as plt
import fhirclient.models.procedure as pr
import fhirclient.models.encounter as en
import fhirclient.models.patient as pa


def plot_timeline(timeline):
    for time, event in timeline:
        if isinstance(event, pr.Procedure):
            plt.scatter(time, 1)
            plt.annotate(event.code.text, (time, 1), rotation=45)
        if isinstance(event, en.Encounter):
            plt.scatter(time, 2)
            plt.annotate(event.class_fhir.code, (time, 2))
    plt.yticks([1, 2], ['Procedure', 'Encounter'])
    plt.ylim([0, 3])
    plt.show()


def load_resource(server, resource_type, patient_id=None):
    search = resource_type.where(struct=None)
    resources = search.perform_resources(server)
    if id is not None:
        resources = [r for r in resources if r.subject is not None and r.subject.reference == patient_id]
    return resources


def find_patient_ids(server, resource_types):
    search = pa.Patient.where(None)
    patients = search.perform_resources(server)
    ids = list(map(lambda p: p.id, patients))
    good_ones = []
    for id in ids:
        for r in resource_types:
            resources = load_resource(server, r, patient_id=id)
            if len(resources) == 0:
                break
        if len(resources) > 0:
            good_ones.append(id)
    return good_ones


if __name__=="__main__":
    from fhirclient import client
    import fhirclient.models.procedure as pr

    settings = {
        'app_id': 'Anything',
        'api_base': 'http://hapi.fhir.org/baseR4/'
    }
    smart = client.FHIRClient(settings=settings)

    ids = find_patient_ids(smart.server, [pr.Procedure])
    print(ids)
    print(len(ids))
