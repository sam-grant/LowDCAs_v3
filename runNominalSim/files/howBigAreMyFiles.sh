files=""
for file in `cat file2*`; do
#    echo $file
    files=${files}" "${file} 
done

du -sh $files