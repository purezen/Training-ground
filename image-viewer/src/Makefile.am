## Process this file with automake to produce Makefile.in

## Created by Anjuta



AM_CPPFLAGS = \
	-DPACKAGE_LOCALE_DIR=\""$(localedir)"\" \
	-DPACKAGE_SRC_DIR=\""$(srcdir)"\" \
	-DPACKAGE_DATA_DIR=\""$(pkgdatadir)"\" \
	$(IMAGE_VIEWER_CFLAGS)

AM_CFLAGS =\
	 -Wall\
	 -g

bin_PROGRAMS = image_viewer

image_viewer_SOURCES = \
	main.c

image_viewer_LDFLAGS = \
	-Wl,--export-dynamic

image_viewer_LDADD = $(IMAGE_VIEWER_LIBS)


