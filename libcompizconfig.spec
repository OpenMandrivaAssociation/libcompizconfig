%define shortname compizconfig
%define name libcompizconfig
%define version 0.8.4
%define rel 3
%define git 0

%define major 0
%define libname %mklibname %shortname %major
%define libname_devel %mklibname -d %shortname

%if  %{git}
%define srcname %{name}-%{git}.tar.lzma
%define distname %{name}
%define release %mkrel 0.%{git}.%{rel}
%else
%define srcname %{name}-%{version}.tar.bz2
%define distname %{name}-%{version}
%define release %mkrel %{rel}
%endif


Summary: Backend configuration library from Compiz Fusion
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://releases.compiz-fusion.org/%{version}/%{srcname}
License: GPL
Group: System/X11
URL: http://www.compiz-fusion.org/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: libxml2-devel
BuildRequires: compiz-devel >= %{version}
BuildRequires: gettext-devel
BuildRequires: intltool

%description
Backend configuration library from Compiz Fusion

#----------------------------------------------------------------------------

%package -n %libname
Summary: Backend configuration library from Compiz Fusion
Group: System/X11
Provides: %name = %{version}-%{release}

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
  # This is a git snapshot, so we need to generate makefiles.
  sh autogen.sh -V
%endif
# Needed due to X11 link cockup in src/Makefile.in
aclocal
automake
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
%dir %{_sysconfdir}/compizconfig
%{_sysconfdir}/compizconfig/config
%{_libdir}/compiz/libccp.so
%{_libdir}/%{shortname}/backends/libini.so
%{_libdir}/%{name}.so.%{major}*
%{_datadir}/compiz/ccp.xml

%files -n %libname_devel
%defattr(-,root,root)
%dir %{_includedir}/%{shortname}
%{_includedir}/%{shortname}/ccs.h
%{_includedir}/%{shortname}/ccs-backend.h
%{_libdir}/compiz/libccp.a
%{_libdir}/%{shortname}/backends/libini.a
%{_libdir}/%{name}.a
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

