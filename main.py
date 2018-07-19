from idautils import *
from idaapi import *
import idc
import time
import json
import config

def main():
    idaapi.autoWait()
    ea = BeginEA()

    tmp_dir = []
    for tmp in GetInputFilePath().split('/'):
        tmp_dir.append(tmp)
        if tmp[:2] == 'p_':
            break
    tmp_dir = '/'.join(tmp_dir) + '/tmp/func' 
    file_path = GetInputFilePath().replace(config.runtime_path,'')
    if not os.path.isdir(tmp_dir):
        os.system('mkdir -p ' + tmp_dir)
    flag = idaapi.init_hexrays_plugin()
    print flag
    if not flag:
        idaapi.load_plugin('hexrays')
    flag = idaapi.init_hexrays_plugin()
    if not flag:
        return False
    print "Hex-rays version %s has been detected" % idaapi.get_hexrays_version()

    # the init count should be equivalent to the function number +1 in the tmp_dir
    count=len(list(os.listdir(tmp_dir)))/2 + 1
    for func in Functions(SegStart(ea), SegEnd(ea)):
        try:
            

            cfunc = idaapi.decompile(func)
            if cfunc is None:
                print "Failed to decompile!"
                continue
            functionName = GetFunctionName(func)

            strs="sub_"+str(hex(func))[:-1]+"_"+str(hex(FindFuncEnd(func)))[:-1]


            info = {"id":count,"start":str(hex(func))[:-1],"end":str(hex(FindFuncEnd(func)))[:-1],"file_path":file_path}
            record_file = tmp_dir + '/' + str(count)
            open(record_file,'w').write(json.dumps(info))


            pcode = cfunc.get_pseudocode()
            record_code_file = tmp_dir + '/' + str(count) + '_pcode'
            fp = open(record_code_file,'w')

            k = 0
            for sline in pcode:
                print idaapi.tag_remove(sline.line);
                if k==0:
                    fp.write(idaapi.tag_remove(sline.line).replace(functionName,strs)+'\n')
                    k = 1
                else:
                    fp.write(idaapi.tag_remove(sline.line)+'\n')                   
            #if count==2:
            #    break
            count+=1
        except DecompilationFailure,e:
            print e
            continue
    fp.close()
    idc.Exit(0)
    return True

main()

