# Configurator
s = '*'*3
p = ' '*10
# end

#Приветствие
def privet():
    print(p+'*'*50)
    print(p+s+"Приветствую в программе: Работники отдела!!"+s)
    print(p+"Чем вам помочь?? (Введите введите число и нажмите Enter)")
    print(p+"1 - Устроить нового Сотрудника")
    print(p+"2 - Уволить Сотрудника")
    print(p+"3 - Посмотреть список Сотрудников")
    return 0

#************************************************************
#************************************************************
#************     МАССИВЫ ----- DATA              ***********
#************************************************************
#************************************************************
data = []
addres = []
dept = [] 
#************************************************************
#************************************************************
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
        print(p+"1 - введите если хотите удалить сотрудника по номеру в списке")
        print(p+"2 - введите если используя ввод ФИО")
        console_input2 = int(input(p+"Введите номер команды: "))
        
        if console_input2 == 1:
            how_many_workers()
            i = int(input("Введите порядковый согласно таблице для увольнения работника: "))
            b = i - 1
            del data[b]
            del addres[b]
            print("Работник уволен.")
        #index = data.index(str(input("Введите того кого ищите: ")))
        #print(len(data))
        #print(index)

        elif console_input2 == 2:
            index = data.index(str(input("Введите того кого хотите уволить: ")))
            how_many_workers()
            del data[index]
            del addres[index]
            print(p+"Сотрудник был уволен.")
        else:
           print(p+"Ощибка, команды не существует.")
     

    elif console_input == 3:
        a = len(data)
        if a <= 0:
            print(p+p+"ВНИМАНИЕ")
            print(p+"Список сотрудников ПУСТ!!!")
            print(p+"Для начала работы с Базой, заполните список сотрудников")
        

        else:
            how_many_workers()



        #print(*data)
        #print(data)
        


    else:
        print(p+"Ощибка, команды не существуюет.")