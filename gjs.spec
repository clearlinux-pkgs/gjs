#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gjs
Version  : 1.58.1
Release  : 39
URL      : https://download.gnome.org/sources/gjs/1.58/gjs-1.58.1.tar.xz
Source0  : https://download.gnome.org/sources/gjs/1.58/gjs-1.58.1.tar.xz
Summary  : JS bindings for GObjects
Group    : Development/Tools
License  : LGPL-2.0 MIT
Requires: gjs-bin = %{version}-%{release}
Requires: gjs-data = %{version}-%{release}
Requires: gjs-lib = %{version}-%{release}
Requires: gjs-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : glibc-bin
BuildRequires : gobject-introspection
BuildRequires : gobject-introspection-dev
BuildRequires : mozjs60
BuildRequires : mozjs60-dev
BuildRequires : mozjs60-lib
BuildRequires : pkgconfig(gobject-introspection-1.0)
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : readline-dev
BuildRequires : sed
BuildRequires : valgrind
Patch1: gc_a_little_more.patch

%description
[![Build Status](https://gitlab.gnome.org/GNOME/gjs/badges/master/build.svg)](https://gitlab.gnome.org/GNOME/gjs/pipelines)
[![Coverage report](https://gitlab.gnome.org/GNOME/gjs/badges/master/coverage.svg)](https://gnome.pages.gitlab.gnome.org/gjs/)
[![Contributors](https://img.shields.io/github/contributors/GNOME/gjs.svg)](https://gitlab.gnome.org/GNOME/gjs/graphs/master)
[![Last commit](https://img.shields.io/github/last-commit/GNOME/gjs.svg)](https://gitlab.gnome.org/GNOME/gjs/commits/master)
[![Search hit](https://img.shields.io/github/search/GNOME/gjs/goto.svg?label=github%20hits)](https://github.com/search?utf8=%E2%9C%93&q=gjs&type=)
[![License](https://img.shields.io/badge/License-LGPL%20v2%2B-blue.svg)](https://gitlab.gnome.org/GNOME/gjs/blob/master/COPYING)
[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://gitlab.gnome.org/GNOME/gjs/blob/master/COPYING)

%package bin
Summary: bin components for the gjs package.
Group: Binaries
Requires: gjs-data = %{version}-%{release}
Requires: gjs-license = %{version}-%{release}

%description bin
bin components for the gjs package.


%package data
Summary: data components for the gjs package.
Group: Data

%description data
data components for the gjs package.


%package dev
Summary: dev components for the gjs package.
Group: Development
Requires: gjs-lib = %{version}-%{release}
Requires: gjs-bin = %{version}-%{release}
Requires: gjs-data = %{version}-%{release}
Provides: gjs-devel = %{version}-%{release}
Requires: gjs = %{version}-%{release}

%description dev
dev components for the gjs package.


%package lib
Summary: lib components for the gjs package.
Group: Libraries
Requires: gjs-data = %{version}-%{release}
Requires: gjs-license = %{version}-%{release}

%description lib
lib components for the gjs package.


%package license
Summary: license components for the gjs package.
Group: Default

%description license
license components for the gjs package.


%prep
%setup -q -n gjs-1.58.1
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1570463084
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static --disable-readline
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1570463084
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gjs
cp COPYING %{buildroot}/usr/share/package-licenses/gjs/COPYING
cp COPYING.LGPL %{buildroot}/usr/share/package-licenses/gjs/COPYING.LGPL
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/gjs/girepository-1.0/GjsPrivate-1.0.typelib

%files bin
%defattr(-,root,root,-)
/usr/bin/gjs
/usr/bin/gjs-console

%files data
%defattr(-,root,root,-)
/usr/share/gjs-1.0/lsan/lsan.supp
/usr/share/gjs-1.0/valgrind/gjs.supp
/usr/share/glib-2.0/schemas/org.gnome.GjsTest.gschema.xml

%files dev
%defattr(-,root,root,-)
/usr/include/gjs-1.0/gjs/context.h
/usr/include/gjs-1.0/gjs/coverage.h
/usr/include/gjs-1.0/gjs/error-types.h
/usr/include/gjs-1.0/gjs/gjs.h
/usr/include/gjs-1.0/gjs/macros.h
/usr/include/gjs-1.0/gjs/mem.h
/usr/include/gjs-1.0/gjs/profiler.h
/usr/lib64/libgjs.so
/usr/lib64/pkgconfig/gjs-1.0.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libgjs.so.0
/usr/lib64/libgjs.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gjs/COPYING
/usr/share/package-licenses/gjs/COPYING.LGPL
