%include	/usr/lib/rpm/macros.php
Summary:	An Exif reader & writer
Name:		phpExifRW
Version:	1.0
Release:	1
License:	LGPL v2
Group:		Development/Languages/PHP
Source0:	http://www.vinayras.com/projects/%{name}-%{version}.tar.gz
# Source0-md5:	831e9745c47138dfa45957fc3c3e00a3
URL:		http://www.vinayras.com/project/phpexifrw.php
BuildRequires:	rpm-php-pearprov
Requires:	php-exif
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
phpExifRW is a pure PHP class to read, write, and transfer EXIF
information that most digital cameras produce. This class overcomes
the problem of most distributions that do not add Exif extensions in
their default installation of PHP.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{name}

install *.inc $RPM_BUILD_ROOT%{php_pear_dir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES *.php *.txt
%dir %{php_pear_dir}/%{name}
%{php_pear_dir}/%{name}/*.inc
