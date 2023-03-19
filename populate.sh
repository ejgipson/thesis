K=1
for dir in */
do
cd $dir
	cp ../POTCAR .
	cp ../INCAR .
	cp ../KPOINTS .
	cp ../RUN_VASP6 .
	sed -i "s/XXXXX/"$K"/g" ./RUN_VASP6
	((K++))
	grep job-name= RUN_VASP6
cd ../
done