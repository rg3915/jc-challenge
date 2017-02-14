# -*- coding: utf-8 -*-
import csv
from myproject.crm.models import Product

product_list = []

''' Lendo os dados de produtos.csv '''
with open('shell/produtos.csv', 'r') as f:
    r = csv.DictReader(f)
    for dct in r:
        product_list.append(dct)
    f.close()


# Insert Product
obj = [Product(**product) for product in product_list]
Product.objects.bulk_create(obj)
