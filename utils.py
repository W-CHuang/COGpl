def parse_BLAST_tabular_output_as_dict(tabular_output_path):
    """parse BLAST outfmt 6 tabular result into a dict
       the loweset evalue were retained
    """
    results_dict = {}
    for line in open(tabular_output_path,'r'):
        fields = line.strip().split('\t')
        query_id = fields[0]
        target_id = fields[1]
        evalue = float(fields[10])

        if query_id in results_dict:
            if evalue > results_dict[query_id]['evalue']:
                continue

        results_dict[query_id] = {'hit': target_id, 'evalue': evalue}

    return results_dict

def parse_cog_csv_as_dict(cogcsvfile):
	result_dicts={}
	for line in open(cogcsvfile,'r'):
		fileds=line.strip().split(',')
		number=fileds[0]
		cog=fileds[6]
		result_dicts[number]=cog
	return result_dicts

def parse_cognames_as_dict(cognames):
	r_dict={}
	for line in open(cognames,'r',encoding='latin-1'):
		if line.startswith('#'):continue
		fileds=line.strip().split('\t',2)
		#print(fileds)
		COG=fileds[0]
		func=fileds[1]
		name=fileds[2]
		r_dict[COG]=[func,name]
	return r_dict

def query_COG_field(results_dict,cog_dict,cognames_dict):
	"""
	Take dictionary
	d[query_id]:{'hit':target_id,'evalue':evalue} as input
	return dictionary with COG accession And Category
	"""
	final_result_dict={}
	for query_id,hit_result in results_dict.items():
		fileds=hit_result['hit'].split('|')
		gi=fileds[1]
		cog=cog_dict[gi]
		cogdescript=cognames_dict[cog]
		final_result_dict[query_id]={'hit':gi,'evalue':hit_result['evalue'],'COG':cog,'Func':cogdescript[0],'Name':cogdescript[1]}
	return final_result_dict

def write_result_to_tab(final_result_dict,outputpath):
	with open(outputpath,'w') as out:
		out.write('query_id\thit\tevalue\tCOG\tFunc\tName\n')
		out.flush()
		for K,V in final_result_dict.items():
			out.write("{a}\t{b}\t{c}\t{d}\t{e}\t{f}\n".format(a=K,b=V['hit'],c=V['evalue'],d=V['COG'],e=V['Func'],f=V['Name']))
			out.flush()

