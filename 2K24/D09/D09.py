disk_map = list(map(int,open("input").read()))

def print_seq(seq):
    for el in seq:
        print(el,end='')
    print()

def to_blocks(seq):
    res = []
    idx = 0
    for i in range(len(seq)):
        if i%2==0:
            for _ in range(seq[i]): res.append(idx)
            idx += 1
        else:
            for _ in range(seq[i]): res.append('.')
    return res

def compress(seq):

    swap_inx = []
    for i in range(len(seq)): 
        if seq[i]=='.': swap_inx.append(i)


    i = len(seq) - 1
    while swap_inx[0] < i:

        if seq[i] == '.': 
            i-=1
            continue        

        seq[swap_inx[0]] = seq[i]
        seq[i] = '.'

        swap_inx = swap_inx[1:]

    return seq[:i]

def calc_checksum(seq):
    checksum = 0
    for i in range(len(seq)):
        checksum += seq[i]*i
    return checksum


blocks      = to_blocks( disk_map )
compressed  = compress( blocks )
checksum    = calc_checksum( compressed )

print(checksum)