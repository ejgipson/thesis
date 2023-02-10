rm OUT
touch OUT
echo "job-name          TOTEN (eV)" >> OUT
touch TEMP
for i in *-*
do
cd $i
	sed -n -e 's/^.*job-name=//p' RUN_VASP6 > ../TEMP
	sed -n -e 's/^.*TOTEN//p' OUTCAR | tail -1 | sed 's/[^-+0-9\.0-9]//g' >> ../TEMP
	column ../TEMP >> ../OUT
cd ../
done
head OUT