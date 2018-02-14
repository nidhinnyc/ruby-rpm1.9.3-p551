FROM oraclelinux:7.1
RUN mkdir /root/rpmbuild
RUN mkdir -p /root/rpmbuild/{BUILD,RPMS,SOURCES,SPECS,SRPMS}
RUN yum -y install make gcc unzip byacc tree rpmdevtools glibc-devel readline-devel libyaml-devel ncurses-devel gdbm-devel tcl-devel openssl-devel db4-devel libffi-devel; yum clean all
