# A program of finding 'n' numbers of FIBONACCI numbers using class & iterator

class Numbers:
    def __init__(self, n):
        self.noOfElements = n

    def __iter__(self):
        self.fib0 = 0
        self.fib1 = 1
        self.count = 0
        return self

    def __next__(self):
        if self.count == 0:
            self.count += 1
            return self.fib1

        elif self.count < self.noOfElements:
            fib2 = self.fib0 + self.fib1
            self.fib0 = self.fib1
            self.fib1 = fib2
            self.count += 1
            return fib2

        else:
            raise StopIteration


myClass = Numbers(10)
myIter = iter(myClass)

for x in myIter:
    print(x)
