def plusMinus(arr):
    # Write your code here
    positive = 0
    negative = 0
    zeros = 0
    
    arrSize = len(arr)
    
    # print(arrSize)
    
    for i in arr:
        if i < 0:
            negative += 1
        elif i > 0:
            positive += 1
        else:
            zeros += 1
            
    # print(zeros, " ", negative, " ", positive)
    
    print("{:.6f}".format(positive/arrSize))
    print("{:.6f}".format(negative/arrSize))
    print("{:.6f}".format(zeros/arrSize))
    
            