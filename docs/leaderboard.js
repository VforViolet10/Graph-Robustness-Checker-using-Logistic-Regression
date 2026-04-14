document.addEventListener('DOMContentLoaded', function () {

    fetch('leaderboard.csv')
        .then(response => {
            if (!response.ok) throw new Error("CSV not found");
            return response.text();
        })
        .then(csvText => {

            const rows = csvText.trim().split('\n').slice(1);

            let data = rows
                .map(row => row.split(','))
                .filter(cols => cols.length >= 5)
                .map(cols => ({
                    team: cols[1],
                    f1Ideal: parseFloat(cols[2]),
                    f1Pert: parseFloat(cols[3]),
                    gap: parseFloat(cols[4])
                }))
                .filter(d => !isNaN(d.gap));

            // SORT (important)
            data.sort((a, b) => a.gap - b.gap);

            const tbody = document.getElementById('table-body'); // FIXED
            tbody.innerHTML = '';

            data.forEach((entry, index) => {

                const rank = index + 1;

                const medal =
                    rank === 1 ? '🥇' :
                    rank === 2 ? '🥈' :
                    rank === 3 ? '🥉' : rank;

                const tr = document.createElement('tr');

                tr.innerHTML = `
                    <td>${medal}</td>
                    <td>${entry.team}</td>
                    <td>${entry.f1Ideal.toFixed(3)}</td>
                    <td>${entry.f1Pert.toFixed(3)}</td>
                    <td>${entry.gap.toFixed(3)}</td>
                `;

                tbody.appendChild(tr);
            });

        })
        .catch(err => {
            console.error(err);
            document.getElementById('table-body').innerHTML =
                `<tr><td colspan="5">⚠️ Failed to load leaderboard</td></tr>`;
        });
});
