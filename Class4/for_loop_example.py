# for x in range(10): #0,1,2,3,4,5,6,7,8,9
# #for x in range (0, 10):
#     print(x)
#
# for x in range(5, 10): # 5,6,7,8,9 (Includes 5, excludes 10)
#     print(x)
#
# #Is a range type object
# print(range(10))
#
# ## Conversion "8" -> 8
# #
# # int("8")
# #
# # str(8) -> "8"
#
# ## Conversion range to list
# print(list(range(0, 10, 2)))
#
#
# for x in range(0, 10):
#     if x==5:
#         break
#     print(x)


#Its behavior depends on what you feed it
#most popular = list, range
vowel_list=["A","E","I","O","U"]
vowel_count=0
test_string="Guillermo"
for g in test_string:
    g=g.upper()
    #if g == "A" or g=="E" or g=="I" or g=="O" or g=="U":
    if g in vowel_list:
        vowel_count+=1
print(vowel_count)

for x in range (1,101,2):
    if x!=0:
        print(x)

for x in range (1, 101):
    if x%2 == 0:
        print(x)
