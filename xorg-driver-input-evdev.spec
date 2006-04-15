Summary:	X.org input driver for Linux generic event devices
Summary(pl):	Sterownik wej¶ciowy X.org dla ogólnych urz±dzeñ linuksowych generuj±cych zdarzenia
Name:		xorg-driver-input-evdev
Version:	1.1.1
Release:	0.1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-evdev-%{version}.tar.bz2
# Source0-md5:	1fe5ef6abf138ef4f334f28d58a986dc
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Linux generic event devices. It supports all
input devices that the kernel knows about, including most mice and
keyboards.

%description -l pl
Sterownik wej¶ciowy X.org dla ogólnych urz±dzeñ linuksowych
generuj±cych zdarzenia. Obs³uguje wszystkie urz±dzenia wej¶ciowe znane
przez j±dro, w tym wiêkszo¶æ myszy i klawiatur.

%prep
%setup -q -n xf86-input-evdev-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog
%attr(755,root,root) %{_libdir}/xorg/modules/input/evdev_drv.so
%{_mandir}/man4/evdev.4*
