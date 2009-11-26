# -*- coding: utf-8 -*-
#(c) Walther Neuper 2009

print("==================================_____________________===============")
print("===== ReckonPrimer.tests/timesdiv/test_exercise_format.py ============")

#WN091116 Exercise <10> does not generate calculations
#      with settings "1+2  <" OFF
#Traceback (most recent call last):
#  File "/home/neuper/Activities/ReckonPrimer.activity/display.py", line 251, in clicked_start_callback
#    self._co.notify(('setting-done', self._sett))
#  File "/home/neuper/Activities/ReckonPrimer.activity/coach.py", line 90, in notify
#    self._sess.notify((msg, self._ex))
#  File "/home/neuper/Activities/ReckonPrimer.activity/session.py", line 39, in notify
#    _lines, self._input = data.format(_calc)
#  File "/home/neuper/Activities/ReckonPrimer.activity/expassten.py", line 52, in format
#    return Exercise.format_addsub_simp((cs, linepos))
#TypeError: unbound method format_addsub_simp() must be called with Exercise instance as first argument (got tuple instance instead)
#===== correction ============================================================
# in expassten.py:
#   return Exercise.format_addsub_simp((cs, linepos))
#-->return self.format_addsub_simp((cs, linepos))

from expassten import ExPassTen
_ex = ExPassTen(None) #need no Display for this test
_sett = {'cut-max': True, 'newline': False, 'MIN': 10, 'shuffle_all': False, 'MAX': 150, '+': True, 'min': 2, '-': False, 'topic': 'passten', 'calclines': 1, 'max': 2, 'input': [5], 'shuffle_inner': False} #copied from logs
_ex.update_setting(_sett)
print("in test_exercise_format.py: _ex._sett=", _ex.get_setting())
for _i in range(0, _ex.count()):
    _calc = _ex.get_next_calc()
    print("in test_exercise_format.py: _calc=", _calc)
    print("in test_exercise_format.py: format(calc)=",_ex.format(_calc))
    if _i == 0 and (not _calc == (['2', '+', '9', '=', '1', '1'], None, 5)):
        raise Exception()
    if _i == 1 and (not _calc == (['2', '+', '8', '=', '1', '0'], None, 5)):
        raise Exception()

print("===== ReckonPrimer.tests/timesdiv/test_exercise_format.py ============")
print("========================= SUCCESS ~~~~~~~~~~~~~~~~~~~~~~~=============")


