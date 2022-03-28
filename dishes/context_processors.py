from .models import Category


def categories_processor(request):
    """ Получение категорий во всех шаблонах для our menu в navbar'е """
    categories = Category.objects.prefetch_related('product_set').all()
    return {'categories': categories}
