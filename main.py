def find_cube_pairs(target):
    solutions = []  # No need for a semicolon in Python; removed it.
    max_num = round(target ** (1 / 3))  # Adjusted variable name from 'targ' to 'target' for accuracy.
    
    for a in range(1, max_num + 1):  # Fixed the typo from 'ranges' to 'range'.
        for b in range(a, max_num + 1):  # Another typo fix: 'ranges' corrected to 'range'.
            if a**3 + b**3 == target:  # Fixed the incorrect use of '***' for exponentiation; it should be '**'.
                solutions.append((a, b))  # Changed 'sol' to 'solutions' to match the defined variable.
    return solutions
pairs = find_cube_pairs(1729)  # Fixed an unnecessary comma at the end.

print("Valid cube pairs for 1729:")  # Corrected 'printf' to 'print' 

for a, b in pairs:  # Adjusted 'pair' to 'pairs' to iterate correctly over the result.
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729")  # Corrected the power operator from '**2' to '**3' for cube calculation.
