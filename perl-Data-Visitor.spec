%define	module	Data-Visitor
%define	name	perl-%{module}
%define	modprefix Data
%define	version	0.09
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A visitor for Perl data structures
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{module}
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl-Test-MockObject >= 1.04
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::use::ok)

%description
This module is a simple visitor implementation for Perl values.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%__make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes
%{perl_vendorlib}/%{modprefix}
%doc %{_mandir}/*/*

