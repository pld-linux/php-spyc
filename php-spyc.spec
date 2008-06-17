Summary:	A simple PHP YAML class
Name:		php-spyc
Version:	0.2.5
Release:	1
License:	MIT
Group:		Development/Languages/PHP
URL:		http://spyc.sourceforge.net/
Source0:	http://dl.sourceforge.net/spyc/spyc-%{version}.tar.gz
# Source0-md5:	5b25e949e3c016811b194aff8be50d6b
BuildRequires:	rpmbuild(macros) >= 1.461
Requires:	php-common
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Spyc is a YAML loader/dumper written in PHP. Given a YAML document,
Spyc will return an array which you can use however you see fit. Given
an array, Spyc will return a string which contains a YAML document
built from your data.

%prep
%setup -qc
rm -rf CVS *~

# make version independant wrapper
mv spyc.php spyc.php4
cat <<'EOF' > spyc.php
<?
if (intval(PHP_VERSION) < 5) {
	require_once 'spyc.php4';
} else {
	require_once 'spyc.php5';
}
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_data_dir},%{_examplesdir}/%{name}-%{version}}
cp -a spyc.php spyc.php4 spyc.php5 $RPM_BUILD_ROOT%{php_data_dir}
cp -a test.* yaml-{dump,load}.php spyc.yaml $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{php_data_dir}/*
%{_examplesdir}/%{name}-%{version}
