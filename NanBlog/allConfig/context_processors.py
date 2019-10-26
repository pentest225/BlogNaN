from . import models as config

def get_config(request):
	data={
		'configuration':config.AllInfo.objects.filter(status=True),
		'working_hour':config.workingHours.objects.filter(status=True),
		'instagram':config.Instagram.objects.filter(status=True),
		'header':config.HeaderFront.objects.filter(status=True),
		'foot':config.FooterFront.objects.filter(status=True),
		'social':config.Social.objects.filter(status=True),
        'location': config.LocationMap.filter(status=True),
        'copy': config.Copyright.filter(status=True),
	}
	return data