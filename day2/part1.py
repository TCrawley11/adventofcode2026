# look for sequence of digits repeated twice

with open(file='input.txt', mode='r', encoding='utf-8') as f:
    line = f.readline()
    id_list = line.split(',')
    id_list2 = []
    for ids in id_list:
       id1, id2 = ids.split('-')[0], ids.split('-')[1]
       id_list2.append((id1, id2))


# Count the number of digits in the id, split each entry between the ids in chunks of the length/2
# then see if they are equal are not,
def main():
    sum = 0
    for entry in id_list2:
        print(f'NEW RANGE: {entry[0]}, {entry[1]}')

        for id in range(int(entry[0]), int(entry[1])+1):
            str_id = str(id)
            length = len(str_id)

            if length % 2 != 0:
                continue

            half = length // 2 
            first_half = str_id[:half]
            second_half = str_id[half:]

            print(f"first half: {first_half} second half: {second_half}")

            if first_half == second_half:
                print(f'Sum increased: {sum} + {id} = {sum + id}')
                sum += id

    #print(id_list2)
    return sum    

if __name__ == "__main__":
    sum = main()
    print(sum)