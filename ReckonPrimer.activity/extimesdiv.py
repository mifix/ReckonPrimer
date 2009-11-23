# -*- coding: utf-8 -*-

import gtk
import pygtk
import pango
import random
import copy
from sugar.graphics import style

from Exercise import Exercise
from functions import *

class ExTimesDiv(Exercise):
    def __init__(self, dis):
        self._title = 'template extimesdiv'
        self._display = dis
        self._sett = {'topic'        : 'times_div',
         'calclines'    : 1,      # no. of lines for calc to be input.
         'MAX'          : 100,    # maximum of calcs generated;
                                  # TODO: Generate fills up by varying input.
         'MIN'          : 10,     # minimum of calcs generated 090416WN:UNUSED
         '*'            : True,   # eg.  7 . 2 =_
         '*commute'     : True,  # commute the operands 2 . 7 = _
         ':'            : False,  # 14 : 2 = _
         'in'           : False,  # 2 in 14 = _
         'remainder'    : False,  # : | in ... with remainder
         'min'          : 2,      # +: minimum number in right *operand
                                  # -: minimum result
         'max'          : 2,      # +: maximum number in right *operand
                                  # -: maximum result
         'shuffle_all'  : False,   # shuffle all calcs  
         'shuffle_inner': True,   # shuffle only 1st (inner) iteration
         'cut-max'      : True   # cut set of all calcs down to MAX
        }

    def get_setting(self):
        return self._sett

    def get_topic(self):
        return (self._sett)['topic']

    def update_setting(self, sett):
        self._calcs = self.generate_calcs()
        self._sett = sett

    def format(self, (calc, linepos)):
        """format the calc for display, prepare overlays for input"""
        #print('in Display.format_times_div: calc=', (calc, linepos))#@
        _ccs = collect_digits(calc)
        #print('in Display.format_times_div: _ccs=', _ccs)
        _l0 = make_line_remainder(_ccs)
        #print('in Display.format_times_div: _l0=', _l0)
        if contain(calc, '|'):
            #print('in Display.format_times_div: (_l0,_c[4],_c[6])=',
            #      (_l0, _ccs[4], _ccs[6]))
            _ip = make_input_remainder(_l0, _ccs[4], _ccs[6])
            #print('in Display.format_times_div: _ip=', _ip)
        else:
            _ip = make_input(_ccs, linepos)
        #print('in Display.format_times_div: return=', ([_l0], _ip)) #@
        return ([_l0], _ip)

    def generate_calcs(self):
        """generate all calculations between min..max given in dict"""
        #print('in Generate.times_div, (min, max)=',(_dic['min'], _dic['max'], _dic['remainder']))
        _dic = self._sett
        #print('in Generate.times_div, _dic=', _dic)
        _calcs = []
        if _dic['*']:
            _calcs.extend(self.tim_div(_dic['min'], _dic['max'], '*', _dic['shuffle_inner'], _dic['remainder']))
        if _dic['*commute']:
            _calcs.extend(self.tim_div(_dic['min'], _dic['max'], '*commute', _dic['shuffle_inner'], _dic['remainder']))
        if _dic[':']:
             _calcs.extend(self.tim_div(_dic['min'], _dic['max'], ':', _dic['shuffle_inner'], _dic['remainder']))
        if _dic['in']:
            _calcs.extend(self.tim_div(_dic['min'], _dic['max'], 'in', _dic['shuffle_inner'], _dic['remainder']))      
        if _dic['shuffle_all']:
            random.shuffle(_calcs)
        return _calcs

    def count(self):
        """TODO"""
        return len(self._calcs)

    def define_buttons(self):
        """buttons for this setting, which is specific for TimesDiv"""
        self.label = gtk.Label("2")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 0, 1, 13, 14 ) 
        self.label.show()
        
        self.label = gtk.Label("in")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 1, 2, 13, 14 ) 
        self.label.show()
        
        self.label = gtk.Label("2")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 2, 3, 13, 14 ) 
        self.label.show()
        
        self.label = gtk.Label("=")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 3, 4, 13, 14 ) 
        self.label.show()
        
        self.label = gtk.Label("1")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 4, 5, 13, 14 ) 
        self.label.show()
        
        self.label = gtk.Label("|")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 5, 6, 13, 14 ) 
        self.label.show()
        
        self._display.settings_table.resize(15, 8)
        
        self.label = gtk.Label("0")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 6, 7, 13, 14 ) 
        self.label.show()
        
        self.label = gtk.Label("2")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 0, 1, 12, 13 ) 
        self.label.show()
        
        self.label = gtk.Label(":")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 1, 2, 12, 13 ) 
        self.label.show()
        
        self.label = gtk.Label("2")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 2, 3, 12, 13 ) 
        self.label.show()
        
        self.label = gtk.Label("=")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 3, 4, 12, 13 ) 
        self.label.show()
        
        self.label = gtk.Label("1")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 4, 5, 12, 13 ) 
        self.label.show()
        
        self.label = gtk.Label("|")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 5, 6, 12, 13 ) 
        self.label.show()
        
        self.label = gtk.Label("0")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 6, 7, 12, 13 ) 
        self.label.show()
        
        self.label = gtk.Label("1")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 0, 1, 9, 10 ) 
        self.label.show()
        
        self.label = gtk.Label("*")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 1, 2, 9, 10 ) 
        self.label.show()
        
        self.label = gtk.Label("=")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 3, 4, 9, 10 ) 
        self.label.show()
        
        self.label = gtk.Label("2")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 4, 5, 9, 10 ) 
        self.label.show()
        
        self.toggle_shuffle_all = gtk.ToggleButton("@")
        self.toggle_shuffle_all_label = self.toggle_shuffle_all.get_child()
        self.toggle_shuffle_all_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_shuffle_all.connect("toggled", self.toggle_shuffle_all_callback)
        self._display.settings_table.attach(self.toggle_shuffle_all, 2, 3, 11, 12 )
        self.toggle_shuffle_all.show()
        
        self.toggle_shuffle_inner = gtk.ToggleButton("@")
        self.toggle_shuffle_inner_label = self.toggle_shuffle_inner.get_child()
        self.toggle_shuffle_inner_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_shuffle_inner.connect("toggled", self.toggle_shuffle_inner_callback)
        self._display.settings_table.attach(self.toggle_shuffle_inner, 0, 1, 11, 12 )
        self.toggle_shuffle_inner.show()
        
        self.toggle_remainder = gtk.ToggleButton("V")
        self.toggle_remainder_label = self.toggle_remainder.get_child()
        self.toggle_remainder_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_remainder.connect("toggled", self.toggle_remainder_callback)
        self._display.settings_table.attach(self.toggle_remainder, 5, 7, 11, 12 )
        self.toggle_remainder.show()
        
        self.label = gtk.Label("< - >")
        self.label.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label, 0, 3, 10, 11) 
        self.label.show()
        
        self.toggle_times = gtk.ToggleButton("<")
        self.toggle_times_label = self.toggle_times.get_child()
        self.toggle_times_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_times.connect("toggled", self.toggle_times_callback)
        self._display.settings_table.attach(self.toggle_times, 7, 8, 9, 10 )
        self.toggle_times.show()
                
        self.toggle_commute = gtk.ToggleButton("<")
        self.toggle_commute_label = self.toggle_commute.get_child()
        self.toggle_commute_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_commute.connect("toggled", self.toggle_commute_callback)
        self._display.settings_table.attach(self.toggle_commute, 7, 8, 10, 11 )
        self.toggle_commute.show()
        
        self.toggle_div = gtk.ToggleButton("<")
        self.toggle_div_label = self.toggle_div.get_child()
        self.toggle_div_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_div.connect("toggled", self.toggle_div_callback)
        self._display.settings_table.attach(self.toggle_div, 7, 8, 12, 13 )
        self.toggle_div.show()
        
        self.toggle_in = gtk.ToggleButton("<")
        self.toggle_in_label = self.toggle_in.get_child()
        self.toggle_in_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_in.connect("toggled", self.toggle_in_callback)
        self._display.settings_table.attach(self.toggle_in, 7, 8, 13, 14 )
        self.toggle_in.show()
        
        self.number_butts = []

        for i in range(2 ,9 + 1):
            self.toggle = gtk.ToggleButton(str(i))
            self.toggle_label = self.toggle.get_child()
            self.toggle_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))          
            self.toggle.connect("toggled", self.toggle_number_callback, i) 
            self._display.settings_table.attach(self.toggle, 2, 3, 11-i, 12-i)
            self.toggle.show()
            self.number_butts.append(self.toggle)
            
    def set_buttons(self, sett):
        """buttons for setting specific to 'topic' 'times_div'"""
        for i in range(sett['min'],sett['max']+1):
            self.number_butts[i-2].set_active(True)
            
        if (sett['shuffle_all'] == True):
            self.toggle_shuffle_all.set_active(True)
        else:
            self.toggle_shuffle_all.set_active(False)
            
        if (sett['shuffle_inner'] == True):
            self.toggle_shuffle_inner.set_active(True)
        else:
            self.toggle_shuffle_inner.set_active(False)
            
        if (sett['*'] == True):
            self.toggle_times.set_active(True)
        else:
            self.toggle_times.set_active(False)
            
        if (sett['*commute'] == True):
            self.toggle_commute.set_active(True)
        else:
            self.toggle_commute.set_active(False)
            
        if (sett[':'] == True):
            self.toggle_div.set_active(True)
        else:
            self.toggle_div.set_active(False)
            
        if (sett['in'] == True):
            self.toggle_in.set_active(True)
        else:
            self.toggle_in.set_active(False)
            
        if (sett['remainder'] == True):
            self.toggle_remainder.set_active(True)
        else:
            self.toggle_remainder.set_active(False)

    #**** callbacks ********************************************************

    def toggle_shuffle_all_callback(self, widget):
        if widget.get_active():
            self._display._sett['shuffle_all'] = True
            self.toggle_shuffle_inner.set_active(True)
        else:
            self._display._sett['shuffle_all'] = False
            
    def toggle_shuffle_inner_callback(self, widget):
        if widget.get_active():
            self._display._sett['shuffle_inner'] = True
        else:
            if(self.toggle_shuffle_all.get_active()):   
                widget.set_active(True)
            else:
                self._display._sett['shuffle_inner'] = False
        
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

            
    def toggle_times_callback(self, widget):
        if widget.get_active():
            self._display._sett['*'] = True
        else:
            if( self.toggle_commute.get_active() or self.toggle_in.get_active() or self.toggle_div.get_active() ):
                self._display._sett['*'] = False
            else:
                widget.set_active(True)
            
    def toggle_commute_callback(self, widget):
        if widget.get_active():
            self._display._sett['*commute'] = True
        else:
            if( self.toggle_times.get_active() or self.toggle_in.get_active() or self.toggle_div.get_active() ):
                self._display._sett['*commute'] = False
            else:
                widget.set_active(True)
                
    def toggle_div_callback(self, widget):
        if widget.get_active():
            self._display._sett[':'] = True
        else:
            if( self.toggle_times.get_active() or self.toggle_in.get_active() or self.toggle_commute.get_active() ):
                self._display._sett[':'] = False
            else:
                widget.set_active(True)
                
    def toggle_in_callback(self, widget):
        if widget.get_active():
            self._display._sett['in'] = True
        else:
            if( self.toggle_times.get_active() or self.toggle_commute.get_active() or self.toggle_div.get_active() ):
                self._display._sett['in'] = False
            else:
                widget.set_active(True)
                
    def toggle_remainder_callback(self, widget):
        if widget.get_active():
            self._display._sett['remainder'] = True
        else:
            self._display._sett['remainder'] = False
        
    ##### end of public methods ############################################

    def tim_div(self, min, maxx, dic, shuffle_inner, remainder):
        """generate all multiplications between min..max given for * : in;
        to be called such that all *, all : etc are together"""
        _calcs = []
        for _j in range(min, maxx +1):
            if remainder:
                for _i in range(0,10*_j +1):
                    #print('in Generate.tim_div, (j,i,dm)=',(_j, _i),
                    #      divmod(_i, _j))
                    _res, _rem = divmod(_i, _j)
                    if dic == '*': #this should be excluded by settings
                        _c = [str(_i),'*',str(_j),'=',to_str_99(_i*_j)]
                    elif dic == '*commute': #this should be excluded ..
                        _c = [str(_j),'*',str(_i),'=',to_str_99(_i*_j)]
                    elif dic == ':':
                        _c = [to_str_99(_i),':',str(_j),'=',to_str_99(_res),
                              '|', str(_rem)]
                    elif dic == 'in':
                        _c = [str(_j),'in',to_str_99(_i),'=',to_str_99(_res),
                              '|', str(_rem)]
                    _c = flatten(_c)    
                    _c = strip(_c, '#') # to_str_99 returns leading 0 as # 
                    _calcs.append((_c, 5))
            else:
                for _i in range(1,11):
                    #print('in Generate.tim_div, (j,i)=',(_j, _i))
                    if dic == '*':
                        _c = [to_str_99(_i),'*',str(_j),'=',to_str_99(_i*_j)]
                    elif dic == '*commute':
                        _c = [str(_j),'*',to_str_99(_i),'=',to_str_99(_i*_j)]
                    elif dic == ':':
                        _c = [to_str_99(_i*_j),':',str(_j),'=',to_str_99(_i)]
                    elif dic == 'in':
                        _c = [str(_j),'in',to_str_99(_i*_j),'=',to_str_99(_i)]
                    _c = flatten(_c)    
                    _c = strip(_c, '#') # to_str_99 returns leading 0 as # 
                    _calcs.append((_c, 5))
        if shuffle_inner:
            random.shuffle(_calcs)

        return _calcs
            
