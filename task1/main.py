def selection_sort(nums, lesser):
    for b in list(nums):
        if b < lesser:
            nums.remove(b)   #deleted numbers from list which les than lesser
    nums.sort(reverse=True)  #function sort with reverse = True expands the list
    return nums


random_list_of_nums = [12, 8, 3, 20, 11]
print(selection_sort(random_list_of_nums, 10))
