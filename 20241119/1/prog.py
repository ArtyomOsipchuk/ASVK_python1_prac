def objcount(cls):
    class C(cls):
        counter = 0

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.__class__.counter += 1
        
        def __del__(self, *args):
            self.__class__.counter -= 1
            del self
    return C

import sys

exec(sys.stdin.read())
