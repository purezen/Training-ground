## Process this file with automake to produce Makefile.in

## Created by Anjuta



AM_CPPFLAGS = \
	-DPACKAGE_LOCALE_DIR=\""$(localedir)"\" \
	-DPACKAGE_SRC_DIR=\""$(srcdir)"\" \
	-DPACKAGE_DATA_DIR=\""$(pkgdatadir)"\" \
	$(TRY_GRID_CFLAGS)

AM_CFLAGS =\
	 -Wall\
	 -g

bin_PROGRAMS = try_grid

try_grid_SOURCES = \
	main.c

try_grid_LDFLAGS = \
	-Wl,--export-dynamic

try_grid_LDADD = $(TRY_GRID_LIBS)


