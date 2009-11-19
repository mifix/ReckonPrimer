# -*- coding: utf-8 -*-

import gtk
import pygtk
import pango
import random
import copy
from sugar.graphics import style

from Exercise import Exercise
from functions import *

class ExAddSimp(Exercise):
    def __init__(self, dis):
        self._title = 'template exaddsimp'
        self._display = dis
        self._sett = {'topic'  : 'addsub_simp',
         'MAX'    : 50,     # maximum of calcs generated;
                            # Generate fills up by varying input.
         'MIN'    : 20,     # minimum of calcs generated UNUSED
         'min'    : 0,      # minimum in size of a number in a calc
         'max'    : 5,      # maximum  in size of a number in a calc
                            # 0 <= min <= max <= 10
         '+'      : True,   # make all additions min..max
         '-'      : True,   # make all subtactions min..max
         '_+_=_'  : True,   # = is _right_ from operator, e.g. 1+2=3
         'input=' : [1,3,5],# list of positions in calc: 1 | 3 | 5
                            # where input is possible;
                            # actual positions chosen by Generate.
         '_=_+_'  : False,  # = is _left_ from operator, e.g. 3=1+2
         '=input' : [1,3,5],# analogous to '_+_=_'
         'shuffle': True,   # shuffle _all_ the calcs
         'cut-max': True    # cut set of all calcs down to MAX
        }

    def get_setting(self):
        return self._sett

    def get_topic(self):
        return (self._sett)['topic']

    def update_setting(self, sett):
        self._calcs = self.generate_calcs()
        self._sett = sett

    def generate_calcs(self):
        _dic = self._sett
        _calcs = []
        if _dic['+']: # '+' or '-' are True
            _c = self._alladd(_dic['min'], _dic['max'])
            if _dic['_+_=_']: # '_+_=_' or '_=_+_' are True
                # choose 1 actual position for input
                _cc = [(c, random.choice(_dic['input='])) for c in _c]
                _calcs.extend(_cc)
            if _dic['_=_+_']:
                _cc = [swap_eq(c) for c in _c]
                # choose 1 actual position for input
                _cc = [(c, random.choice(_dic['=input'])) for c in _cc]
                _calcs.extend(_cc)
        if _dic['-']:
            _c = self._allsub(_dic['min'], _dic['max'])
            if _dic['_+_=_']:
                _cc = [(c, random.choice(_dic['input='])) for c in _c]
                _calcs.extend(_cc)
            if _dic['_=_+_']:
                _cc = [swap_eq(c) for c in _c]
                _cc = [(c, random.choice(_dic['=input'])) for c in _cc]
                _calcs.extend(_cc)
        #if len(_calcs) < _dic['MIN']: TODO
        if _dic['shuffle']:
            random.shuffle(_calcs)
        if _dic['cut-max']:
            _c = copy.deepcopy(_calcs)  # make a copy
            _calcs = _c[:_dic['MAX']]
        #print('in Generate.addsub_simp calcs=', _calcs)
        return _calcs

    def format(self, (calc, linepos)):
        """format the calc for display, prepare overlays for input"""
        #@print('in Display.format_addsub_simp: calc=', (calc, linepos))#@
        _ccs = collect_digits(calc)
        print('in Display.format_addsub_simp: _ccs=',_ccs )
        _l0 = make_line(_ccs, linepos)
        _ip = make_input(_ccs, linepos)
        #@print('in Display.format_addsub_simp: return=', ([_l0], _ip)) #@
        return ([_l0], _ip)
        #return ([[' ', '1', '0', ' ', '-', ' ', '7', ' ', '=', ' ', '_', ' ']],
        #[(0, 10, '3', ' 10 - 7 = _ ', ' 10 - 7 = 3 ',
        #[' ', '1', '0', ' ', '-', ' ', '7', ' ', '=', ' ', '3', ' '])])

    def count(self):
        """TODO"""
        print('in Display.count: len=', len(self._calcs))
        return len(self._calcs)

    def define_buttons(self):
        self.toggle_shuffle = gtk.ToggleButton("@")
        self.toggle_label = self.toggle_shuffle.get_child()
        self.toggle_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_shuffle.connect("toggled", self.toggle_shuffle_callback)
        self._display.settings_table.attach(self.toggle_shuffle, 5, 6, 13, 14 )
        self.toggle_shuffle.show()

        self.toggle_equal_fixed_right = gtk.ToggleButton("<<")
        self.toggle_label = self.toggle_equal_fixed_right.get_child()
        self.toggle_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_equal_fixed_right.connect("toggled", self.toggle_equal_fixed_right_callback)
        self._display.settings_table.attach(self.toggle_equal_fixed_right, 5, 6, 10, 11 )
        self.toggle_equal_fixed_right.show()

        self.toggle_equal_fixed_left = gtk.ToggleButton("<<")
        self.toggle_label = self.toggle_equal_fixed_left.get_child()
        self.toggle_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_equal_fixed_left.connect("toggled", self.toggle_equal_fixed_left_callback)
        self._display.settings_table.attach(self.toggle_equal_fixed_left, 5, 6, 12, 13 )
        self.toggle_equal_fixed_left.show()

        self.toggle_pos1 = gtk.ToggleButton("--")
        self.toggle_label = self.toggle_pos1.get_child()
        self.toggle_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_pos1.connect("toggled", self.toggle_pos1_callback)
        self._display.settings_table.attach(self.toggle_pos1, 0, 1, 11, 12 )
        self.toggle_pos1.show()

        self.toggle_pos3 = gtk.ToggleButton("--")
        self.toggle_label = self.toggle_pos3.get_child()
        self.toggle_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_pos3.connect("toggled", self.toggle_pos3_callback)
        self._display.settings_table.attach(self.toggle_pos3, 2, 3, 11, 12 )
        self.toggle_pos3.show()

        self.toggle_pos5 = gtk.ToggleButton("--")
        self.toggle_label = self.toggle_pos5.get_child()
        self.toggle_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_pos5.connect("toggled", self.toggle_pos5_callback)
        self._display.settings_table.attach(self.toggle_pos5, 4, 5, 11, 12 )
        self.toggle_pos5.show()

        self.toggle_pos1_lower = gtk.ToggleButton("--")
        self.toggle_label = self.toggle_pos1_lower.get_child()
        self.toggle_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_pos1_lower.connect("toggled", self.toggle_pos1_lower_callback)
        self._display.settings_table.attach(self.toggle_pos1_lower, 0, 1, 13, 14 )
        self.toggle_pos1_lower.show()

        self.toggle_pos3_lower = gtk.ToggleButton("--")
        self.toggle_label = self.toggle_pos3_lower.get_child()
        self.toggle_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_pos3_lower.connect("toggled", self.toggle_pos3_lower_callback)
        self._display.settings_table.attach(self.toggle_pos3_lower, 2, 3, 13, 14 )
        self.toggle_pos3_lower.show()

        self.toggle_pos5_lower = gtk.ToggleButton("--")
        self.toggle_label = self.toggle_pos5_lower.get_child()
        self.toggle_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_pos5_lower.connect("toggled", self.toggle_pos5_lower_callback)
        self._display.settings_table.attach(self.toggle_pos5_lower, 4, 5, 13, 14 )
        self.toggle_pos5_lower.show()

        self.label0 = gtk.Label("0")
        self.label0.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label0, 0, 1, 10, 11 )
        self.label0.show()

        self.toggle_plus = gtk.ToggleButton("+")
        self.toggle_label = self.toggle_plus.get_child()
        self.toggle_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_plus.connect("toggled", self.toggle_plus_callback)
        self._display.settings_table.attach(self.toggle_plus, 1, 2, 10, 11 )
        self.toggle_plus.show()

        self.toggle_minus = gtk.ToggleButton("-")
        self.toggle_label = self.toggle_minus.get_child()
        self.toggle_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_minus.connect("toggled", self.toggle_minus_callback)
        self._display.settings_table.attach(self.toggle_minus, 1, 2, 9, 10 )
        self.toggle_minus.show()

        self.label02 = gtk.Label("0")
        self.label02.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label02, 2, 3, 10, 11 )
        self.label02.show()

        self.label_equal = gtk.Label("=")
        self.label_equal.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label_equal, 3, 4, 10, 11 )
        self.label_equal.show()

        self.label0_lower = gtk.Label("0")
        self.label0_lower.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label0_lower, 0, 1, 12, 13 )
        self.label0_lower.show()

        self.label_equal_lower = gtk.Label("=")
        self.label_equal_lower.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label_equal_lower, 1, 2, 12, 13 )
        self.label_equal_lower.show()

        self.label02_lower = gtk.Label("0")
        self.label02_lower.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label02_lower, 2, 3, 12, 13 )
        self.label02_lower.show()

        self.label_plus_minus_lower = gtk.Label("+")
        self.label_plus_minus_lower.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label_plus_minus_lower, 3, 4, 12, 13 )
        self.label_plus_minus_lower.show()

        self.label03_lower = gtk.Label("0")
        self.label03_lower.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label03_lower, 4, 5, 12, 13 )
        self.label03_lower.show()

        # Buttons 9 .. 0
        self.number_butts = []
        for i in range(0,9+1):
            self.toggle = gtk.ToggleButton(str(i))
            self.toggle_label = self.toggle.get_child()
            self.toggle_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
            self.toggle.connect("toggled", self.toggle_number_callback, i)
            self._display.settings_table.attach(self.toggle, 4, 5, 10-i, 11-i)
            self.toggle.show()
            self.number_butts.append(self.toggle)

    def set_buttons(self, sett):

        for i in range(sett['min'],sett['max']+1):
            self.number_butts[i].set_active(True)

        if ( sett['+'] == True ):
            self.toggle_plus.set_active(True)
        else:
            self.toggle_plus.set_active(False)

        if ( sett['-'] == True ):
            self.toggle_minus.set_active(True)
        else:
            self.toggle_minus.set_active(False)

        if ( sett['shuffle'] == True ):
            self.toggle_shuffle.set_active(True)
        else:
            self.toggle_shuffle.set_active(False)

        if ( sett['_+_=_'] == True ):
            self.toggle_equal_fixed_right.set_active(True)
        else:
            self.toggle_equal_fixed_right.set_active(False)

        if ( sett['_=_+_'] == True ):
            self.toggle_equal_fixed_left.set_active(True)
        else:
            self.toggle_equal_fixed_left.set_active(False)

        for i in sett['input=']:
            if( i == 1 ):
                self.toggle_pos1.set_active(True)
            if ( i == 3 ):
                self.toggle_pos3.set_active(True)
            if ( i == 5 ):
                self.toggle_pos5.set_active(True)

        for i in sett['=input']:
            if( i == 1 ):
                self.toggle_pos1_lower.set_active(True)
            if ( i == 3 ):
                self.toggle_pos3_lower.set_active(True)
            if ( i == 5 ):
                self.toggle_pos5_lower.set_active(True)

    #**** callbacks ********************************************************

    def toggle_number_callback(self, widget, i):

        if widget.get_active():
            if(i < self._display._sett['min']):
                self._display._sett['min'] = i
                self.set_buttons(self._display._sett)
            elif( i > self._display._sett['max'] ):
                self._display._sett['max'] = i
                self.set_buttons(self._display._sett)

        else:
            if( i == self._display._sett['min'] ):
                if( self._display._sett['min'] == self._display._sett['max'] ):
                    widget.set_active(True)
                else:
                    self._display._sett['min'] = i+1
                self.set_buttons(self._display._sett)

            elif( i == self._display._sett['max'] ):
                if( self._display._sett['min'] == self._display._sett['max'] ):
                    widget.set_active(True)
                else:
                    self._display._sett['max'] = i-1
                self.set_buttons(self._display._sett)

            else:
                widget.set_active(True)

    # callbacks updating the settings
    def toggle_plus_callback(self, widget):
        if widget.get_active():
            self._display._sett['+'] = True
        else:
            if( self.toggle_minus.get_active() ):
                self._display._sett['+'] = False
            else:
                widget.set_active(True)

    def toggle_minus_callback(self, widget):
        if widget.get_active():
            self._display._sett['-'] = True
        else:
            if( self.toggle_plus.get_active() ):
                self._display._sett['-'] = False
            else:
               widget.set_active(True)

    def toggle_shuffle_callback(self, widget):
        if widget.get_active():
            self._display._sett['shuffle'] = True
        else:
            self._display._sett['shuffle'] = False

    def toggle_equal_fixed_right_callback(self, widget):
        if widget.get_active():
            self._display._sett['_+_=_'] = True
            self.toggle_pos1.set_active(True)
            self.toggle_pos3.set_active(True)
            self.toggle_pos5.set_active(True)
        else:
            if( self.toggle_equal_fixed_left.get_active() ):
                self._display._sett['_+_=_'] = False
                self.toggle_pos1.set_active(False)
                self.toggle_pos3.set_active(False)
                self.toggle_pos5.set_active(False)
            else:
                widget.set_active(True)

    def toggle_equal_fixed_left_callback(self, widget):
        if widget.get_active():
            self._display._sett['_=_+_'] = True
            self.toggle_pos1_lower.set_active(True)
            self.toggle_pos3_lower.set_active(True)
            self.toggle_pos5_lower.set_active(True)
        else:
            if( self.toggle_equal_fixed_right.get_active() ):
                self._display._sett['_=_+_'] = False
                self.toggle_pos1_lower.set_active(False)
                self.toggle_pos3_lower.set_active(False)
                self.toggle_pos5_lower.set_active(False)
            else:
                widget.set_active(True)

    def toggle_pos1_callback(self, widget):

        if( self.toggle_equal_fixed_right.get_active() ):
            pass
        else:
            self.toggle_pos1.set_active(False)

        if( self.toggle_pos1.get_active() ):
            self._display._sett['input='] = list(set(self._display._sett['input=']) | set([1]))
        else:
            if( self.toggle_equal_fixed_right.get_active() ):
                if( not self.toggle_pos3.get_active() and not self.toggle_pos5.get_active() ):
                    self.toggle_pos1.set_active(True)
                else:
                    self._display._sett['input='] = list(set(self._display._sett['input=']) - set([1]))

    def toggle_pos3_callback(self, widget):
        if( self.toggle_equal_fixed_right.get_active() ):
            pass
        else:
            self.toggle_pos3.set_active(False)

        if( self.toggle_pos3.get_active() ):
            self._display._sett['input='] = list(set(self._display._sett['input=']) | set([3]))
        else:
            if( self.toggle_equal_fixed_right.get_active() ):
                if( not self.toggle_pos1.get_active() and not self.toggle_pos5.get_active() ):
                    self.toggle_pos3.set_active(True)
                else:
                    self._display._sett['input='] = list(set(self._display._sett['input=']) - set([3]))

    def toggle_pos5_callback(self, widget):
        if( self.toggle_equal_fixed_right.get_active() ):
            pass
        else:
            self.toggle_pos5.set_active(False)

        if( self.toggle_pos5.get_active() ):
            self._display._sett['input='] = list(set(self._display._sett['input=']) | set([5]))
        else:
            if( self.toggle_equal_fixed_right.get_active() ):
                if( not self.toggle_pos1.get_active() and not self.toggle_pos3.get_active() ):
                    self.toggle_pos5.set_active(True)
                else:
                    self._display._sett['input='] = list(set(self._display._sett['input=']) - set([5]))

    def toggle_pos1_lower_callback(self, widget):

        if( self.toggle_equal_fixed_left.get_active() ):
            pass
        else:
            self.toggle_pos1_lower.set_active(False)

        if( self.toggle_pos1_lower.get_active() ):
            self._display._sett['=input'] = list(set(self._display._sett['=input']) | set([1]))
        else:
            if( self.toggle_equal_fixed_left.get_active() ):
                if( not self.toggle_pos3_lower.get_active() and not self.toggle_pos5_lower.get_active() ):
                    self.toggle_pos1_lower.set_active(True)
                else:
                    self._display._sett['=input'] = list(set(self._display._sett['=input']) - set([1]))

    def toggle_pos3_lower_callback(self, widget):
        if( self.toggle_equal_fixed_left.get_active() ):
            pass
        else:
            self.toggle_pos3_lower.set_active(False)

        if( self.toggle_pos3_lower.get_active() ):
            self._display._sett['=input'] = list(set(self._display._sett['=input']) | set([3]))
        else:
            if( self.toggle_equal_fixed_left.get_active() ):
                if( not self.toggle_pos1_lower.get_active() and not self.toggle_pos5_lower.get_active() ):
                    self.toggle_pos3_lower.set_active(True)
                else:
                    self._display._sett['=input'] = list(set(self._display._sett['=input']) - set([3]))

    def toggle_pos5_lower_callback(self, widget):
        if( self.toggle_equal_fixed_left.get_active() ):
            pass
        else:
            self.toggle_pos5_lower.set_active(False)

        if( self.toggle_pos5_lower.get_active() ):
            self._display._sett['=input'] = list(set(self._display._sett['=input']) | set([5]))
        else:
            if( self.toggle_equal_fixed_left.get_active() ):
                if( not self.toggle_pos1_lower.get_active() and not self.toggle_pos3_lower.get_active()):
                    self.toggle_pos5_lower.set_active(True)
                else:
                    self._display._sett['=input'] = list(set(self._display._sett['=input']) - set([5]))

    ##### end of public methods ############################################
    def _alladd(self, min, max):
        """generate all calcs for +"""
        _adds = []
        for _i in range(min, max +1):
            for _j in range(0, _i +1):
                #print("in Generate._alladd i= ",_i,"  j= ", _j)
                _c = [to_str_99(_j),'+',to_str_99(_i-_j),'=',to_str_99(_i)]
                _c = flatten(_c)
                _c = strip(_c, '#')
                _adds.append(_c)
                #print("in Generate._alladd adds= ", _adds)
        return _adds

    def _allsub(self, min, max):
        """generate all calcs for -"""
        _subs = []
        for _i in range(min, max +1):
            for _j in range(0, _i +1) :
                #print ("in Generate._allsub i= ",_i,"  j= ", _j)
                _c = [to_str_99(_i), '-', to_str_99(_j), '=', to_str_99(_i - _j)]
                _c = flatten(_c)
                _c = strip(_c, '#')
                _subs.append(_c)
        return _subs

