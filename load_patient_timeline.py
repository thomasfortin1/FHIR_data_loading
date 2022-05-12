from fhirclient import client
import fhirclient.models.procedure as pr
import fhirclient.models.encounter as en


settings = {
    'app_id': 'Anything',
    'api_base': 'http://test.fhir.org/r4/'
}
smart = client.FHIRClient(settings=settings)


def load_timeline(id):
    procedures = load_procedures(id)
    encounters = load_encounters(id)
    resources = procedures + encounters
    times = get_times(resources)
    timeline = [(t, p) for t, p in zip(times, resources) if t is not None]
    return timeline


def get_times(resources):
    times = []
    for res in resources:
        if isinstance(res, pr.Procedure):
            if res.performedPeriod is not None:
                if res.performedPeriod.start is not None:
                    times.append(res.performedPeriod.start.date)
                elif res.performedPeriod.end is not None:
                    times.append(res.performedPeriod.end.date)
                else:
                    times.append(None)
            else:
                times.append(None)
        elif isinstance(res, en.Encounter):
            if res.period is not None:
                if res.period.start is not None:
                    times.append(res.period.start.date)
                elif res.period.end is not None:
                    times.append(res.period.end.date)
                else:
                    times.append(None)
            else:
                times.append(None)
        else:
            times.append(None)

    return times


def load_procedures(id):
    search = pr.Procedure.where(struct=None)
    procedures = search.perform_resources(smart.server)
    filtered_procedures = [p for p in procedures if p.subject.reference == id]
    return filtered_procedures


def load_encounters(id):
    search = en.Encounter.where(struct=None)
    encounters = search.perform_resources(smart.server)
    filtered_encounters = [e for e in encounters if e.subject.reference == id]
    return filtered_encounters


if __name__ == "__main__":
    timeline = load_timeline('Patient/2569979')
    from utils import plot_timeline
    plot_timeline(timeline)
