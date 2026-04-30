const API_BASE_URL = "http://127.0.0.1:8000";

export async function synthesizeAudio(file) {
  const formData = new FormData();
  formData.append("file", file);

  const response = await fetch(`${API_BASE_URL}/synthesize`, {
    method: "POST",
    body: formData
  });

  if (!response.ok) {
    let detail = "音声生成に失敗しました。";

    try {
      const data = await response.json();
      if (typeof data?.detail === "string") {
        detail = data.detail;
      }
    } catch {
      // JSONで返ってこない場合はデフォルト文言のままにする
    }

    throw new Error(detail);
  }

  return response.blob();
}
