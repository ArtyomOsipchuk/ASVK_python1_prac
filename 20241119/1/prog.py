def objcount(cls):
    class C(cls):
        counter = 0

        def __init__(self, *args):
            super().__init__(*args)
            self.__class__.counter += 1
        
        def __del__(self, *args):
            #super().__del__(*args)
            self.__class__.counter -= 1
    return C
