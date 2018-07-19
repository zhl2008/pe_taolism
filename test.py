from idautils import *
from idaapi import *
import idc
import time

def main():
    idaapi.autoWait()
    ea = BeginEA()
    dll_functions = []
    f = GetIdbPath()[0:-4] + "de.c"
    fp = open(f, "w")
    flag = idaapi.init_hexrays_plugin()
    print flag
    if not flag:
        idaapi.load_plugin('hexrays')
    flag = idaapi.init_hexrays_plugin()
    if not flag:
        return False
    print "Hex-rays version %s has been detected" % idaapi.get_hexrays_version()

    count=0
    for funcea in Functions(SegStart(ea), SegEnd(ea)):
        try:
            count+=1
            print hex(funcea)
            #fp.write(str(hex(funcea))+'\n')
            #fp.write(str(hex(FindFuncEnd(funcea)))+'\n')
            cfunc = idaapi.decompile(funcea)
            if cfunc is None:
                print "Failed to decompile!"
                continue
            functionName = GetFunctionName(funcea)
            dll_functions.append(functionName)
            print(functionName)
            strs="sub_"+str(hex(funcea))[:-1]+"_"+str(hex(FindFuncEnd(funcea)))[:-1]
            # for (startea, endea) in Chunks(funcea):
            #     strs+="sub_"+str(hex(startea))[:-1]
            #     strs+="_"+str(hex(endea))[:-1]

            sv = cfunc.get_pseudocode();
            k=0
            for sline in sv:
                print idaapi.tag_remove(sline.line);
                if k==0:
                    fp.write(idaapi.tag_remove(sline.line).replace(functionName,strs)+'\n')
                    k=1
                else:
                    fp.write(idaapi.tag_remove(sline.line)+'\n')
            
            #if count==2:
            #    break
        except DecompilationFailure,e:
            print e
            continue

    fp.close()
    idc.Exit(0)
    return True

main()
#print GetIdbPath()



    # for funcea in Functions(SegStart(ea), SegEnd(ea)):
    #     try:
    #         print hex(funcea)
    #         cfunc = idaapi.decompile(funcea)
    #         if cfunc is None:
    #             print "Failed to decompile!"
    #             continue

    #         sv = cfunc.get_pseudocode();
    #         for sline in sv:
    #             print idaapi.tag_remove(sline.line);
    #             fp.write(idaapi.tag_remove(sline.line)+'\n')
    #         functionName = GetFunctionName(funcea)
    #         dll_functions.append(functionName)
    #         print(functionName)
    #     except DecompilationFailure,e:
    #         print e
    #         continue
