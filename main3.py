from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

import os
import uvicorn

app = FastAPI()

# CORS settings
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/static", StaticFiles(directory="static"), name="static")
@app.get("/", response_class=HTMLResponse)
async def portfolio():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8" />
        <title>AB KAIUM – AI Portfolio</title>
        <link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;600&display=swap" rel="stylesheet">
        <style>
            * {
                box-sizing: border-box;
            }

            body {
                margin: 0;
                padding: 0;
                font-family: 'Space Grotesk', sans-serif;
                background: linear-gradient(-45deg, #1a1a2e, #16213e, #0f3460, #53354a);
                background-size: 400% 400%;
                animation: gradientAI 15s ease infinite;
                color: #f1f1f1;
                overflow-x: hidden;
            }

            @keyframes gradientAI {
                0% { background-position: 0% 50%; }
                50% { background-position: 100% 50%; }
                100% { background-position: 0% 50%; }
            }

            .ai-float {
                position: fixed;
                top: 30px;
                right: 30px;
                z-index: 1;
                animation: rotate 20s linear infinite;
                width: 80px;
                opacity: 0.8;
            }

            @keyframes rotate {
                from { transform: rotate(0deg); }
                to { transform: rotate(360deg); }
            }

            header {
                text-align: center;
                padding: 2rem;
                background: rgba(0,0,0,0.3);
                border-bottom: 2px solid #00e6e6;
            }

            header h1 {
                font-size: 3rem;
                margin-bottom: 0.5rem;
                color: #00e6e6;
            }

            header p a {
                color: #ffffff;
                text-decoration: underline;
            }

            .links a {
                color: #fff;
                margin: 0 10px;
                padding: 0.5rem 1rem;
                text-decoration: none;
                background-color: rgba(0, 230, 230, 0.2);
                border-radius: 8px;
                border: 1px solid #00e6e6;
                transition: 0.3s;
                display: inline-block;
            }

            .links a:hover {
                background-color: #00e6e6;
                color: #001f3f;
            }

            section {
                margin: 1.5rem auto;
                padding: 1rem 2rem;
                background: #11161b;
                width: 90%;
                max-width: 1000px;
                border-radius: 12px;
                box-shadow: 0 6px 20px rgba(0,0,0,0.4);
                position: relative;
                z-index: 0;
            }

            h2 {
                color: #00e6e6;
                cursor: pointer;
                margin-bottom: 1rem;
                position: relative;
            }

            h2::after {
                content: "▼";
                float: right;
                font-size: 1rem;
                transition: transform 0.2s ease;
            }

            h2.collapsed::after {
                transform: rotate(-90deg);
            }

            .content {
                display: block;
                transition: all 0.3s ease;
            }

            .collapsed + .content {
                display: none;
            }

            h3 {
                color: #ffcc00;
                margin-top: 1rem;
            }

            ul {
                list-style: none;
                padding-left: 0;
            }

            ul li {
                margin-bottom: 0.6rem;
                padding-left: 1.5rem;
                position: relative;
            }

            ul li::before {
                content: "🤖";
                position: absolute;
                left: 0;
            }

            a {
                color: #00e6e6;
                text-decoration: none;
            }

            a:hover {
                text-decoration: underline;
            }

            p {
                line-height: 1.6;
            }
        </style>
        <script>
            document.addEventListener("DOMContentLoaded", () => {
                document.querySelectorAll("h2").forEach(h2 => {
                    h2.addEventListener("click", () => {
                        h2.classList.toggle("collapsed");
                        const content = h2.nextElementSibling;
                        if (content) content.classList.toggle("collapsed");
                    });
                });
            });
        </script>
    </head>
    <body>
        <img class="ai-float" src="/static/logo.gif" alt="AI Logo" />

        <header>
            <h1>AB KAIUM</h1>
            <p>Email: <a href="mailto:akkaium33@gmail.com">akkaium33@gmail.com</a></p>
            <div class="links">
                <a href="https://linkedin.com/in/ab-kaium" target="_blank">LinkedIn</a>
                <a href="https://github.com/Qyum" target="_blank">GitHub</a>
                <a href="https://leetcode.com/Qyum/" target="_blank">LeetCode</a>
                <a href="https://www.fiverr.com/users/qyum_ai/manage_gigs" target="_blank">Fiverr</a>
                <a href="https://www.upwork.com/freelancers/~0173f8e3cad7a922c6" target="_blank">Upwork</a>
            </div>
        </header>
        <section>
            <h2>🧠 Summary</h2>
            <div class="content">
                <p>
                    6+ years in AI-driven innovation: fraud detection, speech recognition, recommendation engines, and intelligent bots. <br>
                    Specialized in backend (Django/Flask/FastAPI), ML Ops, and scalable AI products using LLMs, GNNs, and cutting-edge architectures.
                </p>
            </div>
        </section>

        <section>
            <h2>💼 Experience</h2>
            <div class="content">
                <h3>Senior ML Engineer (TL/CTO) – Fixels Graphix (Jan 2023 – Present)</h3>
                <ul>
                    <li>🚀 Developed GNN and gated neural network models for fraud and AML detection (95% accuracy)</li>
                    <li>🎥 Built backend APIs for face generation and text-to-video (multi-scene) using LLMs and diffusion models</li>
                    <li>🩺 Created a LangChain-powered medical chatbot (92% positive feedback)</li>
                </ul>
                <h3>Senior Software Engineer, ML – REVE Systems</h3>
                <ul>
                    <li>🔊 Built Wav2Vec Transformer for Bengali STT (WER reduced by 5%)</li>
                    <li>📊 Customized inference API using fb-wav2vec2-xlmr-53 (89% test accuracy)</li>
                    <li>🏨 Developed hotel recommender system using collaborative filtering and DL (95% accuracy)</li>
                </ul>
                <h3>ML Engineer – SSL Wireless</h3>
                <ul>
                    <li>🔐 Created multi-face recognition for security & attendance using FaceNet and KNN (99% recall)</li>
                    <li>🗣️ Built end-to-end Bengali speech recognition with Bi-RNN, LSTM, GRU (reduced training loss 50%)</li>
                    <li>🛒Designed a deep product recommender using SVD & collaborative filtering (RMSE < 10%)</li>

                </ul>
                <h3>Technical Lead – HSTU Robo Destroyer</h3>
                <ul>
                    <li>🤖 Built robots (line follower, soccer bot) using C++, Arduino, sonar/color sensors</li>
                    <li>🤖 Implemented reinforcement learning for delivery, cleaning, transportation robots</li>
                </ul>
            </div>
        </section>

        <section>
            <h2>⚙️ Skills</h2>
            <div class="content">
                <p>
                    <strong>Languages:</strong> Python, C++, SQL, MATLAB<br>
                    <strong>Frameworks:</strong> Flask, Django, FastAPI<br>
                    <strong>AI/ML:</strong> TensorFlow, PyTorch, Scikit-learn,Bert,Transformer<br>
                    <strong>Tools:</strong> Docker, Git, AWS, GCP, Azure, CUDA<br>
                    <strong>Concepts:</strong> voice Ai,LLMs, LangChain, NLP, CV, REST APIs<br>
                </p>
            </div>
        </section>

        <section>
            <h2>🎓 Education</h2>
            <div class="content">
                <ul>
                    <li>🎓 B.Sc. in Electrical and Electronic Engineering – HSTU (2017–2020)</li>
                    <li>📘 B.Sc. in Applied Mathematics – NSTU (2015–2016)</li>
                </ul>
            </div>
        </section>

        <section>
            <h2>📁 Projects</h2>
            <div class="content">
                <h3>🕵️‍♂️ Forgery Detection System</h3>
                <p>Used EfficientNet with advanced preprocessing and augmentation to detect facial manipulation in images (80% accuracy) <a href="https://github.com/Qyum/forgery-detection">GitHub</a></p>

                <h3>👕 Visual Detection (VD)</h3>
                <p>Model detects objects in an image and display the detected object's class name above the bounding box on the clothing item.Trained the model by using a dataset (e.g.,iMaterialist, Deepfashion etc)<a href="https://github.com/qyum/VD/tree/dev">GitHub</a></p>

                <h3>📦 Object Detection YOLOv8 vs YOLOv11</h3>
                <p>A state-of-the-art multi-object project for segmentation, object detection on Nvidia Jetson Nano .This repo show performance difference between yolov8 VS yolov11 model according to FPS <a href="https://github.com/qyum/ObjectDetection/tree/dev">GitHub</a></p>

                <h3>🩺 Doctor Suggestion Chatbot</h3>
                <p>Medical chatbot suggesting doctors based on user symptoms and queries. Integrated with LLM, vector search, and user interaction logs.<a href="https://bitbucket.org/techboomai-dev/dr_suggestion_chatbot/src/qyum_dev/chat_bot/">Bitbucket</a></p>

                <h3>🎬 Text-to-Video Generator</h3>
                <p>Text-prompt video generation using Stable Diffusion and GANs <a href="https://github.com/Qyum/face-text-to-video">GitHub</a></p>

                <h3>🗣️ Bangla Speech Recognition</h3>
                <p>End-to-end Bengali speech recognition using Bi-RNN, LSTM, GRU to achieve high transcription accuracy. <a href="https://github.com/Qyum/Bangla-deep-speech-Recognition">Repo</a></p>

                <h3>📄 Skew Correction for OCR</h3>
                <p>Image processing-based project to detect documents and correct skew for better OCR. <a href="https://github.com/Qyum/Document-detection-and-Skew-correction-">Repo</a></p>

                <h3>🎵 Music Generation</h3>
                <p> Music generation using deep learning to create new compositions from learned patterns.<a href="https://github.com/Qyum/Generate-Music-tune">Repo</a></p>

                <h3>🚗 Autonomous Driving</h3>
                <p> Simulated project demonstrating lane following and car detection with computer vision. <a href="https://github.com/Qyum/Autonomous_driving_application">Repo</a></p>

                <h3>🤖 PID-Controlled Robot</h3>
                <p>Autonomous robot with PID control for stable and accurate navigation. <a href="https://github.com/Qyum/pid">Repo</a></p>
            </div>
        </section>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
