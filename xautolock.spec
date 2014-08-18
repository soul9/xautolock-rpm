Name:           xautolock
Version:        2.2
Release:        16%{?dist}
Summary:        Launches a program when your X session has been idle

Group:          User Interface/X
License:        GPLv2
URL:            http://freshmeat.net/projects/xautolock/
Source0:        http://www.ibiblio.org/pub/Linux/X11/screensavers/%{name}-%{version}.tgz
Patch0:         xautolock-2.2-XSS-fix.patch

# See RHBZ#956271. Local change; worth upstreaming?
Patch100:       xautolock-longer-times.patch

BuildRequires:  imake
BuildRequires:  libXScrnSaver-devel

%description
A program that launches a given program when
your X session has been idle for a given time.


%prep
%setup -q
%patch0 -p1 -b .XSS-fix
%patch100 -p1 -b .longer-times
xmkmf


%build
make %{?_smp_mflags} CDEBUGFLAGS="%{optflags}" CC="%{__cc}"


%install
make install install.man DESTDIR=%{buildroot} INSTALL="install -p"


%files
%defattr(-,root,root,-)
%doc Changelog License Readme Todo
%{_bindir}/xautolock
%{_mandir}/man1/xautolock.1*


%changelog
* Mon Aug 18 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sun Jun 08 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 04 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Jun 09 2013 Ben Boeckel <mathstuf@gmail.com> - 2.2-13
- Make maximum lock and kill times 24 hours (RHBZ#956271).

* Fri Feb 15 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Sun Jul 22 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Jul 27 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Mon Oct 06 2008 Ian Weller <ianweller@gmail.com> 2.2-6
- Fix build section from FTFBS (bug 464962)

* Mon Mar 17 2008 Thomas Woerner <twoerner@redhat.com> 2.2-5
- honor XScreenSaver disabled state

* Sun Feb 03 2008 Ian Weller <ianweller@gmail.com> 2.2-4
- Fixed dates in changelog (2007 -> 2008)
- Fixed grouping
- Tightened up files list

* Sat Feb 02 2008 Ian Weller <ianweller@gmail.com> 2.2-3
- Fixed timestamp of Source0
- Removed redundant installation

* Sat Feb 02 2008 Ian Weller <ianweller@gmail.com> 2.2-2
- Shortened summary
- Fixed make flags
- Fixed installation of man page

* Sun Jan 27 2008 Ian Weller <ianweller@gmail.com> 2.2-1
- First package build.
