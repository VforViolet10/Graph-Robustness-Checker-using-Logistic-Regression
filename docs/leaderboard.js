document.addEventListener('DOMContentLoaded', function () {

    fetch('leaderboard.csv')
        .then(response => {
            if (!response.ok) throw new Error("File not found");
            return response.text();
        })
        .then(csvText => {

            const rows = csvText.trim().split('\n');
            const dataRows = rows.slice(1);

            // Parse safely
            let data = dataRows
                .map(row => {
                    const cols = row.split(',');

                    if (cols.length < 5) return null;

                    return {
                        team: cols[1],
                        f1Ideal: parseFloat(cols[2]),
                        f1Pert: parseFloat(cols[3]),
                        gap: parseFloat(cols[4])
                    };
                })
                .filter(d => d !== null && !isNaN(d.gap));

            // ✅ Sort by robustness gap (LOWER = BETTER)
            data.sort((a, b) => a.gap - b.gap);

            // Last updated
            const now = new Date();
            const updatedEl = document.getElementById('last-updated');
            if (updatedEl) {
                updatedEl.textContent = "Last updated: " + now.toLocaleString();
            }

            const tbody = document.getElementById('table-body');
            tbody.innerHTML = '';

            data.forEach((entry, index) => {

                const rank = index + 1;

                let rankDisplay =
                    rank === 1 ? '🥇 1' :
                    rank === 2 ? '🥈 2' :
                    rank === 3 ? '🥉 3' : rank;

                const tr = document.createElement('tr');

                tr.innerHTML = `
                    <td class="rank">${rankDisplay}</td>
                    <td class="team-name">${entry.team}</td>
                    <td class="score primary-score">${entry.f1Ideal.toFixed(4)}</td>
                    <td class="score primary-score">${entry.f1Pert.toFixed(4)}</td>
                    <td class="score">${entry.gap.toFixed(4)}</td>
                `;

                tbody.appendChild(tr);
            });

            // If no data
            if (data.length === 0) {
                tbody.innerHTML =
                    `<tr><td colspan="5" class="empty">No data available</td></tr>`;
            }

        })
        .catch(error => {
            console.error(error);
            document.getElementById('table-body').innerHTML =
                `<tr><td colspan="5" class="empty">⚠️ Error loading leaderboard</td></tr>`;
        });
});
