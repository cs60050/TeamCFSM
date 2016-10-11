a=1
for i in *.mid; do
  new=$(printf "%03d.xml" "$a") #04 pad to length of 4
  mscore "$i" -o "$new"
  let a=a+1
done
