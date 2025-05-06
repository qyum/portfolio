from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
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
            body {
                margin: 0;
                padding: 0;
                font-family: 'Space Grotesk', sans-serif;
                background: linear-gradient(to right, #0f2027, #203a43, #2c5364);
                color: #f1f1f1;
                overflow-x: hidden;
                position: relative;
            }

            header {
                text-align: center;
                padding: 2rem;
                background: linear-gradient(to right, #2b5876, #4e4376);
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

            .emoji {
                margin-right: 0.3rem;
            }

            /* Moveable AI Logo */
            .moveable-logo {
                position: fixed;
                top: 20%;
                left: 5%;
                width: 120px;
                height: auto;
                cursor: move;
                z-index: 1000;
                transition: transform 0.1s ease;
            }

            .ai-background {
                position: absolute;
                top: 0;
                left: 0;
                width: 100%;
                height: 100%;
                background: url('https://example.com/ai-background-image.png') center/cover no-repeat;
                opacity: 0.1;
                z-index: -1;
            }

        </style>
    </head>
    <body>
        <div class="ai-background"></div>
        <img class="moveable-logo" id="moveableLogo" src="D:/portfolio/original-91b920c5af3417e456bc46004300944d.gif" alt="AI Logo" />

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
                    <li>🚀 Fraud detection with GNN (95% acc)</li>
                    <li>🎥 Text-to-video with LLM + Diffusion</li>
                    <li>🩺 LangChain-powered chatbot (92% sat.)</li>
                </ul>
                <h3>Senior Software Engineer, ML – REVE Systems</h3>
                <ul>
                    <li>🔊 Wav2Vec for Bengali STT (5% WER drop)</li>
                    <li>📊 XLM-R based sentiment model (89%)</li>
                    <li>🏨 Hotel recommender (95% accuracy)</li>
                </ul>
                <h3>ML Engineer – SSL Wireless</h3>
                <ul>
                    <li>🔐 FaceNet+KNN for security (99% recall)</li>
                    <li>🗣️ ASR for Bengali using LSTM, GRU</li>
                    <li>🛒 Product recommender using SVD</li>
                </ul>
                <h3>Technical Lead – HSTU Robo Destroyer</h3>
                <ul>
                    <li>🤖 Arduino bots & RL delivery bots</li>
                </ul>
            </div>
        </section>

        <section>
            <h2>⚙️ Skills</h2>
            <div class="content">
                <p>
                    <strong>Languages:</strong> Python, C++, SQL, MATLAB<br>
                    <strong>Frameworks:</strong> Flask, Django, FastAPI<br>
                    <strong>AI/ML:</strong> TensorFlow, PyTorch, Scikit-learn, Transformers<br>
                    <strong>Tools:</strong> Docker, Git, AWS, GCP, Azure, CUDA<br>
                    <strong>Concepts:</strong> LLMs, LangChain, NLP, CV, REST APIs<br>
                </p>
            </div>
        </section>

        <section>
            <h2>🎓 Education</h2>
            <div class="content">
                <ul>
                    <li>🎓 B.Sc. in EEE – HSTU (2017–2020)</li>
                    <li>📘 Applied Mathematics – NSTU (2015–2016)</li>
                </ul>
            </div>
        </section>

        <section>
            <h2>📁 Projects</h2>
            <div class="content">
                <h3>🕵️‍♂️ Forgery Detection System</h3>
                <p>EfficientNet-based forgery detection (80% acc). <a href="https://github.com/Qyum/forgery-detection">GitHub</a></p>

                <h3>👕 Visual Detection (VD)</h3>
                <p>Clothing object detection using DeepFashion. <a href="https://github.com/qyum/VD/tree/dev">GitHub</a></p>

                <h3>📦 Object Detection YOLOv8 vs YOLOv11</h3>
                <p>Multi-object segmentation on Jetson Nano. <a href="https://github.com/qyum/ObjectDetection/tree/dev">GitHub</a></p>

                <h3>🩺 Doctor Suggestion Chatbot</h3>
                <p>LLM + vector search chatbot for medical help. <a href="https://bitbucket.org/techboomai-dev/dr_suggestion_chatbot/src/qyum_dev/chat_bot/">Bitbucket</a></p>

                <h3>🎬 Text-to-Video Generator</h3>
                <p>Prompt-based video gen using GAN + Diffusion. <a href="https://github.com/Qyum/face-text-to-video">GitHub</a></p>

                <h3>🗣️ Bangla Speech Recognition</h3>
                <p>Bi-RNN + LSTM model for Bangla ASR. <a href="https://github.com/Qyum/Bangla-deep-speech-Recognition">Repo</a></p>

                <h3>📄 Skew Correction for OCR</h3>
                <p>Document detection & alignment. <a href="https://github.com/Qyum/Document-detection-and-Skew-correction-">Repo</a></p>

                <h3>🎵 Music Generation</h3>
                <p>DL model to generate musical sequences. <a href="https://github.com/Qyum/Generate-Music-tune">Repo</a></p>

                <h3>🚗 Autonomous Driving</h3>
                <p>Lane-following and car-detection in sim. <a href="https://github.com/Qyum/Autonomous_driving_application">Repo</a></p>

                <h3>🤖 PID-Controlled Robot</h3>
                <p>Autonomous bot with PID optimization. <a href="https://github.com/Qyum/pid">Repo</a></p>
            </div>
        </section>

        <script>
            // Make the logo draggable
            const logo = document.getElementById("moveableLogo");
            let offsetX = 0;
            let offsetY = 0;
            let isDragging = false;

            logo.onmousedown = (e) => {
                isDragging = true;
                offsetX = e.clientX - logo.getBoundingClientRect().left;
                offsetY = e.clientY - logo.getBoundingClientRect().top;
                document.onmousemove = (e) => {
                    if (isDragging) {
                        logo.style.left = `${e.clientX - offsetX}px`;
                        logo.style.top = `${e.clientY - offsetY}px`;
                    }
                };

                document.onmouseup = () => {
                    isDragging = false;
                };
            };
        </script>

    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
