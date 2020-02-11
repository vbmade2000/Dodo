#!/bin/bash

#######################################################################
# This script generates RPM for Dodo
#######################################################################

set -e

SCRIPT_PATH=$(readlink -f "$0")
BASEDIR=$(dirname "$SCRIPT_PATH")
DIST=${DIST:-$BASEDIR/rpmbuild}

echo $BASEDIR
echo $DIST

[ -z "$GIT_VER" ] && GIT_VER=$(git rev-parse --short HEAD)
[ -z "$VERSION" ] && VERSION=$(cat $BASEDIR/VERSION)

echo "Using [VERSION=${VERSION}] ..."
echo "Using [GIT_VER=${GIT_VER}] ..."

# Remove existing directory tree and create fresh one.
rm -rf $DIST/
mkdir -p $DIST/SOURCES

# Create tar of source
tar -czvf $DIST/SOURCES/dodo-$VERSION.tgz -C $BASEDIR/..  Dodo/dodo

# Generate RPM
rpmbuild --define "version $VERSION" --define "_topdir $DIST" -bb $BASEDIR/dodo.spec

# We don't need BUILD directory. Remove it.
\rm -rf $DIST/BUILD
echo -e "\nGenerated RPMs..."

# Print names of generated RPM
find $DIST -name "*.rpm"
