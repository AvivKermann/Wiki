from django.shortcuts import render
from django.http import HttpResponse
from random import choice
from . import util
from markdown2 import Markdown
from django.shortcuts import redirect

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def entry(request, article):
    if util.get_entry(article):

        markdowner = Markdown()
        page_converted = markdowner.convert(util.get_entry(article))
        return render(request, "encyclopedia/entry.html", {
            "article" : page_converted,
            "title" : article
        })
    
    else:
        return HttpResponse(f"404 article {article} not found! .")
    

def rand(request):
    title = choice(util.list_entries())
    return redirect(f"wiki/{title}")


def new(request):

    if request.method == "POST":
            title = request.POST["title"]
            content = request.POST["content"]

            if not title or not content:
                return HttpResponse("Must provide title and content.")
            
            elif util.get_entry(title):
                return HttpResponse(f"This title already exist, please visit /wiki/{title}")
            
            else:

                util.save_entry(title, content)
                return redirect(f"wiki/{title}")
                
    else:
        return render(request, "encyclopedia/new.html")
    

def edit(request, article):

    if request.method == "GET":
        content = util.get_entry(article)

        return render(request, "encyclopedia/edit.html", {
            "title": article,
            "content" : content
            })
    
def save_edit(request):
    if request.method == "POST":
        title, content = request.POST["title"], request.POST["new_content"]
        util.save_entry(title, content)
        return redirect(f"wiki/{title}")


    

    
def search(request):

    search_matches = []
    search_pattern = request.GET["search"]
    entries = util.list_entries()

    for entry in entries:

        if search_pattern.lower() == entry.lower():
            return redirect(f"wiki/{search_pattern}")
        
        elif search_pattern in entry:
            search_matches.append(entry)

        else:
            pass

    if len(search_matches) == 0:
        return redirect("/")

    else:
        return render(request, "encyclopedia/search.html", {
            "search_entries" : search_matches
        })


