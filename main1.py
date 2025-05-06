from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

app = FastAPI()

# Allow requests from all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"]
)

@app.get("/", response_class=HTMLResponse)
async def portfolio():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>AB KAIUM – Portfolio</title>
        <link href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap" rel="stylesheet">
        <style>
            body {
                font-family: 'Poppins', sans-serif;
                background: linear-gradient(to right, #fdfcfb, #e2d1c3);
                color: #2c3e50;
                margin: 0;
                padding: 0;
            }

            header {
                background: linear-gradient(to right, #4facfe, #00f2fe);
                color: white;
                padding: 2rem;
                text-align: center;
                border-bottom: 4px solid #007bff;
            }

            header h1 {
                font-size: 3rem;
                margin: 0;
            }

            header p {
                margin: 0.5rem 0;
                font-size: 1.1rem;
            }

            .links {
                margin-top: 1rem;
            }

            .links a {
                color: white;
                margin: 0 12px;
                font-weight: 600;
                text-decoration: none;
                padding: 0.3rem 0.6rem;
                border: 1px solid white;
                border-radius: 6px;
                background-color: rgba(255, 255, 255, 0.2);
                transition: all 0.3s ease;
            }

            .links a:hover {
                background-color: white;
                color: #007bff;
            }

            section {
                background-color: white;
                margin: 2rem auto;
                padding: 2rem;
                border-radius: 12px;
                width: 85%;
                max-width: 960px;
                box-shadow: 0 8px 24px rgba(0,0,0,0.1);
            }

            h2 {
                color: #007bff;
                border-bottom: 2px solid #007bff;
                padding-bottom: 0.5rem;
                margin-bottom: 1rem;
            }

            h3 {
                color: #4a4a4a;
                margin-top: 1.5rem;
            }

            ul {
                padding-left: 1.5rem;
            }

            ul li {
                margin-bottom: 0.5rem;
                line-height: 1.6;
            }

            a {
                color: #007bff;
                text-decoration: none;
                font-weight: 500;
            }

            a:hover {
                text-decoration: underline;
            }

            .emoji {
                font-size: 1.2rem;
                margin-right: 0.4rem;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>AB KAIUM</h1>
            <p>Email: <a href="mailto:akkaium33@gmail.com" style="color: #fff; text-decoration: underline;">akkaium33@gmail.com</a></p>
            <div class="links">
                <a href="https://www.linkedin.com/in/ab-kaium/" target="_blank">LinkedIn</a>
                <a href="https://github.com/Qyum" target="_blank">GitHub</a>
                <a href="https://leetcode.com/Qyum/" target="_blank">LeetCode</a>
                <a href="https://www.fiverr.com/users/qyum_ai/manage_gigs?current_filter=active" target="_blank">Fiverr</a>
                <a href="https://www.upwork.com/freelancers/~0173f8e3cad7a922c6" target="_blank">Upwork</a>
            </div>
        </header>

        <section>
            <h2>Summary</h2>
            <p>
                6+ years of experience in AI-driven fraud detection, speech recognition, recommender systems, and chatbot development.
                Skilled in backend development (Django, Flask, FastAPI), AI model deployment, and leadership roles.
                Expert in LLMs, GNNs, TensorFlow, PyTorch, and cloud platforms like AWS & Azure. Background in EEE, driven by impactful AI.
            </p>
        </section>

        <section>
            <h2>Experience</h2>

            <h3>Senior ML Engineer (TL/CTO) – Fixels Graphix (Jan 2023 – Present)</h3>
            <ul>
                <li>🚀 Built GNNs for fraud detection (95% accuracy)</li>
                <li>🎥 Developed text-to-video pipeline using LLMs + Diffusion</li>
                <li>🩺 Created a LangChain-powered medical chatbot (92% satisfaction)</li>
            </ul>

            <h3>Senior Software Engineer, ML – REVE Systems (Mar 2022 – Jan 2023)</h3>
            <ul>
                <li>🔊 Built Wav2Vec Transformer for Bengali STT (5% WER drop)</li>
                <li>🎯 Custom API with XLMR-based model (89% test acc)</li>
                <li>🏨 Built hotel recommender system (95% accuracy)</li>
            </ul>

            <h3>ML Engineer – SSL Wireless (Nov 2020 – Feb 2022)</h3>
            <ul>
                <li>🔐 Multi-face recognition using FaceNet & KNN (99% recall)</li>
                <li>🗣️ Bengali ASR using LSTM, GRU (50% loss reduction)</li>
                <li>🛒 Product recommender using SVD (RMSE &lt; 10%)</li>
            </ul>

            <h3>Technical Lead – HSTU Robo Destroyer (2017 – 2020)</h3>
            <ul>
                <li>🤖 Built bots (line follower, soccer bot) with Arduino & C++</li>
                <li>🧠 RL for delivery and cleaning robots</li>
            </ul>
        </section>

        <section>
            <h2>Skills</h2>
            <p>
                <strong>Languages:</strong> Python, C/C++, SQL, MATLAB<br>
                <strong>Backend:</strong> Flask, Django, FastAPI<br>
                <strong>Libraries:</strong> TensorFlow, PyTorch, Scikit-learn, Transformers, Numpy, Pandas<br>
                <strong>Tools:</strong> Docker, Git, Bitbucket, AWS, GCP, Azure, CUDA, VSCode<br>
                <strong>Concepts:</strong> LLMs, LangChain, DSA, NLP, CV, REST APIs<br>
                <strong>Platforms:</strong> Windows, Linux
            </p>
        </section>

        <section>
            <h2>Education</h2>
            <ul>
                <li>🎓 B.Sc. in Electrical and Electronic Engineering – HSTU (2017–2020)</li>
                <li>📘 B.Sc. in Applied Mathematics – NSTU (2015–2016)</li>
            </ul>
        </section>

        <section>
            <h2>Projects</h2>

            <h3>🕵️‍♂️ Forgery Detection System</h3>
            <p>
                EfficientNet-based facial forgery detector with advanced augmentation (80% accuracy).
                <a href="https://github.com/Qyum/forgery-detection" target="_blank">GitHub</a>
            </p>

            <h3>👕 Visual Detection (VD)</h3>
            <p>
                Clothing object detection with bounding box labeling using iMaterialist/DeepFashion.
                <a href="https://github.com/qyum/VD/tree/dev" target="_blank">GitHub</a>
            </p>

            <h3>📦 Object Detection (YOLOv8 vs YOLOv11)</h3>
            <p>
                Multi-object detection with segmentation on Jetson Nano; FPS benchmarking YOLOv8 vs YOLOv11.
                <a href="https://github.com/qyum/ObjectDetection/tree/dev" target="_blank">GitHub</a>
            </p>

            <h3>🩺 Doctor Suggestion Chatbot</h3>
            <p>
                LLM + vector search-powered chatbot for symptom-based doctor suggestions.
                <a href="https://bitbucket.org/techboomai-dev/dr_suggestion_chatbot/src/qyum_dev/chat_bot/" target="_blank">Bitbucket</a>
            </p>

            <h3>🎬 Face & Text-to-Video Generator</h3>
            <p>
                Video generation from prompts using Stable Diffusion + GANs.
                <a href="https://github.com/Qyum/face-text-to-video" target="_blank">GitHub</a> |
                <a href="https://www.upwork.com/freelancers/~0173f8e3cad7a922c6" target="_blank">Upwork</a>
            </p>

            <h3>🗣️ Bangla Deep Speech Recognition</h3>
            <p>
                End-to-end Bengali speech recognition using Bi-RNN, LSTM, GRU.
                <a href="https://github.com/Qyum/Bangla-deep-speech-Recognition" target="_blank">Repository</a>
            </p>

            <h3>📄 Document Detection & Skew Correction</h3>
            <p>
                Image-based document detection and deskewing for OCR preprocessing.
                <a href="https://github.com/Qyum/Document-detection-and-Skew-correction-" target="_blank">Repository</a>
            </p>

            <h3>🎵 Music Generation with Deep Learning</h3>
            <p>
                Generative deep learning model for creating musical patterns.
                <a href="https://github.com/Qyum/Generate-Music-tune" target="_blank">Repository</a>
            </p>

            <h3>🚗 Autonomous Driving Application</h3>
            <p>
                Lane-following and car-detection CV model in driving simulator.
                <a href="https://github.com/Qyum/Autonomous_driving_application" target="_blank">Repository</a>
            </p>

            <h3>🤖 Autonomous Robot with PID Control</h3>
            <p>
                Autonomous navigation bot with optimized PID controller.
                <a href="https://github.com/Qyum/pid" target="_blank">Repository</a>
            </p>
        </section>
    </body>
    </html>
    """

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))  # Default local port
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
