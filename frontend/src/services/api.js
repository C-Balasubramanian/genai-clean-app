const API_BASE_URL = process.env.REACT_APP_API_BASE_URL;

// Send text message
export async function sendMessage(message) {
  const res = await fetch(`${API_BASE_URL}/chat/`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ message }),
  });

  if (!res.ok) {
    throw new Error("Server error: " + (await res.text()));
  }

  return await res.json();
}

// Send image file
export async function sendImage(formData) {
  const res = await fetch(`${API_BASE_URL}/upload-image/`, {
    method: "POST",
    body: formData, // no headers
  });

  if (!res.ok) {
    throw new Error("Server error: " + (await res.text()));
  }

  return await res.json();
}
