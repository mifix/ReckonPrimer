# -*- coding: utf-8 -*-
"""main of ReckonPrimer
see http://wiki.laptop.org/go/Software_projects#ReconPrimer
(c) Walther Neuper 2009
"""
# WN090416 after successful run there is a strange error at the end ?!?


from session import Session

# initializations

_sess = Session("ox-user-name", 'xxx') # TODO.WN090311 name should come from Sugar
_sess.run()

# finalizations

