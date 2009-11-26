# -*- coding: utf-8 -*-

import os
import pprint
import pickle
from settings import Settings
from display import Display
from Exercise import Exercise
from exaddsimp import ExAddSimp
from expassten import ExPassTen
from extimesdiv import ExTimesDiv

class Coach:
    """determines Settings which might come from Display.
    Thus Coach is an observer (!design pattern!) of Display,
    and consequently Session is an observer (!design pattern!) of Coach
    """

    print("DEL import Coach")

    def __init__(self):
        print("DEL do Coach.__init__")
        self._setts = Settings()
        self._key = ''
        # self._dis = sess._dis # see sequence of creation in Session
        # --->???self._curr_sett = None - Coach has only 1 current setting
        # self._exs = self.create_exs()
        self._ex = None

    def register(self, sess, dis):
        self._sess = sess
        self._dis = dis

    def create_exercises(self):
        self._exs = self.create_exs()
        
    def create_exs(self):
        """TODO version preliminary until exs are stored on disk"""

        ['addsub_simp', 'passten', 'times_div']
        _ex1 = ExAddSimp(self._dis)
        _ex2 = ExPassTen(self._dis)
        _ex3 = ExTimesDiv(self._dis)
        return[_ex1, _ex2, _ex3]

    def _update_exs(self, ex):
        """update one of the examples known to Coach by topic.
        TODO after exs are stored on disk: take ID instead topic
        """

        # print('in Coach.update_ex: ex.topic=', ex.get_topic())
        _exs = []
        for _e in self._exs:
            if _e.get_topic() == ex.get_topic():
                _exs.append(ex)
            else:
                _exs.append(_e)
        self._exs = _exs

    # this version will go to VS on Apr.27: get setts from file
    # def get_setting(self):
        # print("in Coach.get_setting")
        # TODO coach selects an exercise
        # self._key = 'addsub_simp' 
        #TODO relate key to sett of exercise
        # _sett = self._setts.load_last_sett(self._key)
        # print("in Coach.get_setting, key=, sett=", self._key, _sett)
        # self._dis.show_setting(self._key, _sett)
        # sett returned from Display by Session.notify
        # + toggle Settings.get_setting - Coach.notify
    # for testing passten: get setts from default_*
    # WN090624 def get_setting(self):

    def request_exercise(self):
        """ This preliminary version just lets the Learner select."""
        print("in Coach.get_setting")
        # WN090624 self._dis.offer_topics(['addsub_simp',
        # 'passten', 'times_div'])
        self._dis.offer_topics([t.get_topic() for t in self._exs])
        # calls back with notify('setting-done'...

    def notify(self, (msg, data)):
        """called by the observed objects"""

        print("in Coach.notify: msg=, data=", (msg, data))
        if msg == 'setting-done': # from 
            # + self._setts.save_last_sett(self._key, data)
            self._ex.update_setting(data)
            self._update_exs(self._ex)
            self._sess.notify((msg, self._ex))
        elif msg == 'new-topic':
            self._ex = self.get_ex(data)
            self._dis.offer_setting(self._ex)

    def get_ex(self, tpc):
        """Get an Exercise by topic. TODO get by ID if exs are stored on disk.
        """
        for _t in self._exs:
            if _t.get_topic() == tpc:
                return _t
