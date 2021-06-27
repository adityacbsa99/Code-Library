def cat(n):
  dp=[0]*n
  dp[0]=1
  dp[1]=1
  res=0
  for i in range(2,n):
    for j in range(i):
      dp[i]= dp[i] + (dp[j] * dp[i-j-1])
  return dp

print(cat(5))