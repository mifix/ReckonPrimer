# -*- coding: utf-8 -*-
# (c) Martin Neppel 2009

print("====================================_____________________=============")
print("===== ReckonPrimer.tests/addsubsimp/test_1_xxx.py ============")

from extimesdiv import ExTimesDiv

sett = {'topic'        : 'times_div',
         'calclines'    : 1,      # no. of lines for calc to be input.
         'MAX'          : 100,    # maximum of calcs generated;
                                  # TODO: Generate fills up by varying input.
         'MIN'          : 10,     # minimum of calcs generated 090416WN:UNUSED
         '*'            : True,   # eg.  7 . 2 =_
         '*commute'     : False,  # commute the operands 2 . 7 = _
         ':'            : False,  # 14 : 2 = _
         'in'           : False,  # 2 in 14 = _
         'remainder'    : False,  # : | in ... with remainder
         'min'          : 2,      # +: minimum number in right *operand
                                  # -: minimum result
         'max'          : 2,      # +: maximum number in right *operand
                                  # -: maximum result
         'shuffle_all'  : False,   # shuffle all calcs  
         'shuffle_inner': False,   # shuffle only 1st (inner) iteration
         'cut-max'      : True   # cut set of all calcs down to MAX
        }
ex = ExTimesDiv(None)
ex.update_setting(sett)
for _i in range(0, ex.count()):
    ca = ex.get_next_calc()
    print(ca)


print("===== ReckonPrimer.tests/addsubsimp/test_1_xxx.py ============")
print("=========================== SUCCESS ~~~~~~~~~~~~~~~~~~~~~ ============")
