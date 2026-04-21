async function loadLeaderboard() {
try {
const res = await fetch("leaderboard.json?t=" + Date.now());
const data = await res.json();

```
// Sort descending
data.sort((a, b) => b.f1_score - a.f1_score);

const tbody = document.getElementById("leaderboard-body");
tbody.innerHTML = "";

data.forEach((entry, index) => {
  const medal = ["🥇", "🥈", "🥉"][index] || (index + 1);

  const row = `
    <tr>
      <td>${medal}</td>
      <td>${entry.group}</td>
      <td>${entry.f1_score.toFixed(4)}</td>
      <td>#${entry.pr || "-"}</td>
    </tr>
  `;
  tbody.innerHTML += row;
});

document.getElementById("last-updated").innerText =
  "Last updated: " + new Date().toLocaleString();
```

} catch (err) {
console.error("Error loading leaderboard:", err);
}
}

// Refresh every 5 sec
setInterval(loadLeaderboard, 5000);
loadLeaderboard();
