# -*- coding: UTF8 -*-
# (c) Patrick Loder 2009

import pickle
import os
class Settings:
    """
    a setting is a dictionary, the settings is a dict of dicts.
    if there is no file then the default settings are taken ...  
    ... see save_last_sett, load_last_sett #due to Sugar write-constraints

    WN090624 settings hardcoded in exercises; this class is
    kept for authoring of new exercises: take defaults from here ?!?
    """
    print("DEL import Settings")

    def __init__(self):
        print("DEL do Settings.__init__")
        #+ and - between min and max, max <= 10
        self._default_addsub_simp = \
        {'topic'  : 'addsub_simp',
         'ID'           : 'addsub_simp_01',
         'descr'  : 'all additions with result 5', #describe this setting
         'MAX'    : 50,     # maximum of calcs generated;
                            # Generate fills up by varying input.
         'MIN'    : 20,     # minimum of calcs generated UNUSED
         'min'    : 0,      # minimum in size of a number in a calc
         'max'    : 5,     # maximum  in size of a number in a calc
                            # 0 <= min <= max <= 10
         '+'      : True,   # make all additions min..max
         '-'      : True,   # make all subtactions min..max
         '_+_=_'  : True,   # = is _right_ from operator, e.g. 1+2=3
         'input=' : [1,3,5],# list of positions in calc: 1 | 3 | 5
                            # where input is possible; 
                            # actual positions chosen by Generate.
         '_=_+_'  : False,   # = is _left_ from operator, e.g. 3=1+2
         '=input' : [1,3,5],# analogous to '_+_=_'
         'shuffle': True,  # shuffle _all_ the calcs
         'cut-max': True   # cut set of all calcs down to MAX
        }

        self._default_passten = \
        {'topic'        : 'passten',
         'ID'           : 'passten_01',
         'descr'        : 'subtractions passing 10',
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

        self._default_times_div = \
        {'topic'        : 'times_div',
         'ID'           : 'times_div_01',
         'descr'        : 'n times 2',
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
        #!!!extend here with additional topic!!!
                          
        self._setts = {'default_addsub_simp' : self._default_addsub_simp,
                       'default_passten'     : self._default_passten,
                       'default_times_div'   : self._default_times_div
                       #!!!extend here with additional topic!!!
        }
    
    def load_last_sett(self, key):
        _dict = None
        _path = 'coach/'
        _path_name = _path + 'LAST_' + key + '.data'
        print('in Setting.load_last_sett: _path_name=', _path_name)
        if os.path.exists(_path_name):
            _addr = open(_path_name, 'rb')
            _dict =  pickle.load(_addr)
            _addr.close()
        return _dict
                
    def save_last_sett(self, key, sett):
        print('in Settings.save_last_sett')
        _path = 'coach/'
        _path_name = _path + 'LAST_' + key + '.data'
        print('in Setting.save_last_sett: _path_name=', _path_name)
        _addr = open(_path_name, 'wb')
        pickle.dump(sett, _addr)
        _addr.close()

#    def load_setting(self, key):
#        """a variant of this will be used for authoring"""
#        dat_name = 'C:/rpa8/coach/latest-topic.txt'
#        if os.path.exists(dat_name):
#            txt_file = open(dat_name, 'rb')
#            if key == 'default_addsub_simp':
#                self._default_addsub_simp = pickle.load(txt_file)
#            elif key == 'default_passten':
#                self._default_passten = pickle.load(txt_file)
#                
#    def save_setting(self, key):
#        """a variant of this will be used for authoring"""
#        dat_name = 'C:/rpa8/coach/latest-topic.txt'
#        txt_file = open(dat_name, 'wb')
#        if key == 'default_addsub_simp':
#            pickle.dump(self._default_addsub_simp, txt_file)
#        elif key == 'default_passten':
#            pickle.dump(self._default_passten, txt_file)


            
#    #this version will go to VS on Apr.27: get setts from file
#    def get_setting(self, key):
#        """a variant of this will be used for authoring"""
#        _sett = None
#        print("in Settings.get_setting, key=" + key)
#        _sett = self.load_setting('addsub_simp') #TODO: key
#        if _sett == None:
#            print('in Settings.get_settings, not existent key=', key)
#            ####FIXME exit
#        return (key, _setts)
########################## + toggle Coach.get_setting ###################
    #for testing passten: get setts from default_*
    def get_setting(self, key):
        print("in Settings.get_setting, key=" + key)
        return (key, self._setts['default_' + key])
        
