from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Recipe, Basket, Calculation
from .helpers.calculate import calculate


# view for recipes
class RecipeListView(LoginRequiredMixin, ListView):
    model = Recipe
    template_name = 'index.html'
    context_object_name = 'recipes'
    # login_url = '/accounts/login/'
    # redirect_field_name = ''


    def post(self, request):
        if 'calculate' in request.POST.keys():
            calculate()
            # may need to find a way to add unit conversions before pressing
            # calculate button, or maybe an ingredient settings for setting
            # default units
        elif 'basket_clear' in request.POST.keys():
            Basket.objects.all().delete()
            Calculation.objects.all().delete()
        elif 'calc_clear' in request.POST.keys():
            Calculation.objects.all().delete()
        else:
            recipe = request.POST['recipe']
            quantity = float(request.POST['quantity'])
            recipe = Recipe.objects.get(name=recipe)
            recipe.addToBasket(quantity)

        return super().get(request)  


    def get_context_data(self, **kwargs: any) -> dict[str, any]:
        context = super().get_context_data(**kwargs)
        context['recipes'] = Recipe.objects.all()
        context['basket'] = Basket.objects.all()
        context['calculation'] = Calculation.objects.all()
        return context

# view for ingredients

# view for basket

# view for calculations