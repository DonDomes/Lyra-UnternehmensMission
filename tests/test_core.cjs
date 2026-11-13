const fs = require('fs'), assert=require('assert');
const html=fs.readFileSync(require('path').resolve(__dirname,'../dist/LYRA_UnternehmensMission_ReWe1_BueroWerk_SKR04_2026_v1.html'),'utf8');
const m=html.match(/<script id="mission-data" type="application\/json">([\s\S]*?)<\/script>/);
assert(m, 'JSON data script exists');
const D=JSON.parse(m[1]);
const js=html.match(/<script>\/\* BüroWerk: deterministic offline engine[\s\S]*?<\/script>/);
assert(js,'converted engine extract');
const vm = require('vm');const moduleObj={exports:{}};vm.runInNewContext(js[0].slice(8,-9),{module:moduleObj,globalThis:global},{timeout:1000});const C=moduleObj.exports;
assert.strictEqual(C.all(D).length,72);assert.strictEqual(D.chapters.length,9);
assert.strictEqual(new Set(C.all(D).map(t=>t.id)).size,72);
const state=C.newState(D,1234);state.started=true;state.avatar.name='Test';
let correctCount=0, max=D.chapters.reduce((s,c)=>s+c.tasks.reduce((v,t)=>v+t.points,0),0);
for(const t of C.all(D)) {
 let sol=t.solution;
 if(t.type==='inspect') sol=t.solution;
 if(t.type==='dialogue') sol=t.solution;
 if(t.type==='reflect') sol=t.solution;
 let g=C.grade(t,sol);
 assert(g.valid,`solution invalid ${t.id}: ${g.message}`);
 assert(Math.abs(g.earned-t.points)<.00001,`solution mismatch ${t.id}: ${g.earned} != ${t.points}`);
 let sub=C.submit(D,state,t,sol);assert(sub.ok,`submit failure ${t.id} ${sub.message}`);
 correctCount++;
}
assert.strictEqual(C.done(D,state),72);
assert(C.finish(D,state).ok);
const review=C.review(D,state);assert.strictEqual(review.maximum,max);assert.strictEqual(review.earned,max);assert.strictEqual(review.rows.length,72);
const exported=JSON.parse(JSON.stringify(state));const restored=C.restore(exported,D);assert(restored.ok);assert(restored.state.finished);assert.strictEqual(C.review(D,restored.state).earned,max);
const altered=JSON.parse(JSON.stringify(exported));altered.contentId='different';assert(!C.restore(altered,D).ok);
// Every graded type can produce partial points without negative deductions.
const types=[...new Set(C.all(D).map(t=>t.type))];
let partial=0;
for(const t of C.all(D)){
 if(t.points===0)continue;
 let candidate=null;
 if(t.type==='single'){candidate=t.options.find(o=>o.id!==t.correct).id;}
 if(t.type==='multi'){candidate=t.correct.slice(1).concat([t.options.find(o=>!t.correct.includes(o.id)).id]);}
 if(t.type==='numbers'){candidate={...t.solution,[t.fields[0].id]:String(t.fields[0].answer+666)};}
 if(t.type==='match'){candidate={...t.solution,[t.pairs[0].id]:t.categories.find(x=>x.id!==t.pairs[0].answer).id};}
 if(t.type==='order'){candidate=t.order.slice();[candidate[0],candidate[1]]=[candidate[1],candidate[0]];}
 if(t.type==='portfolio'){candidate=[t.items.find(x=>!t.required.includes(x.id)).id];}
 if(candidate){let g=C.grade(t,candidate);assert(g.valid,`variant invalid ${t.id}`);assert(g.earned>=0 && g.earned<=t.points);if(g.earned>0&&g.earned<t.points)partial++;}
}
assert(partial>=30,`expect partial cases, got ${partial}`);
// Numbers safety
for(const val of ['','1e3','Infinity','alert(1)','12,50,0','2+2'])assert.strictEqual(C.parseNumber(val),null);
assert.strictEqual(C.parseNumber('1.190,00'),1190);
assert.strictEqual(C.calculate('(120-80)*25'),1000);
assert.strictEqual(C.calculate('alert(1)'),null);
console.log(JSON.stringify({passed:true,chapters:D.chapters.length,tasks:correctCount,maxPoints:max,partialExamples:partial,types,bytes:Buffer.byteLength(html,'utf8')}));
