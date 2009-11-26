import logging

import gtk

from sugar.graphics.toolbutton import ToolButton
from sugar.activity.widgets import CopyButton


logger = logging.getLogger('ReckonPrimer-activity')

class TestToolbar(gtk.Toolbar):
    def __init__(self, pc, toolbar_box):

          gtk.Toolbar.__init__(self)
                    
	  logger.debug('__init__ TestToolbar chm')
          copy = CopyButton()
          copy.connect('clicked', self._copy_clicked)
          self.insert(copy, -1)
          copy.show()
          self.show_all()
          
    def _copy_clicked(widget, info):
        logger.debug("Button %s was clicked" % info)
