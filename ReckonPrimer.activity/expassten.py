# -*- coding: utf-8 -*-
from Exercise import Exercise
import random
import copy
from functions import *
import gtk
import pygtk
import pango
from sugar.graphics import style

class ExPassTen(Exercise):
    def __init__(self, dis):
        self._title = 'template expassten'
        self._display = dis
        self._sett = {'topic'        : 'passten',
         'calclines'    : 1,      # or 2 iff 'newline' : True.
         'MAX'          : 150,    # maximum of calcs generated;
                                  # TODO: Generate fills up by varying input.
         'MIN'          : 10,     # minimum of calcs generated 090416WN:UNUSED
         '+'            :True,   # + crossing the ten barrier!!
         '-'            :False,   # - goes below the ten barrier!!!
                                  # (i.e. iteration on left arg. is "outer" loop)
         'min'          : 2,   # +: minimum in size of number in left argument
         #'min'          : 5,   # +: minimum in size of number in left argument
                                  # -: minimum in size of result
         'max'          : 2,   # +: maximum in size of number in left argument
                                  # -: maximum in size of result
         #'max'          : 9,   # +: maximum in size of number in left argument
         'input'        :[3],  # list of positions in calc 3 | 5
                                  # where input is possible; 
                                  # actual positions chosen by Generate.
         'newline'      : True,    # display 2nd line for intermediate results
         'shuffle_all'  : False,   # shuffle all calcs  
         'shuffle_inner': False,   # shuffle only 1st (inner) iteration
         'cut-max'      : True   # cut set of all calcs down to MAX
        }
        self._calcs = self._generate_calcs()
    
    def format(self, (cs, ms, linepos)):
        """format the calc for display, prepare overlays for input"""
        #print('in ExPassTen.format: (cs, ms, linepos)=', (cs, ms, linepos))
        if ms is None:
            #@print('in Display.format_passten 1: calc=', (cs, linepos)) #@
            return self.format_addsub_simp((cs, linepos))
        elif contain(cs, '+'):
            #@print('in Display.format_passten 2: calc=', (cs, ms, linepos))#@
            if linepos == 1: ################################## unused !
                #(['3', '+', '7', '=', '1', '0'], ['7', '0'], 1))
                #cs[0]     cs[2]          cs[5], ms[0]  [1],  linepos
                ### the lines of the calculation for display_calc
                #     [' ',' ',' ',' ','_',' ','+',' ','7'  ,' ','=',' ','1'  ,'0']
                _l0 = [' ',' ',' ',' ','_',' ','+',' ',cs[2],' ','=',' ',cs[4],cs[5]]
                #     [' ',' ',' ','_','+','_',' ',' ',' ',' ',' ',' ',' ',' ']
                _l1 = [' ',' ',' ','_','+','_',' ',' ',' ',' ',' ',' ',' ',' ']
                ### the 1st input --> _p0 = '(3+_)+7=10'
                _pe0 = ''.join(['(','_','+','_',')','+',cs[2],'=',cs[4],cs[5]])
                _po0 = ''.join(['(',ms[0],'+','_',')','+',cs[2],'=',cs[4],cs[5]])
                _i0 = (1, 3, ms[0], _pe0, _po0,
                       [' ',' ',' ',ms[0],'+','_',' ',' ',' ',' ',' ',' ',' ',' '])
                ### the 2nd input --> _p0 = '(3+0)+7=10'
                _pe1 = ''.join(['(',ms[0],'+','_',')','+',cs[2],'=',cs[4],cs[5]])
                _po1 = ''.join(['(',ms[0],'+',ms[1],')','+',cs[2],'=',cs[4],cs[5]])
                _i1 = (1, 5, ms[1], _pe1, _po1,
                       [' ',' ',' ',ms[0],'+',ms[1],' ',' ',' ',' ',' ',' ',' ',' '])
                ### the 3rd input --> _p0 = '3+7=10'
                _pe2 = ''.join(['_'  ,'+',cs[2],'=',cs[4],cs[5]])
                _po2 = ''.join([cs[0],'+',cs[2],'=',cs[4],cs[5]])
                _i2 = (0, 13, cs[5], _pe2, _po2,
                       [' ',' ',' ',' ','3',' ','+',' ','7',' ','=',' ','1',cs[5]])
                #@print('in Display.format_passten: return=', ([_l0, _l1], [_i2, _i1, _i0])) #@
                return ([_l0, _l1], [_i2, _i1, _i0]) #_iN reversed for pop
            elif linepos == 3:
                #(['3', '+', '7', '=', '1', '0'], ['3', '0'], 5))
                #cs[0]     cs[2]          cs[5], ms[0]  [1],  linepos
                _l0 = [' ',' ',' ',' ',cs[0],' ','+',' ','_',' ','=',' ',cs[4],cs[5]]
                _l1 = [' ',' ',' ',' ',' ',  ' ',' ','_','+',  '_',' ',' ',' '  ,' ']
                #     '3+(7+_)=10'
                _pe0 = ''.join([cs[0],'+','(','_'  ,'+','_',')','=',cs[4],cs[5]])
                _po0 = ''.join([cs[0],'+','(',ms[0],'+','_',')','=',cs[4],cs[5]])
                _i0 = (1, 7, ms[0], _pe0, _po0,
                       [' ',' ',' ',' ',' ',' ',' ',ms[0],'+','_',' ',' ',' '  ,' '])
                #     '3+(7+0)=10'
                _pe1 = ''.join([cs[0],'+','(',ms[0],'+','_'  ,')','=',cs[4],cs[5]])
                _po1 = ''.join([cs[0],'+','(',ms[0],'+',ms[1],')','=',cs[4],cs[5]])
                _i1 = (1, 9, ms[1], _pe1, _po1,
                       [' ',' ',' ',' ',' ',' ',' ',ms[0],'+',ms[1],' ',' ',' ',' '])
                #     '3+7=10'
                _pe2 = ''.join([cs[0],'+','_','=',cs[4],cs[5]])
                _po2 = ''.join([cs[0],'+',cs[2],'=',cs[4],cs[5]])
                _i2 = (0, 8,cs[2], _pe2, _po2,
                       [' ',' ',' ',' ',cs[0],' ','+',' ',cs[2],' ','=',' ',cs[4],cs[5]])
                #@print('in Display.format_passten: return=', ([_l0, _l1], [_i2, _i1, _i0])) #@
                return ([_l0, _l1], [_i2, _i1, _i0]) #_iN reversed for pop
            elif linepos == 5:
                #(['3', '+', '7', '=', '1', '0'], ['7', '0'], 5))
                #cs[0]     cs[2]          cs[5], ms[0]  [1],  linepos
                _l0 = [' ',' ',' ',' ',cs[0],' ','+',' ',cs[2],' ','=',' ',cs[4],'_']
                _l1 = [' ',' ',' ',' ',' ',  ' ',' ','_','+',  '_',' ',' ',' '  ,' ']
                #     '3+(7+_)=1_'
                _pe0 = ''.join([cs[0],'+','(','_'  ,'+','_',')','=',cs[4],'_'])
                _po0 = ''.join([cs[0],'+','(',ms[0],'+','_',')','=',cs[4],'_'])
                _i0 = (1, 7, ms[0], _pe0, _po0,
                       [' ',' ',' ',' ',' ',' ',' ',ms[0],'+','_',' ',' ',' '  ,' '])
                #     '3+(7+0)=1_'
                _pe1 = ''.join([cs[0],'+','(',ms[0],'+','_'  ,')','=',cs[4],'_'])
                _po1 = ''.join([cs[0],'+','(',ms[0],'+',ms[1],')','=',cs[4],'_'])
                _i1 = (1, 9, ms[1], _pe1, _po1,
                       [' ',' ',' ',' ',' ',' ',' ',ms[0],'+',ms[1],' ',' ',' ',' '])
                #     '3+7=10'
                _pe2 = ''.join([cs[0],'+',cs[2],'=',cs[4],'_'  ])
                _po2 = ''.join([cs[0],'+',cs[2],'=',cs[4],cs[5]])
                _i2 = (0, 13,cs[5], _pe2, _po2,
                       [' ',' ',' ',' ',cs[0],' ','+',' ',cs[2],' ','=',' ',cs[4],cs[5]])
                #@print('in Display.format_passten: return=', ([_l0, _l1], [_i2, _i1, _i0])) #@
                return ([_l0, _l1], [_i2, _i1, _i0]) #_iN reversed for pop
            else:
                print('in Display.format_passten: not exists linepos=', linepos)
                #TODO exit, programmer mode
#            #for linepos = 5:
#            return ([[' ',' ',' ',' ','3',' ','+',' ','_',' ','=',' ','1','_'],
#                     [' ',' ',' ',' ',' ','_','+','_',' ',' ',' ',' ',' ',' ']],
#                    [(0, 13,'0', '3+(_+_)=1_', '3+(7+_)=1_',
#                      [' ',' ',' ',' ','3',' ','+',' ','7',' ','=',' ','1','_']),
#                     (1, 7, '0', '3+(7+_)=1_, '3+(7+0)=1_',
#                      [' ',' ',' ',' ',' ','7','+','_',' ',' ',' ',' ',' ',' ']),
#                     (1, 5, '7', '3+7+=1_', '3+7=10'
#                      [' ',' ',' ',' ',' ','_','+','_',' ',' ',' ',' ',' ',' '])])
        else: #contain(calc, '-')
            #@print('in Display.format_passten 3: calc=', (cs, ms, linepos))#@
            if linepos == 1:
                #(['1', '0', '-', '7', '=', '3'], ['3', '0'], 3))
                #     cs[1]     cs[3]     cs[5], ms[0]  [1],  linepos
                _l0 = [cs[0],'_',' ','-',' ',cs[3],' ','=',' ',cs[5],' ']                
                _l1 = [' '  ,' ',' ',' ',' ',' '  ,' ',' ','_','+'  ,'_']                
                ### the 1st input --> _p0 = '1_-7=(3+_)'
                _pe0 = ''.join([cs[0],'_','-',cs[3],'=','(','_'  ,'+','_',')',])
                _po0 = ''.join([cs[0],'_','-',cs[3],'=','(',ms[0],'+','_',')',])
                _i0 = (1, 8, ms[0], _pe0, _po0,
                       [' '  ,' ',' ',' ',' ',' '  ,' ',' ',ms[0],'+'  ,'_'])
                ### the 2nd input --> _p1 = '1_-7=(3+0)'
                _pe1 = ''.join([cs[0],'_','-',cs[3],'=','(',ms[0],'+','_'  ,')',])
                _po1 = ''.join([cs[0],'_','-',cs[3],'=','(',ms[0],'+',ms[1],')',])
                _i1 = (1, 10, ms[1], _pe1, _po1,
                       [' '  ,' ',' ',' ',' ',' '  ,' ',' ',ms[0],'+'  ,ms[1]])
                ### the 3rd input --> _p2 = '10-7=3'
                _pe2 = ''.join([cs[0],'_'  ,'-',cs[3],'=',cs[5]])
                _po2 = ''.join([cs[0],cs[1],'-',cs[3],'=',cs[5]])
                _i2 = (0, 1, cs[1], _pe2, _po2,
                       [cs[0],cs[1],' ','-',' ',cs[3],' ','=',' ',cs[5],' '])
                #@print('in Display.format_passten: return=', ([_l0, _l1], [_i2, _i1, _i0])) #@
                return ([_l0, _l1], [_i2, _i1, _i0]) #_iN reversed for pop
            elif linepos == 3:
                #(['1', '0', '-', '7', '=', '3'], ['0', '7'], 3))
                #     cs[1]     cs[3]     cs[5], ms[0]  [1],  linepos
                _l0 = [cs[0],cs[1],' ','-',' ','_',' ','=',' ',cs[5],' ']                
                _l1 = [' '  ,' '  ,' ',' ','_','+','_',' ',' ',' '  ,' ']
                #     '10-_=(0+_)'
                _pe0 = ''.join([cs[0],cs[1],'-','(','_','+','_',')','=',cs[5]])
                _po0 = ''.join([cs[0],cs[1],'-','(',ms[0],'+','_',')','=',cs[5]])
                _i0 = (1, 4, ms[0], _pe0, _po0,
                       [' '  ,' '  ,' ',' ',ms[0],'+','_',' ',' ',' '  ,' '])
                #     '10-_=(0+3)'
                _pe1 = ''.join([cs[0],cs[1],'-','(',ms[0],'+','_'  ,')','=',cs[5]])
                _po1 = ''.join([cs[0],cs[1],'-','(',ms[0],'+',ms[1],')','=',cs[5]])
                _i1 = (1, 6, ms[1], _pe1, _po1,
                       [' '  ,' '  ,' ',' ',ms[0],'+',ms[1],' ',' ',' '  ,' '])
                #     '10-7=3'
                _pe2 = ''.join([cs[0],cs[1],'-','_'  ,'=',cs[5]])
                _po2 = ''.join([cs[0],cs[1],'-',cs[3],'=',cs[5]])
                _i2 = (0, 5, cs[3], _pe2, _po2,
                       [cs[0],cs[1],' ','-',' ',cs[3],' ','=',' ',cs[5],' '])
                #@print('in Display.format_passten: return=', ([_l0, _l1], [_i2, _i1, _i0])) #@
                return ([_l0, _l1], [_i2, _i1, _i0]) #_iN reversed for pop
            elif linepos == 5:
                #(['1', '0', '-', '7', '=', '3'], ['0', '7'], 3))
                #     cs[1]     cs[3]     cs[5], ms[0]  [1],  linepos
                _l0 = [cs[0],cs[1],' ','-',' ',cs[3],' ','=',' ','_',' ']                
                _l1 = [' '  ,' '  ,' ',' ','_','+'  ,'_',' ',' ',' ',' ']
                #     '10-(0+_)=_'
                _pe0 = ''.join([cs[0],cs[1],'-','(','_'  ,'+','_',')','=','_'])
                _po0 = ''.join([cs[0],cs[1],'-','(',ms[0],'+','_',')','=','_'])
                _i0 = (1, 4, ms[0], _pe0, _po0,
                       [' '  ,' '  ,' ',' ',ms[0],'+'  ,'_',' ',' ',' ',' '])
                #     '10-(0+7)=_'
                _pe1 = ''.join([cs[0],cs[1],'-','(',ms[0],'+','_',')','=','_'])
                _po1 = ''.join([cs[0],cs[1],'-','(',ms[0],'+',ms[1],')','=','_'])
                _i1 = (1, 6, ms[1], _pe1, _po1,
                       [' '  ,' '  ,' ',' ',ms[0],'+'  ,ms[1],' ',' ',' ',' '])
                #     '10-7=3'
                _pe2 = ''.join([cs[0],cs[1],'-',cs[3],'=','_'  ])
                _po2 = ''.join([cs[0],cs[1],'-',cs[3],'=',cs[5]])
                _i2 = (0, 9, cs[5], _pe2, _po2,
                       [cs[0],cs[1],' ','-',' ',cs[3],' ','=',' ',cs[5],' '])
                #@print('in Display.format_passten: return=', ([_l0, _l1], [_i2, _i1, _i0])) #@
                return ([_l0, _l1], [_i2, _i1, _i0]) #_iN reversed for pop
            else:
                print('in Display.format_passten: not exists linepos=', linepos)
                #TODO exit, programmer mode
        
    def _generate_calcs(self):
        _dic = self._sett
        #print("in ExPassTen._generate_calcs: _dic=", _dic)
        _calcs = []
        _c = []
        # generate all calcs
        if _dic['+']:
            _c = self._pass10add(_dic['min'], _dic['max'], _dic['input'], _dic['newline'], _dic['shuffle_inner'], _dic['shuffle_all'])
            _calcs.extend(_c)

        if _dic['-']:
            _c = self.pass10sub(_dic['min'], _dic['max'], _dic['input'], _dic['newline'], _dic['shuffle_inner'], _dic['shuffle_all'])
            _calcs.extend(_c)
            
        if _dic['shuffle_all']:
            random.shuffle(_calcs)   
        return _calcs

    def define_buttons(self):
        """ See comment in Exercies.define_buttons. """    
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
        
        self.label0 = gtk.Label("3")
        self.label0.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label0, 2, 3, 10, 11 ) 
        self.label0.show()
        
        self.label1 = gtk.Label("=")
        self.label1.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label1, 3, 4, 10, 11 ) 
        self.label1.show()
        
        self.label2 = gtk.Label("12")
        self.label2.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label2, 4, 5, 10, 11 ) 
        self.label2.show()
        
        self.label3 = gtk.Label("1 + 2")
        self.label3.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label3, 2, 3, 11, 12 ) 
        self.label3.show()
                
        self.label6 = gtk.Label(self._display._sett['MAX'])
        self.label6.modify_font(pango.FontDescription("sans 12"))
        self._display.settings_table.attach(self.label6, 5, 6, 1, 2 ) 
        self.label6.show()
        
        #self.label7 = gtk.Label(self._display._sess._gen.count((self._display._key, self._display._sett)))
        #self.label7.modify_font(pango.FontDescription("sans 12"))
        #self._display.settings_table.attach(self.label7, 5, 6, 2, 3 ) 
        #self.label7.show()
        
        self.toggle_newline = gtk.ToggleButton("<")
        self.toggle_label = self.toggle_newline.get_child()
        self.toggle_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_newline.connect("toggled", self.toggle_newline_callback)
        self._display.settings_table.attach(self.toggle_newline, 5, 6, 11, 12)
        self.toggle_newline.show()
        
        self.toggle_shuffle_all = gtk.ToggleButton("@")
        self.toggle_shuffle_all_label = self.toggle_shuffle_all.get_child()
        self.toggle_shuffle_all_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_shuffle_all.connect("toggled", self.toggle_shuffle_all_callback)
        self._display.settings_table.attach(self.toggle_shuffle_all, 0, 1, 13, 14 )
        self.toggle_shuffle_all.show()
        
        self.toggle_shuffle_inner = gtk.ToggleButton("@")
        self.toggle_shuffle_inner_label = self.toggle_shuffle_inner.get_child()
        self.toggle_shuffle_inner_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_shuffle_inner.connect("toggled", self.toggle_shuffle_inner_callback)
        self._display.settings_table.attach(self.toggle_shuffle_inner, 2, 3, 13, 14 )
        self.toggle_shuffle_inner.show()
        
        self.toggle_pos3 = gtk.ToggleButton("--")
        self.toggle_label = self.toggle_pos3.get_child()
        self.toggle_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_pos3.connect("toggled", self.toggle_pos3_callback)
        self._display.settings_table.attach(self.toggle_pos3, 2, 3, 12, 13 )
        self.toggle_pos3.show()
        
        self.toggle_pos5 = gtk.ToggleButton("--")
        self.toggle_label = self.toggle_pos5.get_child()
        self.toggle_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))
        self.toggle_pos5.connect("toggled", self.toggle_pos5_callback)
        self._display.settings_table.attach(self.toggle_pos5, 4, 5, 12, 13 )
        self.toggle_pos5.show()
        
        self.number_butts = []

        for i in range(1,9+1):
            self.toggle = gtk.ToggleButton(str(i))
            self.toggle_label = self.toggle.get_child()
            self.toggle_label.modify_font(pango.FontDescription("sans %d" % style.zoom(12)))            
            self.toggle.connect("toggled", self.toggle_number_callback, i) 
            self._display.settings_table.attach(self.toggle, 0, 1, 1+i, 2+i)
            self.toggle.show()
            self.number_butts.append(self.toggle)

    def set_buttons(self, sett):
        """ See comment in Exercies.set_buttons. """
        for i in range(sett['min'],sett['max']+1):
            self.number_butts[i-1].set_active(True)
            
        if (sett['+'] == True):
            self.toggle_plus.set_active(True)
        else:
            self.toggle_plus.set_active(False)
            
        if (sett['-'] == True):
            self.toggle_minus.set_active(True)
        else:
            self.toggle_minus.set_active(False) 
            
        if (sett['newline'] == True):
            self.toggle_newline.set_active(True)
        else:
            self.toggle_newline.set_active(False)
            
        if (sett['shuffle_all'] == True):
            self.toggle_shuffle_all.set_active(True)
        else:
            self.toggle_shuffle_all.set_active(False)
            
        if (sett['shuffle_inner'] == True):
            self.toggle_shuffle_inner.set_active(True)
        else:
            self.toggle_shuffle_inner.set_active(False)
            
        for i in sett['input']:
            if( i == 1 ): 
                self.toggle_pos1.set_active(True)
 
            if ( i == 3 ): 
                self.toggle_pos3.set_active(True)
                
            if ( i == 5 ): 
                self.toggle_pos5.set_active(True)

    #**** callbacks ********************************************************

    def toggle_newline_callback(self, widget):
        if widget.get_active():
            self._display._sett['newline'] = True
        else:
            self._display._sett['newline'] = False
            
            
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
                
    def toggle_pos3_callback(self, widget):
        if widget.get_active():
            self._display._sett['input'] = list(set(self._display._sett['input']) | set([3]))
        else:
            if(self.toggle_pos5.get_active()):
                self._display._sett['input'] = list(set(self._display._sett['input']) - set([3]))
            else:
                widget.set_active(True)
            
    def toggle_pos5_callback(self, widget):
        if widget.get_active():
            self._display._sett['input'] = list(set(self._display._sett['input']) | set([5]))
        else:
            if(self.toggle_pos3.get_active()):
                self._display._sett['input'] = list(set(self._display._sett['input']) - set([5]))
            else:
                widget.set_active(True)
                
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
        
    ##### end of public methods ############################################

    def _pass10add(self, min_, max_, inpt, newlin, shuffle_inner, shuffle_all):
        """generate all calcs with + for crossing the tens barrier"""
        _ret_list= []
        for _m in range(min_, max_ + 1):
            _iter_r = []
            _mdown = min_ + max_ - _m # iterator goes down
            #print('in Generate._pass10add _m=',_m, '_mdown=',_mdown)
            for _j in range(10 - _mdown, 10):
                #print('in Generate._pass10add _j=', _j)
                _inp = random.choice(inpt)
                if newlin:
                    if _inp == 1:
                        _y = (10 - _j)
                    else:
                        _y = (10 - _mdown)
                    _z = (_mdown + _j) - 10
                    _iter_r.append(([str(_mdown), '+', str(_j), '=', '1', str((_mdown + _j) - 10)], [str(_y), str(_z)], _inp))
                else:
                    _iter_r.append(([str(_mdown), '+', str(_j), '=', '1', str((_mdown + _j) - 10)], None, _inp))
            if shuffle_inner:
                random.shuffle(_iter_r)
            _ret_list.extend(_iter_r)
        if shuffle_all:
            random.shuffle(_ret_list)
        return _ret_list
        
    def pass10sub(self, min_, max_, inpt, newlin, shuffle_inner, shuffle_all):
        """generate all calcs with + for crossing the tens barrier"""
        _ret_list= []
        for _m in range(min_, max_ + 1):
            _iter_r = []
            _mdown = min_ + max_ - _m # iterator goes down
            #print('in Generate.pass10sub _m=',_m, '_mdown=',_mdown)
            for _j in range(10 - _mdown, 10):
                #print('in Generate.pass10sub _j=', _j)
                _inp = random.choice(inpt)
                if newlin:
                    if _inp == 1:
                        _y = (10 - _j)
                        _z = (_mdown + _j) - 10
                    else:
                        _y = (_mdown + _j) - 10
                        _z = (10 - _mdown)
                    _iter_r.append((['1',str((_mdown + _j) - 10), '-', str(_j), '=', str(_mdown)], [str(_y), str(_z)], _inp))
                else:
                    _iter_r.append((['1',str((_mdown + _j) - 10), '-', str(_j), '=', str(_mdown)], None, _inp))
            if shuffle_inner:
                random.shuffle(_iter_r)
            _ret_list.extend(_iter_r)
        if shuffle_all:
            random.shuffle(_ret_list)
        return _ret_list
