capacity=[2, 4, 6]
filling=[2, 1, 3]
cost=[2, 5, 3]
target=max(capacity)    
# this same unbounded knapsack with variation

n=len(filling)
dp=[ 0 for j in range(target+1)] 

for j in range(1,target+1):
        dp[j]=float('inf')

for i in range(n):
    for j in range(target+1):
          if j>=filling[i] and dp[j-filling[i]]<float('inf'):
                dp[j]=min(dp[j-filling[i]]+cost[i],dp[j])
    print(dp)




