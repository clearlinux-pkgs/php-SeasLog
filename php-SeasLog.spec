#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : php-SeasLog
Version  : 2.2.0
Release  : 15
URL      : https://pecl.php.net/get/SeasLog-2.2.0.tgz
Source0  : https://pecl.php.net/get/SeasLog-2.2.0.tgz
Summary  : No detailed summary available
Group    : Development/Tools
License  : PHP-3.01
Requires: php-SeasLog-lib = %{version}-%{release}
BuildRequires : buildreq-php

%description
SeasLog
======
[![Build Status](https://travis-ci.org/SeasX/SeasLog.svg?branch=master)](https://travis-ci.org/SeasX/SeasLog)
[![Build status](https://ci.appveyor.com/api/projects/status/xkf8y7msk7kskon2?svg=true)](https://ci.appveyor.com/project/Neeke/seaslog)

%package lib
Summary: lib components for the php-SeasLog package.
Group: Libraries

%description lib
lib components for the php-SeasLog package.


%prep
%setup -q -n SeasLog-2.2.0
cd %{_builddir}/SeasLog-2.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
phpize
%configure --disable-static
make  %{?_smp_mflags}

%install
%make_install


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/extensions/no-debug-non-zts-20210902/seaslog.so
