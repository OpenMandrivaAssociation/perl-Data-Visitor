%define	upstream_name	 Data-Visitor
%define upstream_version 0.27

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	A visitor for Perl data structures
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Data/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(Data::Alias)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Moose)
BuildRequires:	perl(Task::Weaken)
BuildRequires:	perl-Test-MockObject >= 1.04
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::use::ok)
BuildRequires:	perl(Tie::ToObject)
BuildRequires:	perl(Squirrel)
BuildRequires:	perl(namespace::clean)

BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}

Requires:	perl(namespace::clean)

%description
This module is a simple visitor implementation for Perl values.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
%{perl_vendorlib}/Data
%doc %{_mandir}/*/*
