# Pull job name from RUN_VASP6 and total energy from OUTCAR
#job-name      TOTEN (eV)
for i in */
do
cd $i
	sed -n -e 's/^.*job-name=//p' RUN_VASP6 > ../TEMP
	sed -n -e 's/^.*TOTEN//p' OUTCAR | tail -1 | sed 's/[^-+0-9\.0-9]//g' >> ../TEMP
	column ../TEMP >> ../OUT
cd ../
done
head OUT