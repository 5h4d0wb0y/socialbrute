#!/bin/bash
# Script to release a new version

CURRENT_VERSION=$(cat socialbrute | grep 'VERSION =' | cut -d '"' -f 2)

echo -n "Current version is $CURRENT_VERSION, select new version: "
read NEW_VERSION
echo "Creating version $NEW_VERSION ...\n"

echo "Upgrading release ..."
sed -i "s/VERSION = \"$CURRENT_VERSION\"/VERSION = \"$NEW_VERSION\"/g" socialbrute
git add socialbrute

git commit -m "Releasing v$NEW_VERSION"
git push

git tag -a v$NEW_VERSION -m "Release v$NEW_VERSION"
git push origin v$NEW_VERSION

echo
echo "All done, v$NEW_VERSION released!"
