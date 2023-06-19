def count_sorted_vowel_strings(n):
    table = [[0] * 5 for _ in range(n)]
    
    for vowel in range(5):
        table[0][vowel] = 1
    
    for length in range(1, n):
        table[length][0] = table[length-1][0]
        table[length][1] = table[length-1][0] + table[length-1][1]
        table[length][2] = table[length-1][0] + table[length-1][1] + table[length-1][2]
        table[length][3] = table[length-1][0] + table[length-1][1] + table[length-1][2] + table[length-1][3]
        table[length][4] = table[length-1][0] + table[length-1][1] + table[length-1][2] + table[length-1][3] + table[length-1][4]
    
    total_count = sum(table[n-1])
    
    return total_count
print(count_sorted_vowel_strings(2))
