# this solution doesn't work, need to use a two pointer p sure

batts = []
with open('input.txt') as f:
    for line in f.readlines():
        batts.append(line.strip())

def main():
    l, r = 0, 0
    res_arr = []
    for bank in batts:
        res = ''
        lmax, rmax = bank[0], bank[1]
        l, r = 0, 1
        for i, b in enumerate(bank[2:]):
            # print(f'left max {lmax}, left pointer {l}')
            # print(f'right max {rmax}, right pointer {r}')
            # print(f'VALUE {b}')

            # in the case that the value is bigger than both rmax and lmax, move lmax if not at end of bank
            if b > lmax and i+3 != len(bank):
                l = i + 2
                lmax = bank[l]
                r = i + 3
                rmax = bank[r]
                continue
            if b > rmax:
                if rmax > lmax:
                    l = r
                    lmax = bank[l]
                r = i + 2
                rmax = bank[r]

        res = str(lmax) + str(rmax)
        res_arr.append(int(res))
        # print('------------- Moving onto next bank! ----------')
    return res_arr

if __name__ == "__main__":
    res_arr = main()
    print(res_arr)
    sum = sum(res_arr)
    print(f'Got sum: {sum}')