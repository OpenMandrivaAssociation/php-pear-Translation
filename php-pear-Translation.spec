%define		_class		Translation
%define		upstream_name	%{_class}

Name:		php-pear-%{upstream_name}
Version:	1.2.6pl1
Release:	17
Summary:	Class for creating multilingual websites
License:	PHP License
Group:		Development/PHP
URL:		https://pear.php.net/package/Translation/
Source0:	http://download.pear.php.net/package/%{upstream_name}-%{version}.tar.bz2
Requires(post): php-pear
Requires(preun): php-pear
Requires:	php-pear
BuildArch:	noarch
BuildRequires:	php-pear
BuildRequires:	recode

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

cd %{upstream_name}-%{version}
pear install --nodeps --packagingroot %{buildroot} %{upstream_name}.xml
rm -rf %{buildroot}%{_datadir}/pear/.??*

rm -rf %{buildroot}%{_datadir}/pear/docs
rm -rf %{buildroot}%{_datadir}/pear/tests

install -d %{buildroot}%{_datadir}/pear/packages
install -m 644 %{upstream_name}.xml %{buildroot}%{_datadir}/pear/packages

%clean



%files
%defattr(-,root,root)
%doc %{upstream_name}-%{version}/docs/*
%{_datadir}/pear/%{_class}
%{_datadir}/pear/packages/%{upstream_name}.xml


%changelog
* Fri Dec 16 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.6pl1-15mdv2012.0
+ Revision: 742295
- fix major breakage by careless packager

* Fri May 27 2011 Oden Eriksson <oeriksson@mandriva.com> 1.2.6pl1-14
+ Revision: 679599
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 1.2.6pl1-13mdv2011.0
+ Revision: 613787
- the mass rebuild of 2010.1 packages

* Sun Nov 15 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.6pl1-12mdv2010.1
+ Revision: 466329
- spec cleanup
- use pear installer
- don't ship tests, even in documentation
- own all directories
- use rpm filetriggers starting from mandriva 2010.1

* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 1.2.6pl1-11mdv2010.0
+ Revision: 441663
- rebuild

* Thu Jan 01 2009 Oden Eriksson <oeriksson@mandriva.com> 1.2.6pl1-10mdv2009.1
+ Revision: 322713
- rebuild

* Thu Jul 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.2.6pl1-9mdv2009.0
+ Revision: 237155
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Nov 11 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.6pl1-8mdv2007.0
+ Revision: 82763
- Import php-pear-Translation

* Fri Feb 10 2006 Oden Eriksson <oeriksson@mandriva.com> 1.2.6pl1-8mdk
- new group (Development/PHP)

* Fri Aug 26 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.6pl1-7mdk
- rebuilt to fix auto deps

* Wed Aug 10 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.6pl1-6mdk
- rebuilt to use new pear auto deps/reqs from pld

* Sun Jul 31 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.6pl1-5mdk
- fix deps

* Fri Jul 22 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.6pl1-4mdk
- fix the package.xml file so it will register

* Thu Jul 21 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.6pl1-3mdk
- reworked the %%post and %%preun stuff, like in conectiva
- fix deps

* Wed Jul 20 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.6pl1-2mdk
- fix deps

* Tue Jul 19 2005 Oden Eriksson <oeriksson@mandriva.com> 1.2.6pl1-1mdk
- initial Mandriva package (PLD import)

