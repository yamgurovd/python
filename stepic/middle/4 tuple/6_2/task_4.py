"""Используя срезы, дополните приведенный ниже код так, чтобы он вывел все элементы кортежа countries,
кроме последних трех.

Подсказка: Не забывайте, что элементы кортежа нумеруются с −1 начиная с конца."""

countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[:-3])

# Второй способ решения задачи - взято из форума
countries = ('Russia', 'Argentina', 'Slovakia', 'Canada', 'Slovenia', 'Italy', 'Spain', 'Ukraine', 'Chile', 'Cameroon')
print(countries[:countries.index('Ukraine')])
