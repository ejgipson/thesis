K=1
for i in *-*
do
cd $i
	sed -i "" "s/XXXXX/"$K"/g" RUN_VASP6
	((K++))
	grep job-name= RUN_VASP6
cd ../
done