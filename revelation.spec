%include	/usr/lib/rpm/macros.python
Summary:	A password manager for the GNOME 2 desktop
Summary(pl):	Zarz±dca hase³ dla ¶rodowiska GNOME 2
Name:		revelation
Version:	0.2.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://oss.wired-networks.net/%{name}/%{name}-%{version}.tar.bz2
# Source0-md5:	8c0a25a61a9a5d7502c62b9ec6f7c261
URL:		http://oss.wired-networks.net/revelation/
BuildRequires:	python-Crypto
BuildRequires:	python-gnome
BuildRequires:	python-gnome-ui
BuildRequires:	python-libxml2
BuildRequires:	python-pygtk-devel >= 2.0
Requires:	python-Crypto
Requires:	python-gnome
Requires:	python-gnome-ui
Requires:	python-libxml2
Requires:	python-pygtk-devel >= 2.0
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

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=${RPM_BUILD_ROOT} \
	--prefix=%{_prefix} \
	--install-purelib=%{py_sitedir} \
	-O2

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
%dir %{py_sitedir}/%{name}
%{py_sitedir}/%{name}/*.py[oc]
