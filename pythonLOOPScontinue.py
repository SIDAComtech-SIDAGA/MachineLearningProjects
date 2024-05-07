#EXAMPLE OF CONTINUE STATEMENT IN FOR LOOP

from numpy import arange
# GENERATE ARRAY WITH THE VALUES: -4, -3, -2, 0 , 1, 2

x17 = arange(-4, 3)
for i in x17:
    if i == 0 or i == 1:
        continue
    print("i = ", i)
    
    