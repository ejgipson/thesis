K=1
for i in *-*
do
cd $i
	sed -i "" "s/XXXXX/"$K"/g" RUN_VASP6
	((K++))
cd ../
done
