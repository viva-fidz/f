from django.core.management.base import BaseCommand
from fish.models import *


class Command(BaseCommand):
    help = 'Fill DB new data'

    def handle(self, *args, **options):
        categories = [
            {'name': 'Стрижка', 'image': 'cut.jpg', 'url': '/haircut/'},
            {'name': 'Прическа', 'image': 'hairdress.jpg', 'url': '/hairdress/'},
            {'name': 'Окрашивание', 'image': 'color.jpg', 'url': '/color/'},
            {'name': 'Плетение', 'image': 'lock.jpg', 'url': '/locks/'},
        ]

        haircut = [
            {'name': 'Женская стрижка', 'price': '1000', 'category': 'Стрижка'},
            {'name': 'Мужская стрижка', 'price': '1000', 'category': 'Стрижка'},
            {'name': 'Детская стрижа', 'price': '500', 'category': 'Стрижка'},
            {'name': 'Стрижка челки', 'price': '200', 'category': 'Стрижка'},
        ]

        locks = [
            {'name': 'Афрокосички', 'price': '6000', 'amount': '250', 'category': 'Плетение'},
            {'name': 'Афрокосички', 'price': '4000', 'amount': '150', 'category': 'Плетение'},
            {'name': 'Брейды', 'price': '150', 'amount': '1', 'category': 'Плетение'},
            {'name': 'Дреды', 'price': '150', 'amount': '1', 'category': 'Плетение', 'description': 'в зависимости от длины'},
        ]

        color = [
            {'name': 'Полное окрашивание', 'price': '1000', 'category': 'Окрашивание'},
            {'name': 'Декапирование', 'price': ' 1000', 'category': 'Окрашивание'},
            {'name': 'Мелирование фольга', 'price': ' 1300', 'category': 'Окрашивание'},
            {'name': 'Мелирование калифорния', 'price': ' 1000', 'category': 'Окрашивание'},
        ]

        hairdress = [
            {'name': 'Сушка', 'price': '200', 'category': 'Прическа'},
            {'name': 'Укладка', 'price': '500', 'category': 'Прическа'},
            {'name': 'Вечерняя причёска', 'price': '1500', 'category': 'Прическа'},
            {'name': 'Эксклюзивная причёска', 'price': '3000', 'category': 'Прическа'},
        ]
        Category.objects.all().delete()
        for category in categories:
            category = Category(**category)
            category.save()

        HairMaster.objects.all().delete()
        for cut in haircut:
            cut_category = cut['category']
            category = Category.objects.get(name=cut_category)
            cut['category'] = category
            cut = HairMaster(**cut)
            cut.save()

        Locks.objects.all().delete()
        for lock in locks:
            lock_category = lock['category']
            category = Category.objects.get(name=lock_category)
            lock['category'] = category
            lock = Locks(**lock)
            lock.save()

        Hairdress.objects.all().delete()
        for dress in hairdress:
            dress_category = dress['category']
            category = Category.objects.get(name=dress_category)
            dress['category'] = category
            dress = Hairdress(**dress)
            dress.save()

        Haircut.objects.all().delete()
        for cut in haircut:
            cut_category = cut['category']
            category = Category.objects.get(name=cut_category)
            cut['category'] = category
            cut = Haircut(**cut)
            cut.save()

        Color.objects.all().delete()
        for clr in color:
            clr_category = clr['category']
            category = Category.objects.get(name=clr_category)
            clr['category'] = category
            clr = Color(**clr)
            clr.save()
