def format_string(x, y, z):

    return '{hour}時の{target}は{value}'.format(hour=x, target=y, value=z)

x = 12
y = '気温'
z = 22.4
print(format_string(x, y, z))

