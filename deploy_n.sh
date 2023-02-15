rm -r public
hugo -D
git add -A
git commit -m "Update"
git push
echo -e "Deployed."
