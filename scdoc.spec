Name:     scdoc
Version:  1.9.4
Release:  2
Summary:  Tool for generating roff manual pages

License:  MIT
URL:      https://git.sr.ht/~sircmpwn/%{name}
Source0:  %{url}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

#BuildRequires: gcc
BuildRequires: sed

%description
scdoc is a tool designed to make the process of writing man pages more
friendly. It reads scdoc syntax from stdin and writes roff to stdout, suitable
for reading with man.

%prep
%setup -q

# Disable static linking
sed -i '/-static/d' Makefile

# Fix 'harcoded' installation path
sed -i 's/DESTDIR=/DESTDIR?=/g' Makefile
sed -i 's!PREFIX?=/usr/local!PREFIX?=%{_prefix}!'g Makefile

# Fix 'hardcoded' CFLAGS
sed -i 's/CFLAGS=/CFLAGS+=/g' Makefile

# Use INSTALL provided by the make_install macro
sed -i 's/\tinstall/\t$(INSTALL)/g' Makefile

# proper libdir
sed -i 's!lib/pkgconfig!%{_lib}/pkgconfig!g' Makefile

%build
%make CC=%{__cc}

%install
%make_install PREFIX=%{_prefix}

%check
%make check

%files
%license COPYING
%doc README.md
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man5/%{name}.5*
%{_libdir}/pkgconfig/scdoc.pc
