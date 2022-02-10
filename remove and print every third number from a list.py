
nums = [10,20,30,40,50,60,70,80,90]

def remove_nums(int_list):
  #list starts with 0 index

  position = 3 - 1 
  i = 0
  len_list = (len(int_list))

  while len_list>0:
    i = (position+i)%len_list
    print(int_list.pop(i))
    len_list -= 1

remove_nums(nums)