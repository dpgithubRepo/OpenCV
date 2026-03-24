# 📹 DIY AI CCTV Camera (YOLO + OpenCV + SMS Alerts)

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![OpenCV](https://img.shields.io/badge/OpenCV-Enabled-green)
![YOLOv8](https://img.shields.io/badge/YOLOv8-Ultralytics-orange)
![Status](https://img.shields.io/badge/Status-Working-success)
![License](https://img.shields.io/badge/License-MIT-lightgrey)

A simple yet powerful **AI-powered CCTV system** that uses a mobile phone as an IP camera and performs **real-time person detection** using YOLOv8. When a person is detected, the system sends an **SMS alert** using Twilio.

---

## 🚀 Features

- 📷 Live video streaming from mobile (IP Webcam)
- 🤖 Real-time person detection using YOLOv8
- 🟩 Bounding box visualization
- 🚨 Instant SMS alerts via Twilio
- ⏱ Cooldown mechanism to prevent spam alerts
- 💻 Lightweight (runs on CPU)
- 🔌 Plug-and-play with IP camera

---

## 🧠 System Architecture
Mobile Camera (IP Webcam)
↓
HTTP Stream (WiFi)
↓
OpenCV Video Capture
↓
YOLOv8 Detection (Person)
↓
Alert Logic (Cooldown)
↓
Twilio API → SMS Notification



---

## 🎥 Demo

> Add your demo video or GIF below

![Demo](images/demo.gif)



![SMS](images/sms.jpeg)
---

## 📁 Project Structure


diy-cctv-yolo/
│
├── diy_cctv_yolo.py # Main script
├── README.md
├── requirements.txt
└── demo.gif # Demo file (optional)


---

## ⚙️ Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-username/diy-cctv-yolo.git
cd diy-cctv-yolo
2. Install Dependencies
pip install -r requirements.txt

Or manually:

pip install opencv-python ultralytics twilio
📡 Setup IP Webcam
Install IP Webcam app on your phone
Start the server
Note the streaming URL:
http://<phone-ip>:8080/video
Ensure:
Phone & laptop are on same WiFi
Stream works in browser
🔐 Configure Twilio

Update credentials inside the script:

account_sid = "YOUR_ACCOUNT_SID"
auth_token = "YOUR_AUTH_TOKEN"
twilio_number = "+1234567890"
your_number = "+91XXXXXXXXXX"
▶️ Run the Project
python diy_cctv_yolo.py

Press q to exit.

🧠 Detection Logic
Uses pretrained model: yolov8n.pt
Detects only person class (class = 0)
SMS sent only when:
if person_detected and (current_time - last_sent_time > cooldown):
⚠️ Important Notes
Twilio trial account:
Only sends SMS to verified numbers
Adds trial prefix to messages
Keep cooldown enabled to avoid SMS spam 💸
Internet connection required for Twilio API
🔐 Security Best Practices

❌ Avoid hardcoding credentials:

account_sid = "..."
auth_token = "..."

✅ Use environment variables:

set TWILIO_SID=your_sid
set TWILIO_AUTH=your_auth_token
🔮 Future Enhancements
📸 Send image snapshot with alert
🧠 Face recognition (known vs unknown)
📊 People counting system
🌙 Night vision detection
📲 Telegram/Email alerts (free alternative)
☁️ Cloud logging and dashboard
🐞 Known Issues
HTTP stream may lag depending on network
High CPU usage on low-end machines
SMS delay depends on network & Twilio
🙌 Acknowledgements
Ultralytics YOLOv8
OpenCV
Twilio
📜 License

This project is licensed under the MIT License.

⭐ Support

If you found this useful, please give it a ⭐ on GitHub!
