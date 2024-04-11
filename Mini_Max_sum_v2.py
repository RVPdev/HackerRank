def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    minSum = sum(arr) - arr[-1]
    maxSum = sum(arr) - arr[0]
    
    print(minSum,maxSum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)