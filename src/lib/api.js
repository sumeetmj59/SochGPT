// sil-ui/src/lib/api.js

// Prefer CRA env, then Vite env, else empty (to use proxy/relative path)
const API_BASE =
  (typeof process !== 'undefined' && process.env && process.env.REACT_APP_API_BASE) ||
  (typeof import.meta !== 'undefined' && import.meta.env && import.meta.env.VITE_API_BASE) ||
  '';

export async function askLLM(query) {
  // If no API_BASE provided, use relative path so CRA dev proxy (or same-origin) can forward to backend
  if (!API_BASE) {
    const res = await fetch('/chat', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ query }),
    });
    if (!res.ok) throw new Error(`Proxy/relative API error: ${res.status}`);
    return await res.json();
  }

  // Direct to explicit backend URL
  const res = await fetch(`${API_BASE}/chat`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ query }),
  });
  if (!res.ok) throw new Error(`Backend error: ${res.status}`);
  return await res.json();
}