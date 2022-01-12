#
# items = [1,2,3,56,8,9,10]
# price = [1,2,3,4,5,6,7]
#
# x_ij = 1  item i is in bag j
# ======0
#
# y_j = binary 1 bag j is used
#
#
# min sum(y_j)
#
# x_ij*(w_i) <= W_j*y_j
# //x_ij <= M*y_j
# sum_j x_ij == 1
#
#
# BnB
#
# 15% 1 plane in 5 minutes
# at least
# lamb = 1/5
# .15^6
# e(1/5)^6
#
#
# prob of getting 5 tails by fair coin = (1/2)^5
# prob of getting 5 tails unfair = 1
#
# 1/2
# -------
# 1/2*1+1/2*(1/2)^5