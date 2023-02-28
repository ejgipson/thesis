N=1
for dir in */
do
cd $dir
	sbatch RUN_VASP6
	sleep 0.5s	
	if [ $(($N % 10)) == 0 ]
	then
		sleep 600s
	fi
	((N++))
cd ../
done
for dir in */
do
cd $dir
	if grep -q "Your Open MPI job may now hang or fail." *.out
	then
		job=$(grep -l "Your Open MPI job may now hang or fail." *.out | sed 's/[^0-9]//g')
		echo "Open MPI failed for job id $job"
		scancel $job
		rm WAVECAR
		sbatch RUN_VASP6
		sleep 0.5s
	fi
cd ../
done