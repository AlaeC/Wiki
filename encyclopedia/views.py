from django.shortcuts import render, redirect
from django.http import HttpResponseNotFound, HttpResponse      
from . import util
import markdown2  
import random
from .form import NameForm,layout, EditEntryForm


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })


def find_page(request, url_name):
    if url_name not in util.list_entries():
        return HttpResponseNotFound("This page dosen't exist")
    filepath=f'entries\{url_name}.md'
    return render(request, f"encyclopedia/entry.html", { 
        "html_text": read_markdown_file(filepath), "name" : url_name

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

def new_page(request):
    if request.method == "POST":
        form=NameForm(request.POST)
        valid = form.is_valid()
        title = form.cleaned_data['title']
        body = form.cleaned_data['body']
        if valid:
            
            with open(f"entries/{title}.md", "w") as file:
                file.write(body)
            return redirect(f"/wiki/{title}")
            
        else:            
            return render(request, f"encyclopedia/NameForm.html", {"pro" : "The form is not valid" , "validation" : valid})
    return render(request, f"encyclopedia/NameForm.html")

def search_page(request):
    result=[]
    if request.method == "POST":
        form=layout(request.POST)
        valid = form.is_valid()
        title = form.cleaned_data['search']
        if title in util.list_entries() and valid:
            return redirect(f"/wiki/{title}")
        else:
            for example in util.list_entries():
                if title.lower() in example.lower():
                    result.append(example)
            return render(request, f"encyclopedia/query.html", { "result" :result })
    return render(request, f"encyclopedia/layout.html")


def edit_entry(request, url_name):
    if request.method == "POST":
        form = EditEntryForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            util.save_entry(url_name, content)  # Save the updated content
            return redirect(f"/wiki/{url_name}")  # Redirect to the entry page
    else:
        content = util.get_entry(url_name)  # Get current content of the entry
        if content is None:
            return render(request, "encyclopedia/error.html", {
                "message": "The requested page was not found."
            })
        form = EditEntryForm(initial={'content': content})

    return render(request, "encyclopedia/edit_entry.html", {
        "form": form,
        "url_name": url_name
    })
    
    




