# Configurator
s = '*'*3
p = ' '*10
# end


def privet():
    print(p+'*'*50)
    print(p+s+"Приветствую в программе: Работники отдела!!"+s)
    print(p+"Чем вам помочь?? (Введите введите число и нажмите Enter)")
    print(p+"1 Устроить нового Сотрудника")
    print(p+"2 Уволить Сотрудника")
    print(p+"3 Посмотреть список Сотрудников")
    return 0


data = []
addres = []
dept = [] 

#Добавление работников
def vjob():

    pre_data = str(input(p+"Введите имя сотрудника: "))
    #pre_info = [(str(input(p+"Введите имя сотрудника: ")))]
    data.append(pre_data)

    pre_addres = str(input(p+"Введите Адрес места жительства сотрудника: "))
    addres.append(pre_addres)


    print(*data)
    print(*addres)
    return 0


#Вывод всех элементов из списка сотрудников
def how_many_workers():
    print(p+"ФИО Работника"+p+"Место жительства")
    data_len = len(data)
    addres_len = len(addres)
    i=0
    j=0
    while i < data_len and addres_len:
        print(p,data[i], p,addres[j])
        i+=1
        j+=1


while True:

    privet()

    console_input = int(input(p+"Введите номер команды: "))

    if console_input == 1:
        vjob()
        print(p+"Работник устроен на работу")
        
    elif console_input == 2:
        
        index = data.index(str(input("Введите того кого ищите: ")))
        print(len(data))
        print(index)
        how_many_workers()

        print("2")
       
    elif console_input == 3:

        print(*data)
        print(data)
        


    else:
        print(p+"Ощибка, команды не существуюет")

 