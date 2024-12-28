# This package only contains header files.
%global debug_package %{nil}

Summary:	A simple, portable and lightweight library for handling UTF-8 encoded strings
Name:		utf8cpp
Version:	4.0.6
Release:	1
Group:		Development/C++
License:	Boost
URL:		https://github.com/nemtrif/utfcpp
Source0:	https://github.com/nemtrif/utfcpp/archive/v%{version}/utfcpp-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	pkgconfig(gtest)


%description
%{summary}.

Features include:
 - iterating through UTF-8 encoded strings
 - converting between UTF-8 and UTF-16/UTF-32
 - detecting invalid UTF-8 sequences

This project currently only contains header files, which can be found in the
%{name}-devel package.

%package devel
Summary:	Header files for %{name}
Group:		Development/C++
BuildArch:	noarch
Provides:	%{name}-static = %{EVRD}

%description devel
%{summary}.

Features include:
 - iterating through UTF-8 encoded strings
 - converting between UTF-8 and UTF-16/UTF-32
 - detecting invalid UTF-8 sequences

This project currently only contains header files, which can be found in the
%{name}-devel package.


%prep
%autosetup -n utfcpp-%{version} -p1


%build
%cmake \
        -DUTF8_TESTS=ON \
        -DUTF8_SAMPLES=ON

%make_build

%install
%make_install -C build

cd %{buildroot}%{_includedir}
ln -s utf8cpp/utf8.h ./
mkdir utf8
for f in {{un,}checked,core,cpp11}.h ; do
    ln -s ../utf8cpp/utf8/${f} utf8/
done
cd ..

%files devel
%doc README.md
%{_includedir}/utf8.h
%dir %{_includedir}/utf8
%{_includedir}/utf8/checked.h
%{_includedir}/utf8/core.h
%{_includedir}/utf8/cpp11.h
%{_includedir}/utf8/unchecked.h
%{_includedir}/utf8cpp/
%{_libdir}/utf8cpp/cmake/
