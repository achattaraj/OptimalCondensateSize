
python3 LT_writer.py 

python3 memBound_MolArray.py

packmol < populate.inp

python3 mergeXYZ_files.py 

moltemplate.sh -xyz Combined.xyz -atomstyle "full" IC_Neph80.lt  -nocheck

mv *.xyz  \output_ttree 
