#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gjs
Version  : 1.66.1
Release  : 55
URL      : https://download.gnome.org/sources/gjs/1.66/gjs-1.66.1.tar.xz
Source0  : https://download.gnome.org/sources/gjs/1.66/gjs-1.66.1.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : LGPL-2.0 MIT
Requires: gjs-bin = %{version}-%{release}
Requires: gjs-data = %{version}-%{release}
Requires: gjs-lib = %{version}-%{release}
Requires: gjs-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : glibc-bin
BuildRequires : gobject-introspection-dev
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(mozjs-78)
BuildRequires : readline-dev
BuildRequires : sysprof-dev
BuildRequires : sysprof-staticdev
BuildRequires : valgrind

%description
In order to run those example scripts, do:
gjs-console script-filename.js

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


%package tests
Summary: tests components for the gjs package.
Group: Default
Requires: gjs = %{version}-%{release}

%description tests
tests components for the gjs package.


%prep
%setup -q -n gjs-1.66.1
cd %{_builddir}/gjs-1.66.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602218045
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$FFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dskip_gtk_tests=true -Dreadline=disabled  builddir
ninja -v -C builddir

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir || :

%install
mkdir -p %{buildroot}/usr/share/package-licenses/gjs
cp %{_builddir}/gjs-1.66.1/COPYING %{buildroot}/usr/share/package-licenses/gjs/2d6aed797eaffddd3655b309f02e4956183adf0c
cp %{_builddir}/gjs-1.66.1/COPYING.LGPL %{buildroot}/usr/share/package-licenses/gjs/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f
DESTDIR=%{buildroot} ninja -C builddir install

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
/usr/share/package-licenses/gjs/2d6aed797eaffddd3655b309f02e4956183adf0c
/usr/share/package-licenses/gjs/bf50bac24e7ec325dbb09c6b6c4dcc88a7d79e8f

%files tests
%defattr(-,root,root,-)
/usr/libexec/installed-tests/gjs/GIMarshallingTests-1.0.typelib
/usr/libexec/installed-tests/gjs/Regress-1.0.typelib
/usr/libexec/installed-tests/gjs/WarnLib-1.0.typelib
/usr/libexec/installed-tests/gjs/debugger-test.sh
/usr/libexec/installed-tests/gjs/debugger/backtrace.debugger
/usr/libexec/installed-tests/gjs/debugger/backtrace.debugger.js
/usr/libexec/installed-tests/gjs/debugger/backtrace.debugger.output
/usr/libexec/installed-tests/gjs/debugger/breakpoint.debugger
/usr/libexec/installed-tests/gjs/debugger/breakpoint.debugger.js
/usr/libexec/installed-tests/gjs/debugger/breakpoint.debugger.output
/usr/libexec/installed-tests/gjs/debugger/continue.debugger
/usr/libexec/installed-tests/gjs/debugger/continue.debugger.js
/usr/libexec/installed-tests/gjs/debugger/continue.debugger.output
/usr/libexec/installed-tests/gjs/debugger/delete.debugger
/usr/libexec/installed-tests/gjs/debugger/delete.debugger.js
/usr/libexec/installed-tests/gjs/debugger/delete.debugger.output
/usr/libexec/installed-tests/gjs/debugger/detach.debugger
/usr/libexec/installed-tests/gjs/debugger/detach.debugger.js
/usr/libexec/installed-tests/gjs/debugger/detach.debugger.output
/usr/libexec/installed-tests/gjs/debugger/down-up.debugger
/usr/libexec/installed-tests/gjs/debugger/down-up.debugger.js
/usr/libexec/installed-tests/gjs/debugger/down-up.debugger.output
/usr/libexec/installed-tests/gjs/debugger/finish.debugger
/usr/libexec/installed-tests/gjs/debugger/finish.debugger.js
/usr/libexec/installed-tests/gjs/debugger/finish.debugger.output
/usr/libexec/installed-tests/gjs/debugger/frame.debugger
/usr/libexec/installed-tests/gjs/debugger/frame.debugger.js
/usr/libexec/installed-tests/gjs/debugger/frame.debugger.output
/usr/libexec/installed-tests/gjs/debugger/keys.debugger
/usr/libexec/installed-tests/gjs/debugger/keys.debugger.js
/usr/libexec/installed-tests/gjs/debugger/keys.debugger.output
/usr/libexec/installed-tests/gjs/debugger/next.debugger
/usr/libexec/installed-tests/gjs/debugger/next.debugger.js
/usr/libexec/installed-tests/gjs/debugger/next.debugger.output
/usr/libexec/installed-tests/gjs/debugger/print.debugger
/usr/libexec/installed-tests/gjs/debugger/print.debugger.js
/usr/libexec/installed-tests/gjs/debugger/print.debugger.output
/usr/libexec/installed-tests/gjs/debugger/quit.debugger
/usr/libexec/installed-tests/gjs/debugger/quit.debugger.js
/usr/libexec/installed-tests/gjs/debugger/quit.debugger.output
/usr/libexec/installed-tests/gjs/debugger/return.debugger
/usr/libexec/installed-tests/gjs/debugger/return.debugger.js
/usr/libexec/installed-tests/gjs/debugger/return.debugger.output
/usr/libexec/installed-tests/gjs/debugger/set.debugger
/usr/libexec/installed-tests/gjs/debugger/set.debugger.js
/usr/libexec/installed-tests/gjs/debugger/set.debugger.output
/usr/libexec/installed-tests/gjs/debugger/step.debugger
/usr/libexec/installed-tests/gjs/debugger/step.debugger.js
/usr/libexec/installed-tests/gjs/debugger/step.debugger.output
/usr/libexec/installed-tests/gjs/debugger/throw.debugger
/usr/libexec/installed-tests/gjs/debugger/throw.debugger.js
/usr/libexec/installed-tests/gjs/debugger/throw.debugger.output
/usr/libexec/installed-tests/gjs/debugger/until.debugger
/usr/libexec/installed-tests/gjs/debugger/until.debugger.js
/usr/libexec/installed-tests/gjs/debugger/until.debugger.output
/usr/libexec/installed-tests/gjs/js/testByteArray.js
/usr/libexec/installed-tests/gjs/js/testCairo.js
/usr/libexec/installed-tests/gjs/js/testExceptions.js
/usr/libexec/installed-tests/gjs/js/testFormat.js
/usr/libexec/installed-tests/gjs/js/testFundamental.js
/usr/libexec/installed-tests/gjs/js/testGDBus.js
/usr/libexec/installed-tests/gjs/js/testGIMarshalling.js
/usr/libexec/installed-tests/gjs/js/testGLib.js
/usr/libexec/installed-tests/gjs/js/testGObject.js
/usr/libexec/installed-tests/gjs/js/testGObjectClass.js
/usr/libexec/installed-tests/gjs/js/testGObjectInterface.js
/usr/libexec/installed-tests/gjs/js/testGTypeClass.js
/usr/libexec/installed-tests/gjs/js/testGettext.js
/usr/libexec/installed-tests/gjs/js/testGio.js
/usr/libexec/installed-tests/gjs/js/testImporter.js
/usr/libexec/installed-tests/gjs/js/testIntrospection.js
/usr/libexec/installed-tests/gjs/js/testLang.js
/usr/libexec/installed-tests/gjs/js/testLegacyByteArray.js
/usr/libexec/installed-tests/gjs/js/testLegacyClass.js
/usr/libexec/installed-tests/gjs/js/testLegacyGObject.js
/usr/libexec/installed-tests/gjs/js/testMainloop.js
/usr/libexec/installed-tests/gjs/js/testNamespace.js
/usr/libexec/installed-tests/gjs/js/testPackage.js
/usr/libexec/installed-tests/gjs/js/testParamSpec.js
/usr/libexec/installed-tests/gjs/js/testPrint.js
/usr/libexec/installed-tests/gjs/js/testRegress.js
/usr/libexec/installed-tests/gjs/js/testSignals.js
/usr/libexec/installed-tests/gjs/js/testSystem.js
/usr/libexec/installed-tests/gjs/js/testTweener.js
/usr/libexec/installed-tests/gjs/js/testWarnLib.js
/usr/libexec/installed-tests/gjs/js/testself.js
/usr/libexec/installed-tests/gjs/libgimarshallingtests.so
/usr/libexec/installed-tests/gjs/libregress.so
/usr/libexec/installed-tests/gjs/libwarnlib.so
/usr/libexec/installed-tests/gjs/minijasmine
/usr/libexec/installed-tests/gjs/scripts/testCommandLine.sh
/usr/libexec/installed-tests/gjs/scripts/testWarnings.sh
/usr/share/installed-tests/gjs/backtrace.test
/usr/share/installed-tests/gjs/breakpoint.test
/usr/share/installed-tests/gjs/continue.test
/usr/share/installed-tests/gjs/delete.test
/usr/share/installed-tests/gjs/detach.test
/usr/share/installed-tests/gjs/down-up.test
/usr/share/installed-tests/gjs/finish.test
/usr/share/installed-tests/gjs/frame.test
/usr/share/installed-tests/gjs/keys.test
/usr/share/installed-tests/gjs/next.test
/usr/share/installed-tests/gjs/print.test
/usr/share/installed-tests/gjs/quit.test
/usr/share/installed-tests/gjs/return.test
/usr/share/installed-tests/gjs/set.test
/usr/share/installed-tests/gjs/step.test
/usr/share/installed-tests/gjs/testByteArray.test
/usr/share/installed-tests/gjs/testCairo.test
/usr/share/installed-tests/gjs/testCommandLine.sh.test
/usr/share/installed-tests/gjs/testExceptions.test
/usr/share/installed-tests/gjs/testFormat.test
/usr/share/installed-tests/gjs/testFundamental.test
/usr/share/installed-tests/gjs/testGDBus.test
/usr/share/installed-tests/gjs/testGIMarshalling.test
/usr/share/installed-tests/gjs/testGLib.test
/usr/share/installed-tests/gjs/testGObject.test
/usr/share/installed-tests/gjs/testGObjectClass.test
/usr/share/installed-tests/gjs/testGObjectInterface.test
/usr/share/installed-tests/gjs/testGTypeClass.test
/usr/share/installed-tests/gjs/testGettext.test
/usr/share/installed-tests/gjs/testGio.test
/usr/share/installed-tests/gjs/testImporter.test
/usr/share/installed-tests/gjs/testIntrospection.test
/usr/share/installed-tests/gjs/testLang.test
/usr/share/installed-tests/gjs/testLegacyByteArray.test
/usr/share/installed-tests/gjs/testLegacyClass.test
/usr/share/installed-tests/gjs/testLegacyGObject.test
/usr/share/installed-tests/gjs/testMainloop.test
/usr/share/installed-tests/gjs/testNamespace.test
/usr/share/installed-tests/gjs/testPackage.test
/usr/share/installed-tests/gjs/testParamSpec.test
/usr/share/installed-tests/gjs/testPrint.test
/usr/share/installed-tests/gjs/testRegress.test
/usr/share/installed-tests/gjs/testSignals.test
/usr/share/installed-tests/gjs/testSystem.test
/usr/share/installed-tests/gjs/testTweener.test
/usr/share/installed-tests/gjs/testWarnLib.test
/usr/share/installed-tests/gjs/testWarnings.sh.test
/usr/share/installed-tests/gjs/testself.test
/usr/share/installed-tests/gjs/throw.test
/usr/share/installed-tests/gjs/until.test
