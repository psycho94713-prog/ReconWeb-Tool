document.addEventListener("DOMContentLoaded", function () {
    
    console.log("app.js loaded"); 
      
    const scanBtn = document.getElementById("scanBtn");

    scanBtn.addEventListener("click", async function () {

        console.log("Scan button clicked");

        const domain = document.getElementById("domain").value.trim();

        if (domain === "") {
            alert("Please enter a domain");
            return;
        }

        document.getElementById("whois").textContent = "Loading...";
        document.getElementById("dns").textContent = "Loading...";
        document.getElementById("ssl").textContent = "Loading...";
        document.getElementById("cms").textContent = "Loading...";
        document.getElementById("waf").textContent = "Loading...";

        try {
            
             console.log("Sending API request...");
            
             const response = await fetch("/api/v1/osint/domain", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    domain: domain
                })
            });
            
            console.log(response);
           
            const data = await response.json();

            console.log("API Response:", data);

            document.getElementById("whois").textContent =
                JSON.stringify(data.whois, null, 2);

            document.getElementById("dns").textContent =
                JSON.stringify(data.dns, null, 2);

            document.getElementById("ssl").textContent =
                JSON.stringify(data.ssl, null, 2);

            document.getElementById("cms").textContent =
                JSON.stringify(data.cms, null, 2);

            document.getElementById("waf").textContent =
                JSON.stringify(data.waf, null, 2);

        } catch (error) {
            console.error("JavaScript Error:", error);
            alert("JavaScript Error: " + error);
            }

    });

});