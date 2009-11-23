# -*- coding: utf-8 -*-

from coach import Coach
#from Generate import Generate
from display import Display

class Session:
    """
    for stand-alone usage by the ox-user.
    ?for collaborative sessions see CoSession
    """
    print("DEL import Session")
            
    def __init__(self, name, window):
        self._name = name
        self._dis = Display(window)
        self._co = Coach()
        self._co.register(self, self._dis)
        self._dis.register(self, self._co)
        self._co.create_exercises() #TODO.WN091101 replace by storing Exerc.s
        self._calcs = None #pop !

    def run(self):
        """as long as user does exercises"""
        #print("in Session.run")
        self._co.request_exercise()
        self._dis.init_calc() #TODOWN091101 take Exercise as argument
        
    def notify(self, (msg, data)):
        '''called by the observed objects'''
        #print('in Session.notify: msg=,data=', msg, data)
        if msg == 'setting-done': # from Coach
            self._ex = data
            self._calcs = data._generate_calcs()
            self._key = data.get_topic()
            (self._calcs).reverse()
            _calc = (self._calcs).pop()
            #print('in Session.notify: calc=', _calc)
            _lines, self._input = data.format(_calc)
            self._dis.display_calc(_lines)
            self._curr_in = self._input.pop() #need _curr_in in notify
            self._dis.create_entryline(self._curr_in)
            # create_entryline sets the callback from gtk to Display
        if msg == 'digit-done': # from Display
            #print('in Session.notify, digit-done: _input=', self._input)
            (lino, pos, dig, proterr, protok, li) = self._curr_in
            self._dis.create_entryline((lino, -1, dig, proterr, protok, li))
            if len(self._input) > 0:
                self._curr_in = self._input.pop()
                self._dis.create_entryline(self._curr_in)
            else: # start new calc
                self._dis.show_progress()
                if len(self._calcs) > 0:
                    _calc = (self._calcs).pop()
                    print('in Session.notify: calc=', _calc)
                    _lines, self._input = self._ex.format(_calc)
                    self._dis.display_calc(_lines)
                    self._curr_in = self._input.pop() #need _curr_in in notify
                    self._dis.create_entryline(self._curr_in)
                    # create_entryline sets the callback from gtk to Display
                else:
                    self._dis.finish_calc()
