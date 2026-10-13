#!/usr/bin/env python3
from pathlib import Path
import sys
sys.path.insert(0,str(Path(__file__).parent/'Tools'))
from compile_srhd_dat import build_bp,build_cache,parse_bp_raw,unpack_dat_bytes
p=Path(__file__).resolve().parent.parent
for src,dest in [('Main.txt','Main.dat'),('Lang.txt','Rus/Lang.dat')]:
 build_bp(p/'SOURCE/CFG'/src,p/'CFG'/dest)
 tree=parse_bp_raw(unpack_dat_bytes((p/'CFG'/dest).read_bytes(),0xB1E8C689))
 assert any(e.name in ('ML','Script','Help') for e in tree.elems)
build_cache(p/'SOURCE/CFG/CacheData.txt',p/'CFG/CacheData.dat')
print('All three DAT files compiled and BlockPar roundtrip verified')
