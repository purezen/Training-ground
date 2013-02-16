# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

#Added later

import gettext
from gettext import gettext as _
gettext.textdomain('mybrowser')

#till here

from locale import gettext as _

from gi.repository import Gtk, WebKit # pylint: disable=E0611
import logging
logger = logging.getLogger('new_project')

from new_project_lib import Window
from new_project.AboutNewProjectDialog import AboutNewProjectDialog
from new_project.PreferencesNewProjectDialog import PreferencesNewProjectDialog

# See new_project_lib.Window.py for more details about how this class works
class NewProjectWindow(Window):
    __gtype_name__ = "NewProjectWindow"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the main window"""
        super(NewProjectWindow, self).finish_initializing(builder)

        self.AboutDialog = AboutNewProjectDialog
        self.PreferencesDialog = PreferencesNewProjectDialog

        # Code for other initialization actions should be added here.

        self.refreshbutton = self.builder.get_object("refreshbutton")
        self.urlentry = self.builder.get_object("urlentry")
        self.scrolledwindow = self.builder.get_object("scrollwindow")
        self.toolbar = self.builder.get_object("toolbar")

        content = self.toolbar.get_style_context()
        context.add_class(Gtk.STYLE_CLASS_PRIMARY_TOOLBAR)

        self.webview = WebKit.WebView()

        self.scrolledwindow.add(self.webview)
        self.webview.show()

    def on_refreshbutton_clicked(self, widget):
        print "refresh"

    def on_urlentry_activate(self, widget):
        url = widget.get_text()
        
        self.webview.open(url)
