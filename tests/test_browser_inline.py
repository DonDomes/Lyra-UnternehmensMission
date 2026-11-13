import json, pathlib
from playwright.sync_api import sync_playwright
root=pathlib.Path(__file__).resolve().parents[1]
src=root/'src'
report_dir=root/'build-test-output'
report_dir.mkdir(exist_ok=True)
url='inline-content (browser restrictions on local navigation)'
data=json.loads((src/'rewe1-mission.json').read_text())
tasks=[t for c in data['chapters'] for t in c['tasks']]
js=r'''(t)=>{
 const $=(s)=>document.querySelector(s);
 const ensure=(cond,msg)=>{if(!cond)throw new Error(msg)};
 const card=$('.taskcard');ensure(card, 'task card missing');ensure(card.dataset.task===t.id,`current ${card.dataset.task}, expected ${t.id}`);
 if(t.type==='inspect'){
  for(const e of t.evidence){ const b=$(`[data-act="evidence"][data-id="${e.id}"]`);ensure(b,'evidence missing '+e.id);b.click();
    const close=$('#modal [data-act="close"]');ensure(close,'modal close missing');close.click();
  }
 } else if(t.type==='dialogue'){
  $(`[data-act="dialogue"][data-id="${t.solution.choice}"]`).click();const c=$('[data-read]');ensure(c,'dialogue read missing');c.checked=true;c.dispatchEvent(new Event('change',{bubbles:true}));
 } else if(t.type==='single'){
   const c=$(`[data-choice="${t.solution}"]`);ensure(c,'single option missing');c.checked=true;c.dispatchEvent(new Event('change',{bubbles:true}));
 } else if(t.type==='multi'){
   for(const id of t.solution){const c=$(`[data-choice="${id}"]`);ensure(c,'multi option missing '+id);c.checked=true;c.dispatchEvent(new Event('change',{bubbles:true}));}
 } else if(t.type==='numbers'){
   for(const f of t.fields){const inp=$(`[data-number="${f.id}"]`);ensure(inp,'number missing');inp.value=t.solution[f.id];inp.dispatchEvent(new Event('input',{bubbles:true}));}
 } else if(t.type==='match'){
   for(const p of t.pairs){const sel=$(`[data-match="${p.id}"]`);ensure(sel,'match missing');sel.value=t.solution[p.id];sel.dispatchEvent(new Event('change',{bubbles:true}));}
 } else if(t.type==='order'){
   for(let i=0;i<t.order.length;i++){
     const goal=t.items.find(x=>x.id===t.order[i]).text;
     let current=[...document.querySelectorAll('.order-list li span')].findIndex(x=>x.textContent===goal);
     ensure(current>=i,'order target missing '+goal);
     while(current>i){const b=$(`[data-act="order"][data-index="${current}"][data-direction="-1"]`);ensure(b,'order move missing');b.click();current--;}
   }
 } else if(t.type==='reflect'){
   const box=$('[data-reflect]');ensure(box,'reflection missing');box.value=t.solution;box.dispatchEvent(new Event('input',{bubbles:true}));
 } else if(t.type==='portfolio'){
   for(const id of t.required){const box=$(`[data-portfolio="${id}"]`);ensure(box,'portfolio missing');box.checked=true;box.dispatchEvent(new Event('change',{bubbles:true}));}
 }
 ensure(!document.body.innerText.includes('Musterlösung:') || document.getElementById('modal').open===true,'solution leaked before completion');
 const submit=$('[data-act="submit"]');ensure(submit,'submit missing');submit.click();
 return {id:t.id,next:document.querySelector('.taskcard')?.dataset.task||null,status:document.querySelector('.status')?.textContent||null,progress:document.querySelector('[role="progressbar"]')?.getAttribute('aria-valuenow')};
}'''
with sync_playwright() as p:
 b=p.chromium.launch(executable_path='/usr/bin/chromium',headless=True,args=['--no-sandbox','--disable-dev-shm-usage','--disable-gpu'])
 page=b.new_page(viewport={'width':1440,'height':960},accept_downloads=True)
 errors=[]
 page.on('pageerror',lambda e: errors.append(str(e)))
 page.set_content((root/'dist/LYRA_UnternehmensMission_ReWe1_BueroWerk_SKR04_2026_v1.html').read_text(),wait_until='load',timeout=25000)
 assert 'BüroWerk' in page.locator('#app').inner_text(),page.locator('#app').inner_text()[:200]
 assert '72' in page.locator('#app').inner_text()
 page.locator('[data-act="theme"][data-id="adventure"]').click()
 assert page.locator('body').get_attribute('data-theme')=='adventure'
 page.locator('[data-act="theme"][data-id="studio"]').click()
 page.locator('[data-act="theme"][data-id="cartoon"]').click()
 page.locator('[data-act="start"]').click()
 page.locator('#player-name').fill('Testteilnehmer')
 page.locator('[data-act="begin"]').click()
 assert page.locator('[data-task="ankunft-01"]').count()==1
 page.screenshot(path=str(report_dir/'rewe1-game-start.png'),full_page=True)
 for i,t in enumerate(tasks):
  result=page.evaluate(js,t)
  if i<71: assert result['next']==tasks[i+1]['id'],(i,result)
  else: assert result['next']==t['id'],(i,result)
  if i in (7,31,55):
   page.screenshot(path=str(report_dir/f'rewe1-game-step{i+1}.png'),full_page=True)
 assert page.locator('[data-act="finish"]').count()==1,'finish button missing'
 assert page.locator('[role="progressbar"]').get_attribute('aria-valuenow')=='72'
 assert page.locator('.review-row').count()==0, 'review must not be accessible before completion'
 page.locator('[data-act="finish"]').click()
 assert 'Alle 72 Schritte' in page.locator('#modal').inner_text()
 page.locator('[data-act="finish-confirm"]').click()
 report=page.locator('#app').inner_text()
 assert '352' in report,report[:300]
 assert page.locator('.review-row').count()==72
 page.locator('.review-row').nth(4).locator('summary').click()
 assert 'Musterlösung / erwartete Zuordnung' in page.locator('.review-row').nth(4).inner_text()
 page.screenshot(path=str(report_dir/'rewe1-game-report.png'),full_page=True)
 assert not errors,errors
 # Mobile view with loaded completed state
 page.set_viewport_size({'width':390,'height':820})
 assert 'Besprechung' in page.locator('#app').inner_text()
 page.screenshot(path=str(report_dir/'rewe1-game-mobile.png'),full_page=True)
 print(json.dumps({'passed':True,'file':url,'steps':len(tasks),'maxPoints':352,'noPageErrors':len(errors)==0,'mobileLayout':True,'persistReload':'not_verified','screenshots':5},ensure_ascii=False))
 b.close()
