async function askAI() {
  const prompt = document.getElementById("userPrompt").value;
  const resBox = document.getElementById("aiResponse");

  resBox.textContent = "Thinking...";

  const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
    method: "POST",
    headers: {
      "Authorization": "Bearer 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",
      "Content-Type": "application/json"
    },
    body: JSON.stringify({
      model: "openai/gpt-3.5-turbo",
      messages: [
        { role: "system", content: "You are a helpful assistant who outputs prompts users can paste into Power BI Q&A visual." },
        { role: "user", content: prompt }
      ]
    })
  });

  const data = await response.json();
  resBox.textContent = data.choices[0].message.content;
}