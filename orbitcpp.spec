Summary:	C++ bindings for the ORBit Corba ORB
Summary(pl):	Powi±zania C++ dla ORBit Corba ORB
Name:		orbitcpp
Version:	1.3.4
Release:	1
License:	GPL
Group:		Applications/Engineering
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/orbitcpp/1.3/%{name}-%{version}.tar.bz2
URL:		http://orbitcpp.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ORBit2-devel >= 2.5.
BuildRequires:	libIDL >= 0.7.4
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Orbitcpp is a project to develop C++ bindings for the ORBit Corba ORB

%description -l pl
Orbitcpp to projekt umo¿liwiaj±cy tworzenie powi±zañ C++ dla ORBit
Corba ORB

%package devel
Summary:	Header files, and utilities for orbitcpp
Summary(pl):	Pliki nag³ówkowe i u¿ytki dla orbitcpp
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	libIDL-devel
Requires:	ORBit2-devel

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
Summary:	Static libraries for orbitcpp
Summary(pl):	Biblioteki statyczne dla orbitcpp
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Orbitcpp is a project to develop C++ bindings for the ORBit Corba ORB.

This package includes static libraries neecessary to write programs
statically linked that use CORBA technology.

%description static -l pl
Orbitcpp to projekt umo¿liwiaj±cy tworzenie powi±zañ C++ dla ORBit
Corba ORB.

Ten Pakiet zawiera biblioteki statyczne potrzebne do pisania programów
zlinkowanych statycznie u¿ywaj±cych technologii CORBA.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*
%{_libdir}/orbit-2.0/idl-backends/*.la
%{_libdir}/orbit-2.0/idl-backends/*.so*

%files devel
%defattr(644,root,root,755)
%doc ChangeLog
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc
%{_includedir}/orbitcpp-*

%files static
%defattr(644,root,root,755)
%{_libdir}/libORBit-2-cpp.a
%{_libdir}/orbit-2.0/idl-backends/*.a
