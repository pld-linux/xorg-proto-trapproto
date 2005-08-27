Summary:	Trap protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Trap i pomocnicze
Name:		xorg-proto-trapproto
Version:	3.4
Release:	0.02
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/proto/trapproto-%{version}.tar.bz2
# Source0-md5:	12ea7125950f7e5f989f4df2858978e0
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Trap protocol and ancillary headers.

%description -l pl
Nag³ówki protoko³u Trap i pomocnicze.

%package devel
Summary:	Trap protocol and ancillary headers
Summary(pl):	Nag³ówki protoko³u Trap i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Trap protocol and ancillary headers.

%description devel -l pl
Nag³ówki protoko³u Trap i pomocnicze.

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
%{_includedir}/X11/extensions/*.h
%{_pkgconfigdir}/trapproto.pc
