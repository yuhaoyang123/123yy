#冒泡排序
x = [5,4,6,3,8,9,1]
def Bubble_sort(x):
    for i in range(len(x)):
        for j in range(i,len(x)):
            if x[i] > x[j]:
                x[i],x[j] = x[j],x[i]
    return x
print(Bubble_sort(x))




