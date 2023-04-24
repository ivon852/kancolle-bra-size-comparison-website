rm -r public resources .hugo_build.lock
git add -A
git commit -m "Update"
git push
echo -e "Deployed."
