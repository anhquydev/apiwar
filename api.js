// Full Node.js API download video/image from multiple platforms

const express = require('express');
const { exec } = require('child_process');
const cors = require('cors');
const app = express();

app.use(cors());

app.get('/down', async (req, res) => {
  const url = req.query.url;
  if (!url) return res.status(400).json({ error: 'Thiếu tham số url' });

  const detected = detectPlatform(url);
  if (!detected) return res.status(400).json({ error: 'Không hỗ trợ nền tảng này' });

  // Dùng yt-dlp để xử lý tải video từ nhiều nền tảng
  exec(`yt-dlp -j "${url}"`, (err, stdout, stderr) => {
    if (err) return res.status(500).json({ error: 'Lỗi khi tải video', detail: stderr });

    try {
      const info = JSON.parse(stdout);

      let video_url = info.url || (info.requested_downloads?.[0]?.url ?? null);
      let title = info.title || info.description || 'No title';
      let thumbnail = info.thumbnail || null;
      let duration = info.duration;
      let uploader = info.uploader || info.channel || info.author || null;

      return res.json({
        status: true,
        platform: detected,
        title,
        thumbnail,
        duration,
        uploader,
        video_url,
        formats: info.formats?.map(f => ({
          quality: f.format_note,
          ext: f.ext,
          size: f.filesize,
          url: f.url
        })) || []
      });
    } catch (e) {
      return res.status(500).json({ error: 'Phân tích JSON thất bại', detail: e.message });
    }
  });
});

function detectPlatform(url) {
  if (url.includes('tiktok.com')) return 'tiktok';
  if (url.includes('youtube.com') || url.includes('youtu.be')) return 'youtube';
  if (url.includes('facebook.com') || url.includes('fb.watch')) return 'facebook';
  if (url.includes('instagram.com')) return 'instagram';
  if (url.includes('twitter.com') || url.includes('x.com')) return 'twitter';
  if (url.includes('capcut.com')) return 'capcut';
  if (url.includes('douyin.com')) return 'douyin';
  if (url.includes('pinterest.com')) return 'pinterest';
  return null;
}

app.listen(3000, () => console.log('API video downloader đang chạy tại http://localhost:3000/down?url=...'));
