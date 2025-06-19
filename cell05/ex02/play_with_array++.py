Original_array = [2,8,9,48,8,22,-12,2]
print(Original_array)
New_array = [x + 2 for x in Original_array if x > 0 and (x + 2) >5]
print(New_array)