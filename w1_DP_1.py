# 돌 게임 (no.9655)

# 풀이 1 : success(31252KB, 40ms) 🤦‍♀️
num = int(input())
 
if num % 2 == 0 :
    print("CY")
else:
    print("SK")

# 풀이 2: 런타임에러(IndexError)😳
# idea: 돌의 개수마다의 최소 턴을 메모이제이션
# n개의 돌이 있을때 최소턴을 구하기 위해, 미리 연산해둔 n-1, n-3개 때의 최소턴 결과값을 활용한다(reuse sub problems)

num = int(input())
dp=[0]*(num+1)

dp[1] = 1
dp[2] = 2
dp[3] = 1

for i in range(4,num+1):
    if dp[i-1] > dp[i-3]:
        dp[i] = dp[i-3] + 1
    else:   
        dp[i] = dp[i-1] + 1

if (dp[num] %2 == 0):
    print("CY")
else:
    print("SK")