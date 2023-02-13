split -a 4 -l 11 -d OBe_22 PREPOS
length=$(wc -l < PREPOS)
nfile=$((($length -1)/11))
for ((num=0000; num<=$nfile; num++))
do
	printf -v j "%04d" $num
	mkdir $j
	mv PREPOS$j ./$j/PREPOS
done