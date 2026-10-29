import { useEffect, useState } from "react";
import type { FormEvent } from "react";
import { api, errorMessage } from "./api";

type Hello = { message: string };
type Echo = { message: string; length: number };

export default function App() {
  const [hello, setHello] = useState<Hello | null>(null);
  const [draft, setDraft] = useState("");
  const [echo, setEcho] = useState<Echo | null>(null);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    // StrictMode runs effects twice in dev; aborting the first request keeps this safe.
    const controller = new AbortController();
    api<Hello>("/api/hello?name=Commure", { signal: controller.signal })
      .then(setHello)
      .catch((err) => {
        if (!controller.signal.aborted) setError(errorMessage(err));
      });
    return () => controller.abort();
  }, []);

  async function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError(null);
    try {
      const body = JSON.stringify({ message: draft });
      setEcho(await api<Echo>("/api/echo", { method: "POST", body }));
    } catch (err) {
      setEcho(null);
      setError(errorMessage(err));
    }
  }

  return (
    <main style={{ maxWidth: 640, margin: "40px auto", fontSize: 18 }}>
      <h1>Commure interview</h1>
      <p>GET /api/hello → {hello ? hello.message : "loading…"}</p>
      <form onSubmit={handleSubmit}>
        <input value={draft} onChange={(e) => setDraft(e.target.value)} placeholder="Type a message" />
        <button type="submit">POST /api/echo</button>
      </form>
      {echo && <p>Echoed “{echo.message}” ({echo.length} chars)</p>}
      {error && <p style={{ color: "crimson" }}>{error}</p>}
    </main>
  );
}