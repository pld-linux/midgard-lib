Summary:	Midgard Library
Summary(pl):	Biblioteka Midgard
Name:		midgard-lib
Version:	1.4.4
Release:	0.1
License:	distributable
Group:		Networking/Daemons
Source0:	http://www.midgard-project.org/attachment/434f392e6f87e1e76202f00695dd251f/14f7a3c18ba99abeb844ff1dd73580d4/%{name}-%{version}.tar.bz2
# Source0-md5:	ac54f0fd505d33368e80968c3828c546
Patch0:		%{name}-id.patch
URL:		http://www.midgard-project.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	expat-devel >= 1.95.1
BuildRequires:	glib-devel >= 1.2
BuildRequires:	libtool
BuildRequires:	mysql-devel >= 3.23.20
BuildRequires:	zlib-devel
Requires:	expat >= 1.95.1
Requires:	mysql-libs >= 3.23.20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sysconfdir	/etc/repligard

%description
Midgard is a freely-available Web application development and
publishing platform based on the popular PHP scripting language. It is
an Open Source development project, giving you the freedom to create
your solutions in an open environment. Midgard is the tool for
creating, modifying and maintaining dynamic database-enabled web
services.

%description -l pl
Midgard jest wolnodostêpn± platform± do tworzenia i publikowania
aplikacji WWW, bazuj±c± na jêzyku skryptowym PHP. Midgard jest
narzêdziem do tworzenia, modyfikacji i prowadzenia serwisów opartych
na dynamicznej bazie danych.

%package devel
Summary:	Header files etc to develop midgard-lib applications
Summary(pl):	Pliki nag³ówkowe i inne do tworzenia aplikacji z u¿yciem midgard-lib
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files etc to develop midgard-lib applications.

%description devel -l pl
Pliki nag³ówkowe i inne do tworzenia aplikacji z u¿yciem midgard-lib.

%package static
Summary:	Static version of midgard library
Summary(pl):	Statyczna wersja biblioteki midgard
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of midgard library.

%description static -l pl
Statyczna wersja biblioteki midgard.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--with-mysql=/usr \
	--with-sitegroups \
	--with-iconv \
	--with-repligard-owner=mysql
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%lang(ru) %doc README.ru
%attr(755,root,root) %{_bindir}/repligard
%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/repligard.conf
%{_datadir}/midgard
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/midgard-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/midgard

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
