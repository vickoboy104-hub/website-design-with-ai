from pathlib import Path
# Reuse the recovered curriculum parser; the page design below is new.
source=Path('visual_redesign/build.py').read_text().split('# Plan every page')[0]
exec(compile(source.replace("R=Path(__file__).parent;", "R=Path('visual_redesign');"),'curriculum','exec'))
for sec in S:
 for b in sec['blocks']:
  if b['type']=='image':b['path']=str(Path('visual_redesign/assets')/Path(b['path']).name)
from pygments import lex
from pygments.lexers import guess_lexer,TextLexer
from pygments.token import Token
from reportlab.lib.colors import Color
ROOT=Path('app_handout');OUT=ROOT/'output';OUT.mkdir(exist_ok=True)
WEB='https://vickoboy104-hub.github.io/website-design-with-ai/'
W,H=595.2756,841.8898;X=36;CW=W-2*X;INK='#182043';MUTED='#596580';BG='#F6F8FF';BLUE='#1765ED';PURPLE='#793CF1';TEAL='#008C91';PALETTE=[TEAL,BLUE,BLUE,TEAL,PURPLE,'#C34478','#496CCF',PURPLE,BLUE]
labels=['Welcome','Computer & internet','Notepad & VS Code','HTML','CSS','JavaScript','PHP','SQL','Complete websites','AI & publishing']
gicons=['⌂','@','<>','<>','#','JS','php','DB','▦','AI']
for i,g in enumerate(groups):g['color']=PALETTE[(i-1)%len(PALETTE)];g['label']=labels[i]
for s in S:s['color']=groups[s['group']]['color']
# Replace repeated edition instructions with a single brief orientation.
def p(t):return {'type':'p','text':t}
S[0]['title']='Your practical learning guide'
S[0]['blocks']=[p('Read a step. Try it on your computer.'),{'type':'explain','items':[['1 · Look','See what you are about to make.'],['2 · Do','Follow one step and try it.'],['3 · Check','Compare your result. Make one change.']]},p('Tap Lessons when you want the menu. Code opens the code index. Resources holds downloads and quick references.'),p('Select code to copy it. If long lines copy poorly in your PDF reader, use Copy code online for the exact text.'),p('The lessons work offline. Online previews and downloads need internet.')]
S[1]['blocks']=[p('Never used a computer? Start with the mouse and keyboard lesson. You do not need an AI account.'),p('Take one small step at a time. You are learning when you can try it yourself, even if you make a mistake.')]
S[2]['blocks']=[{'type':'h','text':'Paul Victor'},p('Web developer, ICT trainer and digital media creator. Paul teaches practical skills through small projects and visible results.'),{'type':'h','text':'Beloved Technology'},p('From your first click to your first website. Learn by making something that works.')]
S[3]['blocks']=[{'type':'p','text':'Open the online Code Lab','links':[{'text':'Open the online Code Lab','url':WEB}]},{'type':'p','text':'Download the practice ZIP','links':[{'text':'Download the practice ZIP','url':'https://github.com/vickoboy104-hub/website-design-with-ai/raw/refs/heads/main/downloads/Website_Design_Practice_Files.zip'}]},p('1. Download the ZIP. Press Ctrl + J in your browser, then choose Show in folder.'),p('2. Right-click the ZIP → Extract All. Choose Documents → Website Class → Extract.'),p('3. Open Website_Design_Practice_Files. Use START_HERE.html to find an exercise.'),p('4. Copy that exercise into a separate My Practice folder. Edit your copy.')]
S[4]['blocks']=[p('Home returns to the dashboard. Lessons opens the course menu. Code finds examples. Resources holds your quick references.'),p('Use the arrow buttons to move through pages. At the end of a lesson, Next takes you to the following lesson.'),p('A page number shows your place in the book. It does not track completed work.')]
oldshort=short
def short(t):
 t=oldshort(t)
 t=re.sub(r'^(HTML|CSS|JavaScript|PHP|SQL) (practical \d+|foundation|preparation|help) ', '', t)
 t=re.sub(r'^Website (\d+) File ', r'Website \1 · ',t)
 return t
# Show SQL records as real result tables, once per query.
for sec in S:
 if sec['title'].startswith('SQL practical') and 'Output' in sec['title']:
  result_rows=[];seen_rows=set();keep=[];insert_at=None
  for b in sec['blocks']:
   if b['type']=='explain' and b['items'][0][0] in ['id','name']:
    key=tuple(tuple(x) for x in b['items'])
    if key not in seen_rows:result_rows.append(b['items']);seen_rows.add(key)
    if insert_at is None:insert_at=len(keep)
   else:keep.append(b)
  tables=[]
  for row in result_rows:
   cols=[x[0] for x in row];vals=[x[1] for x in row]
   if not tables or tables[-1]['columns']!=cols:tables.append({'type':'sqltable','columns':cols,'rows':[]})
   tables[-1]['rows'].append(vals)
  keep[insert_at:insert_at]=tables;sec['blocks']=keep
# Keep technical coverage while removing repeated filler and merging code with its explanation.
oldprepare=prepare
fixes={
'Create a binding to a value; the binding is not reassigned here.':'Give a value a name. This example does not assign a new value to that name.',
'Find an element by its id in the DOM, the browser representation of HTML.':'Find part of the page using its id. The DOM is the browser’s working model of the page.',
'Test strict equality with empty text and stop early if it is missing.':'Check whether the field is empty. If it is, stop this action.',
'Read field text and remove outer whitespace.':'Read the typed text. Remove spaces from its beginning and end.',
'Choose typeface and size; rem follows the root text size.':'Set the font and text size. rem scales from the page’s base text size.',
'Set text safely and join strings; typed HTML is not executed.':'Join words and show them as text. A visitor’s typed HTML stays text.'}
repeated=set();all_notes=set();dropped=0
for s in S:
 out=[];seen=set()
 for bi,b in enumerate(s['blocks']):
  b=dict(b)
  if b['type']=='h':
   b['text']=b['text'].replace('Inside body in index html','In index.html: inside <body>').replace('style css','style.css').replace('app js','app.js')
  if b['type']=='code':b['sample']=s['id']+'-'+str(bi)
  if b['type']=='p':
   t=b['text']
   if len(t)>45 and not re.match(r'^\d+\.',t) and not b.get('links'):
    if t in all_notes:dropped+=1;continue
    all_notes.add(t)
   if t in seen:continue
   seen.add(t)
   if t.startswith('Now run the page or query') or t.startswith('Save this file. The complete project runs'):dropped+=1;continue
   # Shared troubleshooting is taught once per subject, not after every exercise.
   if t.startswith(('IF IT DOES NOT WORK','Save your files. Right-click index.html')):
    if t in repeated:dropped+=1;continue
    repeated.add(t)
   if t.startswith('Use: VS Code and the folder '):
    m=re.search(r'folder ([\w-]+)',t)
    if m:b['text']=f'Open {m[1]} in VS Code. Put the HTML below inside the body of index.html.'
   if t.startswith('Profile basis:') or t.startswith('A public Facebook listing'):continue
   if b.get('links'):
    for a in b['links']:
     if a['url'].endswith('Website_Design_Mobile_Reader.html'):a['url']=WEB
  if b['type']=='explain':b['items']=[[a,fixes.get(z,z)] for a,z in b['items']]
  out.append(b)
 s['blocks']=out
# Every source snippet keeps its original online ID even after shortened text blocks.
original=json.loads(Path('visual_redesign/sections.json').read_text());orig_by={s['id']:s for s in original}
for s in S:
 codes=[(i,b) for i,b in enumerate(orig_by[s['id']]['blocks']) if b['type']=='code'];k=0
 for b in s['blocks']:
  if b['type']=='h':
   b['text']=b['text'].replace('Inside body in index html','In index.html: inside <body>').replace('style css','style.css').replace('app js','app.js')
  if b['type']=='code':b['sample']=s['id']+'-'+str(codes[k][0]);k+=1
# Combine consecutive practical result pages and continued files into one lesson.
merged=[]
for s in S:
 join=bool(re.search(r'(Output and code explanation|code continued|continued \d+)',s['title']))
 if join and merged:
  merged[-1]['aliases'].append(s['id']);merged[-1]['blocks']+=s['blocks']
 else:s['aliases']=[];merged.append(s)
S=merged
# Resource chapters stay accessible from Resources, not on every lesson screen.
resource_start=next(i for i,s in enumerate(S) if s['title'].startswith('Your course completion'))
resources=S[resource_start:];resource_ids={s['id'] for s in resources}
for g in groups:g['secs']=[s for s in S if s['group']==groups.index(g) and s['id'] not in resource_ids]
# Identify practical projects for accurate preview links.
def project(s):
 m=re.match(r'(HTML|CSS|JavaScript|PHP|SQL) practical (\d)',s['title'])
 if m:return m[1].lower()+'-'+m[2]
 m=re.match(r'Website (\d)',s['title'])
 if m:return 'website-'+m[1]
 return None

def prepare2(s):
 blocks=[];codeidx=0
 for b in s['blocks']:
  if b['type']=='sqltable':blocks.append(dict(b,kind='sqltable'));continue
  if b['type']=='explain' and len(b['items'])==2:
   blocks.append({'kind':'meaning','term':b['items'][0][1],'text':b['items'][1][1]});continue
  if b['type']=='code':
   # Syntax highlighting retains text; line wrapping changes display only.
   text=b['text'];lns=[]
   try:lexer=guess_lexer(text)
   except:lexer=TextLexer()
   styled=[]
   for tok,v in lex(text,lexer):
    co='#D7E4FF'
    if tok in Token.Comment:co='#9CACC9'
    elif tok in Token.String:co='#A7EDD8'
    elif tok in Token.Keyword:co='#C7ACFF'
    elif tok in Token.Name.Tag or tok in Token.Name.Builtin:co='#7FD8FF'
    elif tok in Token.Number:co='#FFD58A'
    styled.extend((ch,co) for ch in v)
   # Do not include Pygments' synthetic final newline.
   styled=styled[:len(text)];cur=[]
   for ch,co in styled:
    if ch=='\n':lns.append(cur);cur=[]
    else:
     if len(cur)==86:lns.append(cur);cur=[]
     cur.append((ch,co))
   lns.append(cur)
   for j in range(0,len(lns),45):blocks.append({'kind':'code','lines':lns[j:j+45],'sample':b['sample'],'label':'CODE EXAMPLE' if j==0 else 'CODE CONTINUED'})
   continue
  tmp=dict(s,blocks=[b]);blocks+=oldprepare(tmp)
 for b in blocks:
  if b['kind']=='note' and b['label']=='NOTICE':b['label']=''
  if b['kind']=='meaning':b['text']=fixes.get(b['text'],b['text'])
 if s['title'] in diagrams:
  blocks=[b for b in blocks if b['kind']!='image'];blocks.insert(0,{'kind':'diagram','rows':diagrams[s['title']]})
 pr=project(s)
 if pr and re.match(r'(HTML|CSS|JavaScript|PHP|SQL) practical',s['title']):
  blocks.insert(1,{'kind':'web','project':pr,'live':pr.startswith(('html-','css-','javascript-'))})
 return blocks

pages=[]
def add(kind,s=None,items=None,anchor=None):pages.append({'kind':kind,'s':s,'items':items or [],'key':anchor or s['id']})
def height(b):
 k=b['kind']
 if k=='heading':return para(E(b['text']),CW,16,'Bold')[1]+4
 if k=='source':return para(E(b['text']),CW,10)[1]+8
 if k=='code':return 57+len(b['lines'])*12.5
 if k=='web':return 40
 if k=='sqltable':
  n=len(b['columns']);b['widths']=[CW/n]*n;b['rh']=[max(para(E(v),w-16,14)[1] for v,w in zip(row,b['widths']))+20 for row in b['rows']];return 42+sum(b['rh'])
 if k=='diagram':return len(b['rows'])*77
 if k=='image':
  with Image.open(b['path']) as im:w,h=im.size
  b['ih']=min(265,(CW-24)*h/w);return b['ih']+44
 if k=='meaning':return 18+para(E(b['term']),CW-41,12,'Bold')[1]+para(E(b['text']),CW-32,12)[1]
 return (18 if not b.get('label') else 32)+para(b['text'],CW-58 if k=='step' else CW-32,12)[1]
def pack(s):
 bs=prepare2(s);cur=[];used=0;cap=H-150
 # Continue short lessons on the same A4 page when the new heading and first
 # teaching block fit together. Keep subject boundaries distinct.
 if pages and pages[-1]['kind']=='lesson' and pages[-1]['s']['group']==s['group'] and not s['title'].startswith('Part '):
  prev=pages[-1];occupied=sum(height(x)+7 for x in prev['items'])
  titleblock={'kind':'heading','text':short(s['title'])}
  opening=sum(height(x)+7 for x in bs[:2])
  if occupied+height(titleblock)+opening+21<cap:
   prev['items'].append(titleblock);prev.setdefault('embedded',[]).append(s['id'])
   for b in bs:
    reserve=height(bs[bs.index(b)+1])+7 if b['kind']=='heading' and bs.index(b)+1<len(bs) else 0
    if sum(height(x)+7 for x in prev['items'])+height(b)+reserve>cap:break
    prev['items'].append(b)
   # Only the blocks actually added above are removed from the remaining flow.
   n=0
   while n<len(bs) and any(x is bs[n] for x in prev['items']):n+=1
   bs=bs[n:]

 for j,b in enumerate(bs):
  bh=height(b)
  if bh>cap:raise Exception(('Tall',s['title'],bh,b))
  reserve=height(bs[j+1])+7 if b['kind']=='heading' and j+1<len(bs) else 0
  if cur and used+bh+reserve>cap:add('lesson',s,cur);cur=[];used=0
  cur.append(b);used+=bh+7
 if cur:add('lesson',s,cur)
add('home',anchor='home')
# Index pages sit at the end, so reading flows straight into the first lesson.
for s in S:pack(s)
for start in range(0,len(groups),8):add('roadmap',items=list(enumerate(groups))[start:start+8],anchor='lessons')
for i,g in enumerate(groups):
 for start in range(0,len(g['secs']),9):add('menu',{'id':f'group_{i}','title':g['label'],'color':g['color'],'group':i},g['secs'][start:start+9])
code_lessons=[s for s in S if any(b['type']=='code' for b in s['blocks'])]
for start in range(0,len(code_lessons),9):add('menu',{'id':'code','title':'Code Lab','color':PURPLE,'group':0},code_lessons[start:start+9])
for start in range(0,len(resources)+1,9):
 r=[S[3]]+resources
 add('menu',{'id':'resources','title':'Resources','color':TEAL,'group':0},r[start:start+9])
first={};local={}
for i,pag in enumerate(pages):first.setdefault(pag['key'],i);local.setdefault(pag['key'],[]).append(i)
for pi,pag in enumerate(pages):
 for anchor in pag.get('embedded',[]):first[anchor]=min(first.get(anchor,pi),pi)
for s in S:
 for a in s['aliases']:first[a]=first[s['id']]
C=canvas.Canvas(str(OUT/'Practical_Website_Design_with_AI.pdf'),pagesize=(W,H));C.setTitle('Website Design with AI | Practical A4 Handbook');C.setAuthor('Paul Victor · Beloved Technology');C.setSubject('A practical mobile-first course with live examples and copyable code')
def rect(x,y,w,h,fill,r=0,stroke=None):
 C.setFillColor(HexColor(fill));C.setStrokeColor(HexColor(stroke or fill));C.roundRect(x,H-y-h,w,h,r,fill=1,stroke=bool(stroke))
def txt(t,x,y,size=12,color=INK,font='Text'):
 C.setFillColor(HexColor(color));C.setFont(font,size);C.drawString(x,H-y-size,t)
def drawp(t,x,y,w,size=18,font='Text',color=INK):
 ob,h=para(t,w,size,font,color);ob.drawOn(C,x,H-y-h);return h
def gradient(x,y,w,h,a,b,r=18):
 C.saveState();path=C.beginPath();path.roundRect(x,H-y-h,w,h,r);C.clipPath(path,stroke=0);ca=HexColor(a);cb=HexColor(b)
 for j in range(100):
  t=j/99;C.setFillColor(Color(ca.red*(1-t)+cb.red*t,ca.green*(1-t)+cb.green*t,ca.blue*(1-t)+cb.blue*t));C.rect(x+j*w/100,H-y-h,w/100+1,h,stroke=0,fill=1)
 C.restoreState()
def linkbox(label,x,y,w,h,target,external=False,fill=BLUE,sz=13):
 rect(x,y,w,h,fill,11);drawp(E(label),x+12,y+(h-sz*1.34)/2,w-24,sz,'Bold','#FFFFFF')
 box=(x,H-y-h,x+w,H-y)
 if external:C.linkURL(target,box,relative=0,thickness=0)
 else:C.linkAbsolute(label,'p'+str(first[target]),box,thickness=0)
def symbol(kind,x,y,color=BLUE,size=26):
 C.setStrokeColor(HexColor(color));C.setFillColor(HexColor(color));C.setLineWidth(1.8)
 if kind=='home':
  z=C.beginPath();z.moveTo(x,H-y-12);z.lineTo(x+12,H-y-2);z.lineTo(x+24,H-y-12);C.drawPath(z);C.rect(x+5,H-y-24,14,13,stroke=1,fill=0)
 elif kind=='lessons':
  for j in range(3):C.circle(x+3,H-y-5-j*8,1.5,fill=1,stroke=0);C.line(x+9,H-y-5-j*8,x+24,H-y-5-j*8)
 elif kind=='resources':
  z=C.beginPath();z.moveTo(x,H-y-22);z.lineTo(x,H-y-5);z.lineTo(x+9,H-y-5);z.lineTo(x+13,H-y-9);z.lineTo(x+25,H-y-9);z.lineTo(x+25,H-y-22);z.close();C.drawPath(z)
 else:txt('</>',x,y+1,16,color,'Code')
def footer(active):
 y=H-34
 rect(X,y,CW,24,'#FFFFFF',6,stroke='#DCE3F3')
 entries=[('home','Home',64),('lessons','Lessons',70),('code','Code',58),('resources','Resources',80)]
 xx=X+5
 for key,label,w in entries:
  co=BLUE if active==key else MUTED
  txt(label,xx+9,y+6,9,co,'Bold' if active==key else 'Text')
  C.linkAbsolute(label,'p'+str(first[key]),(xx,H-y-24,xx+w,H-y),thickness=0);xx+=w
 for label,px,target in [('‹',W-X-142,max(0,i-1)),('›',W-X-26,min(len(pages)-1,i+1))]:
  txt(label,px+7,y+1,17,BLUE,'Bold');C.linkAbsolute(label,'p'+str(target),(px,H-y-24,px+25,H-y),thickness=0)
 txt(f'{i+1} / {len(pages)}',W-X-107,y+6,9,MUTED)
def brand():symbol('code',X,17,BLUE);txt('Beloved Technology',X+37,16,13,BLUE,'Bold');txt('WEBSITE DESIGN WITH AI',X+37,34,8,MUTED)
def hero_laptop(x,y):
 gradient(x,y,116,84,'#346BF8','#7442F1',10);rect(x+7,y+7,102,66,'#182642',6)
 for j,w in enumerate([42,69,52,73]):rect(x+17,y+20+j*10,w,3,['#80DCEA','#BAA1FF','#95E5BD','#7CA8F8'][j],1)
 C.setFillColor(HexColor('#9EACFF'));z=C.beginPath();z.moveTo(x-12,H-y-88);z.lineTo(x+128,H-y-88);z.lineTo(x+116,H-y-101);z.lineTo(x,H-y-101);z.close();C.drawPath(z,fill=1,stroke=0)
 rect(x-12,y-13,39,36,'#FFFFFF',9);txt('</>',x-7,y-5,17,BLUE,'Code');rect(x+93,y-22,37,34,'#9D78FF',9);txt('AI',x+99,y-15,16,'#FFFFFF','Bold')
def head(pag,i):
 s=pag['s'];co=s['color'];brand();seq=local[pag['key']];n=seq.index(i)+1
 txt(labels[s['group']] if pag['key'] not in ['code','resources'] else 'YOUR LEARNING TOOLS',X,60,11,co,'Bold');txt(f'{n}/{len(seq)}',W-59,60,11,MUTED)
 title=short(s['title']);sz=20
 while para(E(title),CW,sz,'Bold')[1]>40:sz-=.5
 drawp(E(title),X,75,CW,sz,'Bold');rect(X,103,CW,2,'#E6EAF7',1)
def block(b,y,co):
 k=b['kind'];bh=height(b)
 if k=='heading':drawp(E(b['text']),X,y,CW,16,'Bold',co)
 elif k=='source':drawp(E(b['text']),X,y,CW,10,color=MUTED)
 elif k=='sqltable':
  rect(X,y,CW,bh,'#FFFFFF',12,stroke='#E5EAF6');rect(X,y,CW,38,'#E3EAFE',12);xx=X
  for name,w in zip(b['columns'],b['widths']):drawp(E(name),xx+8,y+10,w-16,12,'Bold',co);xx+=w
  yy=y+40
  for row,rh in zip(b['rows'],b['rh']):
   xx=X
   for val,w in zip(row,b['widths']):drawp(E(val),xx+8,yy+8,w-16,14);xx+=w
   yy+=rh
 elif k=='web':
  if b['live']:linkbox('Preview live ↗',X,y,CW/2-5,32,WEB+'examples/'+b['project']+'/index.html',True,BLUE);linkbox('Copy files ↗',X+CW/2+5,y,CW/2-5,32,WEB+'#project/'+b['project'],True,PURPLE)
  else:linkbox('Open code online ↗',X,y,CW,32,WEB+('#code' if b['project'].startswith('sql') else '#project/'+b['project']),True,PURPLE)
 elif k=='code':
  rect(X,y,CW,bh,'#172136',14);rect(X,y,CW,32,'#26334E',12)
  for j,col in enumerate(['#FF9AB5','#FFE399','#8BE1CD']):C.setFillColor(HexColor(col));C.circle(X+14+j*10,H-y-16,2.5,fill=1,stroke=0)
  txt(b['label'],X+49,y+10,8,'#D6E3FB','Bold')
  txt('Copy online ↗',X+CW-101,y+9,10,'#D5C5FF','Bold');C.linkURL(WEB+'#sample/'+b['sample'],(X+CW-108,H-y-31,X+CW,H-y),thickness=0)
  for j,line in enumerate(b['lines']):
   for n,(ch,col) in enumerate(line):txt(ch,X+12+n*pdfmetrics.stringWidth('M','Code',9.5),y+40+j*12.5,9.5,col,'Code')
 elif k=='image':
  rect(X,y,CW,bh,'#FFFFFF',14,stroke='#E4EAF7');txt(b['caption'],X+12,y+10,9,co,'Bold')
  with Image.open(b['path']) as im:w,h=im.size
  ih=b['ih'];iw=ih*w/h;C.drawImage(b['path'],X+(CW-iw)/2,H-y-31-ih,width=iw,height=ih,mask='auto')
 elif k=='meaning':
  rect(X,y,CW,bh,'#FFFFFF',14,stroke='#E5EAF6');rect(X+12,y+14,4,20,co,2);th=drawp(E(b['term']),X+25,y+8,CW-41,12,'Bold',co);drawp(E(b['text']),X+16,y+13+th,CW-32,12)
 elif k=='diagram':
  for j,(a,z) in enumerate(b['rows']):
   yy=y+j*77;rect(X,yy,CW,65,'#EBF1FF' if j%2==0 else '#EFEAFC',13);rect(X+12,yy+13,33,33,co,10);txt(str(j+1),X+23,yy+19,15,'#FFFFFF','Bold');txt(a,X+57,yy+10,12,co,'Bold');drawp(E(z),X+57,yy+30,CW-72,14)
   if j<len(b['rows'])-1:txt('↓',X+CW/2-4,yy+61,13,co,'Bold')
 else:
  fill,c={'TRY':('#EEE8FF',PURPLE),'CHECK':('#E1F6EF','#147354'),'FIX IT':('#FFF1DE','#915900'),'RESULT':('#E4F6FC',TEAL)}.get(b.get('label'),('#FFFFFF',co))
  rect(X,y,CW,bh,fill,14,stroke='#E6EAF5' if fill=='#FFFFFF' else None)
  if k=='step':rect(X+12,y+13,27,27,co,8);txt(b['label'],X+20,y+17,13,'#FFFFFF','Bold');drawp(b['text'],X+46,y+12,CW-58,12)
  else:
   if b.get('label'):txt(b['label'],X+16,y+11,10,c,'Bold')
   drawp(b['text'],X+16,y+(23 if b.get('label') else 9),CW-32,12)
 return bh
for i,pag in enumerate(pages):
 C.bookmarkPage('p'+str(i));rect(0,0,W,H,BG);kind=pag['kind']
 if i==first[pag['key']]:C.addOutlineEntry(pag['s']['title'] if pag['s'] else ('Home' if kind=='home' else 'Lessons'),'p'+str(i),0,False)
 if kind=='home':
  brand();gradient(X,69,CW,272,'#E6ECFF','#E5F7FC');txt('YOUR PRACTICAL WEBSITE HANDBOOK',X+16,86,9,BLUE,'Bold');drawp('Website Design<br/>with <font color="#753CF1">AI</font>',X+16,114,CW-32,30,'Bold');drawp('Start with one click.<br/>Build something real.',X+16,202,190,16,color=MUTED);hero_laptop(X+200,224);linkbox('Start learning →',X+16,282,170,41,S[0]['id'])
  txt('Your learning space',X,365,21,INK,'Bold')
  for j,(a,title,desc,ic,col) in enumerate([('lessons','Lessons','Follow the course','lessons',BLUE),('code','Code Lab','Copy and practise','code',PURPLE),('resources','Resources','Files and quick help','resources',TEAL)]):
   y=405+j*66;rect(X,y,CW,55,'#FFFFFF',15,stroke='#E5EAF6');symbol(ic,X+15,y+14,col);txt(title,X+60,y+8,17,INK,'Bold');txt(desc,X+60,y+32,11,MUTED);txt('›',W-48,y+14,20,col);C.linkAbsolute(title,'p'+str(first[a]),(X,H-y-55,W-X,H-y),thickness=0)
  txt('Paul Victor · Beloved Technology',X,613,11,MUTED);footer('home')
 elif kind=='roadmap':
  brand();txt('YOUR COURSE ROADMAP',X,66,10,BLUE,'Bold');txt('Choose a subject',X,92,28,INK,'Bold')
  for j,(gi,g) in enumerate(pag['items']):
   y=132+j*78;rect(X,y,CW,68,'#FFFFFF',15,stroke='#E5EAF6');gradient(X+12,y+12,42,42,g['color'],PURPLE,11);txt(str(gi).zfill(2),X+21,y+23,14,'#FFFFFF','Bold');txt(g['label'],X+66,y+12,17,INK,'Bold');txt(f'{len(g["secs"])} lessons',X+66,y+39,12,MUTED);C.linkAbsolute(g['label'],'p'+str(first['group_'+str(gi)]),(X,H-y-68,W-X,H-y),thickness=0)
  footer('lessons')
 elif kind=='menu':
  head(pag,i)
  for j,s in enumerate(pag['items']):
   y=120+j*72;rect(X,y,CW,64,'#FFFFFF',14,stroke='#E5EAF6');txt('OPEN LESSON',X+15,y+10,9,pag['s']['color'],'Bold');sz=14
   while para(E(short(s['title'])),CW-44,sz,'Bold')[1]>33:sz-=.5
   drawp(E(short(s['title'])),X+15,y+28,CW-44,sz,'Bold');C.linkAbsolute(s['title'],'p'+str(first[s['id']]),(X,H-y-64,W-X,H-y),thickness=0)
  footer('code' if pag['key']=='code' else 'resources' if pag['key']=='resources' else 'lessons')
 else:
  head(pag,i);y=112
  for b in pag['items']:y+=block(b,y,pag['s']['color'])+7
  footer('resources' if pag['s']['id'] in resource_ids else 'code' if any(b['kind']=='code' for b in pag['items']) else 'lessons')
 C.showPage()
C.save();(ROOT/'manifest.json').write_text(json.dumps([{'page':i+1,'kind':p['kind'],'title':p['s']['title'] if p['s'] else p['key'],'blocks':[b.get('kind') if isinstance(b,dict) else 'row' for b in p['items']]} for i,p in enumerate(pages)],ensure_ascii=False));print(len(pages),'pages;',len(S),'lessons;',dropped,'repeated transitions removed')
