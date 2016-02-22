%global pkg_name plexus-classworlds
%{?scl:%scl_package %{pkg_name}}
%{?maven_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        2.5.2
Release:        3.3%{?dist}
Summary:        Plexus Classworlds Classloader Framework
License:        ASL 2.0 and Plexus
URL:            https://github.com/codehaus-plexus/plexus-classworlds
Source0:        https://github.com/sonatype/%{pkg_name}/archive/%{pkg_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  %{?scl_prefix_java_common}maven-local
BuildRequires:  %{?scl_prefix}mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires:  %{?scl_prefix}mvn(org.apache.maven.plugins:maven-dependency-plugin)

%description
Classworlds is a framework for container developers
who require complex manipulation of Java's ClassLoaders.
Java's native ClassLoader mechanisms and classes can cause
much headache and confusion for certain types of
application developers. Projects which involve dynamic
loading of components or otherwise represent a 'container'
can benefit from the classloading control provided by
classworlds.

%package javadoc
Summary:        Javadoc for %{pkg_name}

%description javadoc
API documentation for %{pkg_name}.

%prep
%setup -q -n %{pkg_name}-%{pkg_name}-%{version}
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_file : %{pkg_name} plexus/classworlds
%mvn_alias : classworlds:classworlds
%{?scl:EOF}

%build
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl} - <<"EOF"}
set -e -x
%mvn_install
# XXX - rebuild XMvn and remove
pushd %{buildroot}%{_javadir}
ln -s %{_javadir}/plexus/classworlds.jar %{name}.jar
popd
%{?scl:EOF}

%files -f .mfiles
%dir %{_javadir}/plexus
%dir %{_mavenpomdir}/plexus
%{_javadir}/%{name}.jar
%doc LICENSE.txt LICENSE-2.0.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt LICENSE-2.0.txt

%changelog
* Tue Jan 19 2016 Michal Srb <msrb@redhat.com> - 2.5.2-3.3
- Add auxiliary symlink for XMvn

* Tue Jan 19 2016 Michal Srb <msrb@redhat.com> - 2.5.2-3.2
- Fix artifact location

* Thu Jan 14 2016 Michal Srb <msrb@redhat.com> - 2.5.2-3.1
- Prepare spec for SCL build

* Thu Jan 14 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.5.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Jan 14 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.2-2
- Update upstream URL

* Thu Jan 14 2016 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.5.2-1
- Update to upstream version 2.5.2

* Mon Jan 11 2016 Michal Srb <msrb@redhat.com> - 2.4.2-8.12
- maven33 rebuild #2

* Sat Jan 09 2016 Michal Srb <msrb@redhat.com> - 2.4.2-8.11
- maven33 rebuild

* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 2.4.2-8.10
- Fix directory ownership properly

* Thu Jan 15 2015 Michal Srb <msrb@redhat.com> - 2.4.2-8.9
- Fix directory ownership

* Tue Jan 13 2015 Michael Simacek <msimacek@redhat.com> - 2.4.2-8.8
- Mass rebuild 2015-01-13

* Tue Jan 06 2015 Michael Simacek <msimacek@redhat.com> - 2.4.2-8.7
- Mass rebuild 2015-01-06

* Mon May 26 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.2-8.6
- Mass rebuild 2014-05-26

* Wed Feb 19 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.2-8.5
- Mass rebuild 2014-02-19

* Tue Feb 18 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.2-8.4
- Mass rebuild 2014-02-18

* Mon Feb 17 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.2-8.3
- SCL-ize build-requires

* Thu Feb 13 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.2-8.2
- Rebuild to regenerate auto-requires

* Tue Feb 11 2014 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.2-8.1
- First maven30 software collection build

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 2.4.2-8
- Mass rebuild 2013-12-27

* Fri Jul 26 2013 Michal Srb <msrb@redhat.com> - 2.4.2-7
- Fix Provides and Obsoletes

* Fri Jul 12 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.2-6
- Build with XMvn
- Update to current packaging guidelines
- Provide and obsolete classworlds

* Fri Jun 28 2013 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4.2-5
- Rebuild to regenerate API documentation
- Resolves: CVE-2013-1571

* Thu Apr 11 2013 Mat Booth <fedora@matbooth.co.uk> - 2.4.2-4
- Remove superfluous BRs, fixes rhbz #915616

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4.2-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.4.2-2
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 22 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4.2-1
- Update to latest bugfix release 2.4.2 (#895445)

* Wed Nov 21 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-11
- Install required ASL 2.0 license text

* Wed Nov 21 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-10
- Revert change from 2.4-9

* Tue Nov 20 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-9
- Provide and obsolete classworlds

* Mon Nov 19 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-8
- Fix source URL to be stable

* Tue Aug  7 2012 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-7
- Export only proper OSGI packages
- Do not generate "uses" OSGI clauses

* Mon Aug 06 2012 Gerard Ryan <galileo@fedoraproject.org> - 2.4-6
- Generate OSGI info using maven-plugin-bundle

* Sat Jul 21 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu Apr  5 2012 Mikolaj Izdebski <mizdebsk@redhat.com> - 2.4-4
- Update to maven 3
- Remove rpm bug workaround

* Sat Jan 14 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Feb  2 2011 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.4-1
- Update to latest upstream version
- Drop ant build parts
- Versionless jars & javadocs
- Enable tests again

* Tue Dec 21 2010 Alexander Kurtakov <akurtako@redhat.com> 2.2.3-2
- Fix FTBFS.

* Tue Jul 13 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2.2.3-1
- Version bump
- Fix few small packaging guidelines violations

* Thu Aug 20 2009 Andrew Overholt <overholt@redhat.com> 0:1.2-0.a9.8
- Bump release.

* Wed Aug 19 2009 Andrew Overholt <overholt@redhat.com> 0:1.2-0.a9.7
- Document sources and patches

* Wed Aug 19 2009 Andrew Overholt <overholt@redhat.com> 0:1.2-0.a9.6
- Update tarball-building instructions
- Remove gcj support
- Remove unnecessary post requirements

* Thu May 14 2009 Fernando Nasser <fnasser@redhat.com> 0:1.2-0.a9.6
- Fix license specification

* Tue Apr 28 2009 Yong Yang <yyang@redhat.com> 0:1.2-0.a9.5
- Add BRs maven2-plugin-surfire*, maven-doxia*
- Rebuild with maven2-2.0.8 built in non-bootstrap mode

* Mon Mar 16 2009 Yong Yang <yyang@redhat.com> 0:1.2-0.a9.4
- rebuild with new maven2 2.0.8 built in bootstrap mode

* Tue Jan 13 2009 Yong Yang <yyang@redhat.com> 0:1.2-0.a9.3jpp.1
- re-build with maven

* Tue Jan 06 2009 Yong Yang <yyang@redhat.com> 0:1.2-0.a9.2jpp.1
- Imported into devel from dbhole's maven 2.0.8 packages

* Wed Jan 30 2008 Deepak Bhole <dbhole@redhat.com> 0:1.2-0.a9.1jpp.1
- Initial build -- merged from JPackage
