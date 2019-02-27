#program penerima bantuan
#tupro_2_AI
#firman ramdahni 1301164052
#if4011

import csv

# aturan fuzzy yang menentukan siapa yang mendapat BLT dan tidak mendapat BLT
def aturanFuzzy(pendapatanRendah,pendapatanSedang,pendapatanTinggi,hutangRendah,hutangSedang,hutangTinggi):

    mendapatBLT = [0,0,0]
    tidakMendapatBLT = [0,0,0,0,0,0]

    if (pendapatanRendah > 0) and (hutangRendah > 0):
        tidakMendapatBLT[0] = min(pendapatanRendah, hutangRendah);
    if (pendapatanSedang> 0) and (hutangRendah> 0):
        tidakMendapatBLT[1] = min(pendapatanSedang, hutangRendah);
    if (pendapatanTinggi>0) and (hutangRendah>0):
         tidakMendapatBLT[2] = min(pendapatanTinggi, hutangRendah);
    if (pendapatanRendah > 0) and (hutangSedang > 0):
        mendapatBLT[0] = min(pendapatanRendah,hutangSedang);
    if (pendapatanSedang > 0) and (hutangSedang > 0):
        tidakMendapatBLT[3] = min(pendapatanSedang, hutangSedang);
    if (pendapatanTinggi > 0) and (hutangSedang > 0):
         tidakMendapatBLT[4] = min(pendapatanTinggi, hutangSedang);
    if (pendapatanRendah > 0) and (hutangTinggi > 0):
        mendapatBLT[1] = min(pendapatanRendah,hutangTinggi);
    if (pendapatanSedang> 0) and (hutangTinggi > 0):
         mendapatBLT[2] = min(pendapatanSedang,hutangTinggi);
    if (pendapatanTinggi > 0) and (hutangTinggi > 0):
         tidakMendapatBLT[5] = min(pendapatanTinggi, hutangTinggi);
         
    return  max(mendapatBLT),max(tidakMendapatBLT)


# rumus defuzzy
def defuzzy(mendapatBLT,tidakMendapatBLT):
    return ((mendapatBLT * 60) + (tidakMendapatBLT * 40)) / (mendapatBLT + tidakMendapatBLT)

# Fungsi keanggotaan variabel Pendapatan
def kurvaPendapatan(pendapatan):
    pendapatanRendah =0;
    pendapatanSedang =0;
    pendapatanTinggi =0;

    if(pendapatan >= 1.5):
        pendapatanTinggi =1 ;
    elif (pendapatan > 1) and (pendapatan <1.5 ):
        pendapatanSedang = (1.5 - pendapatan)/(1.5 - 1);
        pendapatanTinggi = 1- pendapatanSedang;
    elif (pendapatan > 0.5) and (pendapatan<1):
        pendapatanRendah = (1-pendapatan)/(1 - 0.5);
        pendapatanSedang = 1- pendapatanRendah;
    elif (pendapatan <= 0.5):
        pendapatanRendah =1;

    return pendapatanRendah,pendapatanSedang,pendapatanTinggi

# Fungsi keanggotaan variabel hutang
def kurvaHutang(hutang):
    hutangRendah = 0;
    hutangSedang = 0;
    hutangTinggi = 0;

    if (hutang >= 66):
        hutangTinggi = 1;
    elif (hutang > 44) and (hutang < 66):
        hutangSedang = ( 66 - hutang)/(66-44);
        hutangTinggi = 1 - hutangSedang;
    elif(hutang == 44):
        hutangSedang = 1;
    elif (hutang > 22) and (hutang < 44):
        hutangRendah = (44-hutang)/(44-22);
        hutangCukup = 1-hutangRendah;
    elif (hutang <= 22 ):
        hutangRendah = 1;
    return hutangRendah,hutangSedang,hutangTinggi;




# membaca file DataTugas2.csv
with open('DataTugas2.csv') as file:
    reader = csv.reader(file, delimiter=',')
    next(reader)
    with open('HasilTebakan.csv', 'w', newline='') as data:
        fiedlname =['No','Pendapatan','Hutang']
        writer = csv.DictWriter(data,fiedlname)
        writer.writeheader()
        for row in reader:
            hutangR,hutangS,hutangT = kurvaPendapatan(float(row[1]))
            pendapatanR, pendapatanS, pendapatanT = kurvaHutang(float(row[2]))
            mendapatBLT, tidakMendapatBLT = aturanFuzzy(pendapatanR,pendapatanS,pendapatanT,hutangR,hutangS,hutangT)
            x = defuzzy(mendapatBLT, tidakMendapatBLT)
            if(x >=60):
                print('Nomor', row[0],' penghasian',row[1],' hutang',row[2],' leyak mendapatkan BLT')
                writer.writerow({'No':row[0],'Pendapatan':row[1],'Hutang':row[2]})

            #print(row[0], row[1], row[2])
            #print(" ".join(row))
