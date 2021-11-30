
import numpy as np

def guess_number(Start=1,Finish=101)-> int:
    """Данная функция угадывает число которая сама же и загадавыет))
    Args:
        Она принимает 2 значения Start ,Finish - начало диапозона конец диапозона из которго она берёт числа
    Returns:
           Возввращает кортеж из угаданного числа и количество попыток ушедших на разгадку
    """
    number=np.random.randint(Start,Finish)  #случайное число загаданное компьютером 

    predikt_number=int(Finish/2) #первым предложенным числом будет середина интервалла
    count=0 # подсчёт попыток
    big_predict_number=[Start-1,] # список чисел которые меньше предложенного числа
    small_predict_number=[Finish+1,] # список чисел которые больше предложенного чсила

    while True:
        """ принцеп работы данного цикла :
        получаем ответ о том что число больше , меньше , или равно загаданному.
        Если предложенное число меньше заданного мы добавляем предложенное число в список чисел которые меньше предложенного числа big_predict_number 
        Сужаем диапозон поиска : берём минимальное число из списка чисел которые больше предложенного числа из small_predict_number
        и предложенное число находим число равно удалённое от них обоих 
        т.е предложенное число 50   минимальное большее 100  они оба равно удалены от 75
        далее сохраняем найденное число (75) в переменную predict_number для повторного повторения цикла
        Для случая больше алгоритм зекланьный
        Если мы угадали просто выйдем из цикла"""
    
        count+=1 # начисление попыток
        
        if number>predikt_number:                                  #узнаем что чило меньше загаданного
            big_predict_number.append(predikt_number)              # добавляем элемент в список большых загаданного числа
            diffrence=abs(int((min(small_predict_number)-predikt_number)/2)) 
            if diffrence==0:                                       # Защита от зацикливания
                print("corr",number)                               # Сообщение появится если значения придётся корректировать
                diffrence=1         # прировняет разнось к 1 чтоб данный брок кода не повторялся постоянно и переменная predikt_number менялась
            predikt_number=predikt_number+diffrence                # измение переменной predict_number
            
            
        elif number<predikt_number:
            small_predict_number.append(predikt_number) 
            diffrence=abs(int((max(big_predict_number)-predikt_number)/2)) 
            if diffrence==0:
                print("corr",number) 
                diffrence=1 
            predikt_number=predikt_number-diffrence 
            
        else: # Число угаданно выход из цикла
            break
        
    return(number,count)  



def test_funks(trys=1000,return_tuple=False)->tuple:
    """Данная функция предназначена для тестировки функции по угадыванию числа

    Args:
        trys это сколько тестов надо провести поумолчанию равно 1000
        return_tuple нужно ли вернуть список с резульнатами тестируемой функции (поумолчание не возвращает)

    Returns:
        Максимальное количество попыток
        Список результатов работы чункции и в конце кортежа максимальное количество попыток
        
    """

    def dek_arg(*args,**kwargs):
        """аргументы тестируемой функции
        """
        def dek_funk(funk):
            """проводит заданное переменной ТРАЙ число тестов

            Args:
                funk тестируемая функция

            Returns:
                результаты тестирования функции
            """
            list_results=[] # список результатов 
            max_value=0 # максимальное количество попыток
            for T in range(trys): 
                result=funk(*args,**kwargs)  #результат работы функции
                if result[1]>max_value:      #поиск наибольшего количества попытак
                    max_value=result[1]      #рисваивание наибольшего значения попыток 
                list_results.append(result)  #заполнение списка результатами
            if return_tuple==False:          #какой результат вернуть
                return max_value
            else:
                return sorted(list_results,key=lambda tup:tup[0]),max_value
        return dek_funk
    return dek_arg


a=test_funks(1000,return_tuple=True)()(guess_number)


print(a)