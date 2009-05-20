%define	module	Data-Visitor
%define	name	perl-%{module}
%define	modprefix Data
%define	version	0.25
%define	release	%mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	A visitor for Perl data structures
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}
Source:		http://www.cpan.org/modules/by-module/%{modprefix}/%{module}-%{version}.tar.bz2
Requires:	    perl-namespace-clean
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Data::Alias)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl-Test-MockObject >= 1.04
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(Tie::ToObject)
BuildRequires:	perl(Squirrel)
BuildRequires:	perl-namespace-clean
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

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

