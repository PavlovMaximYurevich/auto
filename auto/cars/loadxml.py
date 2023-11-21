# import os
import xml.etree.ElementTree as ET
from pprint import pprint

# from django.core.management import BaseCommand
#
# from auto.settings import BASE_DIR
# from cars.models import Mark, ModelCar

# Парсинг XML-файла
tree = ET.parse('cars/cars.xml')
root = tree.getroot()


def parser(xml_file):
    car_dict = {}
    for tag in xml_file.findall('mark'):
        # print(tag.get('name'))
        key = tag.get('name')
        list_value = []
        for elem in tag.findall('folder'):
            # print(elem.get('name').split(',')[0])
            list_value.append(elem.get('name').split(',')[0])
        car_dict[key] = list_value

    return car_dict


CAR_DICT = parser(root)



