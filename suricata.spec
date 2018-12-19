#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xF7F9B0A300C1B70D (releases@openinfosecfoundation.org)
#
Name     : suricata
Version  : 4.1.1
Release  : 17
URL      : https://www.openinfosecfoundation.org/download/suricata-4.1.1.tar.gz
Source0  : https://www.openinfosecfoundation.org/download/suricata-4.1.1.tar.gz
Source99 : https://www.openinfosecfoundation.org/download/suricata-4.1.1.tar.gz.sig
Summary  : A security-aware HTTP parser, designed for use in IDS/IPS and WAF products.
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause GPL-2.0 MIT Unlicense
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
BuildRequires : cargo
BuildRequires : curl-dev
BuildRequires : doxygen
BuildRequires : grep
BuildRequires : hyperscan-dev
BuildRequires : jansson-dev
BuildRequires : libcap-ng-dev
BuildRequires : libpcap-dev
BuildRequires : lz4-dev
BuildRequires : pkgconfig(libhs)
BuildRequires : pkgconfig(libnetfilter_queue)
BuildRequires : pkgconfig(libpcre)
BuildRequires : pkgconfig(lua)
BuildRequires : pkgconfig(luajit)
BuildRequires : pkgconfig(nspr)
BuildRequires : pkgconfig(nss)
BuildRequires : pkgconfig(zlib)
BuildRequires : rustc
BuildRequires : xz-dev
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
Requires: suricata-man = %{version}-%{release}
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
%setup -q -n suricata-4.1.1
pushd ..
cp -a suricata-4.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1545252498
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=haswell"
export CXXFLAGS="$CXXFLAGS -m64 -march=haswell"
export LDFLAGS="$LDFLAGS -m64 -march=haswell"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check
cd ../buildavx2;
make VERBOSE=1 V=1 %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1545252498
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/suricata
cp COPYING %{buildroot}/usr/share/package-licenses/suricata/COPYING
cp LICENSE %{buildroot}/usr/share/package-licenses/suricata/LICENSE
cp contrib/file_processor/LICENSE %{buildroot}/usr/share/package-licenses/suricata/contrib_file_processor_LICENSE
cp contrib/tile_pcie_logd/LICENSE %{buildroot}/usr/share/package-licenses/suricata/contrib_tile_pcie_logd_LICENSE
cp libhtp/LICENSE %{buildroot}/usr/share/package-licenses/suricata/libhtp_LICENSE
cp rust/vendor/build_const/LICENSE.txt %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_build_const_LICENSE.txt
cp rust/vendor/crc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_crc_LICENSE-APACHE
cp rust/vendor/crc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_crc_LICENSE-MIT
cp rust/vendor/der-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_der-parser_LICENSE-APACHE
cp rust/vendor/der-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_der-parser_LICENSE-MIT
cp rust/vendor/ipsec-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_ipsec-parser_LICENSE-APACHE
cp rust/vendor/ipsec-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_ipsec-parser_LICENSE-MIT
cp rust/vendor/kerberos-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_kerberos-parser_LICENSE-APACHE
cp rust/vendor/kerberos-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_kerberos-parser_LICENSE-MIT
cp rust/vendor/libc/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_libc_LICENSE-APACHE
cp rust/vendor/libc/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_libc_LICENSE-MIT
cp rust/vendor/memchr/COPYING %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_memchr_COPYING
cp rust/vendor/memchr/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_memchr_LICENSE-MIT
cp rust/vendor/memchr/UNLICENSE %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_memchr_UNLICENSE
cp rust/vendor/nom/LICENSE %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_nom_LICENSE
cp rust/vendor/ntp-parser/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_ntp-parser_LICENSE-APACHE
cp rust/vendor/ntp-parser/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_ntp-parser_LICENSE-MIT
cp rust/vendor/rusticata-macros/LICENSE-APACHE %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_rusticata-macros_LICENSE-APACHE
cp rust/vendor/rusticata-macros/LICENSE-MIT %{buildroot}/usr/share/package-licenses/suricata/rust_vendor_rusticata-macros_LICENSE-MIT
cp suricata-update/LICENSE %{buildroot}/usr/share/package-licenses/suricata/suricata-update_LICENSE
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
/usr/share/suricata/rules/app-layer-events.rules
/usr/share/suricata/rules/decoder-events.rules
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
/usr/share/package-licenses/suricata/COPYING
/usr/share/package-licenses/suricata/LICENSE
/usr/share/package-licenses/suricata/contrib_file_processor_LICENSE
/usr/share/package-licenses/suricata/contrib_tile_pcie_logd_LICENSE
/usr/share/package-licenses/suricata/libhtp_LICENSE
/usr/share/package-licenses/suricata/rust_vendor_build_const_LICENSE.txt
/usr/share/package-licenses/suricata/rust_vendor_crc_LICENSE-APACHE
/usr/share/package-licenses/suricata/rust_vendor_crc_LICENSE-MIT
/usr/share/package-licenses/suricata/rust_vendor_der-parser_LICENSE-APACHE
/usr/share/package-licenses/suricata/rust_vendor_der-parser_LICENSE-MIT
/usr/share/package-licenses/suricata/rust_vendor_ipsec-parser_LICENSE-APACHE
/usr/share/package-licenses/suricata/rust_vendor_ipsec-parser_LICENSE-MIT
/usr/share/package-licenses/suricata/rust_vendor_kerberos-parser_LICENSE-APACHE
/usr/share/package-licenses/suricata/rust_vendor_kerberos-parser_LICENSE-MIT
/usr/share/package-licenses/suricata/rust_vendor_libc_LICENSE-APACHE
/usr/share/package-licenses/suricata/rust_vendor_libc_LICENSE-MIT
/usr/share/package-licenses/suricata/rust_vendor_memchr_COPYING
/usr/share/package-licenses/suricata/rust_vendor_memchr_LICENSE-MIT
/usr/share/package-licenses/suricata/rust_vendor_memchr_UNLICENSE
/usr/share/package-licenses/suricata/rust_vendor_nom_LICENSE
/usr/share/package-licenses/suricata/rust_vendor_ntp-parser_LICENSE-APACHE
/usr/share/package-licenses/suricata/rust_vendor_ntp-parser_LICENSE-MIT
/usr/share/package-licenses/suricata/rust_vendor_rusticata-macros_LICENSE-APACHE
/usr/share/package-licenses/suricata/rust_vendor_rusticata-macros_LICENSE-MIT
/usr/share/package-licenses/suricata/suricata-update_LICENSE

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
