const API_URL = "http://localhost:8080/api/ideas";

export async function getIdeas({ signal } = {}) {
  const response = await fetch(API_URL, { signal });

  if (!response.ok) {
    throw new Error("Failed to load ideas.");
  }

  return response.json();
}

export async function createIdea(idea) {
  const response = await fetch(API_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(idea),
  });

  if (!response.ok) {
    throw new Error("Failed to create idea.");
  }

  return response.json();
}
