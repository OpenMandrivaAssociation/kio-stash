Name:           kio-stash
Version:	1.0
Release:        2
Summary:        KIO slave and daemon to stash discontinuous file selections
License:        GPLv2+
Group:          Graphical desktop/KDE
URL:            http://www.kde.org
Source0:        https://download.kde.org/stable/%{name}/%{name}-%{version}.tar.xz

BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5DBus)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Test)

BuildRequires:  cmake(ECM)
BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5I18n)
BuildRequires:  cmake(KF5KIO)
BuildRequires:  cmake(KF5DBusAddons)

%description
This KIO slave can be used to stash files in a virtual
folder temporarily. It requires use of a KIO-compatible
file manager, like dolphin.

%files
%doc README.md COPYING
%{_qt5_plugindir}/kf5/kio/filestash.so
%{_qt5_plugindir}/kf5/kded/stashnotifier.so
%{_kde5_datadir}/metainfo/org.kde.filestash.appdata.xml
%{_kde5_datadir}/dbus-1/interfaces/org.kde.kio.StashNotifier.xml

#--------------------------------------------------------------------

%prep
%setup -q
%apply_patches

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build

