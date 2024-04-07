#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v7
# autospec commit: f56f1fa
#
Name     : perl-Clipboard
Version  : 0.29
Release  : 34
URL      : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Clipboard-0.29.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/S/SH/SHLOMIF/Clipboard-0.29.tar.gz
Summary  : 'Copy and paste with any OS'
Group    : Development/Tools
License  : Artistic-1.0-Perl GPL-2.0
Requires: perl-Clipboard-bin = %{version}-%{release}
Requires: perl-Clipboard-license = %{version}-%{release}
Requires: perl-Clipboard-man = %{version}-%{release}
Requires: perl-Clipboard-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(CGI)
BuildRequires : perl(URI::Escape)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# NAME
Clipboard - Copy and paste with any OS
# VERSION
version 0.29
# SYNOPSIS
use Clipboard;
print Clipboard->paste;
Clipboard->copy('foo');
# Same as copy on non-X / non-Xclip systems
Clipboard->copy_to_all_selections('text_to_copy');

%package bin
Summary: bin components for the perl-Clipboard package.
Group: Binaries
Requires: perl-Clipboard-license = %{version}-%{release}

%description bin
bin components for the perl-Clipboard package.


%package dev
Summary: dev components for the perl-Clipboard package.
Group: Development
Requires: perl-Clipboard-bin = %{version}-%{release}
Provides: perl-Clipboard-devel = %{version}-%{release}
Requires: perl-Clipboard = %{version}-%{release}

%description dev
dev components for the perl-Clipboard package.


%package license
Summary: license components for the perl-Clipboard package.
Group: Default

%description license
license components for the perl-Clipboard package.


%package man
Summary: man components for the perl-Clipboard package.
Group: Default

%description man
man components for the perl-Clipboard package.


%package perl
Summary: perl components for the perl-Clipboard package.
Group: Default
Requires: perl-Clipboard = %{version}-%{release}

%description perl
perl components for the perl-Clipboard package.


%prep
%setup -q -n Clipboard-0.29
cd %{_builddir}/Clipboard-0.29
pushd ..
cp -a Clipboard-0.29 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Clipboard
cp %{_builddir}/Clipboard-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-Clipboard/38e94f89ec602e1a6495ef7c30477d01aeefedc9 || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

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
/usr/share/man/man3/Clipboard::MacPasteboard.3
/usr/share/man/man3/Clipboard::Win32.3
/usr/share/man/man3/Clipboard::Xclip.3
/usr/share/man/man3/Clipboard::Xsel.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Clipboard/38e94f89ec602e1a6495ef7c30477d01aeefedc9

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/clipaccumulate.1
/usr/share/man/man1/clipbrowse.1
/usr/share/man/man1/clipedit.1
/usr/share/man/man1/clipfilter.1
/usr/share/man/man1/clipjoin.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
