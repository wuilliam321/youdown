from django.shortcuts import render
from django.http import HttpResponse
import logging
import pafy
import os
from datetime import datetime
from .models import Download


def index(request):
  return render(request, 'download/index.html')

def info(request):
  url = request.POST['url']
  video = pafy.new(url)
  context = {
    'url': url,
    'streams': video.audiostreams,
    'title': video.title
  }
  return render(request, 'download/info.html', context)

def download(request):
  url = request.POST['url']
  stream = int(request.POST['choice'])
  video = pafy.new(url)
  file = video.audiostreams[stream].download(quiet=True)
  os.rename(file, '../static/' + file);
  context = {
    'stream': stream,
    'title': video.title,
    'file': file
  }
  download_file = Download(title=video.title, url='/static/' + file, download_date=datetime.now())
  download_file.save()
  return render(request, 'download/download.html', context)