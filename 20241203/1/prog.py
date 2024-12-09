class dump(type):
    def __new__(cls, name, bases, attrs):
        for key, value in attrs.items():
            if callable(value):
                method = value

                def wrapper(name, method):
                    def new_method(self, *args, **kwargs):
                        print(f"{name}: {args}, {kwargs}")
                        return method(self, *args, **kwargs)
                    return new_method
                
                attrs[key] = wrapper(key, method)
        return super().__new__(cls, name, bases, attrs)

import sys

exec(sys.stdin.read())
