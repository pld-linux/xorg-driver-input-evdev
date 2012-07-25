Summary:	X.org input driver for Linux generic event devices
Summary(pl.UTF-8):	Sterownik wejściowy X.org dla ogólnych urządzeń linuksowych generujących zdarzenia
Name:		xorg-driver-input-evdev
Version:	2.7.1
Release:	1
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-evdev-%{version}.tar.bz2
# Source0-md5:	fa7660c6fb09a8365289219d4d1de0e5
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	mtdev-devel
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	udev-devel
BuildRequires:	xorg-proto-inputproto-devel >= 2.2
BuildRequires:	xorg-proto-kbproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.12
%{?requires_xorg_xserver_xinput}
Requires:	xorg-xserver-server >= 1.12
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Linux generic event devices. It supports all
input devices that the kernel knows about, including most mice and
keyboards.

%description -l pl.UTF-8
Sterownik wejściowy X.org dla ogólnych urządzeń linuksowych
generujących zdarzenia. Obsługuje wszystkie urządzenia wejściowe znane
przez jądro, w tym większość myszy i klawiatur.

%package devel
Summary:	Header file for evdev driver
Summary(pl.UTF-8):	Plik nagłówkowy sterownika evdev
Group:		Development/Libraries

%description devel
Header file for evdev driver.

%description devel -l pl.UTF-8
Plik nagłówkowy sterownika evdev.

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/input/evdev_drv.so
%{_mandir}/man4/evdev.4*

%files devel
%defattr(644,root,root,755)
%{_includedir}/xorg/evdev-properties.h
%{_pkgconfigdir}/xorg-evdev.pc
