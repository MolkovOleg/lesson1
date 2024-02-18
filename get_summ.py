def get_summ(one, two, delimiter='&'):
    return f'{one}{delimiter}{two}'

print(get_summ(10, 20))
res = get_summ('Learn', 'python', delimiter=' ')
print(res)
print(res.upper())