import array as arr
arr_num=arr.array('i',[1,2,3,4,5,6,7,8,9])
print(f"The original array is: {str(arr_num)}")
#count occurences of "3"
print(f"The number '3' occurs {str(arr_num.count(3))} time")