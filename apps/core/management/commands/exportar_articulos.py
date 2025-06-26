import csv
from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_date

from apps.core.models.articulo_model import Articulo


class Command(BaseCommand):
    help = 'Exporta artículos publicados en CSV, ordenados por fecha_publicacion descendente.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--fecha',
            type=str,
            help='Fecha mínima de publicación (formato YYYY-MM-DD). Si no se proporciona, se exportan todos.'
        )

    def handle(self, *args, **options):
        fecha = options.get('fecha')
        fecha_filtrada = parse_date(fecha) if fecha else None

        qs = Articulo.objects.filter(estado='publicado')
        if fecha_filtrada:
            qs = qs.filter(fecha_publicacion__gte=fecha_filtrada)

        articulos = qs.order_by('-fecha_publicacion')

        with open('articulos_exportados.csv', 'w', newline='', encoding='utf-8') as archivo_csv:
            writer = csv.writer(archivo_csv)
            writer.writerow(['ID', 'Título', 'Fecha de publicación', 'Estado', 'Autor'])

            for art in articulos:
                writer.writerow([
                    art.id,
                    art.titulo,
                    art.fecha_publicacion,
                    art.estado,
                    art.autor.nombre_completo if art.autor else 'Desconocido'
                ])

        self.stdout.write(self.style.SUCCESS(f'{articulos.count()} artículo(s) exportado(s) a "articulos_exportados.csv".'))
