from Check import check_time

@check_time
def solution(mtrx):
    return any('>x' in ''.join(r).replace(' ', '') for r in mtrx)

mat = [
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', ' ', ' ', ' '],
  [' ', ' ', '>', ' ', 'x'],
  [' ', ' ', '', ' ', ' ']
]
print(solution(mat))

# 8.5e-06 s
# 1.14e-05 s