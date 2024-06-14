start_index = int(input())
final_index = int(input())
for index in range(start_index, final_index + 1):
    if index == final_index:
        print(chr(index))
    else:
        print(chr(index), end=" ")
start_index = int(input())
final_index = int(input())
new_string = ""
for index in range(start_index, final_index + 1):
    new_string += chr(index) + " "
print(new_string.strip())
# strip - remove intervals from start and final