# -*- coding: UTF8 -*-
# Display-NOGUI.py !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

from functions import contain, collect_digits, make_line, make_input
from functions import make_line_remainder, make_input_remainder

class Display:
    """.. all gui-elements of ReckonPrimer"""
    print("DEL import Display")

    
    def __init__(self, window):
        pass #see sequence of creation in Session

    def register(self, sess, co):
        self._sess = sess
        self._co = co
        
    def init_calc(self):
        """prepares for calculations from 1 setting.
        for instance, a calculation might be on 1 ore more lines.
        """
        print("in Display.init_calc")
        pass
    
    # different with GUI
    #WN090624 def show_setting(self, key, sett):
    #WN090624 def offer_setting(self, key, sett):
    def offer_setting(self, ex):
        #WN090624 self._sett = sett
        #WN090624 self._key = key
        self._sett = ex.get_setting()
        self._key = ex.get_topic()
        print('in Display.offer_setting: key=,sett=',self._key,self._sett)
        input('in Display.show_setting: Start-Button #')
        self._co.notify(('setting-done', self._sett))
        
    def notify(self, (msg, data)):
        """only used by gtk"""
        if msg == 'digit-done':
            self._sess.notify(('digit-done', None)) #WN090624
            #if len(self._input) > 0:
            #    self._curr_in = self._input.pop()
            #    self.create_entryline(self._curr_in)
            #else:
            #    self._sess.notify(('calc-done', None))


            
    def show_calc (self, calc):
        """start calc: format calc for display and input, input first digit"""
        #TODO: warum ist calc ein Argument _und_ self. ? ENTWEDER..ODER !
        #TODO: warum ist _key kein Argument            ? ENTWEDER..ODER !
        print('in Display.show_calc: calc=',calc)
        if(self._key == 'addsub_simp'):
            _lines, self._input = self.format_addsub_simp(calc)
        elif(self._key == 'passten'):
            _lines, self._input = self.format_passten(calc)
        elif(self._key == 'times_div'):
            _lines, self._input = self.format_times_div(calc)
        else:
            print('in Display.show_calc: ERROR no key=', self._key)
            #TODO: exit (programmer mode!)
        self.display_calc(_lines)
        self._curr_in = self._input.pop() #need _curr_in in notify
        self.create_entryline(self._curr_in)
        # create_entryline sets the callback from gtk

    def display_calc(self, lines):
        """display the lines of a calc with _ at all input positions"""
        for l in lines:
            print('in Display.display_calc, line=', l) #@
            pass

    #OLD show_calc_addsub_simp(self,  calc):
    def create_entryline(self,(lineno, linepos, dig, prot_err, prot_ok, line)):
        """create gtk.Entry in line at linepos and set callback_input_digit"""
        calculation, cursor = line, linepos
        #print('in Display.create_entryline:l=', line) #@
        self.input_digit('widget', dig, prot_err, prot_ok)


    def input_digit(self, widget, dig, prot_err, prot_ok):
        """input a digit and give feedback.
        The _only_ other active widget is the <stop>-button on the right"""
        print('in Display.input_digit: dig=', dig, ', prot_err=', prot_err) #@
        #_dig = input('in Display.input_digit: dig= ')
        #while str(_dig) != dig:
        #    _dig = input('in Display.input_digit: dig= ')            
        self.notify(('digit-done', None))
        

    def finish_calc(self):
        #WN090518 needed ???
        pass

    def offer_topics(self, topics):
        """TODO: get the users choice from buttons above the settings"""
        _i = 0
        for _t in topics:
            _i = _i + 1
            print('in Display.offer_topics: ' + _t + '....' + str(_i))
        #TODO: make that a callback...
        self.new_topic(topics)

    #TODO: make that a callback...
    def new_topic(self, topics):
        """TODO: get the users choice from buttons above the settings"""
        _choice = int(input('in Display.new_topic: ...............?'))
        while _choice < 1 and 3 < _choice:
            _choice = int(input('in Display.new_topic: ...............?'))
        self._co.notify(('new-topic', topics[_choice - 1]))
            
    
