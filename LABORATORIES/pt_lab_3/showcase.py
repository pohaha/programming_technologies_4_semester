import LAB3_VAR6
import numbers
print("введите число - N - длинна искомого ряда:")
inp = input()
try:
    N = int(inp)
except:
    N = inp
LAB3_VAR6.row_summ(N)
