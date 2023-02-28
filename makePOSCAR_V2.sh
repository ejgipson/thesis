split -a 2 -l 10 -d OBe_12 PREPOS
length=$(wc -l < OBe_12)
njob=$(($length/10))
for ((num=00; num<=$(($njob-1)); num++))
do
	printf -v j "%02d" $num
	mkdir $j
	mv PREPOS$j ./$j/PREPOS
done
for dir in */
do
cd $dir 
	# Strip the formatting off of PREPOS
	sed -i -e '1,2d;4,5d;8,10d' PREPOS
	sed -i -e 's/ //g' PREPOS
	sed -i -e 's/\[//g' PREPOS
	sed -i -e 's/\]//g' PREPOS
	sed -i -e 's/\,//g' PREPOS
	grep -n -o -f PREPOS ../LATREF | cut -d: -f1 >> REPLACE
	readarray -t REPLACE < REPLACE
	LAT=($(seq 1 1 32))
	for ((i=1; i<=3; i++))
	do	
		LAT[$((${REPLACE[$i-1]}-1))]=0
	done
	printf "%d\n" "${LAT[@]}" > TEMP
	sort -n TEMP > TEMP2
	sed '/^0/d' TEMP2 > TEMP
	for ((i=1; i<=3; i++))
	do
		echo ${REPLACE[$i-1]} >> TEMP
	done
	cp ../HEAD POSCAR
	echo -e "" >> POSCAR
	for ((i=1; i<=32; i++))
	do
		j=$(sed -n "${i}p" TEMP)
		sed -n "${j}p" ../BODY >> POSCAR
	done
	rm TEMP
	rm TEMP2
	rm REPLACE
	rm PREPOS
cd ..	
done
