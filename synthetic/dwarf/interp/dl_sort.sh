#scp dwhitten@nuit.phys.nd.edu:/emc1/home/dwhitten/INTERPOLATION/output/G77/AC6.5/* T4000_AC6.5/
#scp dwhitten@nuit.phys.nd.edu:/emc1/home/dwhitten/INTERPOLATION/output/G77/AC6.6/* T4000_AC6.6/
#scp dwhitten@nuit.phys.nd.edu:/emc1/home/dwhitten/INTERPOLATION/output/G77/AC6.7/* T4000_AC6.7/
#scp dwhitten@nuit.phys.nd.edu:/emc1/home/dwhitten/INTERPOLATION/output/G77/AC6.8/* T4000_AC6.8/
#scp dwhitten@nuit.phys.nd.edu:/emc1/home/dwhitten/INTERPOLATION/output/G77/AC6.9/* T4000_AC6.9/
#scp dwhitten@nuit.phys.nd.edu:/emc1/home/dwhitten/INTERPOLATION/output/G77/AC7.0/* T4000_AC7.0/
#scp dwhitten@nuit.phys.nd.edu:/emc1/home/dwhitten/INTERPOLATION/output/G77/AC7.1/* T4000_AC7.1/
#scp dwhitten@nuit.phys.nd.edu:/emc1/home/dwhitten/INTERPOLATION/output/G77/AC7.2/* T4000_AC7.2/
#scp dwhitten@nuit.phys.nd.edu:/emc1/home/dwhitten/INTERPOLATION/output/G77/AC7.3/* T4000_AC7.3/
#scp dwhitten@nuit.phys.nd.edu:/emc1/home/dwhitten/INTERPOLATION/output/G77/AC7.4/* T4000_AC7.4/
#scp dwhitten@nuit.phys.nd.edu:/emc1/home/dwhitten/INTERPOLATION/output/G77/AC7.5/* T4000_AC7.5/
#scp dwhitten@nuit.phys.nd.edu:/emc1/home/dwhitten/INTERPOLATION/output/G77/AC7.6/* T4000_AC7.6/
#scp dwhitten@nuit.phys.nd.edu:/emc1/home/dwhitten/INTERPOLATION/output/G77/AC7.7/* T4000_AC7.7/
#scp dwhitten@nuit.phys.nd.edu:/emc1/home/dwhitten/INTERPOLATION/output/G77/AC7.8/* T4000_AC7.8/
#scp dwhitten@nuit.phys.nd.edu:/emc1/home/dwhitten/INTERPOLATION/output/G77/AC7.9/* T4000_AC7.9/
#scp dwhitten@nuit.phys.nd.edu:/emc1/home/dwhitten/INTERPOLATION/output/G77/AC8.0/* T4000_AC8.0/
#
for C in 6.5 6.6 6.7 6.8 6.9 7.0 7.1 7.2 7.3 7.4 7.5 7.6 7.7 7.8 7.9 8.0; 
    do 
        for item in $(`ls T4000_AC$C/T4100* | awk '{print $NF}' FS=/`);do mv T4000_AC$C/$item T4100_AC$C/;done
        for item in $(`ls T4000_AC$C/T4200* | awk '{print $NF}' FS=/`);do mv T4000_AC$C/$item T4200_AC$C/;done
        for item in $(`ls T4000_AC$C/T4300* | awk '{print $NF}' FS=/`);do mv T4000_AC$C/$item T4300_AC$C/;done
        for item in $(`ls T4000_AC$C/T4400* | awk '{print $NF}' FS=/`);do mv T4000_AC$C/$item T4400_AC$C/;done
        for item in $(`ls T4000_AC$C/T4500* | awk '{print $NF}' FS=/`);do mv T4000_AC$C/$item T4500_AC$C/;done
        #mv T4000_AC$C/T4100* T4100_AC$C/
        #mv T4000_AC$C/T4200* T4200_AC$C/
        #mv T4000_AC$C/T4300* T4300_AC$C/
        #mv T4000_AC$C/T4400* T4400_AC$C/
        #mv T4000_AC$C/T4500* T4500_AC$C/
    done
