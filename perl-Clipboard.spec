#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Clipboard
Version  : 0.13
Release  : 5
URL      : https://cpan.metacpan.org/authors/id/K/KI/KING/Clipboard-0.13.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/K/KI/KING/Clipboard-0.13.tar.gz
Summary  : 'Cliboard - Copy and Paste with any OS'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Clipboard-bin = %{version}-%{release}
Requires: perl-Clipboard-man = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(Module::Install)

%description
SYNOPSIS
use Clipboard; print Clipboard->paste; Clipboard->copy('foo');
Clipboard->cut() is an alias for copy(). copy() is the preferred
method, because we're not really "cutting" anything.

%package bin
Summary: bin components for the perl-Clipboard package.
Group: Binaries
Requires: perl-Clipboard-man = %{version}-%{release}

%description bin
bin components for the perl-Clipboard package.


%package dev
Summary: dev components for the perl-Clipboard package.
Group: Development
Requires: perl-Clipboard-bin = %{version}-%{release}
Provides: perl-Clipboard-devel = %{version}-%{release}

%description dev
dev components for the perl-Clipboard package.


%package man
Summary: man components for the perl-Clipboard package.
Group: Default

%description man
man components for the perl-Clipboard package.


%prep
%setup -q -n Clipboard-0.13

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.28.1/Clipboard.pm
/usr/lib/perl5/vendor_perl/5.28.1/Clipboard/MacPasteboard.pm
/usr/lib/perl5/vendor_perl/5.28.1/Clipboard/Win32.pm
/usr/lib/perl5/vendor_perl/5.28.1/Clipboard/Xclip.pm

%files bin
%defattr(-,root,root,-)
/usr/bin/clipaccumulate
/usr/bin/clipbrowse
/usr/bin/clipedit
/usr/bin/clipfilter
/usr/bin/clipjoin

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Clipboard.3

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/clipaccumulate.1
/usr/share/man/man1/clipbrowse.1
/usr/share/man/man1/clipedit.1
/usr/share/man/man1/clipfilter.1
/usr/share/man/man1/clipjoin.1
