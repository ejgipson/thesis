N=1
for dir in */
do
cd $dir
	sbatch RUN_VASP6
	sleep 0.5s	
	if [ $(($N % 10)) == 0 ]
	then
		sleep 60s
	fi
	((N++))
cd ../
done
