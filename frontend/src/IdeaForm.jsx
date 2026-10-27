import { useState } from "react";

function IdeaForm({ onAddIdea }) {
  const [title, setTitle] = useState("");
  const [category, setCategory] = useState("");
  const [saving, setSaving] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  async function handleSubmit(event) {
    event.preventDefault();
    if (saving) return;

    if (!title.trim()) {
      setError("Please enter a valid idea title.");
      setSuccess("");
      return;
    }

    setSaving(true);
    setError("");
    setSuccess("");

    try {
      await onAddIdea({
        title: title.trim(),
        category: category.trim(),
      });

      setTitle("");
      setCategory("");
      setSuccess("Idea added successfully!");
    } catch (err) {
      setError(err.message || "Failed to save idea.");
    } finally {
      setSaving(false);
    }
  }

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add a New Idea</h2>

      <div>
        <label htmlFor="idea-title">Title:</label>
        <input
          id="idea-title"
          type="text"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
        />
      </div>

      <div>
        <label htmlFor="idea-category">Category:</label>
        <input
          id="idea-category"
          type="text"
          value={category}
          onChange={(e) => setCategory(e.target.value)}
        />
      </div>

      <button type="submit" disabled={saving}>
        {saving ? "Saving..." : "Add Idea"}
      </button>

      {error && <p role="alert">{error}</p>}
      {success && <p role="status">{success}</p>}
    </form>
  );
}

export default IdeaForm;
