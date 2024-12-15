disk_map = list(map(int,open("input").read()))

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

def compress_blocks(seq):

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
        if seq[i] == '.': continue
        checksum += seq[i]*i
    return checksum

# PART 1

blocks      = to_blocks(disk_map)
compressed  = compress_blocks(blocks)
checksum    = calc_checksum(compressed)
print(checksum)

# PART 2

def compress_files(seq):

    file_id = 0
    for el in seq: 
        if isinstance(el,int) and el > file_id: 
            file_id = el

    file_id_max= file_id

    while file_id > 0:
        
        print(f"{((file_id_max-file_id+1)*100/file_id_max):6.2f} %",end="\r")
        
        file_size,file_blocks = 0,[]

        for i in range(len(seq)):
            if seq[i] == file_id:
                file_size += 1
                file_blocks.append(i)


        free_space_size, free_space_idx = 0,0
        for i in range(len(seq)):
            if seq[i] == '.':
                free_space_size += 1
            else: 
                free_space_idx = i + 1
                free_space_size = 0
            if free_space_size == file_size: break

        if free_space_size != file_size or free_space_idx > file_blocks[0]: free_space_idx = 0
        
        if free_space_idx != 0:
            for i in range( free_space_idx, free_space_idx + file_size ): seq[i] = file_id
            for i in file_blocks: seq[i] = '.'

        # print(f"{file_id}. S{file_size} {free_space_idx:2}",end=" ")
        # for el in seq: print(el,end="")
        # print(f" {file_blocks}")

        file_id -= 1
    
    print(" "*10,end="\r")
    return seq

blocks     = to_blocks(disk_map)
compressed = compress_files(blocks)
checksum   = calc_checksum(compressed)
print(checksum)