# -*- coding: utf-8 -*-
# (c) Martin Neppel 2009

print("====================================_____________________=============")
print("===== ReckonPrimer.tests/addsubsimp/test_to_str_99.py ================")

from functions import to_str_99
print("----- to_str_99 ------------------------------------------------------")

ls = to_str_99(9)
print(ls)
if ls != ['9']:
    raise Exception()

ls = to_str_99(98)
print(ls)
if ls != ['9', '8']:
    raise Exception()

ls = to_str_99(987654321)
print(ls)
if ls != ['9', '8', '7', '6', '5', '4', '3', '2', '1']:
    raise Exception()

print("===== ReckonPrimer.tests/addsubsimp/test_to_str_99.py ================")
print("=========================== SUCCESS ~~~~~~~~~~~~~~~~~~~~~ ============")
