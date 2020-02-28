# Student_Name:
Mariam Oweda 
,Mohamed Nofal  ID: 191057
,Mohamed Emam   ID: 1910038
,Nouran Tantawy ID: 181045
,Hadder Hassan  ID: 191051
# Comparison of different RNA-Seq data aligners and its effect on differential expression analysis 
The great advantage of RNA sequencing is to answer the biological questions that lead to a generation of huge amounts of gene expression data across different biological fields such as biology and medicine. Differential expression analysis of RNA-seq data become one of the frequently used analysis to understand cellular processes in biological and biomedical research moreover to discover diagnostic markers for diseases. However, one of the crucial steps for significant differential expression is precise mapping of the reads to the its transcript. With the advances in the NGS technologies different software packages are developed to overcome the mapping problems like repeats and pseudogenes accompanied with competitive performance and accuracy. From this point, we will test the concordance of RNA sequencing (RNA-seq) analysis output between five mapping software; three alignment-based tools; HISAT2, STAR and the recently developed MAGIC BLAST which does not build an index of a genome and instead it builds an index of a batch of reads and scans a BLAST database for potential matches and two alignment-free tools; KALISTO and SALMON with the most common program for differential gene expression in RNA-seq experiments DESeq2. we will use publicly available RNA-seq dataset of 64 paired end Illumina Hepatocellular Carcinoma samples that correlates with survival. The samples were retrospectively derived from hepatocellular carcinoma tissue as well as non-tumor tissue from the livers of the same patients. We will investigate the differences in aligners performance through comparing DESeq2 list of differentially expressed genes for each aligner and validate the results accuracy based on wet lab published literature. As transcriptomics analysis becomes an important tool of precision medicine, the choice of the bioinformatics software is a very critical step for clinical research. 


# Multiqc-Report

## General Statistics

![1](https://user-images.githubusercontent.com/33230332/75452867-ac03c880-597b-11ea-9db6-84c033840d01.PNG)
![2](https://user-images.githubusercontent.com/33230332/75452906-bb831180-597b-11ea-9923-ad6afd62894a.PNG)
![3](https://user-images.githubusercontent.com/33230332/75452912-bd4cd500-597b-11ea-9e69-4df270942d76.PNG)
![4](https://user-images.githubusercontent.com/33230332/75452913-bf169880-597b-11ea-8368-28e092f15b04.PNG)
![5](https://user-images.githubusercontent.com/33230332/75452915-c047c580-597b-11ea-9b2b-79dfb6dbc53a.PNG)
![6](https://user-images.githubusercontent.com/33230332/75452919-c178f280-597b-11ea-847e-e443e3eeaa08.PNG)

## Sequence Counts
Sequence counts for each sample. Duplicate read counts are an estimate only.

![7](https://user-images.githubusercontent.com/33230332/75452923-c342b600-597b-11ea-8dd8-e3fff29d508e.PNG)
![8](https://user-images.githubusercontent.com/33230332/75452925-c3db4c80-597b-11ea-9631-1ef51a8845e8.PNG)
![9](https://user-images.githubusercontent.com/33230332/75452941-c9d12d80-597b-11ea-8166-55aa4e375f6e.PNG)

## Sequence Quality Histograms
The mean quality value across each base position in the read.

![10](https://user-images.githubusercontent.com/33230332/75452942-ca69c400-597b-11ea-8a06-0b4e9d187b10.PNG)

## Per Sequence Quality Scores 
The number of reads with average quality scores. Shows if a subset of reads has poor quality.

![11](https://user-images.githubusercontent.com/33230332/75452949-cc338780-597b-11ea-8e5d-e6f65318dfbd.PNG)

## Per Base Sequence Content
The proportion of each base position for which each of the four normal DNA bases has been called.

![12](https://user-images.githubusercontent.com/33230332/75452956-cf2e7800-597b-11ea-9118-86c22672f4d8.PNG)

## Per Sequence GC Content 
The average GC content of reads. Normal random library typically have a roughly normal distribution of GC content.

![13](https://user-images.githubusercontent.com/33230332/75452960-d190d200-597b-11ea-9087-45fbaf804358.PNG)

## Per Base N Content 
The percentage of base calls at each position for which an N was called.

![14](https://user-images.githubusercontent.com/33230332/75453220-3ea46780-597c-11ea-9d4a-6c23c97f1df7.PNG)

## Sequence Duplication Levels 
The relative level of duplication found for every sequence.

![15](https://user-images.githubusercontent.com/33230332/75453164-259bb680-597c-11ea-874f-27e320b70710.PNG)

## Adapter Content 12800
The cumulative percentage count of the proportion of your library which has seen each of the adapter sequences at each position.

![16](https://user-images.githubusercontent.com/33230332/75453197-34826900-597c-11ea-98ad-a11d685c5259.PNG)

## Status Checks
Status for each FastQC section showing whether results seem entirely normal (green), slightly abnormal (orange) or very unusual (red).

![17](https://user-images.githubusercontent.com/33230332/75453204-35b39600-597c-11ea-875b-a0a810b54fda.PNG)
