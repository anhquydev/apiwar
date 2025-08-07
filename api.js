const express = require("express");
const cors = require("cors");
const { exec } = require("child_process");

const app = express();
const port = process.env.PORT || 3000;

app.use(cors());

app.get("/down", (req, res) => {
  const videoUrl = req.query.url;
  if (!videoUrl) return res.status(400).json({ error: "Thiếu URL" });

  // Lệnh yt-dlp để lấy JSON info
  const command = `yt-dlp -j "${videoUrl}"`;

  exec(command, (err, stdout, stderr) => {
    if (err) {
      return res.status(500).json({ error: "Không thể tải video", detail: stderr });
    }

    try {
      const info = JSON.parse(stdout);
      const download = info.url || info.formats?.[0]?.url;
      res.json({
        title: info.title,
        thumbnail: info.thumbnail,
        duration: info.duration,
        download_url: download,
        formats: info.formats?.map(f => ({
          quality: f.format_note,
          ext: f.ext,
          url: f.url
        })),
        source: info.webpage_url,
        uploader: info.uploader
      });
    } catch (e) {
      res.status(500).json({ error: "Lỗi phân tích dữ liệu video" });
    }
  });
});

app.listen(port, () => {
  console.log(`API video downloader chạy tại http://localhost:${port}`);
});
