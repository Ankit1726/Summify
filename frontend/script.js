// Point this at your FastAPI backend. If the frontend is served BY the
// FastAPI app itself, "" (same origin) is correct and you can leave it.
const API_BASE_URL = "";

const form = document.getElementById("summarization-form");
const dialogueInput = document.getElementById("dialogue-input");
const charCount = document.getElementById("char-count");
const submitBtn = document.getElementById("submit-btn");
const clearBtn = document.getElementById("clear-btn");
const copyBtn = document.getElementById("copy-btn");
const outputPlaceholder = document.getElementById("output-placeholder");
const summaryText = document.getElementById("summary-text");

function updateCharCount() {
  const count = dialogueInput.value.length;
  charCount.textContent = `${count.toLocaleString()} character${count === 1 ? "" : "s"}`;
}

function setLoading(isLoading) {
  submitBtn.classList.toggle("is-loading", isLoading);
  submitBtn.disabled = isLoading;
}

function showSummary(text, isError = false) {
  outputPlaceholder.style.display = "none";
  summaryText.textContent = text;
  summaryText.classList.toggle("is-error", isError);
  // restart the reveal animation
  summaryText.classList.remove("is-visible");
  // force reflow so the transition re-triggers
  void summaryText.offsetWidth;
  summaryText.classList.add("is-visible");
}

function resetOutput() {
  summaryText.textContent = "";
  summaryText.classList.remove("is-visible", "is-error");
  outputPlaceholder.style.display = "block";
}

dialogueInput.addEventListener("input", updateCharCount);
updateCharCount();

form.addEventListener("submit", async (e) => {
  e.preventDefault();

  const dialogue = dialogueInput.value.trim();
  if (!dialogue) return;

  setLoading(true);

  try {
    const response = await fetch(`${API_BASE_URL}/summarize/`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ dialogue }),
    });

    if (!response.ok) {
      throw new Error(`Server error: ${response.status}`);
    }

    const data = await response.json();
    showSummary(data.summary || "No summary returned.");
  } catch (err) {
    showSummary(`Something went wrong: ${err.message}`, true);
  } finally {
    setLoading(false);
  }
});

clearBtn.addEventListener("click", () => {
  dialogueInput.value = "";
  updateCharCount();
  resetOutput();
  dialogueInput.focus();
});

copyBtn.addEventListener("click", async () => {
  const text = summaryText.textContent.trim();
  if (!text) return;
  try {
    await navigator.clipboard.writeText(text);
    copyBtn.title = "Copied!";
    setTimeout(() => (copyBtn.title = "Copy summary"), 1500);
  } catch {
    /* clipboard API unavailable — silently ignore */
  }
});
