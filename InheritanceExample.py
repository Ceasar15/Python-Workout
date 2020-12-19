from os import times
import time

class Progression():
    def __init__(self, start=0):
        self._current = start

    def _advance(self):
        self._current += 1

    def __next__(self):
        if self._current is None:
            raise StopIteration
        else:
            answer = self._current
            self._advance()
            return answer

    def __iter__(self):
        return self

    def print_progression(self, n):
        print(' '.join(str(next(self)) for j in range(n)))

print('\n Progression: ')
Progression(3).print_progression(10)

class ArithmeticProgression(Progression):
    def __init__(self, increment=1, start=0):
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        self._current += self._increment

print('\n Arithmetric Progression: ')
ArithmeticProgression(10,85).print_progression(10)


class GeometricProgression(Progression):
    def __init__(self, base=2,start=1):
        super().__init__(start)
        self._base = base

    def _advance(self):
        self._current *= self._base

print('\n Geometric Progression: ')
GeometricProgression(10,5).print_progression(10)

class FibonacciProgression(Progression):
    def __init__(self, first=0, second =1):
        super().__init__(first)
        self._prev = second - first

    def _advance(self):
        self._prev,self._current =  self._current, self._prev + self._current

print('\n Fiibonacci Progression: ')
FibonacciProgression(0,1).print_progression(10)

if __name__ == '__main__':

    print('\n Unit Test Loading In 5 secs')
    time.sleep(5)
    print('\n Default Progression: ')
    Progression().print_progression(10)

    print('\n Arithmetic Progression starting from 5')
    ArithmeticProgression(5).print_progression(10)

    print('\n Arithmetic Progression with increment 5 and start 2')
    ArithmeticProgression(5,2).print_progression(10)

    print('\n Geometric Progression with default base 2')
    GeometricProgression().print_progression(10)

    print('\n Geometric Progression with base 3 and start 5')
    GeometricProgression(3,5).print_progression(10)

    print('\n Fibonnaci Sequence with default start values')
    FibonacciProgression().print_progression(10)

    print('\n Fibonnaci Sequence with start values 4 and 6')
    FibonacciProgression(4,6).print_progression(10)

