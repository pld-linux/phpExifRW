Summary:	An Exif reader & writer
Summary(pl.UTF-8):	Klasa do odczytu i zapisu Exif
Name:		phpExifRW
Version:	1.1
Release:	2
License:	LGPL v2
Group:		Development/Languages/PHP
Source0:	http://www.vinayras.com/projects/%{name}-%{version}.tar.gz
# Source0-md5:	27a9313e8682e54db9f2255ffac7de60
URL:		http://www.vinayras.com/project/phpexifrw.php
BuildRequires:	rpm-php-pearprov
Requires:	php(exif)
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
phpExifRW is a pure PHP class to read, write, and transfer EXIF
information that most digital cameras produce. This class overcomes
the problem of most distributions that do not add Exif extensions in
their default installation of PHP.

%description -l pl.UTF-8
phpExifRW to napisana w czystym PHP klasa do odczytu, zapisu i
przesyłania informacji EXIF tworzonych przez większość aparatów
cyfrowych. Klasa ta przezwycięża problem istniejący w większości
dystrybucji nie dodających rozszerzeń Exif w domyślnej instalacji PHP.

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
