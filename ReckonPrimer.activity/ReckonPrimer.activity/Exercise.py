# -*- coding: UTF8 -*-
from functions import contain, collect_digits, make_line, make_input
from functions import make_line_remainder, make_input_remainder

class Exercise:
    """This is the base class for the individual exercises.
    An exercise is characterized by a topic. A topic determines the 
    fields of the settings self._sett and public methods of Exercise.
    The values of self._sett may vary from exercise to exercise.
    """
    def __init__(self):
        """ The settings determine the generation of calculations.
        The fields of the settings are determined by the topic;
        the values of the settings are different for exercises;
        the settings may even be changed by the user."""
        self._sett = None
        """Calculations have a format GOON"""
        self._calcs = []

    def get_setting(self):
        pass
        
    def get_topic(self):
        """The topic is preliminarily used to identify an exercise;
        TODO: use self._sett['ID'] instead as soon as exs are stored."""
        pass

    def update_setting(self, sett): ####??????????
        """The settings may be changed by the user. This method
        is inherited and thus not contained in subclasses."""
        ####self._sett = sett

    def format(self, calc):
        """Prepare the representation of a calculation for Display.
        This method is public for eventual use on calculations
        coming through the net (TODO cooperative games, etc)"""
        pass

    def generate_calcs(self):
        """TODO"""
        pass

    def count(self):
        """TODO"""
        pass
        #return len(self._calcs)

    def define_buttons(self):
        """XXX"""
        pass

    def set_buttons(self, sett):
        """XXX"""
        pass
    






    def format_addsub_simp(self, (calc, linepos)):
        """format the calc for display, prepare overlays for input"""
        #@print('in Display.format_addsub_simp: calc=', (calc, linepos))#@
        _ccs = collect_digits(calc)
        print('in Display.format_addsub_simp: _ccs=',_ccs )
        _l0 = make_line(_ccs, linepos)
        _ip = make_input(_ccs, linepos)
        #@print('in Display.format_addsub_simp: return=', ([_l0], _ip)) #@
        return ([_l0], _ip)
#return ([[' ', '1', '0', ' ', '-', ' ', '7', ' ', '=', ' ', '_', ' ']], [(0, 10, '3', ' 10 - 7 = _ ', ' 10 - 7 = 3 ', [' ', '1', '0', ' ', '-', ' ', '7', ' ', '=', ' ', '3', ' '])])
