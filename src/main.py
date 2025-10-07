from src.calculate import calculate

def main() -> None:
    """
    Обязательнная составляющая программ, которые сдаются. Является точкой входа в приложение
    :return: Данная функция ничего не возвращает
    """
    while True:

        expression = input("Введите выражение для подсчета калькулятором\n")
        if expression.lower() == "exit":
            break
        print("Результат: " + str(calculate(expression)))

if __name__ == "__main__":
    main()
