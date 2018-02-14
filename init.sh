docker build -t rpmcontainer .
docker run \
--rm \
-h rpmdev \
-v $(pwd)/SOURCES:/root/rpmbuild/SOURCES \
-v $(pwd)/SPECS:/root/rpmbuild/SPECS \
-w /root/rpmbuild/ \
-i -t rpmcontainer /bin/bash
