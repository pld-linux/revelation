Summary:	A password manager for the GNOME 2 desktop
Summary(pl):	Zarz±dca hase³ dla ¶rodowiska GNOME 2
Name:		revelation
Version:	0.4.4
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://oss.codepoet.no/revelation/%{name}-%{version}.tar.bz2
# Source0-md5:	79c5af34e19c0d1eb25de15b47567060
Patch0:		%{name}-desktop.patch
URL:		http://oss.codepoet.no/revelation/
BuildRequires:	cracklib-devel
BuildRequires:	python-Crypto >= 1.9
BuildRequires:	python-gnome >= 2.0.0
BuildRequires:	python-gnome-extras-devel
BuildRequires:	python-gnome-ui >= 2.0.0
BuildRequires:	python-libxml2 >= 2.0.0
BuildRequires:	python-pygtk-devel >= 2.0.0
BuildRequires:	rpmbuild(macros) >= 1.197
Requires(post,preun):	GConf2
Requires(post,postun):	desktop-file-utils
Requires(post,postun):	shared-mime-info
Requires:	hicolor-icon-theme
Requires:	python-Crypto >= 1.9
Requires:	python-gnome >= 2.0.0
Requires:	python-gnome-extras-applet 
Requires:	python-gnome-gconf >= 2.0.0
Requires:	python-gnome-ui >= 2.0.0
Requires:	python-libxml2 >= 2.0.0
Requires:	python-pygtk-devel >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Revelation is a password manager for the GNOME 2 desktop. It organizes
accounts in a tree structure, and stores them as AES-encrypted XML
files.

%description -l pl
Revelation jest zarz±dc± hase³ dla ¶rodowiska GNOME 2. Wy¶wietla konta
w postaci drzewa, a dane przechowuje w zakodowanych plikach XML.

%prep
%setup -q
%patch0 -p1

%build
%configure \
	--disable-schemas-install \
	--disable-desktop-update \
	--disable-mime-update
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
	
rm -f $RPM_BUILD_ROOT%{py_sitedir}/%{name}/*.py
rm -f $RPM_BUILD_ROOT%{py_sitedir}/%{name}/datahandler/*.py

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

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/revelation-applet
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_iconsdir}/hicolor/16x16/apps/*.png
%{_iconsdir}/hicolor/24x24/apps/*.png
%{_iconsdir}/hicolor/32x32/apps/*.png
%{_iconsdir}/hicolor/48x48/apps/*.png
%{_iconsdir}/hicolor/48x48/mimetypes/*.png
%{_iconsdir}/hicolor/scalable/filesystems/*.svg
%{_datadir}/mime/packages/revelation.xml
%{_libdir}/bonobo/servers/GNOME_RevelationApplet.server
%dir %{py_sitedir}/%{name}
%dir %{py_sitedir}/%{name}/datahandler
%attr(755,root,root) %{py_sitedir}/%{name}/*.so
%{py_sitedir}/%{name}/*.py[oc]
%{py_sitedir}/%{name}/datahandler/*.py[co]
%{_sysconfdir}/gconf/schemas/revelation.schemas
%{_sysconfdir}/gconf/schemas/revelation-applet.schemas
