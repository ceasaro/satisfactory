from django.core.management.base import BaseCommand, CommandError

from satisfactory.production.models import Product, Factory


class Command(BaseCommand):
    help = 'Creates / updates products'

    # def add_arguments(self, parser):
    #     parser.add_argument('poll_ids', nargs='+', type=int)
    def handle(self, *args, **options):
        Product.get_or_create_product('Iron', 'Fe', 30)
        Product.get_or_create_product('Iron pipe', 'Fe-pipe', 15, [('Fe', 15)])
        Product.get_or_create_product('Screw', 'screw', 40, [('Fe-pipe', 10)])
        Product.get_or_create_product('Iron plate', 'Fe-plate', 20, [('Fe', 30)])
        Product.get_or_create_product('Reinforced plate', 'Fe-rplate', 5, [('screw', 60), ('Fe-plate', 20)])
        Product.get_or_create_product('Modular frame', 'modular_frame', 5, [('screw', 140), ('Fe-rplate', 7.5)])
