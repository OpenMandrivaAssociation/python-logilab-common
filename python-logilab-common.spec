%define module	logilab-common

# Depenedency geenrator finds too many abi deps here
%define __noautoreq 'python\\(abi\\).*'

Summary:	Python modules used by Logilab software
Name:		python-%{module}
Version:	0.62.1
Release:	2
Source0:	http://download.logilab.org/pub/common/logilab-common-%{version}.tar.gz
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
