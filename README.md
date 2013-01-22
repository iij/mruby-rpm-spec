mruby-rpm-spec
==============

1. Download a zipball into SOURCES directory as "mruby-master.zip".
```
curl -L -o $RPM/SOURCES/mruby-master.zip https://github.com/mruby/mruby/archive/master.zip
```
2. Run rpmbuild.
```
rpmbuild -bb mruby.spec
```
3. You have an mruby rpm :)
