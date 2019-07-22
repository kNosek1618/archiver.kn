
# score = 630
#
# for i in range(2,15,2):
#     print(i)
#     score += i
#
# print('\n')
# print(score)
# print("\n")

# 56 = 14




input = 999000
check = 0
iter = -1
dif = 0


for a in range(2,10000000000000,2):
    check += a
    iter += 1
    if check > input:
        iter *= 2
        check -= a
        dif = input - check
        break

print(f"archive of  {input} take {iter} and a child {dif}")

