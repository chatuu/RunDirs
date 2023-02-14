#!/usr/bin/env python3

import sys
import os
import shutil

def main():
    """This is the main function
    """
    print(f"Input file: {sys.argv[1]}")
    with open(sys.argv[1],"r") as f:
        os.mkdir("outdir")
        runs = []
        fclinfo = []
        lines = f.readlines()
        for line in lines:
            runNo = line[72:77]
            runs.append(int(runNo))

        finalRuns = set(runs)

        for run in finalRuns:
            l = str(run)
            directory = f"000{l[0:3]}"
            path = f"./outdir/{directory}/{l}"

            try:
                os.makedirs(path)
            except OSError:
                print ("Creation of the directory %s failed" % path)
            else:
                print ("Successfully created the directory %s" % path)

    with open(sys.argv[1],"r") as file:
        fclinfo = []
        lines = file.readlines()
        for line in lines:
            runNo = line[72:77]
            src_path  = f"./largefcls/{line}"
            dest_path = f"./outdir/000{runNo[0:3]}/{runNo}/"

            try:    
                shutil.copy(src_path.strip(), dest_path.strip())
            except OSError:
                print(f"Unable to copy {src_path} to {dest_path}")
            else:
                print(f"Suceessfully copied {src_path} to {dest_path}")
            file.close() 

if __name__=='__main__':
    main()