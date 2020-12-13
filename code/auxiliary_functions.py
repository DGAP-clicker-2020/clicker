from settings import INITIAL_TARGET_HP


def to_fixed(num_obj, digits=0):
    """
    Приводит числа к виду *digits* цифр после запятой
    :param num_obj: число
    :param digits: цифры после запятой
    :return: обработанное число в формате строки
    """
    return f"{num_obj:.{digits}f}"


def calculate_hp(kills, start_hp=INITIAL_TARGET_HP):
    """
    Функция рассчитывает зворовье цели
    :param start_hp: начальное здоровье
    :param kills: колличество цбитых целей
    :return: здоровье следующей цели
    """
    return start_hp + kills ** 1.5
