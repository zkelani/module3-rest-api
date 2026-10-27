import { describe, it, expect, vi } from "vitest";
import { render, screen, fireEvent } from "@testing-library/react";
import "@testing-library/jest-dom/vitest";
import IdeaForm from "./IdeaForm";

describe("IdeaForm validation tests", () => {
  it("shows an error when the title is empty", () => {
    const onAddIdea = vi.fn();
    render(<IdeaForm onAddIdea={onAddIdea} />);

    fireEvent.click(screen.getByRole("button", { name: "Add Idea" }));

    expect(screen.getByRole("alert")).toHaveTextContent(
      "Please enter a valid idea title."
    );
    expect(onAddIdea).not.toHaveBeenCalled();
  });

  it("submits a valid idea successfully", async () => {
    const onAddIdea = vi.fn().mockResolvedValue({});
    render(<IdeaForm onAddIdea={onAddIdea} />);

    fireEvent.change(screen.getByLabelText("Title:"), {
      target: { value: "Start a book club" },
    });

    fireEvent.change(screen.getByLabelText("Category:"), {
      target: { value: "Education" },
    });

    fireEvent.click(screen.getByRole("button", { name: "Add Idea" }));

    expect(await screen.findByRole("status")).toHaveTextContent(
      "Idea added successfully!"
    );

    expect(onAddIdea).toHaveBeenCalledWith({
      title: "Start a book club",
      category: "Education",
    });
  });

  it("displays an error when the API request fails", async () => {
    const onAddIdea = vi.fn().mockRejectedValue(
      new Error("Failed to connect to API")
    );

    render(<IdeaForm onAddIdea={onAddIdea} />);

    fireEvent.change(screen.getByLabelText("Title:"), {
      target: { value: "New campus idea" },
    });

    fireEvent.click(screen.getByRole("button", { name: "Add Idea" }));

    expect(await screen.findByRole("alert")).toHaveTextContent(
      "Failed to connect to API"
    );
  });
});