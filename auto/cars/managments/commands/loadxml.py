import os
import xml.etree.ElementTree as ET

from django.core.management import BaseCommand

from auto.settings import BASE_DIR
from cars.models import Mark, ModelCar

# Парсинг XML-файла
tree = ET.parse('cars.xml')
root = tree.getroot()


def parser(xml_file):
    for tag in xml_file.findall('mark'):
        # print(tag.get('name'))
        Mark.objects.get_or_create(
            brand_auto=tag.get('name')
        )
        for elem in tag.findall('folder'):
            # print(elem.get('name').split(',')[0])
            ModelCar.objects.get_or_create(
                model_auto=elem.get('name').split(',')[0]
            )


parser(root)
