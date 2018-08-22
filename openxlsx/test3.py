def binary_search(list,target):
    #判断入参是否合格
    if not list or not target:
        print("wrong input")
        return -1
    #二分查找逻辑
    low = 0;
    high = len(list) - 1
    while(low <= high):
        mid = int((low + high)/2)
        item = list[mid]
        if item < target:
            low = mid + 1
        elif item > target:
            high = mid -1
        elif item == target:
            return list.index(item)
        else:
            return None

list = [1,2,2,4,5,5]
finding = binary_search(list, 5)
print(finding)

def bubble_sort(lists):
    # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i] > lists[j]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists
result = bubble_sort([3,2,1,9,4])
print(result)