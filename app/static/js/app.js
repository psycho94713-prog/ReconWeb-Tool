document.addEventListener("DOMContentLoaded", function () {

    console.log("app.js loaded");

    const scanBtn = document.getElementById("scanBtn");

    // Dashboard open hote hi History load karo
    loadHistory();

    scanBtn.addEventListener("click", async function () {

        const progress = document.getElementById("progressBar");

        progress.style.width = "10%";
        progress.innerText = "Starting...";

        const domain = document.getElementById("domain").value.trim();

        if (domain === "") {
            alert("Please enter a domain");
            return;
        }

        document.getElementById("whois").textContent = "Loading...";
        document.getElementById("dns").textContent = "Loading...";
        document.getElementById("ssl").textContent = "Loading...";
        document.getElementById("technology").textContent = "Loading...";
        document.getElementById("cms").textContent = "Loading...";
        document.getElementById("waf").textContent = "Loading...";

        try {

            const response = await fetch("/api/v1/osint/domain", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    domain: domain
                })
            });

            const data = await response.json();

            progress.style.width = "100%";
            progress.innerText = "Completed";

            document.getElementById("whois").innerHTML =
                formatObject(data.whois);

            document.getElementById("dns").innerHTML =
                formatObject(data.dns);

            document.getElementById("ssl").innerHTML =
                formatObject(data.ssl);

            document.getElementById("technology").innerHTML =
                formatObject(data.technology);

            document.getElementById("cms").innerHTML =
                formatObject(data.cms);

            document.getElementById("waf").innerHTML =
                formatObject(data.waf);

            // Scan complete hone ke baad history refresh
            loadHistory();

        } catch (error) {

            progress.style.width = "100%";
            progress.classList.remove("progress-bar-animated");
            progress.classList.add("bg-danger");
            progress.innerText = "Failed";

            console.error(error);
            alert(error);

        }

    });

});


function formatObject(obj) {

    if (!obj) {
        return "<span class='text-danger'>No Data</span>";
    }

    let html = "";

    for (const key in obj) {

        html += `
            <div class="mb-2">
                <strong>${key}</strong><br>
                <span class="text-danger">${obj[key]}</span>
            </div>
        `;

    }

    return html;

}


async function loadHistory() {

    try {

        const response = await fetch("/api/v1/history/");

        const result = await response.json();

        const table = document.getElementById("historyTable");

        if (!table) return;

        table.innerHTML = "";

        if (result.data.length === 0) {

            table.innerHTML = `
                <tr>
                    <td colspan="5" class="text-center">
                        No Scan History
                    </td>
                </tr>
            `;

            return;
        }

        result.data.forEach(scan => {

            table.innerHTML += `
                <tr>
                    <td>${scan.id}</td>
                    <td>${scan.domain}</td>
                    <td>${scan.risk_score}</td>
                    <td>${scan.grade}</td>
                    <td>${scan.status}</td>
                </tr>
            `;

        });

    } catch (error) {

        console.error("History Error:", error);

    }

}