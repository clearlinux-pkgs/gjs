#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: meson
# autospec version: v5
# autospec commit: c02b2fe
#
Name     : gjs
Version  : 1.80.1
Release  : 99
URL      : https://download.gnome.org/sources/gjs/1.80/gjs-1.80.1.tar.xz
Source0  : https://download.gnome.org/sources/gjs/1.80/gjs-1.80.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 MIT MPL-1.1 MPL-2.0
Requires: gjs-bin = %{version}-%{release}
Requires: gjs-data = %{version}-%{release}
Requires: gjs-lib = %{version}-%{release}
Requires: gjs-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : glibc-bin
BuildRequires : gobject-introspection-dev
BuildRequires : gtk4-dev
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(mozjs-115)
BuildRequires : readline-dev
BuildRequires : sysprof-dev
BuildRequires : sysprof-staticdev
BuildRequires : valgrind
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
In order to run those example scripts, do:
```sh
gjs -m script-filename.js
```

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
%setup -q -n gjs-1.80.1
cd %{_builddir}/gjs-1.80.1
pushd ..
cp -a gjs-1.80.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1711378393
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dskip_gtk_tests=true \
-Dreadline=disabled \
-Dinstalled_tests=false  builddir
ninja -v -C builddir
GOAMD64=v3
CFLAGS="$CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " CXXFLAGS="$CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -march=x86-64-v3 " meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dskip_gtk_tests=true \
-Dreadline=disabled \
-Dinstalled_tests=false  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
mkdir -p %{buildroot}/usr/share/package-licenses/gjs
cp %{_builddir}/gjs-%{version}/LICENSES/BSD-3-Clause.txt %{buildroot}/usr/share/package-licenses/gjs/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c || :
cp %{_builddir}/gjs-%{version}/LICENSES/CC0-1.0.txt %{buildroot}/usr/share/package-licenses/gjs/8287b608d3fa40ef401339fd907ca1260c964123 || :
cp %{_builddir}/gjs-%{version}/LICENSES/GPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/gjs/e712eadfab0d2357c0f50f599ef35ee0d87534cb || :
cp %{_builddir}/gjs-%{version}/LICENSES/GPL-3.0-or-later.txt %{buildroot}/usr/share/package-licenses/gjs/6091db0aead0d90182b93d3c0d09ba93d188f907 || :
cp %{_builddir}/gjs-%{version}/LICENSES/LGPL-2.0-or-later.txt %{buildroot}/usr/share/package-licenses/gjs/20079e8f79713dce80ab09774505773c926afa2a || :
cp %{_builddir}/gjs-%{version}/LICENSES/LGPL-2.1-or-later.txt %{buildroot}/usr/share/package-licenses/gjs/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567 || :
cp %{_builddir}/gjs-%{version}/LICENSES/MIT.txt %{buildroot}/usr/share/package-licenses/gjs/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3 || :
cp %{_builddir}/gjs-%{version}/LICENSES/MPL-1.1.txt %{buildroot}/usr/share/package-licenses/gjs/c0a0e1595feceb8ecf63b095a3611d544ef9bba8 || :
cp %{_builddir}/gjs-%{version}/LICENSES/MPL-2.0.txt %{buildroot}/usr/share/package-licenses/gjs/67b089bde98b075d9aed0ca5a7d34c1bc78044d1 || :
cp %{_builddir}/gjs-%{version}/examples/test.jpg.license %{buildroot}/usr/share/package-licenses/gjs/213035d373bd94af036120780d18d42c9536f3bc || :
GOAMD64=v3
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
GOAMD64=v2
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/gjs/girepository-1.0/GjsPrivate-1.0.typelib

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/gjs-console
/usr/bin/gjs
/usr/bin/gjs-console

%files data
%defattr(-,root,root,-)
/usr/share/gjs-1.0/lsan/lsan.supp
/usr/share/gjs-1.0/valgrind/gjs.supp

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
/V3/usr/lib64/libgjs.so.0.0.0
/usr/lib64/libgjs.so.0
/usr/lib64/libgjs.so.0.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gjs/20079e8f79713dce80ab09774505773c926afa2a
/usr/share/package-licenses/gjs/213035d373bd94af036120780d18d42c9536f3bc
/usr/share/package-licenses/gjs/6091db0aead0d90182b93d3c0d09ba93d188f907
/usr/share/package-licenses/gjs/67b089bde98b075d9aed0ca5a7d34c1bc78044d1
/usr/share/package-licenses/gjs/81b58c89ceef8e9f8bd5d00a287edbd15f9d3567
/usr/share/package-licenses/gjs/8287b608d3fa40ef401339fd907ca1260c964123
/usr/share/package-licenses/gjs/9950d3fdce1cff1f71212fb5abd31453c6ee2f8c
/usr/share/package-licenses/gjs/a0193e3fccf86c17dc71e3f6c0ac0b535e06bea3
/usr/share/package-licenses/gjs/c0a0e1595feceb8ecf63b095a3611d544ef9bba8
/usr/share/package-licenses/gjs/e712eadfab0d2357c0f50f599ef35ee0d87534cb
