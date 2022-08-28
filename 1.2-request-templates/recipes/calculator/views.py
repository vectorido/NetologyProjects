from django.shortcuts import render
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


def get_omlet_recipe(request):
    servings = int(request.GET.get("servings", 1))
    recipe = {
        'recipe': {k: round((v * servings), 3) for (k, v) in DATA.get('omlet').items()},
    }
    print(recipe)
    return render(request, 'calculator/index.html', context=recipe)


def get_pasta_recipe(request):
    servings = int(request.GET.get("servings", 1))
    recipe = {
        'recipe': {k: round((v * servings), 3) for (k, v) in DATA.get('pasta').items()},
    }
    return render(request, 'calculator/index.html', context=recipe)


def get_buter_recipe(request):
    servings = int(request.GET.get("servings", 1))
    recipe = {
        'recipe': {k: round((v * servings), 3) for (k, v) in DATA.get('buter').items()},
    }
    return render(request, 'calculator/index.html', context=recipe)
