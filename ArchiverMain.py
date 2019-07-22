
# score = 0
#
# for i in range(2,15,2):
#     print(i)
#     score += i
#
# print('\n')
# print(score)
# print("\n")

# 56 = 14




score = 4
check = 0
iter = -1
dif = 0


for a in range(2,1000,2):
    check += a
    iter += 1
    if check > score:
        iter *= 2
        check -= a
        dif = score - check
        break

print(f"kompresja liczby {score} daje liczbe matke {iter} oraz potomna {dif}")

