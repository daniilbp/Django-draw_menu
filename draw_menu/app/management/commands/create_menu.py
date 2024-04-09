import random
from string import ascii_letters, digits

from django.core.management import BaseCommand
from django.db import IntegrityError

from app.models import Menu, MenuItem

ALPHABET = ascii_letters + digits


class Command(BaseCommand):
    _class = Menu
    name = 'MENU'
    menu_size: int = 3
    menu_depth: int = 2

    def __create_menu_items(
        self,
        level_name: str,
        menu: Menu,
        parent: MenuItem = None,
        depth: int = 0,
    ) -> None:
        if depth >= self.menu_depth:
            try:
                menu_item = MenuItem.objects.create(
                    name='CV',
                    menu=menu,
                    parent=parent,
                )
                MenuItem.objects.create(
                    name='daniilbp',
                    menu=menu,
                    parent=menu_item,
                    url='https://ulyanovsk.hh.ru/resume/6581bb2fff08096d4c0039ed1f526a36767659',
                )
            except IntegrityError:
                pass
            return
        for i in range(self.menu_size):
            unique_id = ''.join(random.choice(ALPHABET) for i in range(4))
            menu_item_name = (
                f'{level_name}-{depth+1}-{i+1}-{unique_id}')
            menu_item = MenuItem.objects.create(
                name=menu_item_name,
                menu=menu,
                parent=parent,
            )
            self.__create_menu_items(level_name, menu, menu_item, depth + 1)

    def __create_menu(self, menu_name: str) -> None:
        menu = Menu.objects.create(name=menu_name)
        self.__create_menu_items(level_name=menu.name, menu=menu)

    def handle(self, *args, **kwargs):
        for menu_name in (
            'menu_1',
            'menu_2',
            'menu_3',
        ):
            self.__create_menu(menu_name)
            