<script>
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
      tbody.innerHTML =
        "<tr><td colspan='4'>No submissions yet</td></tr>";
      return;
    }

    // Sort descending
    data.sort((a,b)=>b.f1_score-a.f1_score);

    tbody.innerHTML = "";

    data.forEach((entry,index)=>{
      const medal=["🥇","🥈","🥉"][index] || (index+1);

      tbody.innerHTML += `
      <tr>
        <td>${medal}</td>
        <td>${entry.group || "Unknown"}</td>
        <td>${
          entry.f1_score !== undefined
            ? Number(entry.f1_score).toFixed(4)
            : "N/A"
        }</td>
        <td>#${entry.pr || "-"}</td>
      </tr>
      `;
    });

    document.getElementById("last-updated").innerText =
      "Last updated: " + new Date().toLocaleString();

  } catch(err){
    console.error("Error loading leaderboard:", err);

    document.getElementById("leaderboard-body").innerHTML =
      "<tr><td colspan='4'>Error loading leaderboard</td></tr>";
  }
}

loadLeaderboard();
setInterval(loadLeaderboard, 5000);
</script>
