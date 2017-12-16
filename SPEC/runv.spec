%global         _dwz_low_mem_die_limit 0
%global         import_path  src/github.com/hyperhq/runv

Name:           runv
Version:        1.0.0
Release:        1%{?dist}
Summary:        Hypervisor-based Runtime for OCI

License:        Apache License, Version 2.0
URL:            https://github.com/hyperhq/runv
Source0:        %{name}-%{version}.tar.gz

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  golang
BuildRequires:  libvirt-devel
Requires:      	hyperstart
Requires:       libvirt-libs

%description
runV is a hypervisor-based runtime for OCI.

%prep
mkdir -p %{import_path}
%setup -q
cp -ar * ../%{import_path}/

%build
export GOPATH=%{_builddir}
cd ../%{import_path}
./autogen.sh

%configure
make %{?_smp_mflags}

%install
rm -rf $RPM_BUILD_ROOT
%{__mkdir} -p $RPM_BUILD_ROOT%{_bindir}
%{__install} -p -m 755 %{_builddir}/%{import_path}/runv $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT
rm -rf %{_builddir}%{import_path}

%files
%{_bindir}/runv
