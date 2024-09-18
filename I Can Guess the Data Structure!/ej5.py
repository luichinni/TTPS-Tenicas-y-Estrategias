from collections import deque
from queue import PriorityQueue
from sys import stdin

def is_stack(values_in_f: list[int], values_out_f: list[int]) -> bool:
    return values_out_f[::-1] == values_in_f

def is_queue(values_in_f: list[int], values_out_f: list[int]) -> bool:
    return values_out_f == values_in_f

def is_priority_queue(values_in_f: list[int], values_out_f: list[int]) -> bool:
    return values_out_f == values_in_f

msg = ['stack','queue','priority queue']

for linea in stdin:
    casos = int(linea)
    values_in = []
    values_out = []
    for I in range(0,casos):
        cmd_valor = input().split(' ')
        if (cmd_valor[0] == '1'):
            values_in.append(int(cmd_valor[1]))
        elif (cmd_valor[0] == '2'):
            values_out.append(int(cmd_valor[1]))
    
    in_to_compare = values_in[0:len(values_out)]
    
    in_to_comp_sort = values_in.copy()
    in_to_comp_sort.sort(reverse=True)
    
    estructura = [
        is_stack(in_to_compare,values_out),
        is_queue(in_to_compare,values_out),
        is_priority_queue(in_to_comp_sort[0:len(values_out)],values_out)
    ]
    
    if estructura.count(True) > 1:
        print('not sure')
    elif (estructura.count(True) == 0):
        print('impossible')
    else:
        print(msg[estructura.index(True)])
