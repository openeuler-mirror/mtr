%global _hardened_build 1

Name:          mtr
Version:       0.94
Release:       3
Epoch:         2
Summary:       Ping and Traceroute Network Diagnostic Tool
License:       GPLv2 and BSD
URL:           https://www.bitwizard.nl/mtr/
Source0:       https://github.com/traviscross/mtr/archive/v%{version}/%{name}-%{version}.tar.gz
Source1:       net-x%{name}.desktop
Source2:       mtr-gtk-pkexec-wrapper.sh
Patch0:       fix_for_printw_error.patch
BuildRequires: git autoconf automake libtool ncurses-devel gtk2-devel desktop-file-utils

Provides:       %{name}-gtk = %{epoch}:%{version}-%{release}
Obsoletes:      %{name}-gtk < %{epoch}:%{version}-%{release}

%description
It is a network diagnostic tool,it has the "ping" and "traceroute" features.
It prints information about the route and packets that sent from the host to
the specified destination system.This tool can also print the response times
and percentage for all network hops between the systems.

%package_help

%prep
%autosetup -n %{name}-%{version} -p1

%build
export CFLAGS="%{optflags} -fPIE"
export LDFLAGS="-z now -pie"

echo "%{version}" > .tarball-version

./bootstrap.sh
%configure --with-gtk
%make_build && mv -f mtr xmtr.bin && make distclean
%configure --without-gtk
%make_build

%install
install -D -p -m 0755 mtr %{buildroot}%{_sbindir}/mtr
install -D -p -m 0755 %{SOURCE2} %{buildroot}%{_bindir}/xmtr
install -D -p -m 0755 xmtr.bin %{buildroot}%{_bindir}/xmtr.bin
install -D -p -m 0644 img/mtr_icon.xpm %{buildroot}%{_datadir}/pixmaps/mtr_icon.xpm

%make_install
desktop-file-install --dir=%{buildroot}%{_datadir}/applications %{SOURCE1}

%check
make test

%files
%license COPYING BSDCOPYING
%doc AUTHORS FORMATS
%caps(cap_net_raw=pe)
%{_bindir}/xmtr*
%{_sbindir}/%{name}
%{_sbindir}/%{name}-packet
%{_datadir}/pixmaps/mtr_icon.xpm
%{_datadir}/applications/net-x%{name}.desktop
%{_datadir}/bash-completion/completions/%{name}

%files help
%defattr(-,root,root)
%doc NEWS README.md SECURITY TODO
%{_mandir}/man8/*

%changelog
* Fri Mar 11 2022 lin.zhang <lin.zhang@turbolinux.com.cn> - 0.94-3
- add patch fix_for_printw_error.patch

* Wed Mar 3 2021 lin.zhang <lin.zhang@turbolinux.com.cn> - 0.94-2
- modify net-xmtr.desktop file for Xfce4 Traceroute

* Tue Jan 26 2021 SimpleUpdate Robot <tc@openeuler.org> - 0.94-1
- Upgrade to version 0.94

* Mon Jul 20 2020 cuibaobao <cuibaobao1@huawei.com> - 2:0.93-9
- Type:update
- ID:NA
- SUG:NA
- DESC:update to 1.93

* Sat Jan 11 2020 openEuler Buildteam <buildteam@openeuler.org> - 2:0.92-8
- Type:NA
- ID:NA
- SUG:NA
- DESC:delete unused info

* Sat Dec 28 2019 openEuler Buildteam <buildteam@openeuler.org> - 2:0.92-7
- Type:bugfix
- Id:NA
- SUG:NA
- DESC:modify the spec

* Thu Nov 7 2019 openEuler Buildteam <buildteam@openeuler.org> - 2:0.92-6
- Type:enhancement
- Id:NA
- SUG:NA
- DESC:modify the spec1

* Sat Oct 26 2019 openEuler Buildteam <buildteam@openeuler.org> - 2:0.92-5
- Type:enhancement
- Id:NA
- SUG:NA
- DESC:modify the license

* Mon Oct 14 2019 openEuler Buildteam <buildteam@openeuler.org> - 2:0.92-4
- Package init
