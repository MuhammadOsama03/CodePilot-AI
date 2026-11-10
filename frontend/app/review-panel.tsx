"use client";
import { useState } from "react";
type Finding = {rule:string;severity:string;line:number;message:string};
export default function ReviewPanel(){
 const [code,setCode]=useState("const answer = 42;");
 const [language,setLanguage]=useState("javascript");
 const [findings,setFindings]=useState<Finding[]>([]);
 const [status,setStatus]=useState("");
 async function runReview(){setStatus("Reviewing…");try{const response=await fetch((process.env.NEXT_PUBLIC_API_URL||"http://localhost:8000")+"/review",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify({language,code})});if(!response.ok)throw new Error("API request failed");const data=await response.json();setFindings(data.findings);setStatus("Local heuristic review complete — not an AI audit.");}catch{setStatus("Cannot reach the API. Start the FastAPI backend.");}}
 return <section className="review"><h2>Try a local review</h2><p>Early prototype: simple pattern-based hints only.</p><label htmlFor="language">Language</label><select id="language" value={language} onChange={e=>setLanguage(e.target.value)}><option value="javascript">JavaScript</option><option value="typescript">TypeScript</option><option value="python">Python</option></select><label htmlFor="source">Source code</label><textarea id="source" spellCheck={false} value={code} onChange={e=>setCode(e.target.value)}/><button onClick={runReview} disabled={!code.trim()}>Review code</button><p role="status">{status}</p>{findings.map((f,i)=><div className="finding" key={i}><strong>{f.severity.toUpperCase()} · line {f.line}</strong><p>{f.message}</p></div>)}</section>
}
