# Configurator
s = '*'*3
p = ' '*10
# end

#Приветствие
def privet():
    print(p+'*'*50)
    print(p+s+"Приветствую в программе: Работники отдела!!"+s)
    print(p+"Чем вам помочь?? (Введите введите число и нажмите Enter)")
    print(p+"1 Устроить нового Сотрудника")
    print(p+"2 Уволить Сотрудника")
    print(p+"3 Посмотреть список Сотрудников")
    return 0

#************************************************************
#************************************************************
#************     ВНИМАНИЕ ТЕСТОВЫЕ ДАННЫЕ!!      ***********
#************************************************************
#************************************************************
data = ['Жора', 'Жопа']
addres = ['Ул.Пичерская', 'Ул.Достоевская' ]
dept = ['Спутник V','Вектор 7'] 
#************************************************************
#************************************************************
#**    Перед ЭКСПЛУАТАЦИЕЙ удалить данные из массивов      **
#************************************************************
#************************************************************

#Добавление работников
def vjob():

    pre_data = str(input(p+"Введите имя сотрудника: "))
    #pre_info = [(str(input(p+"Введите имя сотрудника: ")))]
    data.append(pre_data)

    pre_addres = str(input(p+"Введите Адрес места жительства сотрудника: "))
    addres.append(pre_addres)


    #print(*data)
    #print(*addres)
    return 0


#Вывод всех элементов из списка сотрудников
def how_many_workers():
    print("Номер"+p+"ФИО Работника"+p+"Место жительства")
    data_len = len(data)
    addres_len = len(addres)
    i=0
    j=0
    while i < data_len and addres_len:
        print(p+"-" * 50)
        print(i+1,p,data[i], p,addres[j])
        i+=1
        j+=1


while True:

    privet()

    console_input = int(input(p+"Введите номер команды: "))

    if console_input == 1:
        vjob()
        print(p+"Работник устроен на работу")
        
    elif console_input == 2:
        print("1 - введите если хотите удалить сотрудника по номеру в списке")
        print("2 - введите если используя ввод ФИО")
        console_input2 = int(input(p+"Введите номер команды"))
        
        if console_input2 == 1:
            how_many_workers()
        #index = data.index(str(input("Введите того кого ищите: ")))
        #print(len(data))
        #print(index)

        elif console_input2 == 2:
            index = data.index(str(input("Введите того кого ищите: ")))
            del data[index]
            print("Сотрудник был уволен")
       
    elif console_input == 3:

        how_many_workers()


        #print(*data)
        #print(data)
        


    else:
        print(p+"Ощибка, команды не существуюет")