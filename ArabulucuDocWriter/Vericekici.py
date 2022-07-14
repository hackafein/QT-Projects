class Vericekici():
    def __init__(self):
        self.veri=""



    def vericek(self,metin):
        # programın ilk aşaması adresin hangi satırlarda olduğunu tespit ediyor ve isim
        # satır listesi listesine numara olarak ekliyor.

        fhand=[]

        for line in metin:

            if line.startswith("KARŞI TARAF BİLGİLERİ"):
                break
            else:
                fhand.append(line)
        #print(fhand)
        #inp açılan txtdeki harfi belirtiyor.
        verisozluk={"buro":"","basvurunumarasi":"","basvurutarihi":"","adisoyadi":"","tckimlikno":"","adres":"","vekili":"","barosicilno":"","ceptel":""
        }
        buro=fhand[1]
        buro=buro.split(" ")
        verisozluk["buro"]=buro[0]
        for line in fhand:
            
            
            if line.startswith("BAŞVURU NUMARASI"):
                try:
                    ikinokta=line.split(":")
                    line=ikinokta[1]
                    line=line[:len(line)-1]
                except:
                    line=line
                verisozluk["basvurunumarasi"]=line
            elif line.startswith("BAŞVURU TARİHİ"):
                try:
                    ikinokta=line.split(":")
                    line=ikinokta[1]
                    line=line[:len(line)-1]
                except:
                    line=line
                verisozluk["basvurutarihi"]=line
            elif line.startswith("Adı Soyadı"):
                try:
                    ikinokta=line.split(":")
                    line=ikinokta[1]
                    line=line[:len(line)-1]
                except:
                    line=line
                verisozluk["adisoyadi"]=line
            elif line.startswith("TC Kimlik No"):
                try:
                    ikinokta=line.split(":")
                    line=ikinokta[1]
                    line=line[:len(line)-1]
                except:
                    line=line
                verisozluk["tckimlikno"]=line
            elif line.startswith("Adres"):
                try:
                    ikinokta=line.split(":")
                    line=ikinokta[1]
                    line=line[:len(line)-1]
                except:
                    line=line
                verisozluk["adres"]=line
            elif line.find("Vekili")!=-1:
                
                line=line.split(":")
                line=line[1]
                self.vekili=str(line)
                
                
                
                
            elif line.startswith("Baro Sicil Numarası"):
                try:
                    ikinokta=line.split(":")
                    line=ikinokta[1]
                    line=line[:len(line)-1]
                except:
                    line=line
                verisozluk["barosicilno"]=line
            elif line.startswith("Cep Telefonu") or line.startswith("Tel") or line.startswith("Cep Tel"):
                try:
                    ikinokta=line.split(":")
                    line=ikinokta[1]
                    line=line[:len(line)-1]
                except:
                    line=line
                verisozluk["ceptel"]=line
            
        
        #print(verisozluk)
        

        karsi=[]
        a=0
        fhand=metin
        for i in metin:
            if "KARŞI TARAF BİLGİLERİ" in i:
                karsi.append(a)
                #print(i)
            if "BAŞVURU BİLGİLERİ" in i:
                karsi.append(a)
            a+=1
            #print(a)

        karsibilgiliste=[]
        lenkarsi=len(karsi)
        
        #print(karsi)
        for i in range(0,lenkarsi-1):
            
            karsibilgiliste.append(metin[(karsi[i]+1):(karsi[i+1])])

        c=0

        self.isimlistesi=[]
        self.adreslistesi=[]
        self.vekillistesi=[]
        self.verginolistesi=[]
        self.telnolistesi=[]
        self.tcnolistesi=[]
        kisi=0
        print(karsibilgiliste)
        for i in karsibilgiliste:

            for j in i:

                ilkind=j.find("Adı Soyadı")
                if ilkind !=-1:
                    sonind=j.find("\r",ilkind)
                    temp=(j[ilkind:sonind]).split(':')
                    temp=temp[1]
                    self.isimlistesi.append(temp)

                ilkind=j.find("TC Kimlik No	")
                if ilkind !=-1:
                    sonind=j.find("\r",ilkind)
                    temp=(j[ilkind:sonind]).split(':')
                    temp=temp[1]
                    self.tcnolistesi.append(temp)
                ilkind=j.find("Kurum Adı")
                if ilkind !=-1:
                    sonind=j.find("\r",ilkind)
                    temp=(j[ilkind:sonind]).split(':')
                    temp=temp[1]
                    self.isimlistesi.append(temp)
                ilkind=j.find("Adres")
                if ilkind !=-1:
                    sonind=j.find("\r",ilkind)
                    temp=(j[ilkind:sonind]).split(':')
                    temp=temp[1:]
                    #print(temp)
                    self.adreslistesi.append(temp)

                ilkind=j.find("Vekili")   
                if ilkind !=-1:
                    sonind=j.find("\r",ilkind)
                    temp=(j[ilkind:sonind]).split(':')
                    temp=temp[1:]
                    self.vekillistesi.append(temp)   
                ilkind=j.find("Vergi/Mersis/Detsis No")   
                if ilkind !=-1:
                    sonind=j.find("\r",ilkind)
                    temp=(j[ilkind:sonind]).split(':')
                    temp=temp[1]
                    self.verginolistesi.append(temp) 
                ilkind=j.find("Baro Sicil Numarası")   
                if ilkind !=-1:
                    sonind=j.find("\r",ilkind)
                    temp=(j[ilkind:sonind]).split(':')
                    temp=temp[1]
                    self.verginolistesi.append(temp) 
                ilkind=j.find("İletişim (Cep Telefonu)") 
                
                if ilkind !=-1:
                    sonind=j.find("\r",ilkind)
                    temp=(j[ilkind:sonind]).split(':')
                    temp=temp[1]
                    self.telnolistesi.append(temp) 

            if len(self.vekillistesi)<len(self.isimlistesi):
                self.vekillistesi.append("")
            if len(self.isimlistesi)<len(self.adreslistesi):
                self.isimlistesi.append("")
            if len(self.adreslistesi)<len(self.vekillistesi):
                self.adreslistesi.append("")
        #print (self.tcnolistesi)
        #print (self.adreslistesi)
        #print (self.telnolistesi)
        #print (self.verginolistesi)
        
        a=0
        
        self.tcno=verisozluk["tckimlikno"]
        self.isimsoyisim=verisozluk["adisoyadi"]
        self.adres=verisozluk["adres"]
        self.basvuranisimsoyisim=verisozluk
        self.basvuranadres=verisozluk
        self.hukukburo=verisozluk["buro"]
        self.basvurunumarasi=verisozluk["basvurunumarasi"]
        self.basvurutarihi=verisozluk["basvurutarihi"]
        


   
        

        return self.tcno,self.isimsoyisim,self.adres,self.basvuranisimsoyisim,self.basvuranadres,self.hukukburo,self.basvurunumarasi,self.basvurutarihi,self.vekili,self.isimlistesi,self.adreslistesi,self.vekillistesi,self.verginolistesi,self.telnolistesi,self.tcnolistesi
