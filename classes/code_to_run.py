class Pop:
    def __init__(self, size) -> None:
        self.size = size

class Pep:
    def __init__(self, Pop) -> None:
        self.pop = Pop

    def remove_pepe(self):
        self.pop.size += 1 

pepe = Pop(2)

popp = Pep(pepe)
pei = Pep(pepe)

popp.remove_pepe()
print(pei.pop.size)