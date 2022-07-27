from django.shortcuts import render


def basket(request):
    """ Returns the shopping basket """

    return render(request, 'basket/basket.html')
