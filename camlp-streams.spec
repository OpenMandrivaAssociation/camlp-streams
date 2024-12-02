%undefine _debugsource_packages

Name: camlp-streams
Version: 5.0.1
Release: 4
Source0: https://github.com/ocaml/camlp-streams/archive/refs/tags/v%{version}.tar.gz
Summary: The Stream and Genlex libraries for OCaml 5.0
URL: https://github.com/ocaml/camlp-streams
License: LGPL-2.1
Group: Development/Other
BuildRequires: ocaml-dune
BuildSystem: dune

%description
The Stream and Genlex modules have been part of the OCaml standard library for
a long time, and have been distributed as part of the core OCaml system.
They have been removed from the OCaml standard library, but will be maintained
and distributed separately in this camlp-streams package.

%package devel
Summary: Development files for camlp-streams
Requires: %{name} = %{EVRD}

%description devel
Development files for camlp-streams.

The Stream and Genlex modules have been part of the OCaml standard library for
a long time, and have been distributed as part of the core OCaml system.
They have been removed from the OCaml standard library, but will be maintained
and distributed separately in this camlp-streams package.

%prep
%autosetup -p1

%files -f .ofiles

%files devel -f .ofiles-devel
