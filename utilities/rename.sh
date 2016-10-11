a=1
for i in *.mid; do
  new=$(printf "%03d.mid" "$a") #04 pad to length of 4
  mv -- "$i" "$new"
  let a=a+1
done
