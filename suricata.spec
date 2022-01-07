#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x2BA9C98CCDF1E93A (releases@openinfosecfoundation.org)
#
Name     : suricata
Version  : 6.0.4
Release  : 61
URL      : https://www.openinfosecfoundation.org/download/suricata-6.0.4.tar.gz
Source0  : https://www.openinfosecfoundation.org/download/suricata-6.0.4.tar.gz
Source1  : https://www.openinfosecfoundation.org/download/suricata-6.0.4.tar.gz.sig
Summary  : A security-aware HTTP parser, designed for use in IDS/IPS and WAF products.
Group    : Development/Tools
License  : 0BSD Apache-2.0 BSD-3-Clause BSL-1.0 GPL-2.0 MIT Unlicense Zlib
Requires: suricata-bin = %{version}-%{release}
Requires: suricata-data = %{version}-%{release}
Requires: suricata-filemap = %{version}-%{release}
Requires: suricata-lib = %{version}-%{release}
Requires: suricata-license = %{version}-%{release}
Requires: suricata-man = %{version}-%{release}
Requires: suricata-python = %{version}-%{release}
Requires: suricata-python3 = %{version}-%{release}
Requires: suricata-services = %{version}-%{release}
BuildRequires : Sphinx
BuildRequires : buildreq-distutils3
BuildRequires : curl-dev
BuildRequires : doxygen
BuildRequires : file-dev
BuildRequires : grep
BuildRequires : hyperscan-dev
BuildRequires : jansson-dev
BuildRequires : libcap-ng-dev
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
BuildRequires : pypi(python_dateutil)
BuildRequires : pypi(pyyaml)
BuildRequires : pypi(sphinx)
BuildRequires : pypi(sphinxcontrib_programoutput)
BuildRequires : rustc
BuildRequires : yaml-dev

%description
LibHTP
============================================================================
============================================================================

%package bin
Summary: bin components for the suricata package.
Group: Binaries
Requires: suricata-data = %{version}-%{release}
Requires: suricata-license = %{version}-%{release}
Requires: suricata-services = %{version}-%{release}
Requires: suricata-filemap = %{version}-%{release}

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


%package filemap
Summary: filemap components for the suricata package.
Group: Default

%description filemap
filemap components for the suricata package.


%package lib
Summary: lib components for the suricata package.
Group: Libraries
Requires: suricata-data = %{version}-%{release}
Requires: suricata-license = %{version}-%{release}
Requires: suricata-filemap = %{version}-%{release}

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
Requires: suricata-filemap = %{version}-%{release}

%description python
python components for the suricata package.


%package python3
Summary: python3 components for the suricata package.
Group: Default
Requires: python3-core
Requires: pypi(pyyaml)

%description python3
python3 components for the suricata package.


%package services
Summary: services components for the suricata package.
Group: Systemd services

%description services
services components for the suricata package.


%prep
%setup -q -n suricata-6.0.4
cd %{_builddir}/suricata-6.0.4
pushd ..
cp -a suricata-6.0.4 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641591835
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static --with-clang=/usr/bin/clang \
--disable-gccmarch-native \
--enable-ebpf \
--enable-ebpf-build \
--enable-lua
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static --with-clang=/usr/bin/clang \
--disable-gccmarch-native \
--enable-ebpf \
--enable-ebpf-build \
--enable-lua
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1641591835
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/suricata
cp %{_builddir}/suricata-6.0.4/COPYING %{buildroot}/usr/share/package-licenses/suricata/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/suricata-6.0.4/LICENSE %{buildroot}/usr/share/package-licenses/suricata/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/suricata-6.0.4/contrib/file_processor/LICENSE %{buildroot}/usr/share/package-licenses/suricata/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
cp %{_builddir}/suricata-6.0.4/libhtp/LICENSE %{buildroot}/usr/share/package-licenses/suricata/ae3dd05d579644da55a95de2cf7f256b15fa4db0
cp %{_builddir}/suricata-6.0.4/rust/vendor/adler/LICENSE-0BSD %{buildroot}/usr/share/package-licenses/suricata/3aedaafe8ea8fce424d1df3be32d1b8816944e0e
cp %{_builddir}/suricata-6.0.4/rust/vendor/adler/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/1d47c63586fe3be7f228cff1ab0c029b53741875
cp %{_builddir}/suricata-6.0.4/rust/vendor/adler/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/ce3a2603094e799f42ce99c40941544dfcc5c4a5
cp %{_builddir}/suricata-6.0.4/rust/vendor/alloc-no-stdlib/LICENSE %{buildroot}/usr/share/package-licenses/suricata/e8857b6d9ac268b2470997b650027e63010881ff
cp %{_builddir}/suricata-6.0.4/rust/vendor/arrayvec/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/arrayvec/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/39c13e52bbc0cee5549d36f3829693726fb50a8b
cp %{_builddir}/suricata-6.0.4/rust/vendor/autocfg/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/autocfg/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/e6d32072ef5f584a805b429ecbd4eec428316dde
cp %{_builddir}/suricata-6.0.4/rust/vendor/base64/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/base64/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/b716916e6b0b96af5ecadf1eaee25f966f5d6cb2
cp %{_builddir}/suricata-6.0.4/rust/vendor/bitflags/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/bitflags/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-6.0.4/rust/vendor/brotli-decompressor/LICENSE %{buildroot}/usr/share/package-licenses/suricata/e8857b6d9ac268b2470997b650027e63010881ff
cp %{_builddir}/suricata-6.0.4/rust/vendor/brotli/LICENSE %{buildroot}/usr/share/package-licenses/suricata/e8857b6d9ac268b2470997b650027e63010881ff
cp %{_builddir}/suricata-6.0.4/rust/vendor/build_const/LICENSE.txt %{buildroot}/usr/share/package-licenses/suricata/b5926737d6a950b5e7714401ebeb8c56f80dc137
cp %{_builddir}/suricata-6.0.4/rust/vendor/byteorder/COPYING %{buildroot}/usr/share/package-licenses/suricata/dd445710e6e4caccc4f8a587a130eaeebe83f6f6
cp %{_builddir}/suricata-6.0.4/rust/vendor/byteorder/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/4c8990add9180fc59efa5b0d8faf643c9709501e
cp %{_builddir}/suricata-6.0.4/rust/vendor/byteorder/UNLICENSE %{buildroot}/usr/share/package-licenses/suricata/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85
cp %{_builddir}/suricata-6.0.4/rust/vendor/cfg-if-0.1.10/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/cfg-if-0.1.10/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/3b042d3d971924ec0296687efd50dbe08b734976
cp %{_builddir}/suricata-6.0.4/rust/vendor/cfg-if/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/cfg-if/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/3b042d3d971924ec0296687efd50dbe08b734976
cp %{_builddir}/suricata-6.0.4/rust/vendor/crc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/dd9b969c81351d17b1585644c99d8fac15f1f523
cp %{_builddir}/suricata-6.0.4/rust/vendor/crc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/0d46ed4ce7ded1a412f57fc7105208ff4451481b
cp %{_builddir}/suricata-6.0.4/rust/vendor/crc32fast/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/669a1e53b9dd9df3474300d3d959bb85bad75945
cp %{_builddir}/suricata-6.0.4/rust/vendor/crc32fast/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/8f178d4cc55689ebdd562cabb1282e33bf8f32fe
cp %{_builddir}/suricata-6.0.4/rust/vendor/der-parser-3.0.4/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/der-parser-3.0.4/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
cp %{_builddir}/suricata-6.0.4/rust/vendor/der-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/der-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
cp %{_builddir}/suricata-6.0.4/rust/vendor/enum_primitive/LICENSE %{buildroot}/usr/share/package-licenses/suricata/abd2dbb680edc6abdba4bb6a530ab411874538ab
cp %{_builddir}/suricata-6.0.4/rust/vendor/flate2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/flate2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/3b042d3d971924ec0296687efd50dbe08b734976
cp %{_builddir}/suricata-6.0.4/rust/vendor/getrandom/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
cp %{_builddir}/suricata-6.0.4/rust/vendor/getrandom/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/d74ad13f1402c35008f22bc588a6b8199ed164d3
cp %{_builddir}/suricata-6.0.4/rust/vendor/ipsec-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/ipsec-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
cp %{_builddir}/suricata-6.0.4/rust/vendor/kerberos-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/kerberos-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
cp %{_builddir}/suricata-6.0.4/rust/vendor/lexical-core/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5feaf15b3fa7d2d226d811e5fcd49098a1ea520c
cp %{_builddir}/suricata-6.0.4/rust/vendor/lexical-core/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/ce3a2603094e799f42ce99c40941544dfcc5c4a5
cp %{_builddir}/suricata-6.0.4/rust/vendor/libc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/libc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/36d69bcb88153a640740000efe933b009420ce7e
cp %{_builddir}/suricata-6.0.4/rust/vendor/md5/LICENSE.md %{buildroot}/usr/share/package-licenses/suricata/7221d3c99a411cdd6254baa9b3debf34e7c25f07
cp %{_builddir}/suricata-6.0.4/rust/vendor/memchr/COPYING %{buildroot}/usr/share/package-licenses/suricata/dd445710e6e4caccc4f8a587a130eaeebe83f6f6
cp %{_builddir}/suricata-6.0.4/rust/vendor/memchr/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/4c8990add9180fc59efa5b0d8faf643c9709501e
cp %{_builddir}/suricata-6.0.4/rust/vendor/memchr/UNLICENSE %{buildroot}/usr/share/package-licenses/suricata/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85
cp %{_builddir}/suricata-6.0.4/rust/vendor/miniz_oxide/LICENSE %{buildroot}/usr/share/package-licenses/suricata/18d7fe3c54698817feec1f2e04a9d5a0f046a80c
cp %{_builddir}/suricata-6.0.4/rust/vendor/miniz_oxide/LICENSE-APACHE.md %{buildroot}/usr/share/package-licenses/suricata/598f87f072f66e2269dd6919292b2934dbb20492
cp %{_builddir}/suricata-6.0.4/rust/vendor/miniz_oxide/LICENSE-MIT.md %{buildroot}/usr/share/package-licenses/suricata/18d7fe3c54698817feec1f2e04a9d5a0f046a80c
cp %{_builddir}/suricata-6.0.4/rust/vendor/miniz_oxide/LICENSE-ZLIB.md %{buildroot}/usr/share/package-licenses/suricata/11f0f1bee61ba6393c3dc7aefee7b92b604ff6c0
cp %{_builddir}/suricata-6.0.4/rust/vendor/nodrop/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/nodrop/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/39c13e52bbc0cee5549d36f3829693726fb50a8b
cp %{_builddir}/suricata-6.0.4/rust/vendor/nom/LICENSE %{buildroot}/usr/share/package-licenses/suricata/27ea6989d4f34b7b944eb884410a31ae20d11686
cp %{_builddir}/suricata-6.0.4/rust/vendor/ntp-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/ntp-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-bigint-0.2.6/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-bigint-0.2.6/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-bigint/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-bigint/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-complex/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-complex/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-derive/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-derive/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-integer/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-integer/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-iter/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-iter/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-rational/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-rational/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-traits-0.1.43/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-traits-0.1.43/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-traits/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/num-traits/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-6.0.4/rust/vendor/num/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/num/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-6.0.4/rust/vendor/ppv-lite86/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/088830dcb78eba1a2052df69bd5cba5445e8f2d7
cp %{_builddir}/suricata-6.0.4/rust/vendor/ppv-lite86/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/e1c86f32641f01a5b85d6e9b20138e8470b883fc
cp %{_builddir}/suricata-6.0.4/rust/vendor/proc-macro-hack/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/proc-macro-hack/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/594599b254cfdf4e8e7a570660d3f7861362acaf
cp %{_builddir}/suricata-6.0.4/rust/vendor/proc-macro2-0.4.30/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/proc-macro2-0.4.30/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/3b042d3d971924ec0296687efd50dbe08b734976
cp %{_builddir}/suricata-6.0.4/rust/vendor/proc-macro2/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/proc-macro2/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/3b042d3d971924ec0296687efd50dbe08b734976
cp %{_builddir}/suricata-6.0.4/rust/vendor/quote-0.6.13/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/quote-0.6.13/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7
cp %{_builddir}/suricata-6.0.4/rust/vendor/quote/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/quote/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7
cp %{_builddir}/suricata-6.0.4/rust/vendor/rand/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/f14afa20edce530124d39cd56312c7781c19b267
cp %{_builddir}/suricata-6.0.4/rust/vendor/rand/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
cp %{_builddir}/suricata-6.0.4/rust/vendor/rand/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/d74ad13f1402c35008f22bc588a6b8199ed164d3
cp %{_builddir}/suricata-6.0.4/rust/vendor/rand_chacha/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/f14afa20edce530124d39cd56312c7781c19b267
cp %{_builddir}/suricata-6.0.4/rust/vendor/rand_chacha/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
cp %{_builddir}/suricata-6.0.4/rust/vendor/rand_chacha/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/d74ad13f1402c35008f22bc588a6b8199ed164d3
cp %{_builddir}/suricata-6.0.4/rust/vendor/rand_core/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/f14afa20edce530124d39cd56312c7781c19b267
cp %{_builddir}/suricata-6.0.4/rust/vendor/rand_core/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
cp %{_builddir}/suricata-6.0.4/rust/vendor/rand_core/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/d74ad13f1402c35008f22bc588a6b8199ed164d3
cp %{_builddir}/suricata-6.0.4/rust/vendor/rand_hc/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/f14afa20edce530124d39cd56312c7781c19b267
cp %{_builddir}/suricata-6.0.4/rust/vendor/rand_hc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
cp %{_builddir}/suricata-6.0.4/rust/vendor/rand_hc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/2e87f5a7544123079270e8178a5ab0bbd19d0e51
cp %{_builddir}/suricata-6.0.4/rust/vendor/rand_pcg/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/f14afa20edce530124d39cd56312c7781c19b267
cp %{_builddir}/suricata-6.0.4/rust/vendor/rand_pcg/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
cp %{_builddir}/suricata-6.0.4/rust/vendor/rand_pcg/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/ac1dc5ec3778e81d0e4041cc84de9f32fd81c663
cp %{_builddir}/suricata-6.0.4/rust/vendor/rustc_version/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/rustc_version/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7
cp %{_builddir}/suricata-6.0.4/rust/vendor/rusticata-macros/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/rusticata-macros/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
cp %{_builddir}/suricata-6.0.4/rust/vendor/ryu/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
cp %{_builddir}/suricata-6.0.4/rust/vendor/ryu/LICENSE-BOOST %{buildroot}/usr/share/package-licenses/suricata/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
cp %{_builddir}/suricata-6.0.4/rust/vendor/semver-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/semver-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/da31fe66a3349c85f4ca594c232d82ac4f02a76b
cp %{_builddir}/suricata-6.0.4/rust/vendor/semver/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/semver/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-6.0.4/rust/vendor/siphasher/COPYING %{buildroot}/usr/share/package-licenses/suricata/89dd598543231b6010a8d57e5cd4f31331fe5364
cp %{_builddir}/suricata-6.0.4/rust/vendor/snmp-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/snmp-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
cp %{_builddir}/suricata-6.0.4/rust/vendor/static_assertions/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/2b8b815229aa8a61e483fb4ba0588b8b6c491890
cp %{_builddir}/suricata-6.0.4/rust/vendor/static_assertions/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/972723ef8f594b1c7515e4c227ff9d5912041fac
cp %{_builddir}/suricata-6.0.4/rust/vendor/syn-0.15.44/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/syn-0.15.44/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/ce3a2603094e799f42ce99c40941544dfcc5c4a5
cp %{_builddir}/suricata-6.0.4/rust/vendor/syn/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/syn/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/ce3a2603094e799f42ce99c40941544dfcc5c4a5
cp %{_builddir}/suricata-6.0.4/rust/vendor/test-case/LICENSE %{buildroot}/usr/share/package-licenses/suricata/8df5650b8e524271748bc56788559a75018d5842
cp %{_builddir}/suricata-6.0.4/rust/vendor/time/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/time/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
cp %{_builddir}/suricata-6.0.4/rust/vendor/tls-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/tls-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
cp %{_builddir}/suricata-6.0.4/rust/vendor/unicode-xid-0.1.0/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/5ed53061419caf64f84d064f3641392a2a10fa7f
cp %{_builddir}/suricata-6.0.4/rust/vendor/unicode-xid-0.1.0/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/unicode-xid-0.1.0/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/60c3522081bf15d7ac1d4c5a63de425ef253e87a
cp %{_builddir}/suricata-6.0.4/rust/vendor/unicode-xid/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/5ed53061419caf64f84d064f3641392a2a10fa7f
cp %{_builddir}/suricata-6.0.4/rust/vendor/unicode-xid/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/unicode-xid/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/60c3522081bf15d7ac1d4c5a63de425ef253e87a
cp %{_builddir}/suricata-6.0.4/rust/vendor/uuid/COPYRIGHT %{buildroot}/usr/share/package-licenses/suricata/5b2ba30524cd989a1f2e6d9447d77d6f1a1a13b9
cp %{_builddir}/suricata-6.0.4/rust/vendor/uuid/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/aca374a3362a76702c50bd4e7d590a57f8834fc7
cp %{_builddir}/suricata-6.0.4/rust/vendor/uuid/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/0eb133022d740845d4047083a552afa05e3862f5
cp %{_builddir}/suricata-6.0.4/rust/vendor/version_check/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/version_check/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/cfcb552ef0afbe7ccb4128891c0de00685988a4b
cp %{_builddir}/suricata-6.0.4/rust/vendor/wasi-0.9.0+wasi-snapshot-preview1/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/wasi-0.9.0+wasi-snapshot-preview1/LICENSE-Apache-2.0_WITH_LLVM-exception %{buildroot}/usr/share/package-licenses/suricata/f137043e018f2024e0414a9153ea728c203ae8e5
cp %{_builddir}/suricata-6.0.4/rust/vendor/wasi-0.9.0+wasi-snapshot-preview1/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/ce3a2603094e799f42ce99c40941544dfcc5c4a5
cp %{_builddir}/suricata-6.0.4/rust/vendor/wasi/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/wasi/LICENSE-Apache-2.0_WITH_LLVM-exception %{buildroot}/usr/share/package-licenses/suricata/f137043e018f2024e0414a9153ea728c203ae8e5
cp %{_builddir}/suricata-6.0.4/rust/vendor/wasi/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/ce3a2603094e799f42ce99c40941544dfcc5c4a5
cp %{_builddir}/suricata-6.0.4/rust/vendor/widestring/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/ea4215a6204b8414db6209c378a78a2dfb91c9ee
cp %{_builddir}/suricata-6.0.4/rust/vendor/widestring/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/9f021a3778be8e7414e81123679384b543612e7b
cp %{_builddir}/suricata-6.0.4/rust/vendor/winapi/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/suricata-6.0.4/rust/vendor/winapi/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/2243f7a86daaa727d34d92e987a741036f288464
cp %{_builddir}/suricata-6.0.4/rust/vendor/x509-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
cp %{_builddir}/suricata-6.0.4/rust/vendor/x509-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
cp %{_builddir}/suricata-6.0.4/suricata-update/LICENSE %{buildroot}/usr/share/package-licenses/suricata/4cc77b90af91e615a64ae04893fdffa7939db84c
pushd ../buildavx2/
%make_install_v3
popd
%make_install
## install_append content
install -m 0644 -D etc/suricata.service %{buildroot}/usr/lib/systemd/system/suricata.service
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/suricata
/usr/bin/suricata-update
/usr/bin/suricatactl
/usr/bin/suricatasc
/usr/share/clear/optimized-elf/bin*

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
/usr/share/suricata/rules/http2-events.rules
/usr/share/suricata/rules/ipsec-events.rules
/usr/share/suricata/rules/kerberos-events.rules
/usr/share/suricata/rules/modbus-events.rules
/usr/share/suricata/rules/mqtt-events.rules
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
/usr/include/suricata-plugin.h
/usr/lib64/libhtp.so
/usr/lib64/pkgconfig/htp.pc

%files doc
%defattr(0644,root,root,0755)
%doc /usr/share/doc/suricata/*

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-suricata

%files lib
%defattr(-,root,root,-)
/usr/lib64/libhtp.so.2
/usr/lib64/libhtp.so.2.0.0
/usr/share/clear/optimized-elf/lib*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/suricata/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
/usr/share/package-licenses/suricata/088830dcb78eba1a2052df69bd5cba5445e8f2d7
/usr/share/package-licenses/suricata/0d46ed4ce7ded1a412f57fc7105208ff4451481b
/usr/share/package-licenses/suricata/0eb133022d740845d4047083a552afa05e3862f5
/usr/share/package-licenses/suricata/11f0f1bee61ba6393c3dc7aefee7b92b604ff6c0
/usr/share/package-licenses/suricata/18d7fe3c54698817feec1f2e04a9d5a0f046a80c
/usr/share/package-licenses/suricata/1d47c63586fe3be7f228cff1ab0c029b53741875
/usr/share/package-licenses/suricata/2243f7a86daaa727d34d92e987a741036f288464
/usr/share/package-licenses/suricata/27ea6989d4f34b7b944eb884410a31ae20d11686
/usr/share/package-licenses/suricata/2b8b815229aa8a61e483fb4ba0588b8b6c491890
/usr/share/package-licenses/suricata/2e87f5a7544123079270e8178a5ab0bbd19d0e51
/usr/share/package-licenses/suricata/36d69bcb88153a640740000efe933b009420ce7e
/usr/share/package-licenses/suricata/39c13e52bbc0cee5549d36f3829693726fb50a8b
/usr/share/package-licenses/suricata/3aedaafe8ea8fce424d1df3be32d1b8816944e0e
/usr/share/package-licenses/suricata/3b042d3d971924ec0296687efd50dbe08b734976
/usr/share/package-licenses/suricata/3cba29011be2b9d59f6204d6fa0a386b1b2dbd90
/usr/share/package-licenses/suricata/4c8990add9180fc59efa5b0d8faf643c9709501e
/usr/share/package-licenses/suricata/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/suricata/5798832c31663cedc1618d18544d445da0295229
/usr/share/package-licenses/suricata/594599b254cfdf4e8e7a570660d3f7861362acaf
/usr/share/package-licenses/suricata/598f87f072f66e2269dd6919292b2934dbb20492
/usr/share/package-licenses/suricata/5b2ba30524cd989a1f2e6d9447d77d6f1a1a13b9
/usr/share/package-licenses/suricata/5ed53061419caf64f84d064f3641392a2a10fa7f
/usr/share/package-licenses/suricata/5feaf15b3fa7d2d226d811e5fcd49098a1ea520c
/usr/share/package-licenses/suricata/60c3522081bf15d7ac1d4c5a63de425ef253e87a
/usr/share/package-licenses/suricata/669a1e53b9dd9df3474300d3d959bb85bad75945
/usr/share/package-licenses/suricata/7221d3c99a411cdd6254baa9b3debf34e7c25f07
/usr/share/package-licenses/suricata/7df059597099bb7dcf25d2a9aedfaf4465f72d8d
/usr/share/package-licenses/suricata/89dd598543231b6010a8d57e5cd4f31331fe5364
/usr/share/package-licenses/suricata/8df5650b8e524271748bc56788559a75018d5842
/usr/share/package-licenses/suricata/8f178d4cc55689ebdd562cabb1282e33bf8f32fe
/usr/share/package-licenses/suricata/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/suricata/972723ef8f594b1c7515e4c227ff9d5912041fac
/usr/share/package-licenses/suricata/9a2b6b4ad55ec42cf19fc686c74668d3a6303ae7
/usr/share/package-licenses/suricata/9f021a3778be8e7414e81123679384b543612e7b
/usr/share/package-licenses/suricata/9f3c36d2b7d381d9cf382a00166f3fbd06783636
/usr/share/package-licenses/suricata/abd2dbb680edc6abdba4bb6a530ab411874538ab
/usr/share/package-licenses/suricata/ac1dc5ec3778e81d0e4041cc84de9f32fd81c663
/usr/share/package-licenses/suricata/aca374a3362a76702c50bd4e7d590a57f8834fc7
/usr/share/package-licenses/suricata/ae3dd05d579644da55a95de2cf7f256b15fa4db0
/usr/share/package-licenses/suricata/b5926737d6a950b5e7714401ebeb8c56f80dc137
/usr/share/package-licenses/suricata/b716916e6b0b96af5ecadf1eaee25f966f5d6cb2
/usr/share/package-licenses/suricata/c097a06b7f5697a25c1e7ec86af49ce8a607de4b
/usr/share/package-licenses/suricata/ce3a2603094e799f42ce99c40941544dfcc5c4a5
/usr/share/package-licenses/suricata/cfcb552ef0afbe7ccb4128891c0de00685988a4b
/usr/share/package-licenses/suricata/d74ad13f1402c35008f22bc588a6b8199ed164d3
/usr/share/package-licenses/suricata/da31fe66a3349c85f4ca594c232d82ac4f02a76b
/usr/share/package-licenses/suricata/dd445710e6e4caccc4f8a587a130eaeebe83f6f6
/usr/share/package-licenses/suricata/dd9b969c81351d17b1585644c99d8fac15f1f523
/usr/share/package-licenses/suricata/e1c86f32641f01a5b85d6e9b20138e8470b883fc
/usr/share/package-licenses/suricata/e6d32072ef5f584a805b429ecbd4eec428316dde
/usr/share/package-licenses/suricata/e8857b6d9ac268b2470997b650027e63010881ff
/usr/share/package-licenses/suricata/e9b475b5dccf14bd66d72dd12a04db75eaad1a9e
/usr/share/package-licenses/suricata/ea4215a6204b8414db6209c378a78a2dfb91c9ee
/usr/share/package-licenses/suricata/f137043e018f2024e0414a9153ea728c203ae8e5
/usr/share/package-licenses/suricata/f14afa20edce530124d39cd56312c7781c19b267
/usr/share/package-licenses/suricata/ff007ce11f3ff7964f1a5b04202c4e95b5c82c85

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/suricata.1
/usr/share/man/man1/suricatactl-filestore.1
/usr/share/man/man1/suricatactl.1
/usr/share/man/man1/suricatasc.1

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/suricata.service
