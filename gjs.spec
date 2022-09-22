#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gjs
Version  : 1.74.0
Release  : 78
URL      : https://download.gnome.org/sources/gjs/1.74/gjs-1.74.0.tar.xz
Source0  : https://download.gnome.org/sources/gjs/1.74/gjs-1.74.0.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.0 LGPL-2.1 MIT MPL-1.1 MPL-2.0
Requires: gjs-bin = %{version}-%{release}
Requires: gjs-data = %{version}-%{release}
Requires: gjs-filemap = %{version}-%{release}
Requires: gjs-lib = %{version}-%{release}
Requires: gjs-license = %{version}-%{release}
BuildRequires : buildreq-gnome
BuildRequires : buildreq-meson
BuildRequires : glibc-bin
BuildRequires : gobject-introspection-dev
BuildRequires : pkgconfig(gtk+-3.0)
BuildRequires : pkgconfig(libxml-2.0)
BuildRequires : pkgconfig(mozjs-102)
BuildRequires : readline-dev
BuildRequires : sysprof-dev
BuildRequires : sysprof-staticdev
BuildRequires : valgrind

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
Requires: gjs-filemap = %{version}-%{release}

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


%package filemap
Summary: filemap components for the gjs package.
Group: Default

%description filemap
filemap components for the gjs package.


%package lib
Summary: lib components for the gjs package.
Group: Libraries
Requires: gjs-data = %{version}-%{release}
Requires: gjs-license = %{version}-%{release}
Requires: gjs-filemap = %{version}-%{release}

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
%setup -q -n gjs-1.74.0
cd %{_builddir}/gjs-1.74.0
pushd ..
cp -a gjs-1.74.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1663870630
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -ffat-lto-objects -flto=auto -fno-semantic-interposition -mprefer-vector-width=256 "
CFLAGS="$CFLAGS" CXXFLAGS="$CXXFLAGS" LDFLAGS="$LDFLAGS" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dskip_gtk_tests=true \
-Dreadline=disabled  builddir
ninja -v -C builddir
CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 -O3" CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 " LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3" meson --libdir=lib64 --prefix=/usr --buildtype=plain -Dskip_gtk_tests=true \
-Dreadline=disabled  builddiravx2
ninja -v -C builddiravx2

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
meson test -C builddir --print-errorlogs || :

%install
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
DESTDIR=%{buildroot}-v3 ninja -C builddiravx2 install
DESTDIR=%{buildroot} ninja -C builddir install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)
/usr/lib64/gjs/girepository-1.0/GjsPrivate-1.0.typelib

%files bin
%defattr(-,root,root,-)
/usr/bin/gjs
/usr/bin/gjs-console
/usr/share/clear/optimized-elf/bin*

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
/usr/lib64/glibc-hwcaps/x86-64-v3/libgjs.so
/usr/lib64/libgjs.so
/usr/lib64/pkgconfig/gjs-1.0.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-gjs

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libgjs.so.0
/usr/lib64/glibc-hwcaps/x86-64-v3/libgjs.so.0.0.0
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

%files tests
%defattr(-,root,root,-)
/usr/libexec/installed-tests/gjs/GIMarshallingTests-1.0.typelib
/usr/libexec/installed-tests/gjs/GjsTestTools-1.0.typelib
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
/usr/libexec/installed-tests/gjs/debugger/lastvalues.debugger
/usr/libexec/installed-tests/gjs/debugger/lastvalues.debugger.js
/usr/libexec/installed-tests/gjs/debugger/lastvalues.debugger.output
/usr/libexec/installed-tests/gjs/debugger/list.debugger
/usr/libexec/installed-tests/gjs/debugger/list.debugger.js
/usr/libexec/installed-tests/gjs/debugger/list.debugger.output
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
/usr/libexec/installed-tests/gjs/debugger/throw-ignored.debugger
/usr/libexec/installed-tests/gjs/debugger/throw-ignored.debugger.js
/usr/libexec/installed-tests/gjs/debugger/throw-ignored.debugger.output
/usr/libexec/installed-tests/gjs/debugger/throw.debugger
/usr/libexec/installed-tests/gjs/debugger/throw.debugger.js
/usr/libexec/installed-tests/gjs/debugger/throw.debugger.output
/usr/libexec/installed-tests/gjs/debugger/until.debugger
/usr/libexec/installed-tests/gjs/debugger/until.debugger.js
/usr/libexec/installed-tests/gjs/debugger/until.debugger.output
/usr/libexec/installed-tests/gjs/js/matchers.js
/usr/libexec/installed-tests/gjs/js/modules/alwaysThrows.js
/usr/libexec/installed-tests/gjs/js/modules/badOverrides/.eslintrc.yml
/usr/libexec/installed-tests/gjs/js/modules/badOverrides/GIMarshallingTests.js
/usr/libexec/installed-tests/gjs/js/modules/badOverrides/Gio.js
/usr/libexec/installed-tests/gjs/js/modules/badOverrides/Regress.js
/usr/libexec/installed-tests/gjs/js/modules/badOverrides/WarnLib.js
/usr/libexec/installed-tests/gjs/js/modules/data.txt
/usr/libexec/installed-tests/gjs/js/modules/dynamic.js
/usr/libexec/installed-tests/gjs/js/modules/encodings.json
/usr/libexec/installed-tests/gjs/js/modules/exports.js
/usr/libexec/installed-tests/gjs/js/modules/foobar.js
/usr/libexec/installed-tests/gjs/js/modules/importmeta.js
/usr/libexec/installed-tests/gjs/js/modules/lexicalScope.js
/usr/libexec/installed-tests/gjs/js/modules/modunicode.js
/usr/libexec/installed-tests/gjs/js/modules/mutualImport/a.js
/usr/libexec/installed-tests/gjs/js/modules/mutualImport/b.js
/usr/libexec/installed-tests/gjs/js/modules/overrides/.eslintrc.yml
/usr/libexec/installed-tests/gjs/js/modules/overrides/GIMarshallingTests.js
/usr/libexec/installed-tests/gjs/js/modules/say.js
/usr/libexec/installed-tests/gjs/js/modules/subA/subB/__init__.js
/usr/libexec/installed-tests/gjs/js/modules/subA/subB/baz.js
/usr/libexec/installed-tests/gjs/js/modules/subA/subB/foobar.js
/usr/libexec/installed-tests/gjs/js/modules/subBadInit/__init__.js
/usr/libexec/installed-tests/gjs/js/modules/subErrorInit/__init__.js
/usr/libexec/installed-tests/gjs/js/testAsync.js
/usr/libexec/installed-tests/gjs/js/testByteArray.js
/usr/libexec/installed-tests/gjs/js/testCairo.js
/usr/libexec/installed-tests/gjs/js/testCairoModule.js
/usr/libexec/installed-tests/gjs/js/testConsole.js
/usr/libexec/installed-tests/gjs/js/testESModules.js
/usr/libexec/installed-tests/gjs/js/testEncoding.js
/usr/libexec/installed-tests/gjs/js/testExceptions.js
/usr/libexec/installed-tests/gjs/js/testFormat.js
/usr/libexec/installed-tests/gjs/js/testFundamental.js
/usr/libexec/installed-tests/gjs/js/testGDBus.js
/usr/libexec/installed-tests/gjs/js/testGIMarshalling.js
/usr/libexec/installed-tests/gjs/js/testGLib.js
/usr/libexec/installed-tests/gjs/js/testGLibLogWriter.js
/usr/libexec/installed-tests/gjs/js/testGObject.js
/usr/libexec/installed-tests/gjs/js/testGObjectClass.js
/usr/libexec/installed-tests/gjs/js/testGObjectInterface.js
/usr/libexec/installed-tests/gjs/js/testGObjectValue.js
/usr/libexec/installed-tests/gjs/js/testGTypeClass.js
/usr/libexec/installed-tests/gjs/js/testGettext.js
/usr/libexec/installed-tests/gjs/js/testGio.js
/usr/libexec/installed-tests/gjs/js/testGlobal.js
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
/usr/libexec/installed-tests/gjs/js/testPromise.js
/usr/libexec/installed-tests/gjs/js/testRegress.js
/usr/libexec/installed-tests/gjs/js/testSignals.js
/usr/libexec/installed-tests/gjs/js/testSystem.js
/usr/libexec/installed-tests/gjs/js/testTimers.js
/usr/libexec/installed-tests/gjs/js/testTweener.js
/usr/libexec/installed-tests/gjs/js/testWarnLib.js
/usr/libexec/installed-tests/gjs/js/testself.js
/usr/libexec/installed-tests/gjs/libgimarshallingtests.so
/usr/libexec/installed-tests/gjs/libgjstesttools.so
/usr/libexec/installed-tests/gjs/libregress.so
/usr/libexec/installed-tests/gjs/libwarnlib.so
/usr/libexec/installed-tests/gjs/minijasmine
/usr/libexec/installed-tests/gjs/scripts/testCommandLine.sh
/usr/libexec/installed-tests/gjs/scripts/testCommandLineModules.sh
/usr/libexec/installed-tests/gjs/scripts/testWarnings.sh
/usr/share/clear/optimized-elf/test*
/usr/share/installed-tests/gjs/backtrace.test
/usr/share/installed-tests/gjs/breakpoint.test
/usr/share/installed-tests/gjs/continue.test
/usr/share/installed-tests/gjs/delete.test
/usr/share/installed-tests/gjs/detach.test
/usr/share/installed-tests/gjs/down-up.test
/usr/share/installed-tests/gjs/finish.test
/usr/share/installed-tests/gjs/frame.test
/usr/share/installed-tests/gjs/keys.test
/usr/share/installed-tests/gjs/lastvalues.test
/usr/share/installed-tests/gjs/list.test
/usr/share/installed-tests/gjs/next.test
/usr/share/installed-tests/gjs/print.test
/usr/share/installed-tests/gjs/quit.test
/usr/share/installed-tests/gjs/return.test
/usr/share/installed-tests/gjs/set.test
/usr/share/installed-tests/gjs/step.test
/usr/share/installed-tests/gjs/testAsync.test
/usr/share/installed-tests/gjs/testByteArray.test
/usr/share/installed-tests/gjs/testCairo.test
/usr/share/installed-tests/gjs/testCairoModule.test
/usr/share/installed-tests/gjs/testCommandLine.sh.test
/usr/share/installed-tests/gjs/testCommandLineModules.sh.test
/usr/share/installed-tests/gjs/testConsole.test
/usr/share/installed-tests/gjs/testESModules.test
/usr/share/installed-tests/gjs/testEncoding.test
/usr/share/installed-tests/gjs/testExceptions.test
/usr/share/installed-tests/gjs/testFormat.test
/usr/share/installed-tests/gjs/testFundamental.test
/usr/share/installed-tests/gjs/testGDBus.test
/usr/share/installed-tests/gjs/testGIMarshalling.test
/usr/share/installed-tests/gjs/testGLib.test
/usr/share/installed-tests/gjs/testGLibLogWriter.test
/usr/share/installed-tests/gjs/testGObject.test
/usr/share/installed-tests/gjs/testGObjectClass.test
/usr/share/installed-tests/gjs/testGObjectInterface.test
/usr/share/installed-tests/gjs/testGObjectValue.test
/usr/share/installed-tests/gjs/testGTypeClass.test
/usr/share/installed-tests/gjs/testGettext.test
/usr/share/installed-tests/gjs/testGio.test
/usr/share/installed-tests/gjs/testGlobal.test
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
/usr/share/installed-tests/gjs/testPromise.test
/usr/share/installed-tests/gjs/testRegress.test
/usr/share/installed-tests/gjs/testSignals.test
/usr/share/installed-tests/gjs/testSystem.test
/usr/share/installed-tests/gjs/testTimers.test
/usr/share/installed-tests/gjs/testTweener.test
/usr/share/installed-tests/gjs/testWarnLib.test
/usr/share/installed-tests/gjs/testWarnings.sh.test
/usr/share/installed-tests/gjs/testself.test
/usr/share/installed-tests/gjs/throw-ignored.test
/usr/share/installed-tests/gjs/throw.test
/usr/share/installed-tests/gjs/until.test
