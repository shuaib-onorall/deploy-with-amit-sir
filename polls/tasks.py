from pickle import TRUE
from celery import shared_task
from .models import detail
@shared_task
def test_func(x , y):
    
    return x+y

test_func(4,5)

@shared_task
def publish_time_celery_task(videoid):
    obj = detail.objects.get(videoid=videoid)
    if obj.ready_to_publish is False:
        obj.ready_to_publish=True
        obj.save()
    
    return F'VideoId : {obj.videoid} has gone to ready_to_pulish=True '