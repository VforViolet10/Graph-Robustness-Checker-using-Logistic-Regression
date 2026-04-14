function loadData(file, element = null) {

    fetch(file)
        .then(res => {
            if (!res.ok) throw new Error("CSV not found");
            return res.text();
        })
        .then(text => {

            const rows = text.trim().split("\n").slice(1);

            const data = rows
                .map(r => r.split(","))
                .filter(r => r.length >= 5)
                .map(r => ({
                    team: r[1],
                    f1Ideal: parseFloat(r[2]),
                    f1Pert: parseFloat(r[3]),
                    gap: parseFloat(r[4])
                }))
                .filter(d => !isNaN(d.gap));

            // ✅ Sort by robustness gap (LOWER is better)
            data.sort((a, b) => a.gap - b.gap);

            const tbody = document.getElementById("table-body");

            if (!tbody) {
                console.error("❌ table-body not found in HTML");
                return;
            }

            tbody.innerHTML = "";

            data.forEach((entry, i) => {

                const rank = i + 1;

                const medal =
                    rank === 1 ? "🥇" :
                    rank === 2 ? "🥈" :
                    rank === 3 ? "🥉" : rank;

                const tr = document.createElement("tr");

                tr.innerHTML = `
                    <td>${medal}</td>
                    <td>${entry.team}</td>
                    <td>${entry.f1Ideal.toFixed(3)}</td>
                    <td>${entry.f1Pert.toFixed(3)}</td>
                    <td>${entry.gap.toFixed(3)}</td>
                `;

                tbody.appendChild(tr);
            });

            // 🕒 Last updated time
            const now = new Date();
            const updatedEl = document.getElementById("last-updated");
            if (updatedEl) {
                updatedEl.textContent = "Last updated: " + now.toLocaleString();
            }

            // 🔄 Tab highlight
            document.querySelectorAll(".tab")
                .forEach(t => t.classList.remove("active"));

            if (element) element.classList.add("active");

        })
        .catch(err => {
            console.error(err);

            const tbody = document.getElementById("table-body");

            if (tbody) {
                tbody.innerHTML =
                    "<tr><td colspan='5'>⚠️ Failed to load leaderboard</td></tr>";
            }
        });
}

// 🚀 Load default leaderboard on page load
document.addEventListener("DOMContentLoaded", () => {
    loadData("leaderboard.csv");
});
