%bcond_without	static_libs	# don't build static library
Summary:	C++ bindings for the ORBit Corba ORB
Summary(pl):	Powi±zania C++ dla ORBit Corba ORB
Name:		orbitcpp
Version:	1.3.9
Release:	1
License:	GPL
Group:		Applications/Engineering
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/orbitcpp/1.3/%{name}-%{version}.tar.bz2
# Source0-md5:	ef1594819cf62fc2dad6e0a1cc4cb578
URL:		http://orbitcpp.sourceforge.net/
BuildRequires:	ORBit2-devel >= 1:2.8.2
BuildRequires:	autoconf >= 2.12
BuildRequires:	automake
BuildRequires:	libIDL-devel >= 0.8.2
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.4d
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Orbitcpp is a project to develop C++ bindings for the ORBit Corba ORB.

%description -l pl
Orbitcpp to projekt umo¿liwiaj±cy tworzenie powi±zañ C++ dla ORBit
Corba ORB.

%package devel
Summary:	Header files and utilities for orbitcpp
Summary(pl):	Pliki nag³ówkowe i u¿ytki dla orbitcpp
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	ORBit2-devel >= 1:2.8.2
Requires:	libIDL-devel >= 0.8.2
Requires:	libstdc++-devel

%description
Orbitcpp is a project to develop C++ bindings for the ORBit Corba ORB.

This package includes the header files and utilities neecessary to
write programs that use orbitcpp.

%description devel -l pl
Orbitcpp to projekt umo¿liwiaj±cy tworzenie powi±zañ C++ dla ORBit
Corba ORB.

Ten pakiet zawiera pliki nag³ówkowe oraz u¿ytki potrzebne do pisania
programów u¿ywaj±cych orbitcpp.

%package static
Summary:	Static orbitcpp library
Summary(pl):	Statyczna biblioteka orbitcpp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Orbitcpp is a project to develop C++ bindings for the ORBit Corba ORB.

This package includes static library neecessary to write programs
statically linked that use CORBA technology.

%description static -l pl
Orbitcpp to projekt umo¿liwiaj±cy tworzenie powi±zañ C++ dla ORBit
Corba ORB.

Ten pakiet zawiera bibliotekê statyczn± potrzebn± do pisania
konsolidowanych statycznie programów u¿ywaj±cych technologii CORBA.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
# -i is workaround for am problems in tests
%{__automake} -i
%configure \
	%{!?with_static_libs:--disable-static}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not needed for ORBit2 backends
rm -f $RPM_BUILD_ROOT%{_libdir}/orbit-2.0/idl-backends/*.{a,la}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%dir %{_libdir}/orbit-2.0/idl-backends
%attr(755,root,root) %{_libdir}/orbit-2.0/idl-backends/*.so*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/orbitcpp-*
%{_pkgconfigdir}/*.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
%endif
