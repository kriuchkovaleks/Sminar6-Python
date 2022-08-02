

values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]

transformation = lambda i: i 

print(transformation)

trans_values  = list(map(transformation, values))

print(trans_values)

if values == trans_values:
    print('Ok')
else:
    print('Fail')