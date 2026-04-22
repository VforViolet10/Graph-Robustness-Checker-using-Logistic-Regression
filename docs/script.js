<script>
// Utility function to prevent Cross-Site Scripting (XSS)
function escapeHTML(str) {
  if (str === null || str === undefined) return "";
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#039;");
}

async function loadLeaderboard() {
  try {
    const res = await fetch(
      "leaderboard.json?t=" + Date.now(),
      { cache: "no-store" }
    );

    if (!res.ok) {
      throw new Error("Could not load leaderboard.json");
    }

    const data = await res.json();
    const tbody = document.getElementById("leaderboard-body");

    if (!data || data.length === 0) {
      tbody.innerHTML = "<tr><td colspan='4'>No submissions yet</td></tr>";
      return;
    }

    // Safely sort descending (handling undefined/missing scores)
    data.sort((a, b) => {
      const scoreA = a.f1_score !== undefined ? Number(a.f1_score) : -Infinity;
      const scoreB = b.f1_score !== undefined ? Number(b.f1_score) : -Infinity;
      return scoreB - scoreA;
    });

    // Build the HTML string in memory first (Performance fix)
    let rowsHTML = "";

    data.forEach((entry, index) => {
      const medal = ["🥇", "🥈", "🥉"][index] || (index + 1);
      
      // Escape user-generated inputs
      const safeGroup = escapeHTML(entry.group || "Unknown");
      const safePR = escapeHTML(entry.pr || "-");
      const scoreDisplay = entry.f1_score !== undefined 
        ? Number(entry.f1_score).toFixed(4) 
        : "N/A";

      rowsHTML += `
      <tr>
        <td>${medal}</td>
        <td>${safeGroup}</td>
        <td>${scoreDisplay}</td>
        <td>#${safePR}</td>
      </tr>
      `;
    });

    // Update the DOM exactly once
    tbody.innerHTML = rowsHTML;

    document.getElementById("last-updated").innerText =
      "Last updated: " + new Date().toLocaleString();

  } catch(err) {
    console.error("Error loading leaderboard:", err);
    document.getElementById("leaderboard-body").innerHTML =
      "<tr><td colspan='4'>Error loading leaderboard</td></tr>";
  }
}

loadLeaderboard();
// Poll every 5 seconds
setInterval(loadLeaderboard, 5000);
</script>
