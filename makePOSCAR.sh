Be=(11 11 11 11 11 11 11 11 11)
O=(22 6 21 17 2 3 19 29 13)
for ((k=01; k<=${#O[@]}; k++))
do	
	printf -v N "%02d" $k
	mkdir $N
	cd $N
	LAT=($(seq 1 1 32))
	LAT[$((${Be[$k-1]}-1))]=0
	LAT[$((${O[$k-1]}-1))]=0
	printf "%d\n" "${LAT[@]}" > TEMP
	sort -n TEMP > TEMP2
	sed '/^0/d' TEMP2 > TEMP
	echo ${Be[$k-1]} >> TEMP
	echo ${O[$k-1]} >> TEMP
	cp ../HEAD POSCAR
	echo -e "" >> POSCAR
	for ((i=1; i<=32; i++))
	do
		j=$(sed -n "${i}p" TEMP)
		sed -n "${j}p" ../BODY >> POSCAR
	done
	rm TEMP
	rm TEMP2
	cd ../
done