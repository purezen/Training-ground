/* -*- Mode: C; indent-tabs-mode: t; c-basic-offset: 4; tab-width: 4 -*-  */
/*
 * main.c
 * Copyright (C) 2012 Aditya <aditya@aditya-HP-Pavilion-dv6-Notebook-PC>
 * 
 * try_grid is free software: you can redistribute it and/or modify it
 * under the terms of the GNU General Public License as published by the
 * Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 * 
 * try_grid is distributed in the hope that it will be useful, but
 * WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
 * See the GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License along
 * with this program.  If not, see <http://www.gnu.org/licenses/>.
 */

#include<gtk/gtk.h>

static void print_it(GtkWidget *widget, gpointer data)
{
	g_print ("Hello everyone..:)\n");
}


int main(int argc, char* argv[])
{
	GtkWidget *window;
	GtkWidget *grid;
	GtkWidget *button;

	gtk_init (&argc, &argv);

	window = gtk_window_new (GTK_WINDOW_TOPLEVEL);
	gtk_window_set_title (GTK_WINDOW(window),"Grid practice");
	g_signal_connect (window, "destroy", gtk_main_quit,NULL);

	grid = gtk_grid_new ();

	gtk_container_add (GTK_CONTAINER (window), grid);

	button = gtk_button_new_with_label ("Button 1");
	g_signal_connect(button,"clicked", G_CALLBACK(print_it),NULL);

	gtk_grid_attach (GTK_GRID(grid), button, 0,0,1,1);

	button = gtk_button_new_with_label ("Button 2");
	g_signal_connect(button, "clicked", G_CALLBACK(print_it),NULL);

	gtk_grid_attach (GTK_GRID (grid), button,0,1,1,1);

	button = gtk_button_new_with_label ("<--Exit-->");
	g_signal_connect(button, "clicked", G_CALLBACK(gtk_main_quit),NULL);

	gtk_grid_attach (GTK_GRID (grid), button,1,0,2,2);

	gtk_widget_show_all (window);

	gtk_main ();

	return 0;
}