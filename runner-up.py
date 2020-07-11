n = int(input())
arr = map(int, input().split())
l, runner_up = [], 0
for i in arr:
     l.append(i)
l.sort()
for i in range(len(l) - 1):
     if l[i] < l[i+1]:
          runner_up = l[i]
print(runner_up)





##     if l[i] == l[i+1]:
##          runner_up = min([l[i-1], l[i]])
##print(runner_up)
