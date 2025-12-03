with open(file='input.txt', mode='r', encoding='utf-8') as f:
    line = f.readline().split(',')
    id_list2 = []
    for ids in line:
       id1, id2 = ids.split('-')[0], ids.split('-')[1]
       id_list2.append((id1, id2))

def check(str_id) -> bool:
    length = len(str_id)

    for l in range(1, length):
        if length % l == 0:
            patt = str_id[:l]
            reps = length // l

            if str_id == patt * reps:
                return True
    return False

def main():
    sum = 0
    for entry in id_list2:
        print(f'NEW RANGE: {entry[0]}, {entry[1]}')

        for id in range(int(entry[0]), int(entry[1])+1):
            str_id = str(id)

            if check(str_id):
                print(f'Sum increased: {sum} + {id} = {sum + id}')
                sum += id

    #print(id_list2)
    return sum    

if __name__ == "__main__":
    sum = main()
    print(sum)