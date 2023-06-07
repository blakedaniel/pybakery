import csv


def importFile(file:str, db:str=None, csv_db_fields:list|None=None):
    with open(file) as data:
        data = csv.DictReader(data, ('Ingredient', 'Volume', 'Ounces', 'Grams'))
        print(data)

importFile('/Users/blakevanfleteren/Desktop/ingredients_volume_weight.csv')