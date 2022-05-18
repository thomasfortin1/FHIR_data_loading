from fhirclient import client

# Just edit the two lines below to test a new resource. Like this:
# import fhirclient.models.your_resource as re
# resource_type = re.Your_resource
import fhirclient.models.encounter as re
resource_type = re.Encounter

settings = {
    'app_id': 'Anything',
    'api_base': 'http://hapi.fhir.org/baseR4/'
}

smart = client.FHIRClient(settings=settings)


resources = resource_type.where(None).perform_resources(smart.server)
resource = resources[0]
print("get_date for 1 resource with return_all=False:")
print(f"{resource.get_date()}\n")
print("get_date for 1 resource with return_all=True:")
print(f"{resource.get_date(return_all=True)}\n")

print("test to make sure we don't get any errors if we try it on 20 examples:")
result = list(map(lambda x: x.get_date(return_all=True), resources))
# if the above raises an exception we won't get to the next line.
print("passed")
