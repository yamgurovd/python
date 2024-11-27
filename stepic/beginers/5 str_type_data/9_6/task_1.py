"""Используя метод format(), дополните приведённый код так, чтобы он вывел текст:

In 2010, someone paid 10k Bitcoin for two pizzas."""
s = 'In {0}, someone paid {1} {2} for two pizzas.'
year = 2010
name = "Bitcoin"
dig = "10k"
print(s.format(year, dig, name))
