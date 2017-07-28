#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gjs
Version  : 1.48.6
Release  : 16
URL      : https://download.gnome.org/sources/gjs/1.48/gjs-1.48.6.tar.xz
Source0  : https://download.gnome.org/sources/gjs/1.48/gjs-1.48.6.tar.xz
Summary  : JS bindings for GObjects
Group    : Development/Tools
License  : LGPL-2.0 MIT
Requires: gjs-bin
Requires: gjs-lib
BuildRequires : gettext
BuildRequires : mozjs38-dev
BuildRequires : perl(XML::Parser)
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : readline-dev
BuildRequires : sed
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: trim.patch
Patch2: gc_a_little_more.patch

%description
JavaScript bindings for GNOME
=============================
Available as part of your GNOME distribution. Powers GNOME Shell, Polari,
GNOME Documents, and many other apps.

%package bin
Summary: bin components for the gjs package.
Group: Binaries

%description bin
bin components for the gjs package.


%package dev
Summary: dev components for the gjs package.
Group: Development
Requires: gjs-lib
Requires: gjs-bin
Provides: gjs-devel

%description dev
dev components for the gjs package.


%package lib
Summary: lib components for the gjs package.
Group: Libraries

%description lib
lib components for the gjs package.


%prep
%setup -q -n gjs-1.48.6
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1501204750
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -fno-semantic-interposition "
%configure --disable-static
make V=1  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1501204750
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/gjs/girepository-1.0/GjsPrivate-1.0.typelib

%files bin
%defattr(-,root,root,-)
/usr/bin/gjs
/usr/bin/gjs-console

%files dev
%defattr(-,root,root,-)
/usr/include/gjs-1.0/gjs/context.h
/usr/include/gjs-1.0/gjs/coverage.h
/usr/include/gjs-1.0/gjs/gjs.h
/usr/include/gjs-1.0/gjs/macros.h
/usr/include/gjs-1.0/util/error.h
/usr/lib64/libgjs.so
/usr/lib64/pkgconfig/gjs-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgjs.so.0
/usr/lib64/libgjs.so.0.0.0
