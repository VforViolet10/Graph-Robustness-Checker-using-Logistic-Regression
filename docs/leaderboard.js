document.addEventListener("DOMContentLoaded", () => {

    fetch("./leaderboard.csv")
        .then(res => {
            if (!res.ok) throw new Error("CSV not found");
            return res.text();
        })
        .then(text => {

            const rows = text.trim().split(/\r?\n/).slice(1);

            const data = rows.map(r => {
                const cols = r.split(",");

                return {
                    team: cols[0],
                    f1Ideal: parseFloat(cols[1]),
                    f1Pert: parseFloat(cols[2]),
                    gap: parseFloat(cols[3])
                };
            });

            const tbody = document.getElementById("table-body");
            tbody.innerHTML = "";

            // SORT by gap
            data.sort((a, b) => a.gap - b.gap);

            data.forEach((d, i) => {

                const rank = i + 1;

                const medal =
                    rank === 1 ? "🥇" :
                    rank === 2 ? "🥈" :
                    rank === 3 ? "🥉" : rank;

                const tr = document.createElement("tr");

                tr.innerHTML = `
                    <td>${medal}</td>
                    <td>${d.team}</td>
                    <td>${d.f1Ideal.toFixed(3)}</td>
                    <td>${d.f1Pert.toFixed(3)}</td>
                    <td>${d.gap.toFixed(3)}</td>
                `;

                tbody.appendChild(tr);
            });

        })
        .catch(err => {
            console.error(err);
            document.getElementById("table-body").innerHTML =
                "<tr><td colspan='5'>❌ ERROR LOADING CSV</td></tr>";
        });
});
