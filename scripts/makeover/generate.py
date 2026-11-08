#!/usr/bin/env python3
"""Build the Rezwan pixel-core visual system without external dependencies.

Python: Pillow, fontTools. Raster export: node + sharp (via render.mjs).
Run from any directory. The canonical 48x48 grid is stored beside this script.
Optional --source can regenerate that grid from the original 460px avatar.
"""
from pathlib import Path
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from PIL import Image, ImageDraw
import argparse, json, math, hashlib, subprocess, os, html, re, tempfile

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'assets/makeover'
HERE=Path(__file__).resolve().parent
BG='#100b18'; CREAM='#fff6c8'; AMBER='#ff9f1c'; YELLOW='#ffe66d'; VIOLET='#ac83c3'; MUTED='#b6a7c1'; LINE='#392445'
CANON=['#100b18','#231331','#5c2a72','#d94a4a','#ff9f1c','#ffe66d','#fff6c8']
FONTROOT=Path('/usr/share/fonts/opentype/urw-base35')
FONTS={k:TTFont(str(FONTROOT/v)) for k,v in {'display':'URWGothic-Demi.otf','body':'NimbusSans-Regular.otf','bold':'NimbusSans-Bold.otf'}.items()}

def text_width(s,size,font='display',tracking=0):
 f=FONTS[font]; cmap=f.getBestCmap(); scale=size/f['head'].unitsPerEm
 return sum(f['hmtx'].metrics[cmap.get(ord(c),'space')][0]*scale+tracking for c in s)-tracking

def text(s,x,y,size,fill=CREAM,font='display',tracking=0):
 f=FONTS[font]; cmap=f.getBestCmap(); gs=f.getGlyphSet(); scale=size/f['head'].unitsPerEm
 pen=SVGPathPen(gs); cursor=x
 for c in s:
  name=cmap.get(ord(c),'space'); p=TransformPen(pen,(scale,0,0,-scale,cursor,y)); gs[name].draw(p)
  cursor+=f['hmtx'].metrics[name][0]*scale+tracking
 return f'<path fill="{fill}" d="{pen.getCommands()}"/>'

def compact(s):
 import re
 # Keep a small, readable SVG; numeric outlines need no excessive precision.
 return re.sub(r'-?\d+\.\d{3,}',lambda m:format(float(m.group()),'.2f').rstrip('0').rstrip('.'),s)

def grid_from_image(path):
 im=Image.open(path).convert('RGB'); rgb=[tuple(bytes.fromhex(c[1:])) for c in CANON]; grid=[]
 for y in range(48):
  row=[]
  for x in range(48):
   v=im.getpixel((min(im.width-1,int((x+.5)*im.width/48)),min(im.height-1,int((y+.5)*im.height/48))))
   row.append(min(range(len(rgb)),key=lambda i:sum((v[j]-rgb[i][j])**2 for j in range(3))))
  grid.append(row)
 return grid

def grid_paths(grid):
 # Join horizontal runs vertically. Source pixels become exact rectilinear paths.
 active={}; rects=[]
 for y,row in enumerate(grid+[[]]):
  runs=[]; x=0
  while x<len(row):
   c=row[x]; end=x+1
   while end<len(row) and row[end]==c:end+=1
   if c:runs.append((c,x,end))
   x=end
  nxt={}
  for run in runs:
   if run in active: nxt[run]=(active[run][0],active[run][1]+1)
   else:nxt[run]=(y,1)
  for run,(start,h) in active.items():
   if run not in nxt:rects.append((*run,start,h))
  active=nxt
 grouped={}
 for c,x,end,y,h in rects: grouped.setdefault(c,[]).append(f'M{x} {y}h{end-x}v{h}h{x-end}z')
 return ''.join(f'<path fill="{CANON[c]}" d="{"".join(ds)}"/>' for c,ds in sorted(grouped.items()))

CSS='''<style>
.signal{animation:signal-orbit 12s linear infinite;transform-box:view-box;transform-origin:640px 320px}
.avatar-signal{animation:avatar-orbit 12s linear infinite;transform-origin:250px 250px}
.banner-signal{animation:banner-orbit 12s linear infinite;transform-origin:1010px 213px}
@keyframes signal-orbit{to{transform:rotate(360deg)}}
@keyframes avatar-orbit{to{transform:rotate(360deg)}}
@keyframes banner-orbit{to{transform:rotate(360deg)}}
@media(prefers-reduced-motion:reduce){.signal,.avatar-signal,.banner-signal{animation:none!important}}
</style>'''


def svg(w,h,title,body,animated=False,desc=''):
 css=CSS if animated else ''
 return compact(f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="title desc"><title id="title">{html.escape(title)}</title><desc id="desc">{html.escape(desc or title)}</desc>{css}<rect width="{w}" height="{h}" fill="{BG}"/>{body}</svg>')

def core(x,y,size):
 return f'<g transform="translate({x-size/2} {y-size/2}) scale({size/48})">{CORE}</g>'

def signal_dot(cx,cy,r,cls='',size=6):
 return f'<g class="{cls}"><rect x="{cx-size/2}" y="{cy-r-size/2}" width="{size}" height="{size}" fill="{YELLOW}"/><rect x="{cx-size/2}" y="{cy+r-size/2}" width="{size}" height="{size}" fill="{VIOLET}"/></g>'

REPOS=[
 ('matlab-simulink-energy-lab',['MATLAB / Simulink','energy lab'],'Battery models. Grid control.','MODELLING', 'model'),
 ('battery-cycle-life-analyzer',['Battery cycle-life','analyzer'],'Capacity fade. Clearer evidence.','ANALYSIS','cycle'),
 ('bess-qaqc-toolkit',['BESS QA/QC','toolkit'],'From supplier review to handover.','ASSURANCE','quality'),
 ('datacenter-twin-lab',['Datacenter','twin lab'],'Power continuity, made inspectable.','CONTINUITY','twin'),
 ('voltrl',['VoltRL'],'Battery arbitrage, reproducibly.','CONTROL','control'),
 ('helioforge-energy-lab',['HelioForge','energy lab'],'Hybrid energy, explicit assumptions.','SYSTEMS','hybrid'),
]

def line(d,stroke=LINE,width=2):return f'<path d="{d}" stroke="{stroke}" stroke-width="{width}" fill="none"/>'

def poster_motif(kind,cx=1010,cy=310):
 # Abstract engineering linework, deliberately not quantitative charts.
 paths=[]
 if kind=='model':
  for yy in [cy-128,cy+128]:paths += [line(f'M760 {yy}H856V{cy}H1165',VIOLET,2)]
  paths += [line(f'M1165 {cy-128}V{cy+128}',VIOLET,2)]
 elif kind=='cycle':
  for r in [170,193]:paths += [f'<circle cx="{cx}" cy="{cy}" r="{r}" stroke="{LINE}" stroke-width="2" fill="none"/>']
  paths += [line(f'M{cx-193} {cy}h24m{338} 0h24',VIOLET,4)]
 elif kind=='quality':
  paths += [line(f'M810 {cy-150}V{cy+150}H1190V{cy-150}H810',VIOLET,2),line(f'M786 {cy-174}h48m-24 -24v48M1166 {cy+174}h48m-24 -24v48',AMBER,3)]
 elif kind=='twin':
  paths += [line(f'M765 {cy-140}H1200M765 {cy+140}H1200',VIOLET,2)]
  for xx in [810,1180]:paths += [line(f'M{xx} {cy-140}V{cy+140}',VIOLET,2)]
 elif kind=='control':
  paths += [line(f'M776 {cy+140}V{cy-140}H1200V{cy+140}H776',VIOLET,2),line(f'M776 {cy}H1216',LINE,2)]
 elif kind=='hybrid':
  for yy in [cy-160,cy+160]: paths += [line(f'M760 {yy}H880L1008 {cy}L1140 {yy}H1210',VIOLET,2)]
 return ''.join(paths)+core(cx,cy,360)


def write_static_and_animated(name,w,h,title,body,moving,desc):
 (OUT/f'{name}.svg').write_text(svg(w,h,title,body+moving,True,desc))
 (OUT/f'{name}-static.svg').write_text(svg(w,h,title,body+moving,False,desc))


def make_avatar_gif(grid):
 # Palette-stable frames; only two tiny orbit signals move. Original pixels stay exact.
 size=320; base=Image.new('RGB',(size,size),BG); draw=ImageDraw.Draw(base)
 inset=8; scale=(size-2*inset)/48
 for yy,row in enumerate(grid):
  for xx,c in enumerate(row):
   if c:draw.rectangle((round(inset+xx*scale),round(inset+yy*scale),round(inset+(xx+1)*scale)-1,round(inset+(yy+1)*scale)-1),fill=CANON[c])
 palette=[]
 for col in CANON+[VIOLET]:palette+=list(bytes.fromhex(col[1:]))
 palette+= [0]*(768-len(palette)); pal=Image.new('P',(1,1));pal.putpalette(palette)
 frames=[]
 for f in range(48):
  im=base.copy();d=ImageDraw.Draw(im);angle=2*math.pi*f/48
  for offset,col in [(0,YELLOW),(math.pi,VIOLET)]:
   x=160+148*math.sin(angle+offset);y=160-148*math.cos(angle+offset)
   d.rectangle((round(x)-2,round(y)-2,round(x)+2,round(y)+2),fill=col)
  frames.append(im.quantize(palette=pal,dither=Image.Dither.NONE))
 frames[0].save(OUT/'avatar.gif',save_all=True,append_images=frames[1:],duration=250,loop=0,optimize=True,disposal=1)


def make_banner_gif():
 # Render a markerless base so fixed signals cannot duplicate the orbit overlay.
 source=(OUT/'profile-banner-static.svg').read_text()
 source,count=re.subn(r'<g class="banner-signal">.*?</g>', '', source, count=1)
 if count != 1:raise ValueError('Expected exactly one banner-signal group')
 with tempfile.TemporaryDirectory(prefix='.banner-',dir=OUT) as tmp:
  clean_svg=Path(tmp)/'base.svg';clean_png=Path(tmp)/'base.png'
  clean_svg.write_text(source)
  subprocess.run([os.environ.get('CODEX_PRIMARY_RUNTIME_NODE','node'),str(HERE/'render.mjs'),str(clean_svg),str(clean_png)],check=True)
  base=Image.open(clean_png).convert('RGB').resize((960,320),Image.Resampling.LANCZOS)
 pal=base.quantize(colors=96,method=Image.Quantize.MEDIANCUT)
 palette=pal.getpalette();palette[96*3:96*3+3]=list(bytes.fromhex(YELLOW[1:]));palette[97*3:97*3+3]=list(bytes.fromhex(VIOLET[1:]));pal.putpalette(palette)
 frames=[]
 for f in range(48):
  im=base.copy();d=ImageDraw.Draw(im);angle=2*math.pi*f/48
  for offset,col in [(0,YELLOW),(math.pi,VIOLET)]:
   x=757.5+147*math.sin(angle+offset);y=160-147*math.cos(angle+offset)
   d.rectangle((round(x)-2,round(y)-2,round(x)+2,round(y)+2),fill=col)
  frames.append(im.quantize(palette=pal,dither=Image.Dither.NONE))
 frames[0].save(OUT/'profile-banner.gif',save_all=True,append_images=frames[1:],duration=250,loop=0,optimize=True,disposal=1)


def manifest():
 records=[]
 for p in sorted(OUT.rglob('*')):
  if not p.is_file() or p.name=='manifest.json':continue
  rec={'path':p.relative_to(ROOT).as_posix(),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()}
  if p.suffix.lower() in ['.png','.gif','.webp','.jpg']:
   im=Image.open(p);rec['width']=im.width;rec['height']=im.height
   if p.suffix=='.gif':rec.update(frames=im.n_frames,loop=im.info.get('loop'),duration_ms=sum((im.seek(i) or im.info.get('duration',0)) for i in range(im.n_frames)))
  elif p.suffix=='.svg':
   import re
   match=re.search(r'viewBox="0 0 (\d+) (\d+)"',p.read_text());rec.update(width=int(match[1]),height=int(match[2]))
   rec['animated']='<style>' in p.read_text();rec['reduced_motion_static']=True if rec['animated'] else None
  records.append(rec)
 data={'design':'Rezwan pixel core / engineered signal','source':'48×48 pixel geometry sampled from the existing user avatar; seven original colors retained','motion':{'period_seconds':12,'iterations':'infinite','moving_elements':'two small signal markers; emblem and text stay fixed','svg':'script-free CSS; reduced-motion preference disables animation','gif':'loop=0; GIF cannot honor reduced-motion preference; use static alternate where needed'},'github':{'native_avatar':'avatar.png; native animation unsupported','social_preview':'Static PNG for dependable sharing; receiving platforms control animation','readme':'GIF fallback; SVG motion depends on renderer'},'files':records}
 (OUT/'manifest.json').write_text(json.dumps(data,indent=2)+'\n')

parser=argparse.ArgumentParser();parser.add_argument('--source');parser.add_argument('--manifest-only',action='store_true');parser.add_argument('--banner-gif-only',action='store_true');args=parser.parse_args()
if args.manifest_only:manifest();raise SystemExit
if args.banner_gif_only:make_banner_gif();manifest();raise SystemExit
OUT.mkdir(parents=True,exist_ok=True);(OUT/'social').mkdir(exist_ok=True)
gridpath=HERE/'pixel-core.json'
if args.source:gridpath.write_text(json.dumps(grid_from_image(args.source),separators=(',',':'))+'\n')
grid=json.loads(gridpath.read_text());CORE=grid_paths(grid)
# Avatar: geometry sits inside a generous circular-crop safe field.
a=core(250,250,460)
write_static_and_animated('avatar',500,500,'Rezwan pixel energy core',a,signal_dot(250,250,232,'avatar-signal',7),'Original amber and cream pixel energy core with violet arcs. Two signal markers orbit every twelve seconds. Reduced motion keeps the complete static emblem.')
# Banner: a strong typographic block with a single fixed emblem and signal orbit.
b=''.join([
 text('Mohammad',64,121,64),text('Rezwan Khan',64,195,64),
 text('Battery insight. Engineering evidence.',66,261,25,font='body'),text('Grid impact.',66,296,25,font='body'),
 line('M66 334H650',LINE,1),text('MATLAB  ·  Python  ·  BESS',66,375,21,fill=MUTED,font='body'),
 line('M740 213H815M1205 213H1250',VIOLET,2),
 f'<circle cx="1010" cy="213" r="196" stroke="{LINE}" stroke-width="1" fill="none"/>',core(1010,213,370)])
write_static_and_animated('profile-banner',1280,426,'Mohammad Rezwan Khan — battery insight, engineering evidence, grid impact',b,signal_dot(1010,213,196,'banner-signal',7),'Mohammad Rezwan Khan. Battery insight. Engineering evidence. Grid impact. MATLAB, Python, BESS. Original pixel core with a restrained infinite signal orbit.')
# Social preview uses a spacious 2:1 poster composition; text is outlined for reproducibility.
s=''.join([text('Mohammad',64,157,74),text('Rezwan Khan',64,243,74),
 text('Battery insight.',66,331,29,font='body'),text('Engineering evidence.',66,371,29,font='body'),text('Grid impact.',66,411,29,font='body'),
 line('M66 495H1214',LINE,1),text('MATLAB  ·  Python  ·  BESS',66,554,24,fill=MUTED,font='body'),
 text('ENERGY SYSTEMS / RESEARCH & PRACTICE',66,590,14,fill=MUTED,font='body',tracking=1.3),
 f'<circle cx="1010" cy="280" r="200" stroke="{LINE}" stroke-width="1" fill="none"/>',core(1010,280,380)])
# Share same CSS orbit but set the dedicated center with a narrow override.
signal=signal_dot(1010,280,200,'social-signal',8)
socialcss='<style>.social-signal{transform-origin:1010px 280px;animation:social-orbit 12s linear infinite}@keyframes social-orbit{to{transform:rotate(360deg)}}@media(prefers-reduced-motion:reduce){.social-signal{animation:none!important}}</style>'
(OUT/'social-preview.svg').write_text(svg(1280,640,'Mohammad Rezwan Khan — energy systems',socialcss+s+signal,False,'Battery insight. Engineering evidence. Grid impact. MATLAB, Python, BESS. Infinite signal orbit with a reduced-motion static version.'))
(OUT/'social-preview-static.svg').write_text(svg(1280,640,'Mohammad Rezwan Khan — energy systems',s+signal,False))
for slug,lines,tagline,discipline,kind in REPOS:
 maxsize=70 if len(lines)>1 else 96
 size=min(maxsize,680/max(text_width(v,1) for v in lines))
 y0=208 if len(lines)>1 else 263
 content=''.join([text('Mohammad Rezwan Khan',64,67,24,fill=MUTED,font='body'),line('M64 101H1216',LINE,1)])
 for i,v in enumerate(lines):content+=text(v,64,y0+i*(size+16),size)
 content+=text(tagline,66,390,29,font='body')
 content+=poster_motif(kind)
 content+=line('M64 502H1216',LINE,1)
 # Canonical repository name is present verbatim, without ungrounded metrics.
 content+=text(slug,66,556,21,fill=CREAM,font='body')+text(discipline,66,595,14,fill=MUTED,font='body',tracking=2)
 (OUT/'social'/f'{slug}.svg').write_text(svg(1280,640,slug,content,False,f'{slug}. {tagline} An original abstract energy-system motif, not a data plot.'))
make_avatar_gif(grid)
node=os.environ.get('CODEX_PRIMARY_RUNTIME_NODE','/opt/codex/runtimes/codex-primary-runtime/dependencies/node/bin/node')
subprocess.run([node,str(HERE/'render.mjs')],check=True,cwd=ROOT)
make_banner_gif();manifest()
print(json.dumps([{'file':str(p.relative_to(ROOT)),'bytes':p.stat().st_size} for p in sorted(OUT.rglob('*')) if p.is_file()],indent=2))
