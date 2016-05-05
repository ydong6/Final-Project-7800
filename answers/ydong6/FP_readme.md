#Final Project: Designing and Examining Gibson Assemble sequence
================================================================================== 

**Introduction**

This project can be used to analysis Gibson Assemble sequencing results. It will read sequence from couple of nucleotide long till the whole genome from the mainstream of sequencing methods, like Sanger sequencing. The file type can be fasta,seq,etc.
 
**Background**

Gibson Assemble is a gateway system which has been used wildly in molecular cloning labs. It uses three different enzymes to cut sequences, anneal, and seal into vectors. In this method, we need to provide single restriction site on the primer for the further insert or digestion proof the correct bacteria column. However, in the case of insert several tandem repeat sites into plasmid, it will generate mutations, either change certain sequence or delete certain part of the sequence.

**Benefits**

This software can read sequences then find out single restriction enzyme that available in NEB company. Then it can help us to check the sequencing result from a bacteria column, then align with the desired sequence to find out whether it can generate mutations. Furthermore, it can provide protein sequence alignment to tell us whether the mutation can influence the protein sequence. Interestingly, it can display the alignment on your terminal with different colors.

**Specific function**

>*1. Read multiple sequence file. 
We can use argparse and SeqIO methods to take and read fasta or seq file into this software. Particularly, we use --in1 and --in2 to take two sequence.
 
>*2. Clean up the sequence file for further analysis. 
By using SeqIO.read attribute, we can separate sequence file from the header and the whole file. Then cleaned sequence data can be used for later analysis.
 
>*3. Transfer the DNA sequence to protein sequence.
By using self.seq1.translate(), we can read protein sequences.
 
>*4. Find out restriction enzyme that available in NEB company. 
This function can be realized by the method "Restriction.RestrictionBatch(first=[], suppliers='N')" 

>*5. extract single cut site enzyme for us to put on primers for further insertion.
By combine "Counter()" and "list" method, we can extract those single cut sites.

>*6. Search through the list to find comparable homologue sequence.
This function can be performed by pairwise2.align method.

>*7. Find out the mismatched nucleotide 
By using "pairwise2.format_alignment()" method, we can align the sequences in a certain format, the mismatched nucleotide will be marked by a bar or a space between alignment to show mismatch.

>*8. Print the sequence on terminal with colorful character. 
We need to install "colorama" module to display colorful character on the terminal.

>*9. Annotate the aligned sequence.
I use ".format" to annotate the output sequence with DNA or protein ID, Alignment or Digestion, in a readable form.

>*10. Output the analyzed  sequence.
I used arg.out to output the analysis in a file. the file can be .txt, .seq, .fasta, etc. but the extension need to be include.

>*11. Output mutation percentage, show large mutations between different files.
This function can be reached by the alignment score provided by the method "align", the higher the better.

>*12. Provide readme.md file to help users.
This readme.md document you are reading is formatted in a markdown file.

Attention: in order to show correct alignment, do not use word wrap format. 

