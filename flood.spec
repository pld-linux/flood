Summary:	Profile-driven HTTP load tester
Summary(pl):	Tester obci±¿enia HTTP sterowany profilami
Name:		flood
Version:	0.4
Release:	0.1
License:	Apache
Group:		Applications/Networking
Source0:	http://www.apache.org/dist/httpd/flood/%{name}-%{version}.tar.gz
# Source0-md5:	c10abd6f46175ab54b554337525d576d
Patch0:		%{name}-libtool.patch
URL:		http://httpd.apache.org/test/flood/
BuildRequires:	apr-devel
BuildRequires:	apr-util-devel
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Flood is a profile-driven HTTP load tester. It can be used to gather
important performance matrics for your website.

%description -l pl
Flood to tester obci±¿enia HTTP sterowany profilami. Mo¿na go u¿ywaæ
do zebrania tabeli istotnych informacji o wydajno¶ci w³asnego serwisu
WWW.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__autoconf}
%configure \
	--enable-ssl \
	--with-openssl="%{_includedir}/openssl" \
	--with-capath="%{_datadir}/ssl/certs" \
	--with-apr=/usr/bin/apr-1-config \
	--with-apr-util=/usr/bin/apu-1-config

%{__make} \
	top_builddir=.

%install
rm -rf $RPM_BUILD_ROOT
install -D flood $RPM_BUILD_ROOT%{_bindir}/flood

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES CONFIG DESIGN LICENSE STATUS examples/
%attr(755,root,root) %{_bindir}/flood
