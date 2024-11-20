Name:          maui-mauikit-nota
Version:       4.0.0
Release:       %autorelease
# the apache license if for gradle-wrapper.jar
License:       BSD-3-Clause AND MIT AND GPL-2.0-or-later AND GPL-3.0-or-later AND CC0-1.0 AND Apache-2.0
Summary:       Nota is a simple text editor for desktop and mobile computers
URL:           https://apps.kde.org/nota/

Source0:       https://invent.kde.org/maui/nota/-/archive/v4.0.0/nota-v%{version}.tar.gz

#backport of the licenses fix to 4.0.0
Patch1:        LICENSES.patch

BuildRequires: extra-cmake-modules
BuildRequires: gcc-c++
BuildRequires: kf6-rpm-macros
BuildRequires: libappstream-glib
BuildRequires: desktop-file-utils

BuildRequires: cmake(Qt6Core)
BuildRequires: cmake(Qt6QuickControls2)
BuildRequires: cmake(Qt6Quick)
BuildRequires: cmake(Qt6DBus)
BuildRequires: cmake(Qt6Widgets)
BuildRequires: cmake(Qt6Qml)
BuildRequires: cmake(KF6I18n)
BuildRequires: cmake(KF6CoreAddons)
BuildRequires: cmake(MauiKit4)
BuildRequires: cmake(MauiKitFileBrowsing4)
BuildRequires: cmake(MauiKitDocuments4)
BuildRequires: cmake(MauiKitTextEditor4)
BuildRequires: cmake(MauiKitTerminal4)
BuildRequires: cmake(KF6KirigamiAddons)

Requires:      maui-mauikit-terminal

%description
%{summary}.


%prep
%autosetup -n nota-v%{version} -p1


%build
%cmake_kf6
%cmake_build


%install
%cmake_install
%find_lang nota --with-man --with-qt --all-name

%check
appstream-util validate-relax --nonet %{buildroot}%{_kf6_metainfodir}/org.kde.nota.metainfo.xml
desktop-file-validate %{buildroot}%{_datadir}/applications/org.kde.nota.desktop

%files -f nota.lang
%license LICENSES/*
%{_kf6_bindir}/nota
%{_kf6_datadir}/applications/org.kde.nota.desktop
%{_kf6_datadir}/icons/hicolor/scalable/apps/nota.svg
%{_metainfodir}/org.kde.nota.metainfo.xml

%changelog
%autochangelog
