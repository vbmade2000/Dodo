Name:   dodo
Version:    1.1
Release:	1%{?dist}
Summary:	RPM Package for dodo test runner

License:    None
Source0:    %{name}-%{version}.tgz
BuildRoot:  %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%description
Functional test runner for Python based application

%prep
%setup -n Dodo/dodo

%build


%install
mkdir -p %{buildroot}/usr/bin/
cp dodo %{buildroot}/usr/bin/

%files
%doc
/usr/bin/dodo


%changelog
* Tue Oct 22 2019 Madhura Mande <mandemadhura@gmail.com>
- Initial Dodo spec file
