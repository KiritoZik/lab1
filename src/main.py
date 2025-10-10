from src.calculate import calculate

def main() -> None:
    """
    Обязательная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """

    '''Запускаем 'бесконечный' цикл, чтобы пользователь мог находить значения выражения без перезапуска, 
    пока не напишет 'exit' или 'выход' - регистр не учитывается'''
    while True:
        expression = input("Введите выражение для подсчета калькулятором\n").replace(',', '.')
        if expression.lower() == "exit" or  expression.lower() == 'выход':
            break
        try:
            result = calculate(expression)
            if result.is_integer():
                print("Результат: " + str(int(result)))
            else:
                print("Результат: " + str(result))
        except OverflowError:
            print("Слишком большое значение")
        except Exception as error:
            print(error)

if __name__ == "__main__":
    main()
