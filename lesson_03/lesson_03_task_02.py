from smartphone import smartphone

catalog = [
smartphone("Nokia", "6230", 79119992325),
smartphone("Sony_Ericsson", "w200", 79813923255),
smartphone("Motorolla", "RzV3", 79110178190),
smartphone("Xiaomi", "mi8", 79999998888),
smartphone("Nokia", "n95", 79154140403)
]

for smartphone in catalog:
    print(f"{smartphone.brend_name}: {smartphone.model_name}, тел.: +{smartphone.ab_number}")