%define		_class		Translation
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	1.2.6pl1
Release:	%mkrel 12
Summary:	Class for creating multilingual websites
License:	PHP License
Group:		Development/PHP
URL:		http://pear.php.net/package/Translation/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRequires:	recode
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Class allows to store and retrieve all the strings on multilingual
site in the database. Class connects to any database using PHP PEAR
extension. The object should be created for every page. While creation
all the strings connected with specific page and the strings connected
with all the pages on the site are loaded into variable, so access to
them is quite fast and does not overload database server connection.

%prep
%setup -q -c
mv package.xml %{upstream_name}-%{version}/%{upstream_name}.xml

%install
rm -rf %{buildroot}

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean
rm -rf %{buildroot}

%post
%if %mdkversion < 201000
pear install --nodeps --soft --force --register-only \
    %{_datadir}/pear/packages/%{upstream_name}.xml >/dev/null || :
%endif

%preun
%if %mdkversion < 201000
if [ "$1" -eq "0" ]; then
    pear uninstall --nodeps --ignore-errors --register-only \
        %{pear_name} >/dev/null || :
fi
%endif

%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml
