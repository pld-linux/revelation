Summary:	A password manager for the GNOME 2 desktop
Summary(pl):	Zarz�dca hase� dla �rodowiska GNOME 2
Name:		revelation
Version:	0.3.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://oss.wired-networks.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	f5dac3c4639b43fca0060804ccef3346
URL:		http://oss.wired-networks.net/revelation/
BuildRequires:	python-Crypto >= 1.9
BuildRequires:	python-gnome >= 2.0.0
BuildRequires:	python-gnome-ui >= 2.0.0
BuildRequires:	python-libxml2 >= 2.0.0
BuildRequires:	python-pygtk-devel >= 2.0.0
Requires(post):	GConf2
Requires:	python-Crypto >= 1.9
Requires:	python-gnome >= 2.0.0
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
Revelation jest zarz�dc� hase� dla �rodowiska GNOME 2. Wy�wietla konta
w postaci drzewa, a dane przechowuje w zakodowanych plikach XML.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=${RPM_BUILD_ROOT} \
	--prefix=%{_prefix} \
	--install-purelib=%{py_sitedir} \
	-O2

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%dir %{py_sitedir}/%{name}
%{py_sitedir}/%{name}/*.py[oc]
%{_sysconfdir}/gconf/schemas/*.schemas
