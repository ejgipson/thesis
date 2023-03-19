for dir in */
do
cd $dir
	if grep -q "DUE TO TIME LIMIT" *.out
	then
		job=$(grep -l "Your Open MPI job may now hang or fail." *.out | sed 's/[^0-9]//g')
		echo "Open MPI failed for job id $job, job resubmitted"
		scancel $job
		rm WAVECAR
		sbatch RUN_VASP6
		sleep 0.5s
	fi
cd ../
done