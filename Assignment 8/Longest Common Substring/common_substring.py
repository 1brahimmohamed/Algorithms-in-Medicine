# python3

from collections import namedtuple
Answer = namedtuple('answer_type', 'i j len')


def polynomial_hash_func(string, prime, multiplier):
    # initialize hash value for 'string'
    hash_value = 0

    # loop through each character of 'string' to get the overall hash value
    for i in range(len(string) - 1, -1, -1):
        hash_value = (hash_value * multiplier + ord(string[i])) % prime
    return hash_value


def hash_tables(string, p_len, prime, multiplier):
    # create the table of lists
    tables = list([] for _ in range(len(string) - p_len + 1))
    substring = string[len(string) - p_len:]
    tables[len(string) - p_len] = polynomial_hash_func(substring, prime, multiplier)

    # y = multiplier ** p_len % prime
    y = pow(multiplier, p_len, prime)
    for i in range(len(string) - p_len - 1, - 1, - 1):
        tables[i] = (multiplier * tables[i + 1] + ord(string[i]) - y * ord(string[i + p_len])) % prime
    return tables


def hash_dictionary(string, p_len, prime, multiplier):
    dics = {}
    substring = string[len(string) - p_len:]
    last = polynomial_hash_func(substring, prime, multiplier)
    dics[last] = len(string) - p_len
    y = pow(multiplier, p_len, prime)
    for j in range(len(string) - p_len - 1, - 1, - 1):
        current = (multiplier * last + ord(string[j]) - y * ord(string[j + p_len])) % prime
        dics[current] = j
        last = current
    return dics


def SearchSubstring(hash_table, hash_dict):
    # initially set the flag to false (not found)
    flag = False
    matches = {}
    for i in range(len(hash_table)):
        b_start = hash_dict.get(hash_table[i], -1)
        if b_start != -1:
            flag = True
            matches[i] = b_start
    return flag, matches


def solve(first_str, second_str, low, high, max_length, first_str_index, second_str_index):
    # a is long string --> hash table, b is short string --> hash dict
    # mid is the length of the tested common substring

    mid = (low + high) // 2
    if low > high:
        return Answer(first_str_index, second_str_index, max_length)

    prime1 = 1000000007
    prime2 = 1000004249
    x = 263

    first_string_hashing_prime1 = hash_tables(first_str, mid, prime1, x)
    first_string_hashing_prime2 = hash_tables(first_str, mid, prime2, x)
    second_string_hashing_prime1 = hash_dictionary(second_str, mid, prime1, x)
    second_string_hashing_prime2 = hash_dictionary(second_str, mid, prime2, x)

    check1, matches1 = SearchSubstring(first_string_hashing_prime1, second_string_hashing_prime1)
    check2, matches2 = SearchSubstring(first_string_hashing_prime2, second_string_hashing_prime2)
    if check1 and check2:
        for a, b in matches1.items():
            temp = matches2.get(a, -1)
            if temp != -1:
                max_length = mid
                first_str_index, second_str_index = a, b
                del first_string_hashing_prime1, first_string_hashing_prime2, second_string_hashing_prime1, second_string_hashing_prime2, matches1, matches2
                return solve(first_str, second_str, mid + 1, high, max_length, first_str_index, second_str_index)
    return solve(first_str, second_str, low, mid - 1, max_length, first_str_index, second_str_index)


while True:
    line = input()
    if line == '':
        break
    else:
        s, t = line.split()
        k = min(len(s), len(t))
        if len(s) <= len(t):
            short_string, long_string = s, t
        else:
            short_string, long_string = t, s
        # l, i, j = solve(long_string, short_string, 0, k, 0, 0, 0)
        ans = solve(long_string, short_string, 0, k, 0, 0, 0)
        if len(s) <= len(t):
            print(ans.j, ans.i, ans.len)
        else:
            print(ans.i, ans.j, ans.len)
