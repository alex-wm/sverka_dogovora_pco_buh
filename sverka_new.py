pnum="3"
buh_data = open("buh.txt")
pco_data = open("pco.txt")

buh_lost = open("buh"+pnum+"_lost.txt", "w")
pco_lost = open("pco"+pnum+"_lost.txt", "w")

b_data = buh_data.readlines()
p_data = pco_data.readlines()


#формируем массивы для данных БУХГАЛТЕРИЯ

b0=[]
b1=[]
b2=[]

for e in b_data:
    buh_part = e.split("	")
    b0.append(buh_part[0])
    b1.append(buh_part[1])
    b2.append(buh_part[2])

#формируем массивы для данных ПЦО

a0=[]
a1=[]
a2=[]
a3=[]
a4=[]
a5=[]

for e1 in p_data:
    pco_part = e1.split("	")
    a0.append(pco_part[0])
    a1.append(pco_part[1])
    a2.append(pco_part[2])
    a3.append(pco_part[3])
    a4.append(pco_part[4])
    a5.append(pco_part[5])

print ('Шаг 1: Поиск лишних договоров в списке ПЦО')

# Выбираем из списка ПЦО договора которых нет в базе бухгалтерии

pco_lost.write("Договора отсутствующие в списках ПЦО-"+pnum+"\n")
for x in range(len(a0)):
    if a0[x] not in b0:
        pco_lost.write(a0[x]+";"+a1[x]+";"+a2[x]+";"+a3[x]+";"+a4[x]+";"+a5[x])

print ('Шаг 2: Поиск лишних договоров в списке БУХГАЛТЕРИЯ')        

buh_lost.write('Поиск лишних договоров в списке БУХГАЛТЕРИЯ \n')
for x in range(len(b0)):
    if b0[x] not in a0:
        buh_lost.write(b0[x]+";"+b1[x]+";"+b2[x])

print ('Завершено')
print ('Обработано записей БУХГАЛТЕРИЯ '+str(len(b_data)))
print ('Обработано записей ПЦО '+str(len(p_data)))
buh_data.close()
pco_data.close()
buh_lost.close()
pco_lost.close()
