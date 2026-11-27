from fastapi import FastAPI, Query
from datetime import date, timedelta
import random

app = FastAPI(title='Groep 5 - Plaagdetectie', description='Uitsluitend fictieve demonstratiedata', version='1.0')
PLAGEN = {'trips': (27,65,15,'Orius laevigatus'), 'witte_vlieg': (25,75,20,'Encarsia formosa'), 'mineervlieg': (24,70,10,'Diglyphus isaea'), 'bladluis': (23,75,10,'Aphidius colemani')}

def dataset():
    rng = random.Random(42)
    return [dict(datum=(date.today()-timedelta(days=29-d)).isoformat(), kas_id=k, vak_id=v, plaag=p, aantal=rng.randint(0,12)+(d if (k,v,p)==(2,3,'trips') else 0), meetperiode_dagen=1, fictief=True) for d in range(30) for k in range(1,4) for v in range(1,6) for p in PLAGEN]

@app.get('/')
def home():
    return {'groep':5,'dienst':'Plaagdetectie','fictief':True,'endpoints':['/vangsten','/risico','/alarmen','/bestrijding','/docs']}

@app.get('/vangsten')
def vangsten(kas_id: int | None=None, vak_id: int | None=None, plaag: str | None=None, datum: date | None=None):
    return [r for r in dataset() if (kas_id is None or r['kas_id']==kas_id) and (vak_id is None or r['vak_id']==vak_id) and (plaag is None or r['plaag']==plaag) and (datum is None or r['datum']==datum.isoformat())]

@app.get('/risico')
def risico(temperatuur: float=25, rv: float=75, kas_id: int | None=None, vak_id: int | None=None):
    if not -20 <= temperatuur <= 60 or not 0 <= rv <= 100:
        from fastapi import HTTPException
        raise HTTPException(422,'Ongeldige klimaatwaarden')
    resultaten=[]
    for r in vangsten(kas_id,vak_id,datum=date.today()):
        t,h,d,b=PLAGEN[r['plaag']]
        score=round(100*(.6*min(1,r['aantal']/d)+.25*max(0,1-abs(temperatuur-t)/15)+.15*max(0,1-abs(rv-h)/50)))
        resultaten.append(dict(r,temperatuur=temperatuur,rv=rv,risicoscore=score,alarm=score>=80,risiconiveau='hoog' if score>=80 else 'middel' if score>=60 else 'laag',advies=b if score>=80 else 'Monitoring voortzetten',model='illustratief, niet gevalideerd'))
    return resultaten

@app.get('/alarmen')
def alarmen(temperatuur: float=25, rv: float=75, kas_id: int | None=None, vak_id: int | None=None):
    return [r for r in risico(temperatuur,rv,kas_id,vak_id) if r['alarm']]

@app.get('/bestrijding')
def bestrijding():
    return {p:dict(temperatuur_optimum=t,rv_optimum=h,drempel=d,bestrijding=b,fictief_model=True) for p,(t,h,d,b) in PLAGEN.items()}
