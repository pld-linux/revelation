Summary:	A password manager for the GNOME 2 desktop
Summary(pl.UTF-8):	Zarządca haseł dla środowiska GNOME 2
Name:		revelation
Version:	0.4.11
Release:	3
License:	GPL
Group:		X11/Applications
Source0:	ftp://oss.codepoet.no/revelation/%{name}-%{version}.tar.bz2
# Source0-md5:	e2db4a2f00f59b18798d4453c778129f
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-zh_CN.patch
URL:		http://oss.codepoet.no/revelation/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cracklib-devel
BuildRequires:	libtool
BuildRequires:	python-Crypto >= 1.9
BuildRequires:	python-gnome-devel >= 2.12.4
BuildRequires:	python-gnome-desktop-devel
BuildRequires:	python-gnome-extras-devel >= 2.0
BuildRequires:	python-gnome-ui >= 2.12.4
BuildRequires:	python-libxml2 >= 2.0.0
BuildRequires:	python-pygtk-devel >= 2.12.4
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
Requires(post,preun):	GConf2
Requires:	hicolor-icon-theme
Requires:	python-Crypto >= 1.9
Requires:	python-gnome >= 2.12.4
Requires:	python-gnome-desktop-applet >= 2.14.0
Requires:	python-gnome-gconf >= 2.12.4
Requires:	python-gnome-vfs >= 2.12.4
Requires:	python-libxml2 >= 2.0.0
Requires:	python-PyXML
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Revelation is a password manager for the GNOME 2 desktop. It organizes
accounts in a tree structure, and stores them as AES-encrypted XML
files.

%description -l pl.UTF-8
Revelation jest zarządcą haseł dla środowiska GNOME 2. Wyświetla konta
w postaci drzewa, a dane przechowuje w zakodowanych plikach XML.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
mv po/zh.po po/zh_CN.po

%build
%{__libtoolize}
%{__aclocal}
%{__automake}
%{__autoconf}
%configure \
	--disable-schemas-install \
	--disable-desktop-update \
	--disable-mime-update
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_pixmapsdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{py_sitedir}/%{name}/*.py
rm -f $RPM_BUILD_ROOT%{py_sitedir}/%{name}/datahandler/*.py

install data/icons/48x48/revelation.png $RPM_BUILD_ROOT%{_pixmapsdir}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install revelation.schemas
%gconf_schema_install revelation-applet.schemas
%update_desktop_database_post
umask 022
/usr/bin/update-mime-database %{_datadir}/mime ||:

%preun
%gconf_schema_uninstall revelation.schemas
%gconf_schema_uninstall revelation-applet.schemas

%postun
%update_desktop_database_postun
if [ $1 = 0 ]; then
	umask 022
	/usr/bin/update-mime-database %{_datadir}/mime
fi

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/revelation-applet
%{_datadir}/%{name}
%{_datadir}/mime/packages/revelation.xml
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/16x16/apps/*.png
%{_iconsdir}/hicolor/24x24/apps/*.png
%{_iconsdir}/hicolor/32x32/apps/*.png
%{_iconsdir}/hicolor/48x48/apps/*.png
%{_iconsdir}/hicolor/48x48/mimetypes/*.png
%{_libdir}/bonobo/servers/GNOME_RevelationApplet.server
%{_pixmapsdir}/*.png

%dir %{py_sitedir}/%{name}
%dir %{py_sitedir}/%{name}/datahandler
%dir %{py_sitedir}/%{name}/bundle
%attr(755,root,root) %{py_sitedir}/%{name}/*.so
%{py_sitedir}/%{name}/*.py[oc]
%{py_sitedir}/%{name}/datahandler/*.py[co]
%{py_sitedir}/%{name}/bundle/*.py[co]

%{_sysconfdir}/gconf/schemas/revelation.schemas
%{_sysconfdir}/gconf/schemas/revelation-applet.schemas
