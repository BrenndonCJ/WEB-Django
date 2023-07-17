from django.shortcuts import redirect

def anonymous_required(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index')  # Redireciona para a página 'index' se estiver logado
        return view_func(request, *args, **kwargs)
    return wrapper
