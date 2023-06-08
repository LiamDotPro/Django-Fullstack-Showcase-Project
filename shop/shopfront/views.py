from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. You're at the shop index.")

def detail(request, product_id):
    return HttpResponse(f"You're looking at product {product_id}.")