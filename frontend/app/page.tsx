import ReviewPanel from "./review-panel";
export default function Home() {
  return <main className="shell">
    <div className="top"><span className="logo">⌘</span><span>CodePilot <strong>AI</strong></span><span className="pill">Prototype</span></div>
    <section className="hero"><p className="eyebrow">DEVELOPER WORKSPACE · EARLY PREVIEW</p><h1>Review code with more clarity.</h1><p>Run local heuristic checks and optionally request Gemini feedback when the backend has been configured. Always verify suggestions before applying them.</p></section>
    <ReviewPanel/><footer>CodePilot AI · Prototype stage · Not a security audit</footer>
  </main>;
}
