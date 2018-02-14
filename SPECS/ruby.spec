%define rubyver         1.9.3
%define rubyminorver    p551

Name:           ruby
Version:        %{rubyver}%{rubyminorver}
Release:        2%{?dist}
License:        Ruby License/GPL - see COPYING
URL:            http://www.ruby-lang.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  byacc
BuildRequires:  gdbm gdbm-devel
BuildRequires:  glibc-devel
BuildRequires:  db4-devel
BuildRequires:  libyaml-devel
BuildRequires:  ncurses ncurses-devel
BuildRequires:  openssl-devel
BuildRequires:  readline readline-devel
BuildRequires:  tcl-devel
BuildRequires:  unzip

Source0:        ftp://ftp.ruby-lang.org/pub/ruby\/ruby-%{rubyver}-%{rubyminorver}.tar.gz
Summary:        Interpreter for an object-oriented scripting language
Group:          Development/Languages
Provides: ruby(abi) = 1.9
Provides: ruby-irb
Provides: ruby-rdoc
Provides: ruby-libs
Provides: ruby-devel
Provides: rubygems
Obsoletes: ruby
Obsoletes: ruby-libs
Obsoletes: ruby-irb
Obsoletes: ruby-rdoc
Obsoletes: ruby-devel
Obsoletes: rubygems

%description
Ruby is the interpreted scripting language for quick
and easy object-oriented programming.  It has many
features to process text files and to do system
management tasks (as in Perl).  It is simple,
straight-forward, and extensible.

%prep
%setup -n ruby-%{rubyver}-%{rubyminorver}

%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"

%configure \
  --enable-shared \
  --disable-rpath \
  --without-X11 \
  --without-tk \
  --includedir=%{_includedir}/ruby \
  --libdir=%{_libdir}

make %{?_smp_mflags}

%install
# installing binaries ...
make install DESTDIR=$RPM_BUILD_ROOT

#we don't want to keep the src directory
#rm -rf $RPM_BUILD_ROOT/usr/src

%clean
#rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%{_bindir}
%{_includedir}
%{_datadir}
%{_libdir}