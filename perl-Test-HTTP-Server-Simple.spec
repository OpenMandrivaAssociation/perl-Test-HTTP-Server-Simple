%define upstream_name    Test-HTTP-Server-Simple
%define upstream_version 0.11

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Test::More functions for HTTP::Server::Simple
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Test/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(HTTP::Server::Simple)
BuildRequires:	perl(NEXT)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::Builder::Tester)
BuildRequires:	perl(Test::More)
BuildArch:	noarch

%description
This mixin class provides methods to test an the HTTP::Server::Simple
manpage-based web server. Currently, it provides only one such method:
'started_ok'.

started_ok [$text]
    'started_ok' takes an optional test description. The server needs to
    have been configured (specifically, its port needs to have been set),
    but it should not have been run or backgrounded. 'started_ok' calls
    'background' on the server, which forks it to run in the background.
    the Test::HTTP::Server::Simple manpage takes care of killing the server
    when your test script dies, even if you kill your test script with an
    interrupt. 'started_ok' returns the URL 'http://localhost:$port' which
    you can use to connect to your server.

    Note that if the child process dies, or never gets around to listening
    for connections, this just hangs. (This may be fixed in a future
    version.)

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc META.yml Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/Test/

%changelog
* Fri Apr 30 2010 Michael Scherer <misc@mandriva.org> 0.110.0-1mdv2010.1
+ Revision: 541112
- import perl-Test-HTTP-Server-Simple


* Fri Apr 30 2010 cpan2dist 0.11-1mdv
- initial mdv release, generated with cpan2dist
