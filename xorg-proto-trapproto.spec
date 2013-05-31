Summary:	Trap extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Trap
Name:		xorg-proto-trapproto
Version:	3.4.3
Release:	3
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/proto/trapproto-%{version}.tar.bz2
# Source0-md5:	3b713239e5e6b269b31cb665563358df
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Trap extension headers.

%description -l pl.UTF-8
Pliki nagłówkowe rozszerzenia Trap.

%package devel
Summary:	Trap extension headers
Summary(pl.UTF-8):	Pliki nagłówkowe rozszerzenia Trap
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel
Requires:	xorg-lib-libXt-devel

%description devel
Trap extension headers.

%description devel -l pl.UTF-8
Pliki nagłówkowe rozszerzenia Trap.

%prep
%setup -q -n trapproto-%{version}

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%{_includedir}/X11/extensions/xtrap*.h
%{_pkgconfigdir}/trapproto.pc
