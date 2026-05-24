class Solution:
  def countDistinctPermutationsOfAWord(self, s: str) -> int:
    from math import prod, factorial 
    
    rep = {
      x: s.count(x) 
      for x in s
      if s.count(x) > 1  
    }

    return factorial(len(s)) // prod(factorial(v) for v in rep.values())
