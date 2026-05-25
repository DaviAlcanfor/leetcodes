class Solution:
  def countDistinctPermutationsOfAWord(self, s: str) -> int:

    def factorial(n: int) -> int:
      if n <= 1:
        return 1
      return n * factorial(n - 1)

    def prod(*nums) -> int:
      result = 1
      for n in nums:
          result *= n
      return result

    
    rep = {
      x: s.count(x) 
      for x in s
      if s.count(x) > 1  
    }

    return factorial(len(s)) // prod(*(factorial(v) for v in rep.values()))

    # o(n²)
