document.getElementById("spamForm").addEventListener("submit", async (e) => {
  e.preventDefault();
  const message = document.getElementById("message").value.trim();
  const resultDiv = document.getElementById("result");

  if (!message) {
    resultDiv.innerText = "⚠️ Please enter a message!";
    resultDiv.style.color = "red";
    return;
  }

  resultDiv.innerText = "⏳ Predicting...";
  resultDiv.style.color = "black";

  try {
    const response = await fetch("/predict", {
      method: "POST",
      body: new URLSearchParams({ message }),
      headers: {
        "Content-Type": "application/x-www-form-urlencoded",
      },
    });

    const data = await response.json();

    if (data.result === "spam") {
      resultDiv.innerText = "🚫 Spam Message";
      resultDiv.className = "spam";
    } else if (data.result === "not spam") {
      resultDiv.innerText = "✅ Not Spam";
      resultDiv.className = "ham";
    } else {
      resultDiv.innerText = "❌ Error: " + (data.message || "unknown");
      resultDiv.className = "";
      resultDiv.style.color = "red";
    }

  } catch (err) {
    resultDiv.innerText = "❌ Failed to connect to server";
    resultDiv.style.color = "red";
    console.error(err);
  }
});
