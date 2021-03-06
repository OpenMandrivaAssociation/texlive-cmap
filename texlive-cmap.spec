# revision 31477
# category Package
# catalog-ctan /macros/latex/contrib/cmap
# catalog-date 2012-11-14 17:49:35 +0100
# catalog-license lppl
# catalog-version 1.0h
Name:		texlive-cmap
Epoch:		1
Version:	1.0h
Release:	10
Summary:	Make PDF files searchable and copyable
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/cmap
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmap.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/cmap.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The cmap package provides character map tables, which make PDF
files generated by pdfLaTeX both searchable and copy-able in
acrobat reader and other compliant PDF viewers. Encodings
supported are OT1, T1, T2A, T2B, T2C and T5, together with LAE
(Arabic), LFE (Farsi) and LGR (Greek) and a variant OT1tt for
cmtt-like fonts. The package's main limitation currently is the
inability to work with virtual fonts, because of limitations of
pdfTeX. This restriction may be resolved in a future version of
pdfTeX.

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
