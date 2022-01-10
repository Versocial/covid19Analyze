x = '232.3%'
y = float(x[0:len(x) - 1]) if isinstance(x, str) and x[len(x) - 1] == '%' else x
print(y)
