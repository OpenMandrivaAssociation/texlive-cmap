# revision 26568
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-cmap
Version:	20120807
Release:	2
Summary:	TeXLive cmap package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmap.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive cmap package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/cmap/cmap.sty
%{_texmfdistdir}/tex/latex/cmap/lae.cmap
%{_texmfdistdir}/tex/latex/cmap/lfe.cmap
%{_texmfdistdir}/tex/latex/cmap/lgr.cmap
%{_texmfdistdir}/tex/latex/cmap/ot1.cmap
%{_texmfdistdir}/tex/latex/cmap/ot1tt.cmap
%{_texmfdistdir}/tex/latex/cmap/ot6.cmap
%{_texmfdistdir}/tex/latex/cmap/t1.cmap
%{_texmfdistdir}/tex/latex/cmap/t2a.cmap
%{_texmfdistdir}/tex/latex/cmap/t2b.cmap
%{_texmfdistdir}/tex/latex/cmap/t2c.cmap
%{_texmfdistdir}/tex/latex/cmap/t5.cmap
%doc %{_texmfdistdir}/doc/latex/cmap/README

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Tue Aug 07 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120807-1
+ Revision: 812142
- Update to latest release.

* Tue Jan 03 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0h-2
+ Revision: 750257
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0h-1
+ Revision: 718074
- texlive-cmap
- texlive-cmap
- texlive-cmap
- texlive-cmap
- texlive-cmap

