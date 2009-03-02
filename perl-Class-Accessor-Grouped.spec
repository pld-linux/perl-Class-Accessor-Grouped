#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Class
%define	pnam	Accessor-Grouped
Summary:	Class::Accessor::Grouped - Lets you build groups of accessors
Summary(pl.UTF-8):	Class::Accessor::Grouped - tworzenie grup funkcji dostępowych
Name:		perl-Class-Accessor-Grouped
Version:	0.08002
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/C/CL/CLACO/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	10e66752abaae0d95d8ca0c932c75c1c
URL:		http://search.cpan.org/dist/Class-Accessor-Grouped/
BuildRequires:	perl-Class-Inspector
BuildRequires:	perl-MRO-Compat
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This class lets you build groups of accessors that will call different
getters and setters.

%description -l pl.UTF-8
Ta klasa pozwala tworzyć grupy funkcji dostępowych wywołujących różne
funkcje odczytujące i ustawiające.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} -MExtUtils::MakeMaker -e 'WriteMakefile(NAME=>"Class::Accessor::Grouped")' \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Class/Accessor/*.pm
%{_mandir}/man3/*
