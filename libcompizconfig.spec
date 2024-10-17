%define _disable_ld_no_undefined 1
%define rel 2
%define git 0

%define shortname compizconfig
%define major 0
%define libname %mklibname %shortname %major
%define develname %mklibname -d %shortname

%if  %{git}
%define srcname %{name}-%{git}.tar.xz
%define distname %{name}
%define release 0.%{git}.%{rel}
%else
%define srcname %{name}-%{version}.tar.bz2
%define distname %{name}-%{version}
%define release %{rel}
%endif

Summary:	Backend configuration library from Compiz Fusion
Name:		libcompizconfig
Version:	0.9.5.92
Release:	%release
Source0:	http://http://releases.compiz.org/%{version}/%{srcname}
Patch0: 	fix_libdir.patch
License:	GPL
Group:		System/X11
URL:		https://www.compiz.org/

BuildRequires: cmake
BuildRequires: libxml2-devel
BuildRequires: boost-devel
BuildRequires: compiz-devel >= %{version}
BuildRequires: gettext-devel
BuildRequires: protobuf-devel
BuildRequires: intltool
BuildRequires: xsltproc

%description
Backend configuration library from Compiz Fusion

%package -n %{libname}
Summary:	Backend configuration library from Compiz Fusion
Group:		System/X11
Provides:	%{name} = %{version}-%{release}

%description -n %{libname}
Backend configuration library from Compiz Fusion

%package -n %{develname}
Summary:	Development files for libcompizconfig
Group:		Development/X11
Requires:	%{libname} = %{version}-%{release}
Provides:	%{name}-devel = %{version}-%{release}

%description -n %{develname}
Development files for libcompizconfig

%prep
%setup -qn %{distname}
%patch0 -p1

%build
%if %{git}
# no idea if this is still valid 2011-11-02
  # This is a git snapshot, so we need to generate makefiles.
  sh autogen.sh -V
%endif

%cmake
%make

%install
rm -rf %{buildroot}
%makeinstall_std -C build
find %{buildroot} -name *.la -exec rm -f {} \;

# This should work, but is buggy upstream:
# make DESTDIR=%{buildroot} findcompizconfig_install
# So we do this instead:
mkdir -p %{buildroot}%{_datadir}/cmake/Modules
cmake -E copy cmake/FindCompizConfig.cmake %{buildroot}%{_datadir}/cmake/Modules

%clean
rm -rf %{buildroot}


%files -n %{libname}
%defattr(-,root,root)
%{_libdir}/compiz/libccp.so
%{_libdir}/%{shortname}/backends/libini.so
%{_libdir}/%{name}.so.*
%{_datadir}/gconf/schemas/*.schemas
%{_datadir}/glib-2.0/schemas/*.xml
%{_datadir}/compiz/ccp.xml

%files -n %{develname}
%defattr(-,root,root)
%dir %{_includedir}/%{shortname}
%{_includedir}/%{shortname}/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/*
%{_datadir}/compiz/cmake/*cmake
%{_datadir}/cmake/Modules


