// Send text message
export async function sendMessage(message) {
  const res = await fetch("http://127.0.0.1:8000/chat/", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message }),
  });

  if (!res.ok) {
    throw new Error("Server error: " + (await res.text()));
  }
  return await res.json();
}

// Send image file
export async function sendImage(formData) {
  const res = await fetch("http://127.0.0.1:8000/upload-image/", {
    method: "POST",
    body: formData,     // <-- no JSON headers!
  });

  if (!res.ok) {
    throw new Error("Server error: " + (await res.text()));
  }
  return await res.json();
}
