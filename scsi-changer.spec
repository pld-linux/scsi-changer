Summary:	Utilities to control SCSI media changers
Summary(pl):	Narzêdzie do sterowania zmieniarkami no¶ników SCSI
Name:		scsi-changer
Version:	0.20
Release:	1
License:	GPL
Group:		Applications/System
Source0:	http://bytesex.org/misc/%{name}-%{version}.tar.gz
URL:		http://bytesex.org/changer.html
#BuildRequires:	motif-devel >= 2.0
# requires kernel with patch supplied in this package
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Utilities to control SCSI media changers.

%description -l pl
Narzêdzie do sterowania zmieniarkami no¶ników SCSI.

%package X11
Summary:	X11 frontend for SCSI media changers
Summary(pl):	Interfejs X11 do zmieniarek no¶ników SCSI
Group:		X11/Applications

%description X11
X11 frontend for SCSI media changers.

%description X11 -l pl
Interfejs X11 do zmieniarek no¶ników SCSI.

%prep
%setup -q -n changer

%build
%{__make} \
	CC="%{__cc}" \
	OPTFLAGS="%{rpmcflags}" \
	MOTIF=no
#MOTIF=yes  (requires motif 2.0)

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	prefix=%{_prefix} \
	MOTIF=no

install unload $RPM_BUILD_ROOT%{_bindir}
ln -sf unload $RPM_BUILD_ROOT%{_bindir}/load
install unload.man $RPM_BUILD_ROOT%{_mandir}/man1/unload.1
echo '.so unload.1' > $RPM_BUILD_ROOT%{_mandir}/man1/load.1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,root) %{_bindir}/*load
%attr(755,root,root) %{_bindir}/mover
%attr(755,root,root) %{_sbindir}/autojuke
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/autojuke.conf
%{_mandir}/man1/*load.1*
%{_mandir}/man1/mover.1*
%{_mandir}/man8/autojuke.8*

%if 0
%files X11
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/xmover
%{_mandir}/man1/xmover.1*
%endif
