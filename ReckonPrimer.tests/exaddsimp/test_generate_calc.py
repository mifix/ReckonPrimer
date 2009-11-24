# -*- coding: utf-8 -*-

print("====================================_____________________=============")
print("===== ReckonPrimer.tests/addsubsimp/test_generate_calc.py ============")

from exaddsimp import ExAddSimp

_ex = ExAddSimp(None)
_calc = _ex.get_next_calc()
print('calc=',_calc)
_calc = _ex.get_next_calc()
print('calc=',_calc)
_calc = _ex.get_next_calc()
print('calc=',_calc)

print("===== ReckonPrimer.tests/addsubsimp/test_generate_calc.py ============")
print("=========================== SUCCESS ~~~~~~~~~~~~~~~~~~~~~ ============")


