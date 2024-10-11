def buscar_libro(request):
    libros = []
    if request.method == 'GET':
        form = BuscarLibroForm(request.GET)
        if form.is_valid():
            titulo = form.cleaned_data['titulo']
            if titulo:
                libros = Libro.objects.filter(titulo__icontains=titulo)
    else:
        form = BuscarLibroForm()
    
    return render(request, 'buscar_libro.html', {
        'form': form,
        'libros': libros,
    })
