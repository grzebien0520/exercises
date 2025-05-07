#cwiczenie 7 - moduł

def kwadraty(numbers2):
    kwadraty = []
    for i in numbers2:
        if i > 10:
            j = i ** 2
            kwadraty.append(j)
    return kwadraty
