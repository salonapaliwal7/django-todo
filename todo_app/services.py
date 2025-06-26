import json
import redis
from django.conf import settings
from django.core.serializers import serialize
from .models import Task

r = redis.Redis.from_url(settings.CACHES['default']['LOCATION'])

class TaskService:
    CACHE_KEY = "tasks:all"

    @staticmethod
    def list_tasks():
        cached_data = r.get(TaskService.CACHE_KEY)
        print(cached_data)
        if cached_data:
            return json.loads(cached_data)
        tasks = Task.objects.all()
        json_data = serialize("json", tasks)
        r.set(TaskService.CACHE_KEY, json_data, ex=300)  # Cache for 5 mins
        return json.loads(json_data)

    @staticmethod
    def add_task(data):
        task = Task.objects.create(**data)
        TaskService.invalidate_cache()
        return task

    @staticmethod
    def delete_task(task_id):
        Task.objects.filter(id=task_id).delete()
        TaskService.invalidate_cache()

    @staticmethod
    def invalidate_cache():
        r.delete(TaskService.CACHE_KEY)
