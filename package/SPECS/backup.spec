Name: backup.py
Version: 1.0
Release: 1
License: GPL
Summary: A python script to backup specific files

%description
Copywrite (c) 2015 Matthew J. Brown

%install
mkdir -p %{_buildrootdir}/usr/local/bin
mkdir -p %{_buildrootdir}/etc

cp ../../backup.py %{_buildrootdir}/usr/local/bin/backup.py
cp ../../backup.config %{_buildrootdir}/etc/backup.config

%files
%defattr(-,root,root)

/usr/local/bin/backup.py
/etc/backup.config

%changelog
*Fri Mar 20 2015 Matthew Brown <hew@techie.com>
-Modified HelloWorld project to backup.py project for CS345 final
*Fri Feb 6 2015 Matthew Brown <hew@techie.com>
-With the help of Michael Cohen <mcohen@coloradotech.edu> in CTU class CS345 Unix Systems Prog
