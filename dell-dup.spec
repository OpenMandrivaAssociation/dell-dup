%define name	dell-dup
%define version	1.1.3
%define rel	2

Name:           %{name}
Version:        %{version}
Release:        %mkrel %{rel}
Summary:        A firmware-tools plugin to handle converting Dell DUPs to FT format
Group:          System/Configuration/Hardware
License:        GPLv2+ and OSL
URL:            http://linux.dell.com/libsmbios/download/
Source0:        http://linux.dell.com/libsmbios/download/%{name}/%{name}-%{version}/%{name}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:  pkgconfig(python)
BuildRequires:	firmware-tools
BuildRequires:	firmware-addon-dell
Provides:	dell-bmcflash
Provides:	dell-lsiflash
Obsoletes:	dell-bmcflash <= 1.5.0
Obsoletes:	dell-lsiflash <= 2.0.6

%description
This firmware-tools plugin will extract Dell DUPs into Firmware-Tools format.

%prep
%setup -q

%build
%configure2_5x
%make

%check
%make check

%install
%makeinstall_std

%files
%doc COPYING-* README AUTHORS
%{python_sitelib}/dell_dup
%config(noreplace) %{_sysconfdir}/firmware/firmware.d/%{name}.conf
%{_datadir}/firmware-tools/*
