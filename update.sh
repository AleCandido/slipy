git submodule update
cd reveal.js
yarn install
#gulp build
cd ..
rm -rf minimal-reveal; mkdir minimal-reveal
cp -r reveal.js/dist minimal-reveal
cp -r reveal.js/plugin minimal-reveal
