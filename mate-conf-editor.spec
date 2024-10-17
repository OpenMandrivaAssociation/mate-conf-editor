Summary:	An editor for the MateConf configuration system
Name:		mate-conf-editor
Version:	1.4.0
Release:	1
License:	GPLv2+
Group:		Graphical desktop/GNOME
URL:		https://mate-desktop.org
Source0:	http://pub.mate-desktop.org/releases/%{lua: print (string.match(rpm.expand("%{version}"),"%d+.%d+"))}/%{name}-%{version}.tar.xz

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


%changelog
* Wed Jun 06 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.2.0-1
+ Revision: 802808
- imported package mate-conf-editor

