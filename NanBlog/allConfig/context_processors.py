from . import models as config

def get_config(request):
	data={
		'configuration':config.AllInfo.objects.filter(status=True)[:1],
		# 'working_hour':config.workingHours.objects.filter(status=True)[:1],
		'instagram':config.Instagram.objects.filter(status=True),
		'header':config.HeaderFront.objects.filter(status=True)[:1],
		'foot':config.FooterFront.objects.filter(status=True)[:1],
		'social':config.Social.objects.filter(status=True),
        # 'location': config.LocationMap.objects.filter(status=True)[:1],
        'copy': config.Copyright.objects.filter(status=True)[:1],
	}
	return data