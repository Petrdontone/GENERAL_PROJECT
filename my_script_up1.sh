#!/bin/bash

BUNDLE=$1
TYPE=$2

echo -n "APP bundle: $BUNDLE $TYPE"


if [ ! -d "$BUNDLE" ]
then
        mkdir $BUNDLE
	echo "Directory $BUNDLE DOES NO exists."
	exit 9999 
fi

PLATFORM="ios"

cd $BUNDLE
mkdir $PLATFORM
cd $PLATFORM

echo -n  "VERSION="1234" MARKETING_VERSION="1.4.5"" > proj1.data

#mv proj1.data $PLATFORM/proj1.data

. data/$BUNDLE/$PLATFORM/proj1.data

VERSION="1234"
MARKETING_VERSION="1.4.5"

cd ios

