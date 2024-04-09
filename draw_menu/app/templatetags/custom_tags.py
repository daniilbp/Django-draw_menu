from django import template
from django.shortcuts import get_object_or_404
from django.core.exceptions import ObjectDoesNotExist

from app.models import MenuItem

register = template.Library()


def get_menu(menu_items: MenuItem, menu_item: str = None, item_menu: list = None):
    menu = list(menu_items.filter(parent=None) if menu_item is None
                else menu_items.filter(parent__name=menu_item))
    try:
        menu.insert(menu.index(item_menu[0].parent) + 1, item_menu)
    except (IndexError, TypeError):
        pass
    try:
        return get_menu(menu_items, menu_items.get(name=menu_item).parent.name, menu)
    except AttributeError:
        return get_menu(menu_items, item_menu=menu)
    except ObjectDoesNotExist:
        return menu


@register.inclusion_tag('app/menu.html')
def draw_menu(menu_name: str = None, menu_item: str = None):
    menu_items = MenuItem.objects.select_related('parent').filter(menu__name=menu_name)
    menu = get_menu(menu_items) if menu_name == menu_item else get_menu(menu_items, menu_item)
    
    return {'menu': menu}
