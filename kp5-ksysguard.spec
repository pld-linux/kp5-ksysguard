%define		kdeplasmaver	5.5.4
%define		qtver		5.5.1
%define		kpname		ksysguard
Summary:	ksysguard
Name:		kp5-%{kpname}
Version:	5.5.4
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	36158a670305ecd8ef29415448917d5a
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= %{qtver}
BuildRequires:	Qt5Widgets-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.5.0
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kdelibs4support-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kitemviews-devel
BuildRequires:	kf5-knewstuff-devel
BuildRequires:	kp5-libksysguard-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
ksysguard

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kpname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksysguard
%{_sysconfdir}/ksysguarddrc
/etc/xdg/ksysguard.knsrc
%attr(755,root,root) %{_bindir}/ksysguardd
%attr(755,root,root) %{_libdir}/libkdeinit5_ksysguard.so
%{_desktopdir}/org.kde.ksysguard.desktop
%{_iconsdir}/hicolor/16x16/apps/computer.png
%{_iconsdir}/hicolor/16x16/apps/daemon.png
%{_iconsdir}/hicolor/16x16/apps/kdeapp.png
%{_iconsdir}/hicolor/16x16/apps/kernel.png
%{_iconsdir}/hicolor/16x16/apps/ksysguardd.png
%{_iconsdir}/hicolor/16x16/apps/running.png
%{_iconsdir}/hicolor/16x16/apps/shell.png
%{_iconsdir}/hicolor/16x16/apps/unknownapp.png
%{_iconsdir}/hicolor/16x16/apps/waiting.png
%{_datadir}/knotifications5/ksysguard.notifyrc
%{_datadir}/ksysguard/ProcessTable.sgrd
%{_datadir}/ksysguard/SystemLoad2.sgrd
%{_datadir}/kxmlgui5/ksysguard/ksysguardui.rc
