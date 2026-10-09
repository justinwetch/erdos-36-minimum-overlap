"""Exact rational compiler for averaged periodic triangle interval rows."""
from fractions import Fraction as F

SCHEMA='periodic-interval-dual-v4'

def rational(value):
    return F(str(value))

def from_uniform(data):
    if data['schema']!='periodic-triangle-dual-v1': raise ValueError('uniform triangle input required')
    n=int(data['cells']); h=F(2,n); rows=[]
    if n<2 or n&(n-1): raise ValueError('power-of-two grid required')
    for i,(lo,hi) in enumerate(zip(data['low'],data['high'])):
        low,high=rational(lo),rational(hi)
        if low or high:
            rows.append({'a':str(i*h),'b':str((i+1)*h),'z_low':str(low/h),'z_high':str(high/h)})
    return {'schema':SCHEMA,'y0':data['y0'],'y2':data['y2'],'cos':data['cos'],
            'intervals':rows,'scope':'exact rational interval representation; requires continuous verification'}

def compile_intervals(data):
    if data['schema']!=SCHEMA: raise ValueError('interval schema required')
    events={F(0):F(0),F(2):F(0)}; bound=F(0); nonzero=0
    def segment(a,b,weight):
        if not weight or b==a: return
        if not 0<=a<b<=2: raise ValueError('compiled segment outside circle')
        events[a]=events.get(a,F(0))+weight; events[b]=events.get(b,F(0))-weight
    def symmetric(a,b,weight):
        segment(a,b,weight/2); segment(2-b,2-a,weight/2)
    def wrapped_symmetric(a,b,weight):
        while a<b:
            turn=a//2; end=min(b,2*(turn+1))
            symmetric(a-2*turn,end-2*turn,weight); a=end
    for row in data['intervals']:
        a,b,low,high=(rational(row[k]) for k in ('a','b','z_low','z_high'))
        if not 0<=a<b<=2 or low>0 or high>0: raise ValueError('invalid interval row')
        bound+=2*(b-a)*high; nonzero+=bool(low)+bool(high)
        symmetric(a,b,2*(high-low)); wrapped_symmetric(2*a,2*b,(low+high)/2)
    points=sorted(events); step=F(0); parts=[]
    for a,b in zip(points[:-1],points[1:]):
        step+=events[a]
        if parts and parts[-1][2]==step: parts[-1]=(parts[-1][0],b,step)
        else: parts.append((a,b,step))
    if step+events[F(2)]!=0: raise ValueError('unbalanced jump events')
    if not parts or parts[0][0]!=0 or parts[-1][1]!=2: raise ValueError('interval cover')
    return parts,bound,nonzero
