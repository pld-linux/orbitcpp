Summary:	C++ bindings for the ORBit Corba ORB
Summary(pl):	Powiązania C++ dla ORBit Corba ORB
Name:		orbitcpp
Version:	1.3.7
Release:	1
License:	GPL
Group:		Applications/Engineering
Source0:	ftp://ftp.gnome.org/pub/gnome/sources/%{name}/1.3/%{name}-%{version}.tar.bz2
# Source0-md5:	14a23ca4a09a9eea7a2b42d70662d015
Patch0:		%{name}-gcc33.patch
URL:		http://orbitcpp.sourceforge.net/
BuildRequires:	ORBit2-devel >= 2.7.6
BuildRequires:	libIDL >= 0.7.4
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Orbitcpp is a project to develop C++ bindings for the ORBit Corba ORB.

%description -l pl
Orbitcpp to projekt umożliwiający tworzenie powiązań C++ dla ORBit
Corba ORB.

%package devel
Summary:	Header files, and utilities for orbitcpp
Summary(pl):	Pliki nagłówkowe i użytki dla orbitcpp
Group:		Development/Libraries
Requires:	%{name} = %{version}
Requires:	ORBit2-devel >= 2.7.6
Requires:	libIDL-devel >= 0.7.4

%description
Orbitcpp is a project to develop C++ bindings for the ORBit Corba ORB.

This package includes the header files and utilities neecessary to
write programs that use orbitcpp.

%description devel -l pl
Orbitcpp to projekt umożliwiający tworzenie powiązań C++ dla ORBit
Corba ORB.

Ten pakiet zawiera pliki nagłówkowe oraz użytki potrzebne do pisania
programów używających orbitcpp.

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
Orbitcpp to projekt umożliwiający tworzenie powiązań C++ dla ORBit
Corba ORB.

Ten Pakiet zawiera biblioteki statyczne potrzebne do pisania
konsolidowanych statycznie programów używających technologii CORBA.

%prep
%setup -q
%patch0 -p1

%build
%configure
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

%files static
%defattr(644,root,root,755)
%{_libdir}/libORBit-2-cpp.a
