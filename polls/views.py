from django.http import HttpResponse
import numpy as np

from learn.simplenet import Simplenet


def index(request):
    c = Simplenet()
    np.random.seed(98052)
    x = c.ffnet()
    return HttpResponse(x)
