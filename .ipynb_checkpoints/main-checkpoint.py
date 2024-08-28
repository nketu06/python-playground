# arr=[1,2,3,4,5,6,7]
# start=0
# end=len(arr)-1
# while start<=end:
#     arr[start],arr[end]=arr[end],arr[start]
#     start+=1
#     end-=1
# print(arr)


# using for loop
# arr=[1,2,3,4,5,6,7,8]
# n=len(arr)
# mid=n//2
# for i in range(mid):
#     start=i
#     end=(n-1)-i
#     arr[start],arr[end]=arr[end],arr[start]
# print(arr)


# # code for const and vol
# vowel={'a','e','i','o','u'}

# s='jakhieuyrjbnmvaeo'
# count_v=0
# count_c=0

# for each in s:
#     if each in vowel:
#         count_v+=1
#         print(each,"vowel")
#     else:
#         count_c+=1
#         print(each,"const")
# print(count_c,count_v)


# number=3885381
# ans=0
# while number>0:
#     rem=number%10
#     ans+=rem
#     number=number//10
# print(ans)

dict={1:'a',2:'b',3:'c'}

# for key in dict:
#     print(key)
#     print(dict[key])

# for key,val in dict.items():
#     print(key,val)
    
# for val in dict.values():
#     print(val)

# del dict[2]
# print(dict)

# print(dict.get(4,0))
# print(dict[4])

# s='iiogajkalk'
# freq={}
# for each in s:
#     freq[each]=freq.get(each,0)+1
# print(freq)

# s=set()
# s.add('a')
# s.add('b')
# s.add('c')
# # print(s)

# # s.remove('a')
# # print(s)

# for each in s:
#     print(each)
