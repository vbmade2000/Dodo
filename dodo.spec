Name:   dodo
Version:    %{version}
Release:	1%{?dist}
Summary:	RPM Package for dodo test runner

Source0:    %{name}-%{version}.tgz
License:    None
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Functional test runner for Python based application

%prep
%setup -n Dodo/dodo

%build


%install
mkdir -p %{buildroot}/usr/bin/
cp dodo %{buildroot}/usr/bin/

mkdir -p %{buildroot}/usr/lib64/python3.6/site-packages/dodo
mkdir -p %{buildroot}/usr/lib64/python3.6/site-packages/dodo/formatters
cp -rp . %{buildroot}/usr/lib64/python3.6/site-packages/dodo

%files
/usr/bin/dodo
/usr/lib64/python3.6/site-packages/dodo

%changelog
* Mon Feb 10 2020 Malhar Vora <mlvora.2010@gmail.com>
- Complete working spec file
* Tue Oct 22 2019 Madhura Mande <mandemadhura@gmail.com>
- Initial Dodo spec file
