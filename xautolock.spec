Name:           xautolock
Version:        2.2
Release:        8%{?dist}
Summary:        Launches a program when your X session has been idle

Group:          User Interface/X
License:        GPLv2
URL:            http://freshmeat.net/projects/xautolock/
Source0:        http://www.ibiblio.org/pub/Linux/X11/screensavers/%{name}-%{version}.tgz
Patch0:         xautolock-2.2-XSS-fix.patch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  imake libXScrnSaver-devel

%description
A program that launches a given program when
your X session has been idle for a given time.

%prep
%setup -q
%patch0 -p1 -b .XSS-fix
xmkmf


%build
make %{?_smp_mflags} CDEBUGFLAGS="$RPM_OPT_FLAGS" CC="%{__cc}"


%install
rm -rf $RPM_BUILD_ROOT
make install install.man DESTDIR=$RPM_BUILD_ROOT INSTALL="install -p"


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc Changelog License Readme Todo
%{_bindir}/xautolock
%{_mandir}/man1/xautolock.1*


%changelog
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
