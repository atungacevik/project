from corsheaders.signals import check_request_enabled



from cysecapp7.models import User7


def cors_allow_mysites(sender, request, **kwargs):
    return User7.objects.filter(host=request.headers["Origin"]).exists()

check_request_enabled.connect(cors_allow_mysites)






def cors_allow_api_to_everyone(sender, request, **kwargs):
    return request.path.startswith("/api/")


check_request_enabled.connect(cors_allow_api_to_everyone)
