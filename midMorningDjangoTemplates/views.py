from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


# def blog(request):
#     return render(request, 'blog.html')


# def contact(request):
#     return render(request, 'contact.html')


# def feature(request):
#     return render(request, 'feature.html')


# def product(request):
#     return render(request, 'product.html')


# def testimonial(request):
#     return render(request, 'testimonial.html')
