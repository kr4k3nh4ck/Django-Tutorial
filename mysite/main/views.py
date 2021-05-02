import sys

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList, Item
from .forms import CreateNewList
from django.db import transaction

# Create your views here.
def index(response, id):
    #return HttpResponse("Hello World!")
    ls = ToDoList.objects.get(id=id)
    #items = Item.objects.item_set.get(id=1)
    #return HttpResponse(f"<h1>{ls}</h1>")
    #return HttpResponse(f"<h1>{ls.name}</h1><br>{items.text}</br><p>{ls.name}</p>")
    #return render(response, "base.html", {"name": ls.name})
    #return render(response, "list.html", {"ls": ls})
    return HttpResponse("Hello World123!")

def index2(response, id):
    ls = ToDoList.objects.get(id=id)

    if response.user.todolist.all():

        if response.method == "POST":
            if response.POST.get("save"):
                print(response.POST)
                for item in ls.item_set.all():
                    if response.POST.get("c" + str(item.id)) == "clicked":
                        item.complete =True
                        item.text = response.POST.get("c" + str(item.id))
                    else:
                        item.complete = False
                        item.text = response.POST.get("c" + str(item.id))
                    item.save()

            elif response.POST.get("newItem"):
                text = response.POST.get("new")
                if len(text) > 2:
                    ls.item_set.create(text=text, complete=False)
                else:
                    print("invalid")
        return render(response, "list.html", {"ls": ls})
    else:
        return render(response, "home.html", {})
    #return HttpResponse("Hello World123!")

def home(response):
    return render(response, "home.html")

#@transaction.atomic()
def create(response):
    if response.method == "POST":
        form = CreateNewList(response.POST)
        if form.is_valid():
            try:
                #return HttpResponseRedirect('/')
                n = form.cleaned_data["name"]
                # t = ToDoList(name=n)
                # t.save()
                # transaction.commit()
                # response.user.todolist.add(t)
                t = ToDoList(name=n, user_id=response.user.id)
                t.save()
                return HttpResponseRedirect(f"/home/{t.id}")
            except Exception as e:
                print("EEEEEERRORRR!!")

    else:
        form = CreateNewList()

    return render(response, "create.html", {"form": form})


def view(response):
    return render(response, "view.html", {})