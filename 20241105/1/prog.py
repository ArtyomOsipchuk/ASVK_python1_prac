class Omnibus:
    cnt = {}
    scnt = {}
    
    def __setattr__(self, name, val):
        if name in self.__class__.cnt:
            self.__class__.cnt[name] += 1
        else:
            self.__class__.cnt[name] = 1
        self.scnt[name] = 1

    def __getattr__(self, name):
        return self.__class__.cnt[name]

    def __delattr__(self, name):
        if name in self.scnt:
            del self.scnt[name]
            self.__class__.cnt[name] -= 1
            if self.__class__.cnt[name] == 0:
                del self.__class__.cnt[name]

import sys

exec(sys.stdin.read())
