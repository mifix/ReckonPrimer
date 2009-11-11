#! -*- coding: utf-8 -*-
#(c) Stefan Heher 2009
from time import strftime
import pygtk
import gtk
from sugar.activity import activity
from sugar.datastore import datastore
from sugar import profile
from session import Session

class ReckonPrimerActivity(activity.Activity):

    def __init__(self, handle):
    
        activity.Activity.__init__(self, handle)
        """ Create the official Sugar toolbox at the top of the screen"""
        toolbox = activity.ActivityToolbox(self)
        self.set_toolbox(toolbox)
        toolbox.show()
        
        file_location = activity.get_activity_root() + \
                        "/data/reckonprimer_report.txt" 
        file_handle = open(file_location, 'w')
        file_handle.write("Report: " + profile.get_nick_name() + \
                          strftime(" %Y-%m-%d %H:%M:%S") + "\n")        
        file_handle.close()
        
        title = "Report: " + profile.get_nick_name() + \
                strftime(" %Y-%m-%d %H:%M:%S")
        mime = "text/plain"
        file_path = activity.get_activity_root() + \
                    "/data/reckonprimer_report.txt"
        favorite = "1"
        tags = "ReckonPrimer"
        
        journal_object = datastore.create()
        journal_object.metadata['title'] = title
        journal_object.metadata['mime_type'] = mime
        journal_object.file_path = file_path  
        journal_object.metadata['keep'] = favorite
        journal_object.metadata['tags'] = tags
        journal_object.metadata['icon-color'] = '#AFD600,#5B615C' 
        datastore.write( journal_object )
        journal_object.destroy()

        self.run_session()
        
        
    def run_session(self):
        session = Session("xo-user-name", self)
        session.run()


        
        
        

        

  



    

        



    
        


	
	


	
        
	


     
