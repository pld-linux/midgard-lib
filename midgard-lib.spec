Summary:	Midgard Library
Summary(pl):	Biblioteka Midgard
Name:		midgard-lib
Version:	1.4.4
Release:	0.1
License:	distributable
Vendor:		Midgard Project <http://www.midgard-project.org>
Group:		Networking/Daemons
Source0:	http://www.midgard-project.org/attachment/434f392e6f87e1e76202f00695dd251f/14f7a3c18ba99abeb844ff1dd73580d4/%{name}-%{version}.tar.bz2
Patch0:		%{name}-id.patch
Patch1:		%{name}-mkinstalldirs.patch
URL:		http://www.midgard-project.org/
Requires:	mysql >= 3.23.20, mysql-libs >= 3.23.20, expat >= 1.95.1
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
aplikacji webowych, bazuj±c± na jêzyku skryptowym PHP. Midgard jest
narzêdziem do tworzenia, modyfikacji i prowadzenia serwisów opartych
na dynamicznej bazie danych.

%package devel
Summary:	Header files etc to develop midgard-lib applications
Summary(pl):	Pliki naglowkowe i inne do midgard-lib
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Header files etc to develop midgard-lib applications.

%description devel -l pl
Pliki naglowkowe i inne do midgard-lib.

%prep
%setup -q -n %{name}-%{_ver}

#%patch0 -p1
#%patch1 -p1

%build
%configure \
	--with-mysql=/usr \
	--with-sitegroups \
	--with-iconv \
	--with-repligard-owner
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir},%{_includedir}/midgard,%{_libdir},%{_datadir}/midgard,%{_bindir}}
install midgard/*.h $RPM_BUILD_ROOT/%{_includedir}/midgard
install src/.libs/* $RPM_BUILD_ROOT/%{_libdir}
install repligard/repligard.conf $RPM_BUILD_ROOT/%{_sysconfdir}
install repligard/repligard $RPM_BUILD_ROOT/%{_bindir}
install repligard/repligard.xml $RPM_BUILD_ROOT%{_datadir}/midgard

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING ChangeLog INSTALL INSTALL.ru NEWS README README.ru
%attr(755,root,root) %{_bindir}/repligard
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/repligard.conf
%{_datadir}/midgard/repligard.xml
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_libdir}/lib*.a
%{_includedir}/*
