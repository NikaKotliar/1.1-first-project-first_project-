from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render

import calculator

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
}


def home_view(request):
    menu = ''
    for recipt_item in DATA.keys():
        menu += f'<li>{recipt_item.title()}</li>'
    response = f""" 
        <ul> {menu}</ul> """
    return HttpResponse(response)
    raise NotImplemented

    return HttpResponse()


def get_recipe(request, recipe):
    recipe_description = DATA.get(recipe, None)
    quantity = int(request.GET.get('quantity', 1))
    if recipe_description:
        new_measuring = {}
        for ingredient, ing_quantity in recipe_description.items():
            quantity_for_show = round(float(ing_quantity) * quantity, 2)
            new_measuring[ingredient] = quantity_for_show
    contex = {
        "recipe": new_measuring
    }
    return render(request, 'calculator/index.html', contex)

# Напишите ваш обработчик. Используйте DATA как источник данных
# Результат - render(request, 'calculator/index.html', context)
# В качестве контекста должен быть передан словарь с рецептом:
# context = {
#   'recipe': {
#     'ингредиент1': количество1,
#     'ингредиент2': количество2,
#   }
# }
