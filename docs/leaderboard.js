function loadData(file, element = null) {

    fetch("./" + file)  // ✅ FIXED PATH
        .then(res => {
            if (!res.ok) throw new Error("CSV not found: " + file);
            return res.text();
        })
        .then(text => {

            const rows = text.trim().split(/\r?\n/).slice(1);

            const data = rows
                .map(r => r.split(","))
                .filter(r => r.length >= 5)
                .map(r => ({
                   team: r[0],
                    f1Ideal: parseFloat(r[1]),
                    f1Pert: parseFloat(r[2]),
                    gap: parseFloat(r[3])
                }))
                .filter(d => !isNaN(d.gap));

            const tbody = document.getElementById("table-body");

            if (!tbody) {
                console.error("table-body not found");
                return;
            }

            tbody.innerHTML = "";

            if (data.length === 0) {
                tbody.innerHTML =
                    "<tr><td colspan='5'>⚠️ No data found</td></tr>";
                return;
            }

            // Sort by robustness gap (LOWER = BETTER)
            data.sort((a, b) => a.gap - b.gap);

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

            // Last updated
            const updated = document.getElementById("last-updated");
            if (updated) {
                updated.textContent =
                    "Last updated: " + new Date().toLocaleString();
            }

            // Tab highlight
            document.querySelectorAll(".tab")
                .forEach(t => t.classList.remove("active"));

            if (element) element.classList.add("active");

        })
        .catch(err => {
            console.error(err);

            document.getElementById("table-body").innerHTML =
                "<tr><td colspan='5'>❌ CSV NOT FOUND</td></tr>";
        });
}

// Load default
document.addEventListener("DOMContentLoaded", () => {
    loadData("leaderboard.csv");
});
