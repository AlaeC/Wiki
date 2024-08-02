from django.shortcuts import render
from django.http import HttpResponseNotFound       
from . import util
import markdown2  
import random


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def find_page(request, url_name):
    if url_name not in util.list_entries():
        return HttpResponseNotFound("This page dosen't exist")
    filepath=f'entries\{url_name}.md'
    return render(request, f"encyclopedia/entry.html", { 
        "html_text": read_markdown_file(filepath)

    })



def read_markdown_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    return markdown2.markdown(content)



def random_page(request):
    list=util.list_entries()
    url_name= random.choice(list)
    filepath=f'entries\{url_name}.md'
    return render(request, f"encyclopedia/entry.html", { 
        "html_text": read_markdown_file(filepath)
        })


    


