def factorial(x):
    dp = [0] * (x + 1)
    dp[0] = dp[1] = 1
    
    if x <= 1:
        return 1
    else:
        for i in range(2, x + 1):
            dp[i] = i * dp[i - 1]
        return dp[x]
        
print(factorial(int(input())))