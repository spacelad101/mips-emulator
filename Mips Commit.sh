echo "Enter a description for this commit, followed by [ENTER]:"
read disc
git add *.circ
git commit -m $disc
git push mips master