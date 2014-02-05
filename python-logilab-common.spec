%define module	logilab-common

# Depenedency geenrator finds too many abi deps here
%define __noautoreq 'python\\(abi\\).*'

Summary:	Python modules used by Logilab software
Name:		python-%{module}
Version:	0.60.1
Release:	1
Source0:	http://ftp.logilab.org/pub/common/logilab-common-%{version}.tar.gz
License:	GPLv2+
Group:		Development/Python
Url:		http://www.logilab.org/
Requires:	python-egenix-mx-base
Requires:       python(abi) = %{py_ver}
BuildArch:	noarch
BuildRequires:	python-setuptools

%description
This package contains a number of Python modules that provide low level
functionality used by various free software projects supported by Logilab.

%prep
%setup -q -n %{module}-%{version}

%build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}
find %{buildroot} -perm 600 -exec chmod a+r {} \;

%files
%doc README COPYING ChangeLog
%{_bindir}/pytest
%{py_puresitedir}/logilab*


%changelog
* Thu Jan 12 2012 Lev Givon <lev@mandriva.org> 0.57.1-1
+ Revision: 760524
- Update to 0.57.1.

* Wed Sep 14 2011 Lev Givon <lev@mandriva.org> 0.56.2-1
+ Revision: 699801
- Update to 0.56.2.

* Mon Jul 18 2011 Lev Givon <lev@mandriva.org> 0.56.0-1
+ Revision: 690567
- Update to 0.56.0.

* Sun May 01 2011 Lev Givon <lev@mandriva.org> 0.55.2-1
+ Revision: 661353
- Update to 0.55.2.

* Wed Mar 23 2011 Lev Givon <lev@mandriva.org> 0.55.0-1
+ Revision: 648142
- Update to 0.55.0

* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.54.0-1
+ Revision: 636246
- update to new version 0.54.0

* Wed Nov 24 2010 Lev Givon <lev@mandriva.org> 0.53.0-1mdv2011.0
+ Revision: 600754
- Update to 0.53.0.

* Mon Nov 08 2010 Funda Wang <fwang@mandriva.org> 0.52.1-2mdv2011.0
+ Revision: 594927
- rebuild for py 2.7

* Thu Oct 14 2010 Lev Givon <lev@mandriva.org> 0.52.1-1mdv2011.0
+ Revision: 585618
- Update to 0.52.1.

* Mon Sep 13 2010 Lev Givon <lev@mandriva.org> 0.51.1-1mdv2011.0
+ Revision: 578037
- Update to 0.51.1.

* Mon Aug 30 2010 Lev Givon <lev@mandriva.org> 0.51.0-1mdv2011.0
+ Revision: 574416
- Update to 0.51.0.

* Wed Jul 28 2010 Lev Givon <lev@mandriva.org> 0.50.3-1mdv2011.0
+ Revision: 562809
- Update to 0.50.3.

* Fri May 28 2010 Lev Givon <lev@mandriva.org> 0.50.2-1mdv2011.0
+ Revision: 546543
- Update to 0.50.2.

* Wed Apr 21 2010 Lev Givon <lev@mandriva.org> 0.50.0-1mdv2010.1
+ Revision: 537638
- Update to 0.50.0.

* Sun Apr 04 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.49.0-1mdv2010.1
+ Revision: 531328
- update to new version 0.49.0

* Mon Mar 01 2010 Lev Givon <lev@mandriva.org> 0.48.1-1mdv2010.1
+ Revision: 513238
- Update to 0.48.1.

* Tue Feb 23 2010 Lev Givon <lev@mandriva.org> 0.47.0-1mdv2010.1
+ Revision: 510389
- Update to 0.47.0.

* Tue Feb 09 2010 Lev Givon <lev@mandriva.org> 0.46.1-1mdv2010.1
+ Revision: 503269
- Update to 0.46.1.

* Tue Dec 29 2009 Lev Givon <lev@mandriva.org> 0.46.0-1mdv2010.1
+ Revision: 483695
- Update to 0.46.

* Thu Nov 12 2009 Lev Givon <lev@mandriva.org> 0.45.1-1mdv2010.1
+ Revision: 465476
- Update to 0.45.1.

* Wed Jul 22 2009 Lev Givon <lev@mandriva.org> 0.43.0-1mdv2010.0
+ Revision: 398648
- Update to 0.43.

* Wed Jun 24 2009 Lev Givon <lev@mandriva.org> 0.41.0-1mdv2010.0
+ Revision: 388890
- Update to 0.41.0.

* Sun Apr 19 2009 Lev Givon <lev@mandriva.org> 0.39.0-1mdv2009.1
+ Revision: 368049
- Update to 0.39.0.

* Mon Mar 16 2009 Lev Givon <lev@mandriva.org> 0.38.1-1mdv2009.1
+ Revision: 355950
- Update to 0.38.1.

* Sun Jan 04 2009 Jérôme Soyer <saispo@mandriva.org> 0.37.1-1mdv2009.1
+ Revision: 324273
- New upstream release

* Sat Jan 03 2009 Funda Wang <fwang@mandriva.org> 0.36.0-2mdv2009.1
+ Revision: 323779
- rebuild

* Tue Nov 04 2008 Lev Givon <lev@mandriva.org> 0.36.0-1mdv2009.1
+ Revision: 299693
- Update to 0.36.0.

* Thu Sep 04 2008 Jérôme Soyer <saispo@mandriva.org> 0.34.0-1mdv2009.0
+ Revision: 280552
- New release

* Fri Aug 01 2008 Thierry Vignaud <tv@mandriva.org> 0.28.2-4mdv2009.0
+ Revision: 259655
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tv@mandriva.org> 0.28.2-3mdv2009.0
+ Revision: 247502
- rebuild

* Tue Feb 19 2008 Lev Givon <lev@mandriva.org> 0.28.2-1mdv2008.1
+ Revision: 172406
- Update to 0.28.2.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Jul 09 2007 Lev Givon <lev@mandriva.org> 0.22.2-1mdv2008.0
+ Revision: 50546
- Update to 0.22.2.

* Tue Apr 17 2007 Lev Givon <lev@mandriva.org> 0.21.2-1mdv2008.0
+ Revision: 13823
- Import python-logilab-common



* Tue Mar 20 2007 Lev Givon <lev@mandriva.org> 0.21.2-1mdv2007.0
- Initial Mandriva package.





