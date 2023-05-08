def solution(num_list):
    hol = ''
    zzak = ''
    n = 0
    for i in num_list:
        if num_list[i] % 2 == 0:
            zzak += num_list[i]
        else:
            hol += num_list[i]
    int(hol) + int(zzak)
    
    return n