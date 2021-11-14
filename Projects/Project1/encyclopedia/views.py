from django.shortcuts import redirect, render
from urllib.parse import parse_qs
from django.contrib import messages
from django.urls.base import reverse

from . import models
from . import util

def index(request):
    title = parse_qs(request.GET.urlencode())
    if title:
        return redirect(f"/wiki/{title['q'].pop()}")
    else:
        return render(request, "encyclopedia/index.html", {
            "title": "All Pages",
            "entries": util.list_entries()
        })

def wiki(request, title):
    results = util.get_entry(title)
    if results:
        return render(request, "encyclopedia/wiki.html", {
            "title": title,
            "titleData": results
        })
    else:
        print("hit wiki else view")
        return render(request, "encyclopedia/index.html", {
            "title": f"\'{title.capitalize()}\' was not found.",
            "entries": util.get_sub(title)
        })

def creation(request):
    if request.method == "POST":
        title = request.POST.get("wiki_title")
        content = request.POST.get("wiki_body")
        if util.get_entry(title):
            messages.warning(request, 'Document already exists.')
            return render(request, "encyclopedia/creation.html", {
                "form": models.wikiCreation
            })
        else:
            util.save_entry(title, content)
            return redirect(reverse("encyclopedia-index"))
    else:
        return render(request, "encyclopedia/creation.html", {
            "form": models.wikiCreation
        })