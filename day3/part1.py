# this solution doesn't work, need to use a two pointer p sure

batts = []
with open('test.txt') as f:
    for line in f.readlines():
        line = line.strip()
        batts.append(sorted(line))

def main():
    sum = 0
    for b in batts:
        len_b = len(b)
        l = b[len_b - 1]
        r = b[len_b - 2]
        two_digit = l + r
        sum += int(two_digit) 
        print(f'added: {b[len_b - 1]} and {b[len_b - 2]} and created {two_digit}')
    return sum

if __name__ == "__main__":
    sum = main()
    print(sum)
#print(batts)