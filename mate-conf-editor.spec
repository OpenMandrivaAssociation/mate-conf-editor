Summary:	An editor for the MateConf configuration system
Name:		mate-conf-editor
Version:	1.2.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		http://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/1.2/%{name}-%{version}.tar.xz

BuildRequires:	docbook-dtd412-xml
BuildRequires:	intltool
BuildRequires:	mate-common
BuildRequires:	mate-conf
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(mateconf-2.0)
BuildRequires:	pkgconfig(mate-doc-utils)

%description
mate-conf-editor is an editor for the MateConf configuration system

%prep
%setup -q

%build
NOCONFIGURE=yes ./autogen.sh
%configure2_5x \
	--disable-scrollkeeper

%make

%install
%makeinstall_std

rm -rf %{buildroot}/var/lib/scrollkeeper

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc README AUTHORS NEWS
%{_sysconfdir}/mateconf/schemas/mateconf-editor.schemas
%{_bindir}/*
%{_datadir}/applications/*
%{_datadir}/mateconf-editor/icons/hicolor/*/*/*
%{_iconsdir}/hicolor/*/*/*
%{_mandir}/man1/*
# mate help files
%{_datadir}/mate/help
