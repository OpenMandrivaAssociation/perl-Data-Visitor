%define	upstream_name	 Data-Visitor
%define upstream_version 0.30

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	A visitor for Perl data structures
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/Data-Visitor-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Data::Alias)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl-Test-MockObject >= 1.04
BuildRequires:	perl(Test::More)
BuildRequires: perl(Test::Requires)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(Tie::ToObject)
BuildRequires:	perl(Squirrel)
BuildRequires:	perl(namespace::clean)

BuildArch:	noarch

Requires:	perl(namespace::clean)

%description
This module is a simple visitor implementation for Perl values.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std

%files
%doc Changes
%{perl_vendorlib}/Data
%{_mandir}/*/*

%changelog
* Sun May 29 2011 Funda Wang <fwang@mandriva.org> 0.270.0-3mdv2011.0
+ Revision: 681386
- mass rebuild

* Tue Dec 07 2010 Oden Eriksson <oeriksson@mandriva.com> 0.270.0-2mdv2011.0
+ Revision: 614498
- the mass rebuild of 2010.1 packages

* Fri Feb 05 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.270.0-1mdv2010.1
+ Revision: 501142
- update to 0.27

* Mon Sep 14 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.260.0-1mdv2010.0
+ Revision: 439419
- adding missing buildrequires:
- update to 0.26

* Sat Aug 01 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.250.0-1mdv2010.0
+ Revision: 406321
- rebuild using %%perl_convert_version

* Wed May 20 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.25-1mdv2010.0
+ Revision: 377987
- update to new version 0.25

* Wed May 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.24-1mdv2010.0
+ Revision: 372390
- new version

* Sun Dec 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2009.1
+ Revision: 320427
- update to new version 0.22

* Sat Oct 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.21-1mdv2009.1
+ Revision: 292103
- update to new version 0.21

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.19-1mdv2009.0
+ Revision: 277946
- update to new version 0.19

* Tue Aug 12 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-2mdv2009.0
+ Revision: 271115
- fix dependencies

* Wed Jul 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2009.0
+ Revision: 242656
- new version

* Sun Jul 20 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.17-1mdv2009.0
+ Revision: 238948
- update to new version 0.17

* Wed Jan 23 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.15-1mdv2008.1
+ Revision: 156964
- new version

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.10-1mdv2008.1
+ Revision: 138008
- update to new version 0.10

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sat Oct 13 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.09-1mdv2008.0
+ Revision: 98023
- update to new version 0.09
- update to new version 0.09

* Tue Jul 03 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.08-1mdv2008.0
+ Revision: 47629
- update to new version 0.08


* Tue Sep 05 2006 Scott Karns <scottk@mandriva.org>
+ 2006-09-05 12:28:48 (60030)
- spec file cleanup
- bump release for rebuild

* Tue Sep 05 2006 Scott Karns <scottk@mandriva.org>
+ 2006-09-05 12:24:07 (60029)
Import perl-Data-Visitor

* Fri May 05 2006 Scott Karns <scottk@mandriva.org> 0.05-3mdk
- Update BuildRequires

* Wed May 03 2006 Scott Karns <scottk@mandriva.org> 0.05-2mdk
- Fix BuildRequires
- Update package file ownership

* Fri Apr 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.05-1mdk
- New release 0.05
- Fix Source URL
- Fix BuildRequires

* Wed Apr 05 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.04-1mdk
- New release 0.04

* Thu Mar 16 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.02-2mdk
- Adjust BuildRequires

* Wed Mar 15 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.02-1mdk
- Initial MDV release


