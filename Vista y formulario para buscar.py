from django.shortcuts import render, redirect # type: ignore
from .forms import ItemForm # type: ignore
from .models import Item # type: ignore

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('form')
    else:
        form = ItemForm()
    return render(request, 'form.html', {'form': form})

def search_item(request):
    query = request.GET.get('q', '')
    results = Item.objects.filter(nombre__icontains=query) if query else []
    return render(request, 'search.html', {'results': results, 'query': query})
