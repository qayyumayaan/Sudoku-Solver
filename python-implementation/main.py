import sudokuAlg as sud
# import os
# os.system('cls')
import time

grid = [
[	0	,	0	,	0	,	0	,	0	,	4	,	0	,	5	,	2	],
[	6	,	0	,	0	,	0	,	0	,	0	,	0	,	0	,	0	],
[	9	,	0	,	5	,	0	,	2	,	0	,	0	,	3	,	0	],
[	0	,	0	,	0	,	8	,	0	,	0	,	7	,	0	,	0	],
[	2	,	0	,	3	,	0	,	4	,	0	,	0	,	9	,	0	],
[	0	,	1	,	0	,	0	,	0	,	0	,	0	,	0	,	0	],
[	5	,	0	,	1	,	0	,	0	,	7	,	9	,	0	,	0	],
[	0	,	6	,	0	,	0	,	5	,	0	,	0	,	0	,	0	],
[	0	,	4	,	0	,	0	,	0	,	0	,	0	,	1	,	0	] ]


start_time = time.time()

if sud.solve(grid):
    for row in grid:
        print(row)
else:
    print("No solution exists.")
    
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Ran in {elapsed_time*1000:.4f} milliseconds ({elapsed_time:.4f} seconds).")
    
