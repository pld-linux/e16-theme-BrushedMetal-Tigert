%define	_tname	BrushedMetal-Tigert
Summary:	Enlightenment BrushedMetal-Tigert theme
Summary(pl):	Wystrój BrushedMetal-Tigert dla Enlightenmenta
Name:		enlightenment-theme-%{_tname}
Version:	0.16
Release:	1
License:	GPL
Group:		Themes
Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
# Source0-md5:	e26afc428365f3e6c4ac4a3ecae81540
# Source0-size:	3905170
Patch0:		%{name}-i18n.patch
URL:		http://www.enlightenment.org/
Requires:	enlightenment >= 0.16.7.1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enlightenment BrushedMetal-Tigert theme.

%description -l pl
Wystrój BrushedMetal-Tigert dla Enlightenmenta.

%prep
%setup -q
mkdir %{_tname}
tar -zxf %{_tname}.etheme -C %{_tname}
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/enlightenment/themes/
cp -a %{_tname} $RPM_BUILD_ROOT%{_datadir}/enlightenment/themes/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/enlightenment/themes/%{_tname}
