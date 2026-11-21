"use client";
import { useState } from "react";

type Finding = {rule:string;severity:string;line:number;message:string};
type Summary = {total:number;by_severity?:Record<string,number>};
type ReviewResult = {language:string;findings:Finding[];summary?:Summary;engine:string;ai_review?:unknown;ai_warning?:string;disclaimer?:string};
type HistoryEntry = {id:number;created_at:string;language:string;engine:string;finding_count:number;source_characters:number};
const API = process.env.NEXT_PUBLIC_API_URL || (process.env.NEXT_PUBLIC_VERCEL_URL ? "/api" : "http://localhost:8000");

export default function ReviewPanel() {
  const [token, setToken] = useState("");
  const authorization: Record<string, string> = token ? {Authorization: `Bearer ${token}`} : {};
  const [code,setCode] = useState("const answer = 42;");
  const [language,setLanguage] = useState("javascript");
  const [useAi,setUseAi] = useState(false);
  const [result,setResult] = useState<ReviewResult|null>(null);
  const [busy,setBusy] = useState(false);
  const [error,setError] = useState("");
  const [history, setHistory] = useState<HistoryEntry[] | null>(null);
  const [historyBusy, setHistoryBusy] = useState(false);
  const [historyError, setHistoryError] = useState("");

  async function loadHistory() {
    setHistoryBusy(true);
    setHistoryError("");
    try {
      const response = await fetch(API + "/reviews?limit=20", {
        cache: "no-store", headers: authorization, signal: AbortSignal.timeout(10000)
      });
      if (!response.ok) throw new Error(`History API returned HTTP ${response.status}.`);
      const data = await response.json();
      if (!Array.isArray(data.reviews)) throw new Error("Unexpected history response.");
      setHistory(data.reviews);
    } catch (err) {
      setHistoryError(err instanceof Error ? err.message : "Review history unavailable.");
    } finally {
      setHistoryBusy(false);
    }
  }

  async function runReview() {
    setBusy(true); setError(""); setResult(null);
    try {
      const response = await fetch(API + "/review", {
        method:"POST",headers:{"Content-Type":"application/json", ...authorization},
        body:JSON.stringify({language,code,use_ai:useAi}),signal:AbortSignal.timeout(30000)
      });
      if (!response.ok) throw new Error(response.status === 422 ? "Check language and source length (maximum 50,000 characters)." : `Review API returned HTTP ${response.status}.`);
      const data: ReviewResult = await response.json();
      if (!Array.isArray(data.findings) || typeof data.engine !== "string") throw new Error("Unexpected API response.");
      setResult(data);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Review failed. Check the backend connection.");
    } finally { setBusy(false); }
  }
  return <section className="review" aria-label="Code review workspace">
    <div className="reviewhead"><div><h2>Code review workspace</h2><p>Paste source code to get heuristic findings and optional Gemini feedback.</p></div><span className="counter">{code.length.toLocaleString()} / 50,000</span></div>
    <label htmlFor="review-token">Operator token (if configured)</label>
    <input id="review-token" type="password" value={token} onChange={event => setToken(event.target.value)} autoComplete="off" />
    <label htmlFor="language">Language</label>
    <select id="language" value={language} onChange={e=>setLanguage(e.target.value)}>
      <option value="javascript">JavaScript</option><option value="typescript">TypeScript</option><option value="python">Python</option>
    </select>
    <label htmlFor="source">Source code</label>
    <textarea id="source" spellCheck={false} value={code} onChange={e=>setCode(e.target.value)} aria-describedby="source-hint"/>
    <p id="source-hint">Your source is sent to the configured review backend. Enable AI only for code you are authorized to share with its provider.</p>
    <label className="toggle"><input type="checkbox" checked={useAi} onChange={e=>setUseAi(e.target.checked)}/> Request Gemini AI feedback (optional)</label>
    <button onClick={runReview} disabled={busy || !code.trim() || code.length > 50000}>{busy ? "Reviewing…" : "Run review"}</button>
    {error && <p role="alert" className="error">{error}</p>}
    {result && <div className="results" aria-live="polite">
      <h3>Review results</h3>
      <p>Engine: <strong>{result.engine}</strong> · {result.findings.length} local finding(s)</p>
      {result.ai_warning && <p className="warning">{result.ai_warning}</p>}
      {result.findings.length === 0 && <p>No local heuristic patterns matched. This does not establish that the code is safe.</p>}
      {result.findings.map((f,i)=><article className="finding" key={i}><strong>{f.severity.toUpperCase()} · line {f.line}</strong><p>{f.message}</p><small>{f.rule}</small></article>)}
      {result.ai_review != null && <div className="airesult"><h3>Gemini feedback</h3><pre>{typeof result.ai_review === "string" ? result.ai_review : JSON.stringify(result.ai_review,null,2)}</pre></div>}
      <p className="disclaimer">{result.disclaimer || "Review findings require human verification."}</p>
    </div>}
    <section className="results" aria-label="Review history">
      <h3>Review history</h3>
      <p>Recent review metadata includes language, engine, and finding count.</p>
      <button type="button" onClick={loadHistory} disabled={historyBusy}>
        {historyBusy ? "Loading history…" : history ? "Refresh history" : "Load history"}
      </button>
      {historyError && <p role="alert" className="error">{historyError}</p>}
      <div aria-live="polite">
        {history?.length === 0 && <p>No reviews have been saved.</p>}
        {history && history.length > 0 && <ol>
          {history.map(entry => <li key={entry.id}>
            <time dateTime={entry.created_at}>{new Date(entry.created_at).toLocaleString()}</time>
            {" · "}{entry.language}{" · "}{entry.engine}{" · "}{entry.finding_count} findings
          </li>)}
        </ol>}
      </div>
    </section>
  </section>;
}
