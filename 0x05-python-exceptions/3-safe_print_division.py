def safe_print_division(a, b):
    try:
        result = a/b
    except:
        result = None
    finally:
        print("Inside result: {0}".format(result))
        return result
