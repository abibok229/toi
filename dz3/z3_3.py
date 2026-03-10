def function_name(search: str, status: bool, *args: object, **kwargs: object) -> list[int] | str:
    """
    Обрабатывает аргументы в зависимости от параметров search и status.

    Параметры:
        search (str): Режим обработки. Допустимые значения: "args" или "kwargs".
        status (bool): Флаг, влияющий на обработку позиционных аргументов.
        *args: Произвольные позиционные аргументы любых типов.
        **kwargs: Произвольные именованные аргументы.

    Возвращаемое значение:
        list[int] | str:
            - Если search == "args" и status == True: список целых чисел,
              отобранных из args.
            - Если search == "args" и status == False: строка, полученная
              последовательным преобразованием всех args в строки и их конкатенацией.
            - Если search == "kwargs": строка, содержащая пары ключ-значение
              из kwargs в формате "Key: ключ, Value: значение; ".

    Исключения:
        ValueError: Возникает, если search не равен "args" или "kwargs".
    """
    result: list[int] = []
    result_2: str = ""

    if search == "args":
        if status:
            for i in args:
                if isinstance(i, int):
                    result.append(i)
            return result
        else:
            for i in args:
                result_2 += str(i)
            return result_2
    elif search == "kwargs":
        for k, v in kwargs.items():
            result_2 += f"Key: {k}, Value: {v}; "
        return result_2
    else:
        raise ValueError("Error for search")
