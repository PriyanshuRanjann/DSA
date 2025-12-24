def median_sorted(lst1:list,lst2:list):
    final_list = []
    for i in lst1:
        final_list.append(i)
    for j in lst2:
        final_list.append(j)
    final_list.sort()
    print(final_list)
    if len(final_list) % 2 == 0:
        x = len(final_list)//2
        y = x-1
        median = (final_list[x]+final_list[y])/2
    else:
        x = len(final_list)//2
        median = final_list[x]
    return median

if __name__ =="__main__":
    lst1=eval(input("Enter list 1:"))
    lst2 = eval(input("Enter list 2:"))
    print(median_sorted(lst1,lst2))