import xml.etree.ElementTree as ET


# Парсинг XML-файла
tree = ET.parse('cars/cars.xml')
root = tree.getroot()


def parser(xml_file):
    car_dict = {}
    for tag in xml_file.findall('mark'):
        key = tag.get('name')
        list_value = []
        for elem in tag.findall('folder'):
            list_value.append(elem.get('name').split(',')[0])
        car_dict[key] = set(list_value)

    return car_dict


CAR_DICT = parser(root)



