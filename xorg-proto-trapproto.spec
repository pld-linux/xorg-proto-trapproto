Summary:	Trap protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u Trap i pomocnicze
Name:		xorg-proto-trapproto
Version:	3.4.1
Release:	0.1
License:	MIT
Group:		X11/Development/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC1/proto/trapproto-%{version}.tar.bz2
# Source0-md5:	12cee4cf212facd7c4a1a2dab02ca731
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Trap protocol and ancillary headers.

%description -l pl
Nag��wki protoko�u Trap i pomocnicze.

%package devel
Summary:	Trap protocol and ancillary headers
Summary(pl):	Nag��wki protoko�u Trap i pomocnicze
Group:		X11/Development/Libraries
Requires:	xorg-proto-xproto-devel

%description devel
Trap protocol and ancillary headers.

%description devel -l pl
Nag��wki protoko�u Trap i pomocnicze.

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
