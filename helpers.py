def is_float(value):
    try:
        f = float(value)
    except ValueError:
        return False
    except NameError:
        return False
    return True