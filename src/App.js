import { useState } from 'react';
import { Mic, Send, Upload, Loader2 } from 'lucide-react';
import { askLLM } from './lib/api';

export default function App() {
  const [input, setInput] = useState('');
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);

  async function handleSend() {
    const q = input.trim();
    if (!q) return;
    const mine = { role: 'user', text: q };
    setMessages((m) => [...m, mine]);
    setInput('');
    setLoading(true);
    try {
      const data = await askLLM(q);
      const bot = { role: 'assistant', text: data?.answer || 'No response.' };
      setMessages((m) => [...m, bot]);
    } catch (e) {
      setMessages((m) => [
        ...m,
        { role: 'assistant', text: '⚠️ Could not reach backend.' },
      ]);
    } finally {
      setLoading(false);
    }
  }

  function onKeyDown(e) {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault();
      handleSend();
    }
  }

  return (
    <div className="min-h-screen bg-gradient-to-b from-[#0b1223] to-[#0a0f1a] text-white flex flex-col items-center p-6">
      {/* Header */}
      <header className="w-full max-w-4xl flex items-center justify-between mb-6">
        <div className="flex items-center gap-3">
          <div className="w-9 h-9 rounded-xl bg-cyan-500/20 border border-cyan-400/40 grid place-items-center">
            <span className="font-bold text-cyan-300">S</span>
          </div>
          <div>
            <h1 className="text-2xl font-bold tracking-wide text-cyan-300">
              SochGPT
            </h1>
            <p className="text-xs text-gray-400 -mt-1">Private LLM</p>
          </div>
        </div>
        <div className="text-xs text-gray-400">v0.1 • Local Only</div>
      </header>

      {/* Chat */}
      <main className="w-full max-w-4xl flex-1 bg-[#101827]/70 rounded-2xl border border-white/10 shadow-xl p-4 overflow-y-auto space-y-3">
        {messages.length === 0 && (
          <div className="text-center text-gray-400 mt-16">
            <p className="text-lg">Ask about your projects, policies, or docs.</p>
            <p className="text-sm opacity-70">Connected to localhost:8000</p>
          </div>
        )}
        {messages.map((m, i) => (
          <div
            key={i}
            className={`max-w-[85%] p-3 rounded-2xl ${
              m.role === 'user'
                ? 'ml-auto bg-cyan-600/80'
                : 'mr-auto bg-white/5 border border-white/10'
            }`}
          >
            {m.text}
          </div>
        ))}
        {loading && (
          <div className="flex items-center gap-2 text-gray-400">
            <Loader2 className="w-4 h-4 animate-spin" />
            <span>Thinking…</span>
          </div>
        )}
      </main>

      {/* Input */}
      <div className="w-full max-w-4xl mt-4 flex items-center gap-2">
        <button
          className="p-3 rounded-xl bg-white/5 border border-white/10 hover:bg-white/10 transition"
          title="Upload (coming soon)"
        >
          <Upload className="w-5 h-5 text-gray-300" />
        </button>
        <div className="flex-1 flex items-center bg-white/5 border border-white/10 rounded-2xl px-3">
          <textarea
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={onKeyDown}
            rows={1}
            placeholder="Type your message… (Enter to send)"
            className="w-full bg-transparent outline-none text-white resize-none py-3"
          />
        </div>
        <button
          className="p-3 rounded-xl bg-white/5 border border-white/10 hover:bg-white/10 transition"
          title="Speak (coming soon)"
        >
          <Mic className="w-5 h-5 text-gray-300" />
        </button>
        <button
          onClick={handleSend}
          className="px-4 py-3 rounded-2xl bg-cyan-600 hover:bg-cyan-500 transition font-medium"
        >
          <Send className="w-4 h-4 inline-block mr-1" />
          Send
        </button>
      </div>

      {/* Footer */}
      <footer className="w-full max-w-4xl text-center text-xs text-gray-500 mt-4">
        © {new Date().getFullYear()} Sumeet’s Intelligence Lab • Privacy-First AI
      </footer>
    </div>
  );
}