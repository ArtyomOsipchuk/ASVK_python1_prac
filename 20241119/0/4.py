class Sender:
    friendly = True
    @classmethod
    def report(cls):
        if cls.friendly:
            print("Greetings, cowboy!")
            cls.friendly = False
        else:
            print("Fall of the horse!")

class Asker:
    @staticmethod
    def askall(lst):
        for r in lst:
            r.report()

lst = [Sender() for i in range(5)]
a = Asker()
a.askall(lst)
