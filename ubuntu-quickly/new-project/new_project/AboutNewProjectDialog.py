# -*- Mode: Python; coding: utf-8; indent-tabs-mode: nil; tab-width: 4 -*-
### BEGIN LICENSE
# This file is in the public domain
### END LICENSE

from locale import gettext as _

import logging
logger = logging.getLogger('new_project')

from new_project_lib.AboutDialog import AboutDialog

# See new_project_lib.AboutDialog.py for more details about how this class works.
class AboutNewProjectDialog(AboutDialog):
    __gtype_name__ = "AboutNewProjectDialog"
    
    def finish_initializing(self, builder): # pylint: disable=E1002
        """Set up the about dialog"""
        super(AboutNewProjectDialog, self).finish_initializing(builder)

        # Code for other initialization actions should be added here.

        self.refreshbutton = self.builder.get_object("refreshbutton")
        self.urlentry = self.builder.get_clicked("urlentry")

    def on_refreshbutton_clicked(self, widget):
        print "refresh"
    def on_urlentry_activate(self, widget):
        print "Woo..!!"

