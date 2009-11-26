#! -*- coding: utf-8 -*-
#(c) Stefan Heher 2009
#1234567890123456789012345678901234567890123456789012345678901234567890123456789
import gtk
import pygtk
import pango
import time
import gobject
from sugar.activity import activity
from functions import *
from settings import Settings
from timer import Timer
from Exercise import Exercise
from sugar import profile
from sugar.graphics import style



class Display:
    """
    Definition and manipulation of all GUI-elemts.
    Exception (redesign?): def define_buttons in classes derived from Exercise.
    """
    print("DEL import Display") 
    
    def __init__(self, window):        
        self.errors = 0
        self._sett = None      # setting updated by callbacks during input
        self.running = False   # first round of calculations
        
        self.active_topic = None
        
                
        # ----- all permanent GUI-elements ----- TODO separate def
        # Save the sugar main window
        self.main_window = window
        
        # Create a table consisting of 4 possible entries
        self.table = gtk.Table(5, 2, True)
        
	    # Put the table in the main window
        self.main_window.set_canvas(self.table)

	    # Create the log_buffer
        self.log_buffer = gtk.TextBuffer()
        
        # Create a tag table from the buffer
        self.tag_table = self.log_buffer.get_tag_table()
        
        # Create a tag for errors
        self.error_tag = gtk.TextTag("error")
        self.error_tag.set_property("foreground", "blue")
        self.tag_table.add(self.error_tag)
        
        # Create a tag for correct calculations
        self.correct_tag = gtk.TextTag("correct")
        self.correct_tag.set_property("foreground", "green")
        self.tag_table.add(self.correct_tag)


        # Create a log_view with the previously created log_buffer
        self.log_view = gtk.TextView(self.log_buffer)
        
        # Set the font size for the log_view
        self.log_view.modify_font(pango.FontDescription('sans bold 14'))

        # Set the log_view to not editable
        self.log_view.set_editable(False)

        # Set the cursor to not visible
        self.log_view.set_cursor_visible(False)

        # Set the justification to center
        self.log_view.set_justification(gtk.JUSTIFY_CENTER)

        # Create a scrollable window for the log_view
        self.scrolled_window = gtk.ScrolledWindow()

        # Set scrollable window policies
        self.scrolled_window.set_policy(gtk.POLICY_AUTOMATIC, gtk.POLICY_AUTOMATIC)

        # Connect log_view and scrolled window
        self.scrolled_window.add(self.log_view)

        # Insert the log_view into the upper half
        self.table.attach(self.scrolled_window, 0, 1, 0, 3)

        # Display the log_view
        self.log_view.show()

        # Display the scrolled_window
        self.scrolled_window.show()
        
        # Settings start here
        self.settings_table = gtk.Table(15, 6, True)
        
        # Topic table
        self.topic_table = gtk.Table(15, 6, True)
        
        # Separate table for start button
        self.table_with_start = gtk.Table(15, 6, True)
        
        # Insert the settings window into the right half of the screen
        self.table.attach(self.settings_table, 1, 2, 0, 5)
        
        # Insert the topic window into the right half of the screen
        self.table.attach(self.topic_table, 1, 2, 0, 5)
        
        # Insert the table for start button into the right half of the screen
        self.table.attach(self.table_with_start, 1, 2, 0, 5) 

        # Display the settings_table
        self.settings_table.show()
        
        # Disply the topic table
        self.topic_table.show()
        
        # Display the table_with_start
        self.table_with_start.show()
          
        # Display the table
        self.table.show()
        
    def register(self, sess, co):
        """register _after_ Session and Coach have been instantiated"""
        self._sess = sess
        self._co = co
        
    def update_time(self):
        minutes, seconds = divmod(self.stopwatch.elapsed, 60)
        if(minutes < 10 and seconds < 10):
            time = "0" + str(int(minutes)) + ":" + "0" + str(int(seconds))
        if(minutes > 9 and seconds > 9):
            time = str(int(minutes)) + ":" + str(int(seconds))
        if(minutes > 9 and seconds < 10):
            time = str(int(minutes)) + ":" + "0" + str(int(seconds))
        if(minutes < 10 and seconds > 10):
            time = "0" + str(int(minutes)) + ":" + str(int(seconds))
        self.stopwatch_label.set_label(time)
        self.stopwatch_label.queue_draw()
        return True

        
        
    def draw_result_screen(self):
        """RENAME to draw_feedback_screen"""
        # Section for stopwatch
        self.stopwatch = Timer()
        self.stopwatch_label = gtk.Label("00:00")
        self.stopwatch_label.modify_font(pango.FontDescription("sans 16"))
        self.table_with_start.attach(self.stopwatch_label, 3, 5, 12, 13)
        
        # Section for nickname
        self.name = profile.get_nick_name()
        self.name_label = gtk.Label(self.name)
        self.name_label.modify_font(pango.FontDescription("sans 16"))
        self.table_with_start.attach(self.name_label, 0, 6, 13, 14)
        
        # Section for progress bar
        self.progressbar = gtk.ProgressBar(adjustment=None)
        
        # Color for progress bar
        style = self.progressbar.get_style()
        style.bg[gtk.STATE_PRELIGHT] = gtk.gdk.color_parse("green")
        self.progressbar.set_style (style)
        self.progressbar.set_fraction(0)      
        self.table_with_start.attach(self.progressbar, 0, 6, 8, 9)

        # Labels for progress bar
        self.progress0 = gtk.Label("0")
        self.progress0.modify_font(pango.FontDescription("sans 16"))
        self.table_with_start.attach(self.progress0, 0, 1, 9, 10 )
        
        # Labels for status update
        self.correct_count = 0
        self.correct_counter = gtk.Label(str(self.correct_count))
        self.correct_counter.modify_font(pango.FontDescription("sans 16"))
       
        
        # Ugly code for label color
        attr = pango.AttrList()
        fg_color = pango.AttrForeground(0, 65535, 0, 0, 6)
        attr.insert(fg_color) 
        self.correct_counter.set_attributes(attr)

        self.table_with_start.attach(self.correct_counter, 2, 4, 9, 10 ) 
        
        self.false_count = 0
        self.false_counter = gtk.Label(str(self.false_count))
        self.false_counter.modify_font(pango.FontDescription("sans 16"))
        
        # Ugly code for label color
        attr = pango.AttrList()
        fg_color = pango.AttrForeground(0, 0, 65535, 0, 6)
        attr.insert(fg_color) 
        self.false_counter.set_attributes(attr)
        
        self.table_with_start.attach(self.false_counter, 2, 4, 10, 11 )
        
        self.stopwatch_label.show()
        gobject.timeout_add(1000, self.update_time)
        self.name_label.show()
        self.progressbar.show()
        self.progress0.show()
        self.correct_counter.show()
        self.false_counter.show()
        
        self.total_calcs = self._ex.count()
        self.progress_total = gtk.Label(str(self.total_calcs))
        self.progress_total.modify_font(pango.FontDescription("sans 16"))
        self.table_with_start.attach(self.progress_total, 5, 6, 9, 10 )
        self.progress_total.show()
        
    def hide_result_screen(self):
        self.progressbar.set_fraction(0)
        self.stopwatch_label.hide()
        self.name_label.hide()
        self.progressbar.hide()
        self.progress0.hide()
        self.correct_counter.hide()
        self.false_counter.hide()
        self.progress_total.hide()
        
    def offer_setting(self,ex):
        self._ex = ex
        self._sett = self._ex.get_setting()
        
        ### START BUTTON BEGIN ###
        self.start_button = gtk.Button(None, gtk.STOCK_GO_FORWARD) 
        self.start_button.connect("clicked", self.clicked_start_callback)     
        self.table_with_start.attach(self.start_button, 0, 6, 14, 15)
        self.start_alignment = self.start_button.get_children()[0]
        self.start_hbox = self.start_alignment.get_children()[0]
        self.start_image, self.start_label = self.start_hbox.get_children()
        self.start_label.set_label("")
        self.start_button.show()
        ### START BUTTON END ###
        
        self.current_exercise = ex
        self.current_exercise.define_buttons()
        self.current_exercise.set_buttons(self._sett)
        
    def clicked_start_callback(self, widget):
        if( self.running == False):
            self.running = True
            self.start_button.set_label(gtk.STOCK_STOP)     
            self.start_alignment = self.start_button.get_children()[0]
            self.start_hbox = self.start_alignment.get_children()[0]
            self.start_image, self.start_label = self.start_hbox.get_children()
            self.start_label.set_label("")  
            self._co.notify(('setting-done', self._sett))
            self.settings_table.hide()
            self.topic_table.hide()
            self.draw_result_screen()
        elif( self.running == True):
            self.protocol('----------------------------------------', 0, 'OK')
            self.running = False
            self.start_button.set_label(gtk.STOCK_GO_FORWARD)     
            self.start_alignment = self.start_button.get_children()[0]
            self.start_hbox = self.start_alignment.get_children()[0]
            self.start_image, self.start_label = self.start_hbox.get_children()
            self.start_label.set_label("")
            self.display_table.destroy()      
            self.hide_result_screen()
            self.settings_table.show()
            self.topic_table.show()

    def init_calc(self):
        """
        prepares for calculations from 1 setting.
        for instance, a calculation might be on 1 ore more lines.
        """
        print("DEL do Display.init_calc")
        # make empty lines such that all calcs are entered at bottom
        for i in range(1,21):
            end_iterator = self.log_buffer.get_end_iter()
            self.log_buffer.insert(end_iterator, "\n")     
            self.log_view.scroll_mark_onscreen(self.log_buffer.get_insert())
            

        
    
    def destroy_box(self):
        self.calculation_box.destroy()
        
    def protocol(self, full_line, errors, feedback):
        end_iterator = self.log_buffer.get_end_iter()

        if( feedback == 'OK' ):
            self.log_buffer.insert_with_tags_by_name(end_iterator, "\n" + full_line, "correct" )
        elif ( feedback == 'XXX' ):
            self.log_buffer.insert_with_tags_by_name(end_iterator, "\n" + full_line, "error" )
        end_iterator = self.log_buffer.get_end_iter()  
        mark = self.log_buffer.create_mark(None, end_iterator, True)   
        self.log_view.scroll_mark_onscreen(mark)

#    def dis_calc(self, clist, cursor, errs): 
#        _i, _calc = 0, ''       
#        for _c in clist: 
#            _i = _i + 1 
#            if (_i == cursor) & (errs > 0):
#                _calc = _calc + '_'
#            else: 
#                _calc = _calc + _c                 
#        return _calc + ' ' + errs * '/'
                
    def input_digit(self, widget, dig, proterr, protok):
        """callback: input a digit and give feedback.
        The _only_ other active widget is the <stop>-button on the right"""
        entry_text = widget.get_text()
        ### bitte anzeigen !???????
        if(entry_text == dig):

            self.errors = 0 #WN090518 ???
            self.protocol(protok, self.errors, 'OK')
            self.destroy_box()
            self.notify(('digit-done', None))
        elif(entry_text == ""):
            pass #otherwise feedback in protocol written twice: see entry.set_text("") below
        else:
            self.false_count = self.false_count + 1
            self.false_counter.set_text(str(self.false_count))
            self.errors = self.errors + 1
            widget.set_text("")
            self.protocol(proterr, self.errors, 'XXX')
            

    #WN090518
    def display_calc(self, lines):
    
        self.display_table = gtk.Table(5, 1, True)    
        self.table.attach(self.display_table, 0, 1, 0, 5)           
        self.display_table.show()
        
        """display the lines of a calc with _ at all input positions"""
        lino = 0
        for li in lines:
            print('in Display.display_calc, line=', li)
            self.create_entryline((lino, -1, 'dummy-dig', 'dummy-proterr', 'dummy-protok', li))
            lino = lino + 1

            
    def create_entryline(self, (lineno, linepos, dig, proterr, protok, line)):
        """create gtk.Entry in line at linepos and set callback_input_digit"""
        print('in Display.create_entryline: lineno=', lineno, ', linepos=',
              linepos, ', line=', line)
        calculation, cursor = line, linepos
        self.calculation_box = gtk.HBox(True, 0)
        calc_pos = 0
        self.display_table.attach(self.calculation_box, 0, 1, 3 + lineno, 4 + lineno)
        for i in calculation:
            if (calc_pos != cursor):  
                self.label = gtk.Label(i)      
                self.label.modify_font(pango.FontDescription("sans 24"))
                self.calculation_box.pack_start(self.label)
                self.label.show()            
            else: # prepare for input
                self.text_entry = gtk.Entry(max = 1)
                self.text_entry.modify_font(pango.FontDescription("sans 24"))
                self.text_entry.connect("changed", self.input_digit, dig, proterr, protok)
                self.calculation_box.pack_start(self.text_entry)
                self.text_entry.show()        
            calc_pos = calc_pos + 1 
        #?kann m.die calculation_box ZUERST aufbauen und DANN self.table.attach
        self.calculation_box.show()
        
        if(cursor != -1):
            self.text_entry.grab_focus()
        #just add lineno to table.attach
        #TODO rename calculation, cursor below ...
        #TODO remove hack on callback:
        #self.input_digit('widget', dig, protline)
    
        
    def finish_calc(self):
        self.stopwatch.stop()
    
                
    def notify(self, msg):
        """only used by gtk"""
        if msg[0] == 'digit-done':
            self._sess.notify(('digit-done', None))

    def show_progress(self):
        self.progressbar.set_fraction(self.progressbar.get_fraction()+(float(1)/float(self.total_calcs)))
        self.correct_count = self.correct_count + 1
        self.correct_counter.set_text(str(self.correct_count))
        self.display_table.destroy()

        
    def offer_topics(self, topics):
        """TODO: get the users choice from buttons above the settings"""
        self.topic_box = gtk.HBox(True, 0)
        self.topic_table.attach(self.topic_box, 0, 6, 0, 1)
        
        _i = 0
        for _t in topics:
            _i = _i + 1
            self.button = gtk.Button()
            self.image = gtk.Image()
            
            if(_t == 'addsub_simp'):
                self.image.set_from_file("img/addsub_simp.jpg")
            elif(_t == 'passten'):
                self.image.set_from_file("img/passten.jpg")
            elif(_t == 'times_div'):
                self.image.set_from_file("img/times_div.jpg")

            self.button.set_image(self.image)
            self.button.connect("clicked", self.new_topic, _t)
            self.topic_box.pack_start(self.button)
            self.button.show()
            
        self.topic_box.show()
            
         
    def new_topic(self, widget, topic):
        """callback:
        TODO: get the users choice from buttons above the settings"""
        
        if(self.active_topic == None):
            self.active_topic = topic
            self._co.notify(('new-topic', topic))
        
        elif(self.active_topic == topic):
            pass
        
        elif(self.active_topic != topic):
            self.active_topic = topic
            self.settings_table.destroy()
            self.settings_table = gtk.Table(15, 6, True)
            self.table.attach(self.settings_table, 1, 2, 0, 5)
            self.settings_table.show()
            
            self.table_with_start.destroy()
            self.table_with_start = gtk.Table(15, 6, True)
            self.table.attach(self.table_with_start, 1, 2, 0, 5)
            self.table_with_start.show()
            self._co.notify(('new-topic', topic))
            
            
        
        
        
