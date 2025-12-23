let uploadedFile = null;

function uploadAudio() {
  const fileInput = document.getElementById("audioFile");
  if (!fileInput.files.length) {
    alert("Please choose an audio file");
    return;
  }

  uploadedFile = fileInput.files[0];

  document.getElementById("loader").style.display = "block";

  const formData = new FormData();
  formData.append("file", uploadedFile);

  fetch("http://127.0.0.1:8000/upload-audio", {
    method: "POST",
    body: formData
  })
    .then(res => res.json())
    .then(data => {
  document.getElementById("uploadStatus").innerText =
    "✔ Audio uploaded successfully";
  analyzeAudio(data.filename);
})

    .catch(() => alert("Upload failed"));
}

function analyzeAudio(filename) {
  fetch(`http://127.0.0.1:8000/transcribe?filename=${filename}`, {
    method: "POST"
  })
    .then(res => res.json())
    .then(data => {
      document.getElementById("uploadSection").classList.add("hidden");
      document.getElementById("resultSection").classList.remove("hidden");

      document.getElementById("summaryText").innerText = data.summary;

      const bullets = document.getElementById("bulletPoints");
      bullets.innerHTML = "";
      data.bullet_points.forEach(p => {
        const li = document.createElement("li");
        li.textContent = p;
        bullets.appendChild(li);
      });

      const kwDiv = document.getElementById("keywords");
      kwDiv.innerHTML = "";
      data.keywords.forEach(k => {
        const span = document.createElement("span");
        span.textContent = k;
        kwDiv.appendChild(span);
      });

      document.getElementById("loader").style.display = "none";
    })
    .catch(() => alert("Analysis failed"));
}

function goBack() {
  location.reload();
}
