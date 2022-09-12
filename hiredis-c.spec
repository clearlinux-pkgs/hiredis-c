#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : hiredis-c
Version  : 1.0.2
Release  : 4
URL      : https://github.com/redis/hiredis/archive/v1.0.2/hiredis-1.0.2.tar.gz
Source0  : https://github.com/redis/hiredis/archive/v1.0.2/hiredis-1.0.2.tar.gz
Summary  : SSL Support for hiredis.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: hiredis-c-data = %{version}-%{release}
Requires: hiredis-c-lib = %{version}-%{release}
Requires: hiredis-c-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : openssl-dev
BuildRequires : pkgconfig(glib-2.0)

%description
[![Build Status](https://travis-ci.org/redis/hiredis.png)](https://travis-ci.org/redis/hiredis)

%package data
Summary: data components for the hiredis-c package.
Group: Data

%description data
data components for the hiredis-c package.


%package dev
Summary: dev components for the hiredis-c package.
Group: Development
Requires: hiredis-c-lib = %{version}-%{release}
Requires: hiredis-c-data = %{version}-%{release}
Provides: hiredis-c-devel = %{version}-%{release}
Requires: hiredis-c = %{version}-%{release}

%description dev
dev components for the hiredis-c package.


%package lib
Summary: lib components for the hiredis-c package.
Group: Libraries
Requires: hiredis-c-data = %{version}-%{release}
Requires: hiredis-c-license = %{version}-%{release}

%description lib
lib components for the hiredis-c package.


%package license
Summary: license components for the hiredis-c package.
Group: Default

%description license
license components for the hiredis-c package.


%prep
%setup -q -n hiredis-1.0.2
cd %{_builddir}/hiredis-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1633657852
mkdir -p clr-build
pushd clr-build
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
%cmake ..
make  %{?_smp_mflags}
popd

%install
export SOURCE_DATE_EPOCH=1633657852
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/hiredis-c
cp %{_builddir}/hiredis-1.0.2/COPYING %{buildroot}/usr/share/package-licenses/hiredis-c/e9c1298de98016808910005a33de3a5f25dce05e
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/hiredis/hiredis-config.cmake
/usr/share/hiredis/hiredis-targets-relwithdebinfo.cmake
/usr/share/hiredis/hiredis-targets.cmake

%files dev
%defattr(-,root,root,-)
/usr/include/hiredis/adapters/ae.h
/usr/include/hiredis/adapters/glib.h
/usr/include/hiredis/adapters/ivykis.h
/usr/include/hiredis/adapters/libev.h
/usr/include/hiredis/adapters/libevent.h
/usr/include/hiredis/adapters/libuv.h
/usr/include/hiredis/adapters/macosx.h
/usr/include/hiredis/adapters/qt.h
/usr/include/hiredis/alloc.h
/usr/include/hiredis/async.h
/usr/include/hiredis/hiredis.h
/usr/include/hiredis/read.h
/usr/include/hiredis/sds.h
/usr/lib64/libhiredis.so
/usr/lib64/pkgconfig/hiredis.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhiredis.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/hiredis-c/e9c1298de98016808910005a33de3a5f25dce05e
