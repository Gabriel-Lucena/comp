quantity = int(input())
user_input = input()

vector_strings = user_input.split()
int_list = []

for i_list_input in vector_strings:
    int_list.append(int(i_list_input))

int_list.sort()

expected_number = 1

for i_list_input in int_list:
  
  if i_list_input != expected_number:
    missing_number = expected_number
    break
  
  expected_number += 1

print(missing_number)

