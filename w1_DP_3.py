# LCS (no.9251)

# idea
# 현재 비교쌍까지의 lcs를 계산하기 위해, 이전에 연산해둔 비교쌍들의 lsc 결과를 활용한다.
# 현재 비교하는 인덱스가  dp[i][j]일때 (str1[i-1], str2[j-1] -> dp 테이블은 인덱스 1부터 시작한다고 가정)
# 비교 문자열 같을때: 왼쪽/위 중에서  max 
    # 왼쪽: c[i][j-1] 
    # 위쪽: c[i-1][j] 
    # 위의 2가지 케이스 중에서, 최대의 공통 부분 수열의 개수를 구함. 

# 비교 문자열이 다를때: 왼쪽 대각선 위의 값 + 1
    # c(i,j) = c(i-1, j-1) + 1
    # 현재쌍은 같기 때문에, 각 문자열에서 현재쌍을 제외했을때까지의 최대 공통 부분 수열 개수 => c(i-1, j-1)
    # 위의 값에서 현재쌍까지 lcs에 포함해야 하므로 +1

# 풀이 : success(56548KB, 376ms)
def get_lcs():
    str1 = input()
    str2 = input()
    len_str1 = len(str1)
    len_str2 = len(str2)

    lcs = [[0 for i in range(len_str2+1)]for j in range(len_str1+1)]

    for i in range(1,len_str1+1,1):
        for j in range(1, len_str2+1,1): 
            if (str1[i-1] == str2[j-1]):
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])


    return lcs[len_str1][len_str2]

print(get_lcs())
