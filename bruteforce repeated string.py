def solution(s,n):
  count = 0  
  if len(s) < n:
    while len(s) < n:
        s = s + s

    s = s[:n]

    for i in s:
        if i == 'a':
            count = count + 1 
    
    return count

print(solution("abcac",10))