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
        #self._co = Coach(self)
        #self._dis = Display(window, self)

        self._dis = Display(window)
        self._co = Coach()
        self._co.register(self, self._dis)
        self._dis.register(self, self._co)
        self._co.create_exercises()
        self._calcs = None #pop !

    def run(self):
        """as long as user does exercises"""
        print("in Session.run")
        #WN090624 self._co.get_setting()
        self._co.request_exercise()
        self._dis.init_calc()
        
    def notify(self, (msg, data)):
        '''called by the observed objects'''
        #print('in Session.notify: msg=,data=', msg, data)
        if msg == 'setting-done': # from Coach
            self._ex = data
            self._calcs = data.generate_calcs()
            self._key = data.get_topic()
            (self._calcs).reverse()
            _calc = (self._calcs).pop()
            #WN090624 self._dis.show_calc((self._calcs).pop())
            #print('in Session.notify: calc=', _calc)
            _lines, self._input = data.format(_calc)
            self._dis.display_calc(_lines)
            self._curr_in = self._input.pop() #need _curr_in in notify
            self._dis.create_entryline(self._curr_in)
            # create_entryline sets the callback from gtk to Display
        #WN090624 new    
        if msg == 'digit-done':
            #print('in Session.notify, digit-done: _input=', self._input)
            (lino, pos, dig, proterr, protok, li) = self._curr_in
            self._dis.create_entryline((lino, -1, dig, proterr, protok, li))
            if len(self._input) > 0:
                self._curr_in = self._input.pop()
                self._dis.create_entryline(self._curr_in)
            else: # start new calc
                #WN090624 self._sess.notify(('calc-done', None))
                self._dis.show_progress()
                if len(self._calcs) > 0:
                    _calc = (self._calcs).pop()
                    #WN090624 self._dis.show_calc((self._calcs).pop())
                    print('in Session.notify: calc=', _calc)
                    _lines, self._input = self._ex.format(_calc)
                    self._dis.display_calc(_lines)
                    self._curr_in = self._input.pop() #need _curr_in in notify
                    self._dis.create_entryline(self._curr_in)
                    # create_entryline sets the callback from gtk to Display
                else:
                    self._dis.finish_calc()
        #WN090624    
        #if msg == 'calc-done':
        #    if len(self._calcs) > 0:
        #        self._dis.show_calc((self._calcs).pop())
        #    else:
        #        self._dis.finish_calc()
        
            
  
