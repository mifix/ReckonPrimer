# -*- coding: utf-8 -*-
"""the module for functions of reckonprimer.py.
placed in reconprimer.py caused recursive import."""
import copy
def reverse_(list):
    """list.reverse() returns None; reverse_ returns the reversed list"""
    li = copy.deepcopy(list[3:5])  # make a copy
    li.reverse()
    del list[3:5]
    list = (li + list)
    return list
    
def get_until(char, chars):
    _i, _chars = 0, []
    while chars[_i] != char:
        #print('in get_until, chars[', _i, ']=', chars[_i])
        _chars.append(chars[_i])
        _i = _i + 1
    return _chars
    
def get_after(char, chars):
    _i, _chars, _max = 0, [], len(chars)
    while (chars[_i] != char) & (_i < _max):
        print('in get_after, chars[', _i, ']=', chars[_i])
        _i = _i + 1
    return chars[_i+1:]

def extend_(chars1, chars2):
    _chars = copy.deepcopy(chars1)  # make a copy
    _chars.extend(chars2)
    return _chars 

def swap_eq(chars):
    _i, _chars = 0, []
    while chars[_i] != '=':
        #print('in swap_eq chars[', _i, ']=', chars[_i])
        _chars.append(chars[_i])
        _i = _i + 1
    return extend_(extend_(chars[_i+1:], ['=']), _chars)
    
#_c = ['2','+','3','=','5']
#print('_c      =', _c)
#_c1 = get_until('=', _c)
#print('get_until', _c1)
#_c2 = get_after('=', _c)
#print('get_after', _c2)
#_c3 = extend_(_c1, _c2)
#print('extend_  ', _c3)
#_c4 = swap_eq(_c)
#print('swap_eq  ', _c4)

def contain(chars, char):
    """do chars (list of characters) contain char ?"""
    if len(chars) > 0:
        for _c in chars:
            if _c == char:
                return True
        else:
            return False
    else:
        return False
#chrs = ['2','+','3',\
#        '=','5']
#print('contain([\'2\',\'+\',\'3\',\'=\',\'5\'], \'+\')', contain(chrs, '+'))
#print('contain([\'2\',\'+\',\'3\',\'=\',\'5\'], \'-\')', contain(chrs, '-'))

def make_blanks(n):
    """create a list of n blanks"""
    _l = []
    for i in range(0, n):
        _l.append(' ')
    return _l
#xxx = make_blanks(3)
#print(xxx)
#xxx[1]='+'
#print(xxx)

#ls = [11,22,33]
#[a,b,c] = ls
#print('in functions: a=',a,', b=',b,', c=',c)
def collect_digits(calc):
    """collect the digits of each number in a calc into a list"""
    _coll_calc, _i = [], 0
    while _i < len(calc):
        _coll_no = []
        while not(calc[_i] in ['=','+','-','*',':','in','|']):
            _coll_no.append(calc[_i])
            #print('in collect_digits: _coll_calc=',_coll_calc,', _i=',_i,\
            #      ', _coll_no=',_coll_no)
            _i = _i+1
            if _i >= len(calc):
                _coll_calc.append(_coll_no)
                return _coll_calc
        _coll_calc.append(_coll_no)
        _coll_calc.append(calc[_i])
        _i = _i+1
#cs = collect_digits(['1','2','+','3','4','=','4','6'])
#print('in functions: cs=', cs)
##('in functions: cs=', [['1', '2'], '+', ['3', '4'], '=', ['4', '6']])
#cs = collect_digits(['1','+','2','=','3'])
#print('in functions: cs=', cs)
##('in functions: cs=', [['1'], '+', ['2'], '=', ['3']])

def make_line(coll_calc, linepos):
    """make a calc (returned by collect_digits) to a line to display;
    linepos is 1 or 3 or 5."""
    _i, _line = 0, [' ']
    for _c in coll_calc:
        #print('in make_line: _c=', _c)
        if _i == linepos -1:
            for _d in _c:
                _line.append('_')
        else:
            for _d in _c:
                #print('in make_line: _d=', _d)
                if _d in ['=','+','-','*',':','in']:
                    _line.extend([' ',_d,' '])
                else:
                    _line.append(_d)
        _i = _i + 1
    _line.append(' ')
    return _line
#coll_calc = [['1', '2'], '+', ['3', '4'], '=', ['4', '6']]
#print('in functions: make_line(coll_calc, 1)=', make_line(coll_calc, 1))
##[' ', '_', '_', ' ', '+', ' ', '3', '4', ' ', '=', ' ', '4', '6', ' ']
#print('in functions: make_line(coll_calc, 3)=', make_line(coll_calc, 3))
##[' ', '1', '2', ' ', '+', ' ', '_', '_', ' ', '=', ' ', '4', '6', ' ']
#print('in functions: make_line(coll_calc, 5)=', make_line(coll_calc, 5))
##[' ', '1', '2', ' ', '+', ' ', '3', '4', ' ', '=', ' ', '_', '_', ' ']
#coll_calc = [['1'], '+', ['2'], '=', ['3']]
#print('in functions: make_line(coll_calc, 1)=', make_line(coll_calc, 1))
##[' ', '_', ' ', '+', ' ', '2', ' ', '=', ' ', '3', ' ']
#print('in functions: make_line(coll_calc, 3)=', make_line(coll_calc, 3))
##[' ', '1', ' ', '+', ' ', '_', ' ', '=', ' ', '3', ' ']
#print('in functions: make_line(coll_calc, 5)=', make_line(coll_calc, 5))
##[' ', '1', ' ', '+', ' ', '2', ' ', '=', ' ', '_', ' ']


def make_line_remainder(coll_calc):
    """make a calc (returned by collect_digits) to a line to display"""
    _i, _line = 0, [' ']
    for _c in coll_calc:
        if _i == 4 or _i == 6:
            for _d in _c:
                #print('in make_line_remainder: _c, _d=', _c, _d)
                _line.append('_')
        else:
            if _c == 'in':
                _line.extend([' ',_c,' '])
            else:
                for _d in _c:
                    #print('in make_line: _c, _d=', _c, _d)
                    if _d in ['=','+','-','*',':']: #not '|'
                        _line.extend([' ',_d,' '])
                    else:
                        _line.append(_d)
        _i = _i + 1
    _line.append(' ')
    return _line
#coll_calc = [['2'], 'in', ['2'], '=', ['1'], '|', ['0']]
#print(make_line_remainder(coll_calc))


def make_input(coll_calc, linepos):
    """make a list of inputs formatted for Display in one line.
    take car of 'in' from times_div"""
    _indig_cnt, _ins = 0, []
    for _indig in coll_calc[linepos-1]:
        _c_cnt, _inline, _in_idx, _in_ahead = 0, [' '], 1, True
        for _c in coll_calc: #build 1 line (see make_line)
            #print('in make_input: _c_cnt=', _c_cnt,', _c=',_c)
            if _c_cnt == linepos-1:
                _d_cnt = 0
                for _d in _c:
                    #print('in make_input:     _d_cnt=',_d_cnt,', _d=',_d)
                    if _indig_cnt >= _d_cnt:
                        _inline.append(_d)
                        _in_ahead = False
                        #_in_idx = _in_idx + 1
                    else:
                        _inline.append('_')
                    _d_cnt = _d_cnt + 1
            else:
                if _c == 'in':
                    _inline.extend([' ',_c,' '])
                    if _in_ahead:
                            _in_idx = _in_idx + 3
                else:
                    for _d in _c:
                        #print('in make_input: _d=', _d)
                        if _d in ['=','+','-','*',':','in']:
                            _inline.extend([' ',_d,' '])
                            if _in_ahead:
                                _in_idx = _in_idx + 3
                        else:
                            _inline.append(_d)
                            if _in_ahead:
                                _in_idx = _in_idx + 1
            _c_cnt = _c_cnt + 1
        _inline.append(' ')
        _idx = _in_idx + _indig_cnt
        _indig = coll_calc[linepos-1][_indig_cnt]
        _prot_err = copy.deepcopy(_inline)
        _prot_err[_idx] = '_'
        _in = (0, _idx, _indig, \
               ''.join(_prot_err), ''.join(_inline), \
               _inline)
        _ins.append(_in)
        _indig_cnt = _indig_cnt + 1
    _ins.reverse() #for pop
    return _ins
####################################################################
#ins = make_input([['1','2','3'], '+', ['4'], '=', ['1','2','7']], 5)
#print(ins)
#[(0, 13, '7', ' 123 + 4 = 12_ ', ' 123 + 4 = 127 ',
#  [' ', '1', '2', '3', ' ', '+', ' ', '4', ' ', '=', ' ', '1', '2', '7',' ']),
# (0, 12, '2', ' 123 + 4 = 1__ ', ' 123 + 4 = 12_ ',
#  [' ', '1', '2', '3', ' ', '+', ' ', '4', ' ', '=', ' ', '1', '2', '_',' ']),
# (0, 11, '1', ' 123 + 4 = ___ ', ' 123 + 4 = 1__ ',
#  [' ', '1', '2', '3', ' ', '+', ' ', '4', ' ', '=', ' ', '1', '_', '_',' '])]
#ins = make_input([['1'], '*', ['2'], '=', ['2']], 5)
#print(ins)
#[(0, 9, '2', ' 1 * 2 = _ ', ' 1 * 2 = 2 ',
#  [' ', '1', ' ', '*', ' ', '2', ' ', '=', ' ', '2', ' '])]


def make_input_remainder(strs, res, rem):
    """make the 2 lines for input result and remainder with ':' and 'in'"""
    #print('in make_input_remainder: len(strs)=', len(strs))
    #print('in make_input_remainder: strs=', strs)
    #print('in make_input_remainder: res=', res, ', rem=', rem)
    _strs = copy.deepcopy(strs)
    if len(_strs) == 13: # 9 : 2 = 4|1
        _line1 = copy.deepcopy(_strs)
        _strs[9] = res[0]
        _line2 = copy.deepcopy(_strs)
        _strs[11] = rem[0]
        _line3 = copy.deepcopy(_strs)
        #print('in make_input_remainder: line1,2,3=', _line1, _line2, _line3)
        _ins = [(0,  9, res[0], "".join(_line1), "".join(_line2), _line2),\
                (0, 11, rem[0], "".join(_line2), "".join(_line3), _line3)]
    elif len(_strs) == 14: # 17 : 2 = 8|1
        _line1 = copy.deepcopy(_strs)
        _strs[10] = res[0]
        _line2 = copy.deepcopy(_strs)
        _strs[12] = rem[0]
        _line3 = copy.deepcopy(_strs)
        _ins = [(0, 10, res[0], "".join(_line1), "".join(_line2), _line2),\
                (0, 12, rem[0], "".join(_line2), "".join(_line3), _line3)]
    elif len(_strs) == 15: # 20 : 2 = 10|0
        _line1 = copy.deepcopy(_strs)
        _strs[10] = res[0]
        _line2 = copy.deepcopy(_strs)
        _strs[11] = res[1]
        _line3 = copy.deepcopy(_strs)
        _strs[13] = rem[0]
        _line4 = copy.deepcopy(_strs)
        _ins = [(0, 10, res[0], "".join(_line1), "".join(_line2), _line2),\
                (0, 11, res[1], "".join(_line2), "".join(_line3), _line3),\
                (0, 13, rem[0], "".join(_line3), "".join(_line4), _line4)]
    else:
        print('in make_input_remainder: ERROR len(_strs)=', len(_strs))
        #exit
    _ins.reverse() # for pop()
    return _ins
#strs = [' ', '9', ' ', ':', ' ', '2', ' ', '=', ' ', '_', '|', '_', ' ']
#print(make_input_remainder(strs, ['4'], ['1']))
#[(0, 9, '4', ' 9 : 2 = _|_ ', ' 9 : 2 = 4|_ ',
#  [' ', '9', ' ', ':', ' ', '2', ' ', '=', ' ', '4', '|', '_', ' ']),
# (0, 11, '1', ' 9 : 2 = 4|_ ', ' 9 : 2 = 4|1 ',
#  [' ', '9', ' ', ':', ' ', '2', ' ', '=', ' ', '4', '|', '1', ' '])]
#strs = [' ', '1','7', ' ', ':', ' ', '2', ' ', '=', ' ', '_', '|', '_', ' ']
#print(make_input_remainder(strs, ['8'], ['1']))
#[(0, 10, '8', ' 17 : 2 = _|_ ', ' 17 : 2 = 8|_ ',
#  [' ', '1', '7', ' ', ':', ' ', '2', ' ', '=', ' ', '8', '|', '_', ' ']),
# (0, 12, '1', ' 17 : 2 = 8|_ ', ' 17 : 2 = 8|1 ',
#  [' ', '1', '7', ' ', ':', ' ', '2', ' ', '=', ' ', '8', '|', '1', ' '])]
#strs = [' ','2','0',' ',':',' ','2',' ','=',' ','_','_','|','_',' ']
#print(make_input_remainder(strs, ['1','0'], ['0']))
#[(0, 10, '1', ' 20 : 2 = __|_ ', ' 20 : 2 = 1_|_ ',
#  [' ', '2', '0', ' ', ':', ' ', '2', ' ', '=', ' ', '1', '_', '|', '_',' ']),
# (0, 11, '0', ' 20 : 2 = 1_|_ ', ' 20 : 2 = 10|_ ',
#  [' ', '2', '0', ' ', ':', ' ', '2', ' ', '=', ' ', '1', '0', '|', '_',' ']),
# (0, 13, '0', ' 20 : 2 = 10|_ ', ' 20 : 2 = 10|0 ',
#  [' ', '2', '0', ' ', ':', ' ', '2', ' ', '=', ' ', '1', '0', '|', '0',' '])]

def strip(chars, c):
    """strip all characters c from a list of characters chars"""
    _cs = []
    for _c in chars:
        if _c != c:
            _cs.append(_c)
    return _cs
#print(strip(['1','2','3','0','4','0'], '0'))
#['1', '2', '3', '4']

def to_str_99(i):
    """ Convert a number to their list of digits (as characters). """
    _digs = []
    _lead, _dig = divmod(i, 10)
    _digs.append(str(_dig))
    while _lead > 9:
        _lead, _dig = divmod(_lead, 10)
        _digs.append(str(_dig))
    if _lead > 0:
        _digs.append(str(_lead))
    _digs.reverse()
    return _digs

def flatten(ls):
    """flatten a list of lists; only one level"""
    _flat = []
    for _e in ls:
        if _e == 'in':
            _flat.append(_e)
        else:
            for _ei in _e:
                #print(_e, '  ', _ei)
                _flat.append(_ei)
    return _flat
#print(flatten([['1', '2'], '+', ['3', '4'], '=', ['4', '6']]))
#['1', '2', '+', '3', '4', '=', '4', '6']
#print(flatten([['2'], 'in', ['2', '0'], '=', ['1', '0'], '|', ['0']]))
#['2', 'in', '2', '0', '=', '1', '0', '|', '0']
