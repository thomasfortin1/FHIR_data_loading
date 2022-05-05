import matplotlib.pyplot as plt
import fhirclient.models.procedure as pr
import fhirclient.models.encounter as en


def plot_timeline(timeline):
    for time, event in timeline:
        if isinstance(event, pr.Procedure):
            plt.scatter(time, 1)
            plt.annotate(event.code.text, (time, 1), rotation=45)
        if isinstance(event, en.Encounter):
            plt.scatter(time, 2)
            plt.annotate(event.class_fhir.code, (time, 2))
    plt.show()