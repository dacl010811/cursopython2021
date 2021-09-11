import locale

local =  locale.getlocale()
print(local)

locale.setlocale(locale.LC_ALL,'en_US')

local =  locale.getlocale()
print(local)
