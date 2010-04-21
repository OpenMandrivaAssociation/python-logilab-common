%define module	logilab-common
%define name 	python-%{module}
%define version 0.50.0
%define release %mkrel 1

Summary:	Python modules used by Logilab software
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://ftp.logilab.org/pub/common/%{module}-%{version}.tar.gz
License:	GPLv2+
Group:		Development/Python
Url:		http://www.logilab.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	python-egenix-mx-base
BuildArch:	noarch
BuildRequires:	python-setuptools
%py_requires -d

%description
This package contains a number of Python modules that provide low level
functionality used by various free software projects supported by Logilab.

%prep
%setup -q -n %{module}-%{version}

%build

%install
%__rm -rf %{buildroot}
%__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README COPYING ChangeLog
%exclude %_bindir/*
%py_sitedir/logilab*
%exclude %py_sitedir/logilab/common/test*
%py_sitedir/*.egg-info
