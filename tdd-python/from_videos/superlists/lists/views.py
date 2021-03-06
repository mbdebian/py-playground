from django.shortcuts import render, redirect


# Create your views here.
from lists.models import Item

def home_page(request):
    if request.method == 'POST':
        new_item_text = request.POST['item_text']
        Item.objects.create(text=new_item_text)
        return redirect('/')
    else:
        items = Item.objects.all()
        return render(request, 'home.html', {'new_item_text': '', 'items': items})
