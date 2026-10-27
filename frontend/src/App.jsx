import { useEffect, useState } from "react";
import { getIdeas, createIdea } from "./api";
import IdeaList from "./IdeaList";
import IdeaForm from "./IdeaForm";
import "./App.css";

function App() {
  const [ideas, setIdeas] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");
  const [retryCount, setRetryCount] = useState(0);

  useEffect(() => {
    const controller = new AbortController();

    async function loadIdeas() {
      setLoading(true);
      setError("");

      try {
        const data = await getIdeas({
          signal: controller.signal,
        });

        if (!controller.signal.aborted) {
          setIdeas(data);
        }
      } catch (err) {
        if (!controller.signal.aborted) {
          setError("Failed to load ideas.");
        }
      } finally {
        if (!controller.signal.aborted) {
          setLoading(false);
        }
      }
    }

    loadIdeas();

    return () => controller.abort();
  }, [retryCount]);

  async function handleAddIdea(idea) {
    const newIdea = await createIdea(idea);
    setIdeas((previous) => [...previous, newIdea]);
  }

  return (
    <main>
      <h1>My Ideas App</h1>
      <p>Ideas loaded from my Python FastAPI backend</p>

      {loading && <p>Loading ideas...</p>}

      {error && (
        <div>
          <p role="alert">{error}</p>
          <button onClick={() => setRetryCount((n) => n + 1)}>
            Retry
          </button>
        </div>
      )}

      {!loading && !error && <IdeaList ideas={ideas} />}

      <IdeaForm onAddIdea={handleAddIdea} />
    </main>
  );
}

export default App;
