koef_list.append(random.randint(0,100))
list_step = [i for i in range(num,-1,-1)]

#koef_list = [5, 7, 0, 0]

poli = ''
for koef, step in (zip(koef_list, list_step)): #(25, 3)  (15, 2) ... (46, 0)
    if step == 0 and koef != 0:
       string = str(koef)
    elif step == 1 and koef != 0:
        string = str(koef)+'*x'
    elif not koef:
       string = ""
    elif koef == 1:
       string = string = 'x**'+str(step)
    else:
        string = string = str(koef)+'*x**'+str(step)
    if string:
        poli += ' + ' + string
poli += ' = 0'
print(poli.strip('+ '))

poli = ''
for koef, step in (zip(koef_list, list_step)):
    if koef:
        koef = koef if koef > 1 else ''
        poli += str(koef)
        if step:
            poli += '*x'
            if step > 1:
                poli += f'**{str(step)}'
            poli += ' + '
poli += ' = 0'
print(poli)
