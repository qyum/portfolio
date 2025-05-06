from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, status
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()
# Allow requests from all origins 
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    expose_headers=["*"])

@app.get("/", response_class=HTMLResponse)
async def portfolio():
    return """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>AB KAIUM – Portfolio</title>
        <style>
            body {
                font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                background: linear-gradient(to bottom, #f0f4ff, #e3eafc);
                color: #2c3e50;
                padding: 2rem;
                margin: 0;
            }
            header {
                background-color: #007bff;
                color: white;
                padding: 1rem 2rem;
                border-radius: 10px;
                margin-bottom: 2rem;
            }
            h1 {
                margin: 0;
                font-size: 2.5rem;
            }
            .links a {
                color: #fff;
                margin-right: 15px;
                text-decoration: none;
                font-weight: bold;
            }
            .links a:hover {
                text-decoration: underline;
            }
            section {
                background-color: white;
                padding: 1.5rem;
                margin-bottom: 1.5rem;
                border-radius: 10px;
                box-shadow: 0 4px 8px rgba(0, 0, 0, 0.05);
            }
            h2 {
                color: #007bff;
            }
            ul {
                padding-left: 1.5rem;
            }
            a {
                color: #007bff;
                text-decoration: none;
            }
            a:hover {
                text-decoration: underline;
            }
        </style>
    </head>
    <body>
        <header>
            <h1>AB KAIUM</h1>
            <p>Email: <a href="mailto:akkaium33@gmail.com" style="color: #fff;">akkaium33@gmail.com</a></p>
            <p class="links">
                <a href="https://www.linkedin.com/in/ab-kaium/" target="_blank">LinkedIn</a>
                <a href="https://github.com/Qyum" target="_blank">GitHub</a>
                <a href="https://leetcode.com/Qyum/" target="_blank">LeetCode</a>
                <a href="https://www.fiverr.com/users/qyum_ai/manage_gigs?current_filter=active" target="_blank">Fiverr</a>
                <a href="https://www.upwork.com/freelancers/~0173f8e3cad7a922c6" target="_blank">Upwork</a>
            </p>
        </header>

        <section class="summary">
            <h2>Summary</h2>
            <p>
                6+ years of experience in AI-driven fraud detection, speech recognition, recommender systems, and chatbot development. Strong Python backend skills (Django, Flask), and expertise in deploying AI models. Proven leadership in deep learning, LLMs, and graph models. Proficient with TensorFlow, PyTorch, and cloud platforms like AWS and Azure. Electrical and Electronic Engineering background, passionate about scalable AI solutions and real-world problem-solving.
            </p>
        </section>

        <section>
            <h2>Experience</h2>

            <h3>Senior ML Engineer (TL/CTO) – Fixels Graphix (Jan 2023 – Present)</h3>
            <ul>
                <li>Developed GNN and gated neural network models for fraud and AML detection (95% accuracy)</li>
                <li>Built backend APIs for face generation and text-to-video (multi-scene) using LLMs and diffusion models</li>
                <li>Created a LangChain-powered medical chatbot (92% positive feedback)</li>
            </ul>

            <h3>Senior Software Engineer, ML – REVE Systems (Mar 2022 – Jan 2023)</h3>
            <ul>
                <li>Built Wav2Vec Transformer for Bengali STT (WER reduced by 5%)</li>
                <li>Customized inference API using fb-wav2vec2-xlmr-53 (89% test accuracy)</li>
                <li>Developed hotel recommender system using collaborative filtering and DL (95% accuracy)</li>
            </ul>

            <h3>ML Engineer – Software Shop Limited (SSL Wireless) (Nov 2020 – Feb 2022)</h3>
            <ul>
                <li>Created multi-face recognition for security & attendance using FaceNet and KNN (99% recall)</li>
                <li>Built end-to-end Bengali speech recognition with Bi-RNN, LSTM, GRU (reduced training loss 50%)</li>
                <li>Designed a deep product recommender using SVD & collaborative filtering (RMSE < 10%)</li>
            </ul>

            <h3>Technical Lead – HSTU Robo Destroyer (Jan 2017 – Oct 2020)</h3>
            <ul>
                <li>Built robots (line follower, soccer bot) using C++, Arduino, sonar/color sensors</li>
                <li>Implemented reinforcement learning for delivery, cleaning, transportation robots</li>
            </ul>
        </section>

        <section>
            <h2>Skills</h2>
            <p>
                Languages: Python, C/C++, SQL, MATLAB<br>
                Backend: Flask, Django, FastAPI<br>
                Libraries: TensorFlow, PyTorch, Scikit-learn, Keras, Numpy, Pandas, Transformers<br>
                Tools: Docker, Git, GitHub, Bitbucket, AWS, GCP, Azure, CUDA, VSCode<br>
                Concepts: LLM, LangChain, DSA, NLP, CV, REST API<br>
                Platforms: Windows, Linux
            </p>
        </section>

        <section>
            <h2>Education</h2>
            <ul>
                <li>B.Sc. in Electrical and Electronic Engineering – HSTU (2017–2020)</li>
                <li>B.Sc. in Applied Mathematics – NSTU (2015–2016)</li>
            </ul>
        </section>

        <section>
            <h2>Projects</h2>

            <h3>Forgery Detection System</h3>
            <p>
                Used EfficientNet with advanced preprocessing and augmentation to detect facial manipulation in images (80% accuracy).
                <a href="https://github.com/Qyum/forgery-detection" target="_blank">GitHub</a>
            </p>


            <h3>Visual Detection (VD)</h3>
            <p>Visual detection pipeline using YOLOv8, Streamlit, and FastAPI. Real-time video/image inference with deployment-ready endpoints. 
            <a href="https://github.com/qyum/VD/tree/dev" target="_blank">GitHub</a></p>

            <h3>Object Detection</h3>
            <p>Complete object detection system using OpenCV, PyTorch, FastAPI. Supports webcam/video input with real-time predictions. 
            <a href="https://github.com/qyum/ObjectDetection/tree/dev" target="_blank">GitHub</a></p>

            <h3>Doctor Suggestion Chatbot</h3>
            <p>Medical chatbot suggesting doctors based on user symptoms and queries. Integrated with LLM, vector search, and user interaction logs.
            <a href="https://bitbucket.org/techboomai-dev/dr_suggestion_chatbot/src/qyum_dev/chat_bot/" target="_blank">Bitbucket</a></p>


            <h3>Face & Text-to-Video Generator</h3>
            <p>
                Text-prompt video generation using Stable Diffusion and GANs.
                <a href="https://github.com/Qyum/face-text-to-video" target="_blank">GitHub</a> |
                <a href="https://www.upwork.com/freelancers/~0173f8e3cad7a922c6" target="_blank">Upwork</a>
            </p>

            <h3>Bangla Deep Speech Recognition</h3>
            <p>
                End-to-end Bengali speech recognition using Bi-RNN, LSTM, GRU to achieve high transcription accuracy.
                <a href="https://github.com/Qyum/Bangla-deep-speech-Recognition" target="_blank">Repository</a>
            </p>

            <h3>📄 Document Detection and Skew Correction</h3>
            <p>
                Image processing-based project to detect documents and correct skew for better OCR.
                <a href="https://github.com/Qyum/Document-detection-and-Skew-correction-" target="_blank">Repository</a>
            </p>

            <h3>🎵 Music Generation with Deep Learning</h3>
            <p>
                Music generation using deep learning to create new compositions from learned patterns.
                <a href="https://github.com/Qyum/Generate-Music-tune" target="_blank">Repository</a>
            </p>

            <h3>🚗 Autonomous Driving Application</h3>
            <p>
                Simulated project demonstrating lane following and car detection with computer vision.
                <a href="https://github.com/Qyum/Autonomous_driving_application" target="_blank">Repository</a>
            </p>

            <h3>🤖 Autonomous Robot with PID Control</h3>
            <p>
                Autonomous robot with PID control for stable and accurate navigation.
                <a href="https://github.com/Qyum/pid" target="_blank">Repository</a>
            </p>
        </section>
    </body>
    </html>
    """
