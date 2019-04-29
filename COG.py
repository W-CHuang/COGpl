import argparse
import os
import utils
import time
def blastWrapper(db,query,out,threads):
    blastp='blastp -db {a} -query {b} -out {c} -num_threads {d} -evalue 0.001 -outfmt 6'.format(a=db,b=query,c=out,d=str(threads))
    print (blastp)
    os.system(blastp)
def refiner(tabular,outpath,cogdict,cognamedict):
    tabresult=utils.parse_BLAST_tabular_output_as_dict(tabular)
    table=utils.query_COG_field(tabresult,cogdict,cognamedict)
    utils.write_result_to_tab(table,outpath)

if __name__ == "__main__":
    argparser=argparse.ArgumentParser()
    argparser.add_argument('-db_dir',help='COG databasedir')
    argparser.add_argument('-query',help='Query File')
    argparser.add_argument('-tmpd',help='Tmp file (when no_blast this option is the blast result',default=os.getcwd())
    argparser.add_argument('-out',help='outfile')
    argparser.add_argument('-no_blast',action='store_true')
    argparser.add_argument('-threads',help='threads',default=4)
    args=argparser.parse_args()
    cogdict=utils.parse_cog_csv_as_dict(os.path.join(args.db_dir,'cog2003-2014.csv'))
    cognamedict=utils.parse_cognames_as_dict(os.path.join(args.db_dir,'cognames2003-2014.tab'))
    if not args.no_blast:
        tmpfile=str(time.time()).replace('.','')+'.tab'
        blastWrapper(os.path.join(args.db_dir,'COG'),args.query,os.path.join(args.tmpd,tmpfile),args.threads)
        refiner(os.path.join(args.tmpd,tmpfile),args.out,cogdict,cognamedict)
    else:
        refiner(os.path.join(args.tmpd),args.out,cogdict,cognamedict)
