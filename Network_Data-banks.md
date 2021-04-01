pilot Data-bank:
  .pilots name + icons
  .pilots gaming records(saved games)
  .pilots -Variables : location, UNITS_health, Total_score, ship count, structure count


YanSanNet Data-bank:
    .YSN__INIT__()
        .YSN_Beacons_activate
        .YSN_AI.Neuro_NET.activate
        .YSN_Ship_engine.sys.activate
        .YSN_Android/drone.sys.activate
        .YSN_migration.add[E].activate
    YSN locations/ points of ORIGIN.doc
            (B = 'beacon' -LOCATION FACTOR-)
                -Sector_Var = str('')
                -Galaxy_Var = str('')
                -Region_Var = str('')
                -Bx = LOC_dem1
                -By = LOC_dem2
                -Bz = LOC_dem3
            (B = 'beacon' -OUTPUT FACTOR-)
                -Bx = total output in units
                -Bt = total output units per min.
                -Bm = total mass of output
            (OBJ = -object factor-)
                -u = # of 'units'
                -s = # of 'ships'
                -S = # of 'structures'


.YSN -EXAMPLE- (CACHE_DATE):
       YSN_dataSET: REC-
           PORT: 2222
           URL: 22222-22222
                   LOC = 10[sec=2, gal=2, reg=2, (x=2,y=2,z=2)]
                   OUT = 23[x=2,t=2,m=2]
  .                OBJ = 08[u=2, s=2, S=2]
   --(12) 'Root_VARs' for -cache_dataSET-


.YSN SYS_ADMIN.exe
    .YSN SYSTEM-CYCLE:
            -INIT-
            -run-
            -record-data-
            -compare with models-
            -update-
            -save-
            -quit-


.YSN Structures, Ships, and Units


.YSN Assets
