# target_height = int(input())
#
# successful = True
# practice_height = target_height - 30
#
# consecutive_fails = 0
# jumps = 0
#
# while True:
#     jump = int(input())
#     jumps += 1
#
#     if jump <= practice_height:
#         consecutive_fails += 1
#     else:
#         consecutive_fails = 0
#         if practice_height < target_height:
#             practice_height += 5
#         else:
#             practice_height = target_height
#
#     if consecutive_fails == 3:
#         successful = False
#         break
#     elif jump > target_height:
#         break
#
# if successful:
#     print(f"Tihomir succeeded, he jumped over {practice_height}cm after {jumps} jumps.")
# else:
#     print(f"Tihomir failed at {practice_height}cm after {jumps} jumps.")


target_height = int(input())
practice_height = target_height - 30

fails_in_row = 0
jumps = 0
success = False

while True:
    jump_height = int(input())
    jumps += 1
    if (jump_height > practice_height) and (practice_height != target_height):
        practice_height += 5
        fails_in_row = 0
    elif (jump_height > practice_height) and (practice_height == target_height):
        success = True
        fails_in_row = 0
        break
    else:
        fails_in_row += 1

    if fails_in_row == 3:
        success = False
        break

if success:
    print(f"Tihomir succeeded, he jumped over {practice_height}cm after {jumps} jumps.")
else:
    print(f"Tihomir failed at {practice_height}cm after {jumps} jumps.")





