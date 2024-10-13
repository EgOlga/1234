import inspect

def introspection_info(obj):
    obj_type = type(obj).__name__
    attributes = [attr for attr in dir(obj)
                if not callable(getattr(obj, attr))]
    methods = [attr for attr in dir(obj)
                if callable(getattr(obj, attr))]
    module = getattr(obj, '__module__', 'builtins')

    info = {
        "type": obj_type,
        "attributes": attributes,
        "methods": methods,
        "module": module,
    }
    return info

def __str__():
        return str(introspection_info())


number_info = introspection_info(42)
print(number_info)
string_info = introspection_info("Hello")
print(string_info)
list_info = introspection_info([1, 2, 3])
print(list_info)
print(inspect.isclass(introspection_info))
print(inspect.isfunction(introspection_info))
print(inspect.isclass(number_info))
print(type(number_info))
print(callable(__str__))
print(isinstance(number_info, dict))



#Вывод на консоль:
#{'type': 'int', 'attributes': [...], 'methods': ['__abs__', '__add__', ...], 'module': '__main__'}

