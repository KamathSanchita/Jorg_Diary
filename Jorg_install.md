Steps to install the tool jorg successfully (things that worked for me).

Prerequisites: Conda in the system's path

1. Installation of Mirabait on Linux
a. Installation using the precompiled binaries. This (https://github.com/bachev/mira/releases/tag/V5rc1) is the link. 
The package that worked for me is "mira_V5rc1_linux-gnu_x86_64_static.tar.bz2".
b. Unpack it using "-xvzf mira_V5rc1_linux-gnu_x86_64_static.tar.bz2"
c. Add the bin directory of the MIRA package to the PATH variable of the system.
d. Check if the binaries are installed correctly on the system by typing -mirabait -v. This should return with the current version that is downloaded and installed.

2. configuration of the tool Mirabait
a. Go to the directory where the database is saved. It will be saved as "dbdata"
b. cd dbdata, The files that are found in this directory are mira-install-sls-rrna.sh rfam_rrna-21-12.sls.gz.
c. Run these scripts by typing "bash mira-install-sls-rrna.sh rfam_rrna-21-12.sls.gz"

This will take a minute or so. Then you're done for MIRA.


3. Installation of BWA and seqtk
seqtk: Install using conda. "conda install -c bioconda seqtk".
bwa: Using conda. "conda install bwa". BWA is used to determine the coverage of the bin. Most binning software should also output coverage values.

4. Clone the Jorg git directory using https.
a. Command: git clone https://github.com/lmlui/Jorg.git.
b. The script named "jorg" is found in the directory called /Example_data. Try running the script with set parameters using the example bin in the same directory.
c. Raw reads are required to run Jorg. This can be downloaded from the "http://dx.doi.org/10.5281/zenodo.3889132" link.

5. Run Jorg
a. Select a bin to run.
b. make a directory where the selected bin, jorg script, manifest_template.conf file are present(I had to save the bin in the directory where I run the jorg. Setting a path as a flag did not work).
c. set parameters. "c" for coverage - This value should be lower than the coverage of the contigs of the selected bin. k -33 default kmer value. --forward --reverse for forward and reverse raw reads.
   If the forward and reverse reads are merged, then -r flag should be sufficient. Use the -i flag to set the number of iterations.
d. command to run: jorg -b [selected bin] -r [raw read] -k 33 -c [80% of the average coverage of the bin] -i 20[10 iterations are a good starting point] --high_contig_num no --single_end_reads no




