Summary: Lightweight Ruby
Name: mruby
Version: 0.0
Release: 0
Source0: mruby-master.zip
License: MIT
Group: Development/Languages
Packager: Tomoyuki Sahara (tsahara@iij.ad.jp)
Buildroot: %{_tmppath}/%{name}-%{version}-%{release}-root
URL: http://github.com/mruby/mruby/
BuildRequires: binutils, bison, gcc, ruby, unzip

%description
mruby is the lightweight implementation of the Ruby language complying to
(part of) the ISO standard.

%prep
%setup -T -c -n mruby-master
cd ..
unzip -q %{SOURCE0}

%build
ruby ./minirake

%install
install -d $RPM_BUILD_ROOT/%{_bindir}
install -c -s -m755 bin/mirb $RPM_BUILD_ROOT/%{_bindir}
install -c -s -m755 bin/mrbc $RPM_BUILD_ROOT/%{_bindir}
install -c -s -m755 bin/mruby $RPM_BUILD_ROOT/%{_bindir}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%{_bindir}/mirb
%{_bindir}/mrbc
%{_bindir}/mruby

%changelog
* Tue Jan 22 2013 Tomoyuki Sahara <tsahara@iij.ad.jp> 0.0-0
initial version.
