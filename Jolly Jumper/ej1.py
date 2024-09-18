import sys

def is_jolly(linea: str):
    nums = linea.split(' ')
    control_numerico = [False] * (int(nums[0])-1)

    for I in range(1,len(nums)-1):
        dif = abs(int(nums[I])-int(nums[I+1]))

        if ((dif == 0) or (dif > len(control_numerico))):
            return False

        if (control_numerico[dif-1]):
            return False
        
        control_numerico[dif-1] = True
        
    return all(control_numerico)

for linea in sys.stdin:
    if is_jolly(linea):
        print('Jolly')
    else:
        print('Not jolly')
