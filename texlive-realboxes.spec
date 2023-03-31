Name:		texlive-realboxes
Version:	64967
Release:	2
Summary:	Variants of common box-commands that read their content as real box
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/realboxes
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realboxes.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realboxes.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/realboxes.source.r%{version}.tar.xz
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
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
