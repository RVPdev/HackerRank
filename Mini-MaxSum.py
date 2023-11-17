def miniMaxSum(arr):
    # Write your code here
    arr.sort()      
    minSum = sum(arr[0:4])
    maxSum = sum(arr[1:5])
    
    print(f"{minSum} {maxSum}")

if __name__ == '__main__':

    # arr = list(map(int, input().rstrip().split()))
    arr = [5, 5, 5, 5, 5]

    miniMaxSum(arr)