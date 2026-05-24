class Solution:
    def reverse(self, x: int) -> int:

        num_str = list(str(x))
        resultado = 0

        if x > 0:
            resultado = int("".join(num_str[::-1]))
        else: 
            resultado = int(num_str.pop(0) + "".join(num_str[::-1]))

        if resultado < -2**31 or resultado > 2**31 - 1:
            return 0

        return resultado
        
        
