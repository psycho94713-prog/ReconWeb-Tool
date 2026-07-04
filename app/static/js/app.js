document.addEventListener("DOMContentLoaded", function () {

    console.log("app.js loaded");
 
    let pdfFilename = "";

    const scanBtn = document.getElementById("scanBtn");
    const downloadBtn = document.getElementById("downloadBtn"); 

    console.log(downloadBtn);

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
        document.getElementById("wayback").textContent = "Loading...";
        document.getElementById("sitemap").textContent = "Loading...";
        document.getElementById("security_txt").textContent = "Loading...";
        
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

            console.log(data);

            if (data.pdf_report) {

               pdfFilename = data.pdf_report.filename;

               console.log("PDF Filename:", pdfFilename);

               downloadBtn.disabled = false;

               alert("PDF Report Ready!");

}

            progress.style.width = "100%";
            progress.innerText = "Completed";

            document.getElementById("whois").innerHTML =
                formatObject(data.whois);

            document.getElementById("dns").innerHTML =
                formatObject(data.dns);

            document.getElementById("ssl").innerHTML =
                formatObject(data.ssl);

            document.getElementById("technology").innerHTML =
                formatTechnology(data.technology);

            document.getElementById("cms").innerHTML =
                formatObject(data.cms);

            document.getElementById("waf").innerHTML =
                formatObject(data.waf);

            document.getElementById("wayback").innerHTML =
                formatObject(data.wayback);

            document.getElementById("sitemap").innerHTML =
                formatObject(data.sitemap);

            document.getElementById("security_txt").innerHTML =
                formatObject(data.security_txt);

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

    downloadBtn.addEventListener("click", function () {

        console.log("Download button clicked");

    if (!pdfFilename) {
        alert("No PDF available.");
        return;
    }

    alert(pdfFilename);

window.open(`/api/v1/osint/download-report/${pdfFilename}`, "_blank");
    
});

});

function formatObject(obj) {

    if (!obj) {
        return "<span class='text-danger'>No Data</span>";
    }

    let html = "";

    for (const key in obj) {

        let value = obj[key];

        // Nested Object
        if (typeof value === "object" && value !== null) {

            value = `<pre>${JSON.stringify(value, null, 2)}</pre>`;

        }
        // Array
        else if (Array.isArray(value)) {

            value = value.join("<br>");

        }

        html += `
            <div class="mb-3">
                <strong>${key}</strong><br>
                ${value}
            </div>
        `;
    }

    return html;
}

function formatTechnology(data) {

    if (!data || data.status !== "success") {
        return "<span class='text-danger'>No Technology Detected</span>";
    }

    let html = "";

    html += `<b>Status:</b> ${data.status}<br>`;
    html += `<b>Count:</b> ${data.count}<br><br>`;

    html += "<b>Technologies</b><br>";

    data.technologies.forEach(function (tech) {

        html += `✅ ${tech}<br>`;

    });

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

        // =============================
// Dashboard Statistics
// =============================

document.getElementById("totalScans").innerText = result.data.length;

let totalScore = 0;
let bestGrade = "-";

result.data.forEach(scan => {

    totalScore += Number(scan.risk_score);

    if (bestGrade === "-") {
        bestGrade = scan.grade;
    }

    const grades = ["F", "D", "C", "B", "B+", "A", "A+"];

    if (
        grades.indexOf(scan.grade) >
        grades.indexOf(bestGrade)
    ) {
        bestGrade = scan.grade;
    }

});

if (result.data.length > 0) {

    document.getElementById("avgScore").innerText =
        Math.round(totalScore / result.data.length);

    document.getElementById("bestGrade").innerText =
        bestGrade;

    document.getElementById("lastScan").innerText =
        result.data[0].domain;

}

    } catch (error) {

        console.error("History Error:", error);

    }

}