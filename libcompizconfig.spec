%define shortname compizconfig
%define name libcompizconfig
%define version 0.0.1
%define rel 1
%define git 20070627

%define major 0
%define libname %mklibname %shortname %major
%define libname_devel %mklibname -d %shortname

%if  %{git}
%define srcname %{name}-%{version}-%{git}
%define distname %{name}
%define release %mkrel 0.%{git}.%{rel}
%else
%define srcname %{name}-%{version}
%define distname %{name}-%{version}
%define release %mkrel %{rel}
%endif


Summary: Backend configuration library from Compiz Fusion
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{srcname}.tar.bz2
License: GPL
Group: System/X11
URL: http://www.compiz-fusion.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libxml2-devel
BuildRequires: compiz-devel

%description
Backend configuration library from Compiz Fusion

#----------------------------------------------------------------------------

%package -n %libname
Summary: Backend configuration library from Compiz Fusion
Group: System/X11
Provides: %name = %{version}-%{release}
Requires: compiz

%description -n %libname
Backend configuration library from Compiz Fusion

#----------------------------------------------------------------------------

%package -n %libname_devel
Summary: Development files for libcompizconfig
Group: Development/X11
Requires: %{libname} = %{version}-%{release}
Provides: %{name}-devel = %{version}-%{release}


%description -n %libname_devel
Development files for libcompizconfig

#----------------------------------------------------------------------------

%prep
%setup -q -n %{distname}

%build
%if %{git}
  # This is a GIT snapshot, so we need to generate makefiles.
  sh autogen.sh -V
%endif
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std
find %{buildroot} -name *.la -exec rm -f {} \;

%clean
rm -rf %{buildroot}

#----------------------------------------------------------------------------

%files -n %libname
%defattr(-,root,root)
%{_libdir}/compiz/libccp.so
%{_libdir}/%{shortname}/backends/libini.so
%{_libdir}/%{name}.so.*
%{_datadir}/%{shortname}/global.xml

%files -n %libname_devel
%defattr(-,root,root)
%dir %{_includedir}/%{shortname}
%{_includedir}/%{shortname}/ccs.h
%{_libdir}/compiz/libccp.a
%{_libdir}/%{shortname}/backends/libini.a
%{_libdir}/%{name}.a
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc
