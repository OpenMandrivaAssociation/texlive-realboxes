# revision 23581
# category Package
# catalog-ctan /macros/latex/contrib/realboxes
# catalog-date 2011-08-16 10:35:18 +0200
# catalog-license lppl1.3
# catalog-version 0.2
Name:		texlive-realboxes
Version:	0.2
Release:	4
Summary:	Variants of common box-commands that read their content as real box
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/realboxes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realboxes.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realboxes.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realboxes.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package uses the author's package collectbox to define
variants of common box related macros which read the content as
real box and not as macro argument. This enables the use of
verbatim or other special material as part of this content. The
provided macros have the same names as the original versions
but start with an upper-case letter instead. The "long-form"
macros, like \Makebox, can also be used as environments, but
not the "short-form" macros, like \Mbox. However, normally the
long form uses the short form anyway when no optional arguments
are used.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/realboxes/realboxes.sty
%doc %{_texmfdistdir}/doc/latex/realboxes/README
%doc %{_texmfdistdir}/doc/latex/realboxes/realboxes.pdf
#- source
%doc %{_texmfdistdir}/source/latex/realboxes/realboxes.dtx
%doc %{_texmfdistdir}/source/latex/realboxes/realboxes.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.2-2
+ Revision: 755628
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.2-1
+ Revision: 719435
- texlive-realboxes
- texlive-realboxes
- texlive-realboxes
- texlive-realboxes

