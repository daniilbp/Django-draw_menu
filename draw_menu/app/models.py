from django.db import models


class Menu(models.Model):
    name = models.CharField('Название меню', max_length=50, unique=True)
    description = models.TextField('Информация', max_length=200, blank=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Меню'
        verbose_name_plural = 'Меню'
    
    def __str__(self) -> str:
        return self.name


class MenuItem(models.Model):
    name = models.CharField('Название пункта меню', max_length=50, unique=True)
    description = models.TextField('Информация', max_length=200, blank=True)
    url = models.CharField('Сылка для конечного пункта меню', max_length=50, blank=True)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name='menu_items')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = ['id']
        verbose_name = 'Пункт меню'
        verbose_name_plural = 'Пункты меню'
    
    def __str__(self) -> str:
        return self.name
