class Solution:
  def countDistinctPermutationsOfAWord(self, s: str) -> int:
    from math import prod # just for product aggregation
    
    def factorial(n: int):
      if n == 1:
        return n
      return n * factorial(n-1)
    
    rep = {
      str(x): s.count(x) 
      for x in s
      if s.count(x) > 1  
    }

    return factorial(len(s)) / prod(factorial(v) for v in rep.values)

    # ig this is right
