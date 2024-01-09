def eh_primo(x):
    i = 0
    divisores = 0
    while i < x:
        i+=1
        if (x%i == 0):
            divisores+=1
    if (divisores == 2):
        return True
    else:
        return False
	
x = int(input())
if eh_primo(x):
	print('S')
else:
	print('N')
