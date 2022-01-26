from django.views.generic import View
from django.shortcuts import render
from django_rq import job
from time import sleep
from .models import WorkerResults

import requests


@job
def count_words_at_url(url):
    resp = requests.get(url)
    result = len(resp.text.split())
    WorkerResults.objects.create(url=url, result=result)


@job
def add(a, b):
    return a + b


class IndexView(View):
    def get(self, request, *args, **kwargs):
        url = 'https://google.com'
        count_words_at_url.delay(url)

        object_list = WorkerResults.objects.all().order_by('-pk')

        # job = add.delay(10, 20)
        # print("job", job.result)
        # sleep(5)
        # print("job", job.result)

        return render(request, 'app/index.html', {
            'object_list': object_list
        })
