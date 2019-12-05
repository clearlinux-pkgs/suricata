#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF7F9B0A300C1B70D (releases@openinfosecfoundation.org)
#
Name     : suricata
Version  : 5.0.0
Release  : 31
URL      : https://www.openinfosecfoundation.org/download/suricata-5.0.0.tar.gz
Source0  : https://www.openinfosecfoundation.org/download/suricata-5.0.0.tar.gz
Source1 : https://www.openinfosecfoundation.org/download/suricata-5.0.0.tar.gz.sig
Summary  : A security-aware HTTP parser, designed for use in IDS/IPS and WAF products.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause GPL-2.0 HPND MIT Unlicense
Requires: suricata-bin = %{version}-%{release}
Requires: suricata-data = %{version}-%{release}
Requires: suricata-lib = %{version}-%{release}
Requires: suricata-license = %{version}-%{release}
Requires: suricata-man = %{version}-%{release}
Requires: suricata-python = %{version}-%{release}
Requires: suricata-python3 = %{version}-%{release}
Requires: suricata-services = %{version}-%{release}
Requires: PyYAML
Requires: Sphinx
Requires: python-dateutil
Requires: sphinxcontrib-programoutput
BuildRequires : PyYAML
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : curl-dev
BuildRequires : doxygen
BuildRequires : elfutils-dev
BuildRequires : grep
BuildRequires : hyperscan-dev
BuildRequires : jansson-dev
BuildRequires : libcap-ng-dev
BuildRequires : libpcap-dev
BuildRequires : llvm
BuildRequires : llvm-dev
BuildRequires : llvm-extras
BuildRequires : lz4-dev
BuildRequires : pcre-dev
BuildRequires : pkgconfig(libbpf)
BuildRequires : pkgconfig(libhs)
BuildRequires : pkgconfig(libnetfilter_queue)
BuildRequires : pkgconfig(libpcap)
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(lua)
BuildRequires : pkgconfig(luajit)
BuildRequires : pkgconfig(nspr)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(zlib)
BuildRequires : python-dateutil
BuildRequires : rustc
BuildRequires : sphinxcontrib-programoutput
BuildRequires : xz-dev
BuildRequires : yaml-dev

%description


%package bin
Summary: bin components for the suricata package.
Group: Binaries
Requires: suricata-data = %{version}-%{release}
Requires: suricata-license = %{version}-%{release}
Requires: suricata-services = %{version}-%{release}

%description bin
bin components for the suricata package.


%package data
Summary: data components for the suricata package.
Group: Data

%description data
data components for the suricata package.


%package dev
Summary: dev components for the suricata package.
Group: Development
Requires: suricata-lib = %{version}-%{release}
Requires: suricata-bin = %{version}-%{release}
Requires: suricata-data = %{version}-%{release}
Provides: suricata-devel = %{version}-%{release}
Requires: suricata = %{version}-%{release}

%description dev
dev components for the suricata package.


%package doc
Summary: doc components for the suricata package.
Group: Documentation
Requires: suricata-man = %{version}-%{release}

%description doc
doc components for the suricata package.


%package lib
Summary: lib components for the suricata package.
Group: Libraries
Requires: suricata-data = %{version}-%{release}
Requires: suricata-license = %{version}-%{release}

%description lib
lib components for the suricata package.


%package license
Summary: license components for the suricata package.
Group: Default

%description license
license components for the suricata package.


%package man
Summary: man components for the suricata package.
Group: Default

%description man
man components for the suricata package.


%package python
Summary: python components for the suricata package.
Group: Default
Requires: suricata-python3 = %{version}-%{release}

%description python
python components for the suricata package.


%package python3
Summary: python3 components for the suricata package.
Group: Default
Requires: python3-core

%description python3
python3 components for the suricata package.


%package services
Summary: services components for the suricata package.
Group: Systemd services

%description services
services components for the suricata package.


%prep
%setup -q -n suricata-5.0.0
pushd ..
cp -a suricata-5.0.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571346510
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --with-clang=/usr/bin/clang --disable-gccmarch-native --enable-ebpf --enable-ebpf-build
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static --with-clang=/usr/bin/clang --disable-gccmarch-native --enable-ebpf --enable-ebpf-build
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../buildavx2;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1571346510
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/suricata
cp %{_builddir}/suricata-5.0.0/COPYING %{buildroot}/usr/share/package-licenses/suricata/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/suricata-5.0.0/LICENSE %{buildroot}/usr/share/package-licenses/suricata/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/suricata-5.0.0/contrib/file_processor/LICENSE %{buildroot}/usr/share/package-licenses/suricata/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/suricata-5.0.0/libhtp/LICENSE %{buildroot}/usr/share/package-licenses/suricata/ae3dd05d579644da55a95de2cf7f256b15fa4db0
cp %{_builddir}/suricata-5.0.0/rust/vendor/autocfg/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/autocfg/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/e6d32072ef5f584a805b429ecbd4eec428316dde
cp %{_builddir}/suricata-5.0.0/rust/vendor/base64/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/base64/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/b716916e6b0b96af5ecadf1eaee25f966f5d6cb2
cp %{_builddir}/suricata-5.0.0/rust/vendor/bitflags/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/bitflags/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-5.0.0/rust/vendor/build_const/LICENSE.txt %{buildroot}/usr/share/package-licenses/suricata/b5926737d6a950b5e7714401ebeb8c56f80dc137
cp %{_builddir}/suricata-5.0.0/rust/vendor/byteorder/COPYING %{buildroot}/usr/share/package-licenses/suricata/dd445710e6e4caccc4f8a587a130eaeebe83f6f6
cp %{_builddir}/suricata-5.0.0/rust/vendor/byteorder/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/4c8990add9180fc59efa5b0d8faf643c9709501e
cp %{_builddir}/suricata-5.0.0/rust/vendor/byteorder/UNLICENSE %{buildroot}/usr/share/package-licenses/suricata/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85
cp %{_builddir}/suricata-5.0.0/rust/vendor/cookie-factory/LICENSE %{buildroot}/usr/share/package-licenses/suricata/e2d62391d392e96241c95aa62ad279aebde68eee
cp %{_builddir}/suricata-5.0.0/rust/vendor/crc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/dd9b969c81351d17b1585644c99d8fac15f1f523
cp %{_builddir}/suricata-5.0.0/rust/vendor/crc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/0d46ed4ce7ded1a412f57fc7105208ff4451481b
cp %{_builddir}/suricata-5.0.0/rust/vendor/der-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/der-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
cp %{_builddir}/suricata-5.0.0/rust/vendor/enum_primitive/LICENSE %{buildroot}/usr/share/package-licenses/suricata/abd2dbb680edc6abdba4bb6a530ab411874538ab
cp %{_builddir}/suricata-5.0.0/rust/vendor/fuchsia-cprng/LICENSE %{buildroot}/usr/share/package-licenses/suricata/e082d0438f395b9128436ab6628c7a96c009426d
cp %{_builddir}/suricata-5.0.0/rust/vendor/ipsec-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/ipsec-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
cp %{_builddir}/suricata-5.0.0/rust/vendor/kerberos-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/kerberos-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
cp %{_builddir}/suricata-5.0.0/rust/vendor/libc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/libc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-5.0.0/rust/vendor/memchr/COPYING %{buildroot}/usr/share/package-licenses/suricata/dd445710e6e4caccc4f8a587a130eaeebe83f6f6
cp %{_builddir}/suricata-5.0.0/rust/vendor/memchr/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/4c8990add9180fc59efa5b0d8faf643c9709501e
cp %{_builddir}/suricata-5.0.0/rust/vendor/memchr/UNLICENSE %{buildroot}/usr/share/package-licenses/suricata/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85
cp %{_builddir}/suricata-5.0.0/rust/vendor/nom/LICENSE %{buildroot}/usr/share/package-licenses/suricata/e7b32657d4608cb4a57afa790801ecb9c2a037f5
cp %{_builddir}/suricata-5.0.0/rust/vendor/ntp-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/ntp-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
cp %{_builddir}/suricata-5.0.0/rust/vendor/num-bigint/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/num-bigint/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-5.0.0/rust/vendor/num-complex/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/num-complex/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-5.0.0/rust/vendor/num-derive/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/num-derive/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-5.0.0/rust/vendor/num-integer/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/num-integer/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-5.0.0/rust/vendor/num-iter/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/num-iter/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-5.0.0/rust/vendor/num-rational/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/num-rational/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-5.0.0/rust/vendor/num-traits-0.1.43/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/num-traits-0.1.43/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-5.0.0/rust/vendor/num-traits/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/num-traits/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-5.0.0/rust/vendor/num/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/num/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-5.0.0/rust/vendor/proc-macro2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/proc-macro2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/3b042d3d971924ec0296687efd50dbe08b734976
cp %{_builddir}/suricata-5.0.0/rust/vendor/quote/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/quote/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/f14afa20edce530124d39cd56312c7781c19b267
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/d74ad13f1402c35008f22bc588a6b8199ed164d3
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_chacha/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/f14afa20edce530124d39cd56312c7781c19b267
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_chacha/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_chacha/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/d74ad13f1402c35008f22bc588a6b8199ed164d3
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_core-0.3.1/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/f14afa20edce530124d39cd56312c7781c19b267
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_core-0.3.1/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_core-0.3.1/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/d74ad13f1402c35008f22bc588a6b8199ed164d3
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_core/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/f14afa20edce530124d39cd56312c7781c19b267
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_core/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_core/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/d74ad13f1402c35008f22bc588a6b8199ed164d3
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_hc/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/f14afa20edce530124d39cd56312c7781c19b267
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_hc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_hc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/2e87f5a7544123079270e8178a5ab0bbd19d0e51
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_isaac/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/f14afa20edce530124d39cd56312c7781c19b267
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_isaac/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_isaac/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/d74ad13f1402c35008f22bc588a6b8199ed164d3
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_jitter/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/f14afa20edce530124d39cd56312c7781c19b267
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_jitter/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_jitter/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/d74ad13f1402c35008f22bc588a6b8199ed164d3
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_os/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/f14afa20edce530124d39cd56312c7781c19b267
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_os/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_os/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/d74ad13f1402c35008f22bc588a6b8199ed164d3
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_pcg/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/f14afa20edce530124d39cd56312c7781c19b267
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_pcg/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_pcg/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/ac1dc5ec3778e81d0e4041cc84de9f32fd81c663
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_xorshift/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/f14afa20edce530124d39cd56312c7781c19b267
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_xorshift/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
cp %{_builddir}/suricata-5.0.0/rust/vendor/rand_xorshift/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/d74ad13f1402c35008f22bc588a6b8199ed164d3
cp %{_builddir}/suricata-5.0.0/rust/vendor/rdrand/LICENSE %{buildroot}/usr/share/package-licenses/suricata/ced8b50e816dfeba0fa899df8f5526a8ec1c1d0b
cp %{_builddir}/suricata-5.0.0/rust/vendor/redox_syscall/LICENSE %{buildroot}/usr/share/package-licenses/suricata/a00165152c82ea55b9fc254890dc8860c25e3bb6
cp %{_builddir}/suricata-5.0.0/rust/vendor/rusticata-macros/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/rusticata-macros/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
cp %{_builddir}/suricata-5.0.0/rust/vendor/siphasher/COPYING %{buildroot}/usr/share/package-licenses/suricata/1fa93df46254c46478d6aad7df9ec5e199694113
cp %{_builddir}/suricata-5.0.0/rust/vendor/snmp-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/snmp-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
cp %{_builddir}/suricata-5.0.0/rust/vendor/syn/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/syn/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/ce3a2603094e799f42ce99c40941544dfcc5c4a5
cp %{_builddir}/suricata-5.0.0/rust/vendor/time/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/time/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-5.0.0/rust/vendor/tls-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/tls-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
cp %{_builddir}/suricata-5.0.0/rust/vendor/unicode-xid/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/5ed53061419caf64f84d064f3641392a2a10fa7f
cp %{_builddir}/suricata-5.0.0/rust/vendor/unicode-xid/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/unicode-xid/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/60c3522081bf15d7ac1d4c5a63de425ef253e87a
cp %{_builddir}/suricata-5.0.0/rust/vendor/version_check/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/version_check/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/cfcb552ef0afbe7ccb4128891c0de00685988a4b
cp %{_builddir}/suricata-5.0.0/rust/vendor/widestring/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/ea4215a6204b8414db6209c378a78a2dfb91c9ee
cp %{_builddir}/suricata-5.0.0/rust/vendor/widestring/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f021a3778be8e7414e81123679384b543612e7b
cp %{_builddir}/suricata-5.0.0/rust/vendor/winapi/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/suricata-5.0.0/rust/vendor/winapi/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/2243f7a86daaa727d34d92e987a741036f288464
cp %{_builddir}/suricata-5.0.0/rust/vendor/x509-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-5.0.0/rust/vendor/x509-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
cp %{_builddir}/suricata-5.0.0/suricata-update/LICENSE %{buildroot}/usr/share/package-licenses/suricata/4cc77b90af91e615a64ae04893fdffa7939db84c
pushd ../buildavx2/
%make_install_avx2
popd
%make_install
## install_append content
install -m 0644 -D etc/suricata.service %{buildroot}/usr/lib/systemd/system/suricata.service
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/haswell/suricata
/usr/bin/suricata
/usr/bin/suricata-update
/usr/bin/suricatactl
/usr/bin/suricatasc

%files data
%defattr(-,root,root,-)
/usr/share/suricata/classification.config
/usr/share/suricata/reference.config
/usr/share/suricata/rules/app-layer-events.rules
/usr/share/suricata/rules/decoder-events.rules
/usr/share/suricata/rules/dhcp-events.rules
/usr/share/suricata/rules/dnp3-events.rules
/usr/share/suricata/rules/dns-events.rules
/usr/share/suricata/rules/files.rules
/usr/share/suricata/rules/http-events.rules
/usr/share/suricata/rules/ipsec-events.rules
/usr/share/suricata/rules/kerberos-events.rules
/usr/share/suricata/rules/modbus-events.rules
/usr/share/suricata/rules/nfs-events.rules
/usr/share/suricata/rules/ntp-events.rules
/usr/share/suricata/rules/smb-events.rules
/usr/share/suricata/rules/smtp-events.rules
/usr/share/suricata/rules/stream-events.rules
/usr/share/suricata/rules/tls-events.rules

%files dev
%defattr(-,root,root,-)
/usr/include/htp/bstr.h
/usr/include/htp/bstr_builder.h
/usr/include/htp/htp.h
/usr/include/htp/htp_base64.h
/usr/include/htp/htp_config.h
/usr/include/htp/htp_connection_parser.h
/usr/include/htp/htp_core.h
/usr/include/htp/htp_decompressors.h
/usr/include/htp/htp_hooks.h
/usr/include/htp/htp_list.h
/usr/include/htp/htp_multipart.h
/usr/include/htp/htp_table.h
/usr/include/htp/htp_transaction.h
/usr/include/htp/htp_urlencoded.h
/usr/include/htp/htp_utf8_decoder.h
/usr/include/htp/htp_version.h
/usr/include/htp/lzma/7zTypes.h
/usr/include/htp/lzma/LzmaDec.h
/usr/lib64/haswell/libhtp.so
/usr/lib64/libhtp.so
/usr/lib64/pkgconfig/htp.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/suricata/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/haswell/libhtp.so.2
/usr/lib64/haswell/libhtp.so.2.0.0
/usr/lib64/libhtp.so.2
/usr/lib64/libhtp.so.2.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/suricata/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/suricata/0d46ed4ce7ded1a412f57fc7105208ff4451481b
/usr/share/package-licenses/suricata/1fa93df46254c46478d6aad7df9ec5e199694113
/usr/share/package-licenses/suricata/2243f7a86daaa727d34d92e987a741036f288464
/usr/share/package-licenses/suricata/2e87f5a7544123079270e8178a5ab0bbd19d0e51
/usr/share/package-licenses/suricata/3b042d3d971924ec0296687efd50dbe08b734976
/usr/share/package-licenses/suricata/4c8990add9180fc59efa5b0d8faf643c9709501e
/usr/share/package-licenses/suricata/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
/usr/share/package-licenses/suricata/5ed53061419caf64f84d064f3641392a2a10fa7f
/usr/share/package-licenses/suricata/60c3522081bf15d7ac1d4c5a63de425ef253e87a
/usr/share/package-licenses/suricata/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/suricata/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7
/usr/share/package-licenses/suricata/9f021a3778be8e7414e81123679384b543612e7b
/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
/usr/share/package-licenses/suricata/a00165152c82ea55b9fc254890dc8860c25e3bb6
/usr/share/package-licenses/suricata/abd2dbb680edc6abdba4bb6a530ab411874538ab
/usr/share/package-licenses/suricata/ac1dc5ec3778e81d0e4041cc84de9f32fd81c663
/usr/share/package-licenses/suricata/ae3dd05d579644da55a95de2cf7f256b15fa4db0
/usr/share/package-licenses/suricata/b5926737d6a950b5e7714401ebeb8c56f80dc137
/usr/share/package-licenses/suricata/b716916e6b0b96af5ecadf1eaee25f966f5d6cb2
/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
/usr/share/package-licenses/suricata/ce3a2603094e799f42ce99c40941544dfcc5c4a5
/usr/share/package-licenses/suricata/ced8b50e816dfeba0fa899df8f5526a8ec1c1d0b
/usr/share/package-licenses/suricata/cfcb552ef0afbe7ccb4128891c0de00685988a4b
/usr/share/package-licenses/suricata/d74ad13f1402c35008f22bc588a6b8199ed164d3
/usr/share/package-licenses/suricata/dd445710e6e4caccc4f8a587a130eaeebe83f6f6
/usr/share/package-licenses/suricata/dd9b969c81351d17b1585644c99d8fac15f1f523
/usr/share/package-licenses/suricata/e082d0438f395b9128436ab6628c7a96c009426d
/usr/share/package-licenses/suricata/e2d62391d392e96241c95aa62ad279aebde68eee
/usr/share/package-licenses/suricata/e6d32072ef5f584a805b429ecbd4eec428316dde
/usr/share/package-licenses/suricata/e7b32657d4608cb4a57afa790801ecb9c2a037f5
/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
/usr/share/package-licenses/suricata/ea4215a6204b8414db6209c378a78a2dfb91c9ee
/usr/share/package-licenses/suricata/f14afa20edce530124d39cd56312c7781c19b267
/usr/share/package-licenses/suricata/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/suricata.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/suricata.service
