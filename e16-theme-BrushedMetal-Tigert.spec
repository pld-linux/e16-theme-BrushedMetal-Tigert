%define	_tname	BrushedMetal-Tigert
Summary:	Enlightenment BrushedMetal-Tigert theme
Summary(pl):	Wystr�j BrushedMetal-Tigert dla Enlightenmenta
Name:		e16-theme-%{_tname}
Version:	0.16.8
Release:	1
License:	GPL
Group:		Themes
Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
# Source0-md5:	e73a4e329369f013d738e965618942d4
URL:		http://www.enlightenment.org/
Requires:	e16
Obsoletes:	enlightenment-theme-%{_tname} <= 0.16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Enlightenment BrushedMetal-Tigert theme.

%description -l pl
Wystr�j BrushedMetal-Tigert dla Enlightenmenta.

%prep
%setup -q
mkdir %{_tname}
tar -zxf %{_tname}.etheme -C %{_tname}
rm %{_tname}/fonts.cfg.*

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/e16/themes/
cp -a %{_tname} $RPM_BUILD_ROOT%{_datadir}/e16/themes/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/e16/themes/%{_tname}
