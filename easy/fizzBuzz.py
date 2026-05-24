class Solution:
    def fizzBuzz(self, n: int) -> List[str]:

        def isMul(x: int, mul: int | list[int]):
            if isinstance(mul, int):
                return x % mul == 0 

            return x % mul[0] == 0 and x % mul[1] == 0

        fbC = {
            str(x): "FizzBuzz" if isMul(x, [3,5])
            else "Fizz" if isMul(x, 3)
            else "Buzz"
            for x in range(1, n + 1)
            if isMul(x, 3) or isMul(x, 5)
        }

        return [str(x) if str(x) not in fbC else fbC.get(str(x)) for x in range(1, n+1)]
