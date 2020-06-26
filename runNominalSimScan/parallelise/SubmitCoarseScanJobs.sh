# Grab each file list and pipe the into xargs
# for fileList in `ls /gm2/app/users/sgrant/Offline/LowDCAs/FileLists`; do
#     echo $fileList
# done | xargs -i --max-procs=20 bash -c ". /gm2/app/users/sgrant/Offline/LowDCAs/Scripts/RunJob.sh {}"

for file in `cd files && ls file*`; do
  echo $file
#  return
done | xargs -i --max-procs=3 bash -c ". RunCoarseScan.sh {}"