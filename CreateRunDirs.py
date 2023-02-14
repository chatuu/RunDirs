#!/usr/bin/env python3

import sys
import os

class fclInfo:
    """This class is made to store run number and fcl file name
    """
    def __init__(self, runNo, fclName):
        """Initialize input variables

        Args:
            runNo (string): run number
            fclName (string): fcl name
        """
        self.runNo   = runNo
        self.fclName = fclName
    
    def GetRunNo(self):
        """Get Run Number

        Returns:
            string: run number
        """
        return self.runNo

    def GetFCL(self):
        """Get FCL Name

        Returns:
            string: fcl name
        """
        return self.fclName



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
            fclinfo.append(fclInfo(int(runNo), line))

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




    





#neardet_genie_numucccoh_fullsim_prod5p1_nonswap_singles_numucccoh_none_r13195_s09_c0_v05.87_1_20230208_231715.fcl

if __name__=='__main__':
    main()