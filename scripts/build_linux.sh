#!/usr/bin/env bash

VERSION=`grep VERSION eplaunch/__init__.py | cut -d= -f2 | cut -d\" -f2`
SHA=`echo ${TRAVIS_COMMIT} | cut -c 1-8`
pyinstaller eplaunch.spec
pyinstaller wf_tester.spec
tar -C dist -zcf EPLaunch-${VERSION}-${SHA}-linux.tar.gz EPLaunch
tar -C dist -zcf EPLaunchWorkflowTester-${VERSION}-${SHA}-linux.tar.gz EpLaunchWorkflowTester
mkdir tmp_build
cp EPLaunch-${VERSION}-${SHA}-linux.tar.gz tmp_build
cp EPLaunchWorkflowTester-${VERSION}-${SHA}-linux.tar.gz tmp_build
