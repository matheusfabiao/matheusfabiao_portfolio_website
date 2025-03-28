from django.shortcuts import render


# Create your views here.
def index(request):
    """Função que retorna a página index.

    Args:
        request (HttpRequest): Objeto de requisição HTTP que contém os
            metadados da requisição do cliente.

    Returns:
        HttpResponse: Renderiza o template 'portfolio/index.html' e retorna
            como resposta HTTP.
    """
    return render(request, 'portfolio/index.html')
