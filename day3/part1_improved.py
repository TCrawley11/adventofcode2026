batts = []
with open('input.txt') as f:
    for line in f.readlines():
        batts.append(line.strip())

res_arr = []

def main():
    for bank in batts:
        res = ''
        best_lmax = max(bank[:-1])
        lmax_index = bank.index(best_lmax)

        rest = bank[lmax_index + 1:]
        best_rmax = max(rest)
        res = int(best_lmax + best_rmax)
        res_arr.append(res)
    return res_arr

if __name__ == "__main__":
    results = res_arr
    print(results)
    sum = sum(res_arr)
    print(f'Got sum {sum}')
